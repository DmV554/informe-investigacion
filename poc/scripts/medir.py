#!/usr/bin/env python3
"""
PoC TI-05 · TERABYTE · Script de medición de arranque en frío y latencia.

Qué hace
--------
Invoca por HTTP las funciones desplegadas (config.json), mide la latencia
total desde este computador y clasifica cada invocación como fría o caliente
usando lo que la propia función devuelve (instance_id, uptime_ms,
first_request). Escribe una fila por invocación en data/mediciones.csv,
con flush inmediato (si el script muere, no se pierde nada).

Dos protocolos:
  natural : 1 invocación tras un período de inactividad + N calientes,
            esperar, repetir. Aplica a todas las plataformas.
  forzado : provoca un entorno de ejecución nuevo + 1 invocación + N
            calientes, sin esperas. Solo plataformas con "forzable": true;
            el mecanismo lo indica "metodo_forzado" en config.json:
              lambda_env      : cambia la variable de entorno POC_MARKER
                                (nueva configuración => nuevo entorno).
              wrangler_deploy : publica una versión nueva del Worker con
                                `npx wrangler deploy` (nueva versión =>
                                isolates nuevos en el PoP).
              gcloud_env      : `gcloud run services update ... --update-env-vars
                                POC_MARKER=<n>` (nueva configuración =>
                                revisión nueva => instancia nueva). En Cloud
                                Run la revisión nueva queda pre-calentada por
                                el health check con el que la plataforma la
                                valida antes de enrutarle tráfico, así que el
                                cliente casi nunca paga ese arranque; se
                                clasifica frío con el criterio
                                `uptime_menor_que_latencia` y el arranque del
                                lado del proveedor se lee aparte con
                                scripts/startup_cloudrun.py.
            Los tres son despliegues/actualizaciones reales, no un mecanismo
            artificial. Las plataformas no forzables se miden igual en cada
            ciclo para tener muestras en la misma ventana. Todas reciben el
            mismo número de peticiones por ciclo (1 + calientes_por_ciclo).

Plataformas con url "PENDIENTE..." en config.json se omiten automáticamente
(por ejemplo, Cloud Run mientras no exista la URL real).

Uso
---
  python scripts/medir.py --prueba
      1 ciclo natural con espera de 1 min + 2 ciclos forzados. ~3 min.
  python scripts/medir.py --forzado 20
      20 ciclos forzados (~10-15 min).
  python scripts/medir.py --natural 6 --espera 15
      6 ciclos naturales con 15 min de inactividad (~1 h 20).
  python scripts/medir.py --natural 4 --espera 10 --solo cloudflare-workers
      Solo una plataforma.

Requiere Python 3.8+. Sin dependencias externas (urllib de la stdlib).
El modo forzado requiere AWS CLI configurada (aws configure) para Lambda,
Wrangler autenticado (npm install + npx wrangler login) para Workers y
gcloud CLI autenticada (gcloud auth login + gcloud config set project) para
Cloud Run.
"""

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(RAIZ, "config.json")


def _resolver_aws_cli():
    """Ruta a la CLI de AWS. Orden: variable POC_AWS_CLI, "aws" en PATH,
    "aws.exe" en PATH (WSL con la CLI instalada en Windows) y, por último, la
    ruta de instalación habitual en Windows, para sesiones cuyo PATH no trae
    las rutas de Windows (por ejemplo, un servidor tmux arrancado con un
    entorno mínimo)."""
    candidatos = [os.environ.get("POC_AWS_CLI"), shutil.which("aws"), shutil.which("aws.exe"),
                  "/mnt/c/Program Files/Amazon/AWSCLIV2/aws.exe"]
    for c in candidatos:
        if c and os.path.isfile(c):
            return c
    return "aws"


AWS_CLI = _resolver_aws_cli()


def _resolver_gcloud_cli():
    """Ruta a la CLI de gcloud. Mismo orden que _resolver_aws_cli: variable
    POC_GCLOUD_CLI, "gcloud" en PATH, "gcloud.cmd" en PATH (WSL con la CLI
    instalada en Windows) y, por último, el nombre desnudo (para que el
    subprocess falle con un mensaje claro si tampoco está en el PATH del
    sistema)."""
    env = os.environ.get("POC_GCLOUD_CLI")
    if env and os.path.isfile(env):
        return env
    candidatos = [shutil.which("gcloud"), shutil.which("gcloud.cmd")]
    for c in candidatos:
        if c:
            return c
    return "gcloud"


GCLOUD_CLI = _resolver_gcloud_cli()

COLUMNAS = [
    "plataforma", "modo", "ciclo", "n_en_ciclo", "timestamp_local",
    "latencia_ms", "http_status", "instance_id", "first_request",
    "uptime_ms", "colo", "request_id", "es_frio", "criterio_frio", "error",
]

UMBRAL_UPTIME_FRIO_MS = 3000  # uptime menor a esto => instancia recién creada

# Segundos de espera entre forzar el arranque en frío y la primera petición
# medida, para que el cambio termine de propagar en el proveedor. Cada
# plataforma puede sobrescribirlo con "espera_tras_forzado_s" en config.json:
# Cloud Run usa 0 porque ahí esperar regala el arranque al health check de la
# revisión (ver forzar_frio_cloudrun).
ESPERA_TRAS_FORZADO_S = 5


def cargar_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def abrir_csv(ruta):
    ruta_abs = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(ruta_abs), exist_ok=True)
    nuevo = not os.path.exists(ruta_abs)
    f = open(ruta_abs, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(f, fieldnames=COLUMNAS)
    if nuevo:
        w.writeheader()
        f.flush()
    return f, w


def invocar(url, timeout_s):
    """Una petición GET. Devuelve (latencia_ms, status, json_o_None, error_o_None)."""
    # cache-buster para que ningún intermediario sirva una respuesta guardada
    sep = "&" if "?" in url else "?"
    url_cb = f"{url}{sep}cb={time.time_ns()}"
    req = urllib.request.Request(url_cb, headers={"User-Agent": "poc-ti05-terabyte/1.0",
                                                  "Cache-Control": "no-cache"})
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            cuerpo = resp.read()
            t1 = time.perf_counter()
            status = resp.status
    except urllib.error.HTTPError as e:
        t1 = time.perf_counter()
        return (t1 - t0) * 1000, e.code, None, f"HTTPError {e.code}"
    except Exception as e:  # timeout, DNS, conexión
        t1 = time.perf_counter()
        return (t1 - t0) * 1000, None, None, f"{type(e).__name__}: {e}"
    try:
        datos = json.loads(cuerpo.decode("utf-8"))
    except Exception as e:
        return (t1 - t0) * 1000, status, None, f"JSON inválido: {e}"
    return (t1 - t0) * 1000, status, datos, None


def clasificar(datos, ultimo_id, criterio="instance_id", latencia_ms=None):
    """Devuelve (es_frio, criterios). El criterio depende de la plataforma:

    instance_id   : frío si la instancia es distinta a la última vista en la
                    corrida. Válido donde las peticiones secuenciales reutilizan
                    el mismo entorno (Lambda). En la primera invocación de la
                    corrida decide uptime_ms bajo.
    first_request : frío solo si la propia instancia declara que esta petición
                    la inicializó (Workers). Ahí el cambio de instance_id NO
                    implica arranque: Cloudflare reparte peticiones consecutivas
                    entre varios isolates vivos del mismo PoP.
    uptime_menor_que_latencia
                  : frío solo si el contenedor nació dentro de la ventana de
                    esta petición, es decir, si su edad al responder es menor
                    que lo que la petición tardó de extremo a extremo. Se usa
                    en Cloud Run, donde el cambio de instance_id NO basta: al
                    crear una revisión la plataforma arranca un contenedor para
                    validarla (health check), así que la petición siguiente
                    puede caer en un contenedor ya despierto sin pagar ningún
                    arranque. La comparación no necesita ningún umbral fijado a
                    mano: si el contenedor es más joven que la petición, solo
                    pudo nacer después de que la petición salió de este cliente.
    """
    if datos is None:
        return None, ""
    iid = datos.get("instance_id")
    up = datos.get("uptime_ms")
    fr = datos.get("first_request") is True
    up_bajo = isinstance(up, (int, float)) and up < UMBRAL_UPTIME_FRIO_MS
    criterios = []
    if criterio == "first_request":
        # La propia instancia declara si esta petición la inicializó. Es la
        # única señal fiable: uptime bajo también lo tienen las calientes que
        # siguen a un arranque, y el cambio de id solo indica otro isolate.
        if fr:
            criterios.append("first_request")
        if ultimo_id is not None and iid != ultimo_id:
            criterios.append("(otro_isolate)")  # informativo, no decide
        es_frio = fr
    elif criterio == "uptime_menor_que_latencia":
        nacio_en_la_peticion = (
            isinstance(up, (int, float))
            and isinstance(latencia_ms, (int, float))
            and up < latencia_ms
        )
        if nacio_en_la_peticion:
            criterios.append("uptime_menor_que_latencia")
        if ultimo_id is not None and iid != ultimo_id:
            criterios.append("(instancia_distinta)")  # informativo, no decide
        es_frio = nacio_en_la_peticion
    else:  # instance_id
        if ultimo_id is None:
            if up_bajo:
                criterios.append("uptime_bajo")
            es_frio = up_bajo
        else:
            if iid != ultimo_id:
                criterios.append("instance_id_cambio")
            es_frio = iid != ultimo_id
    return es_frio, "+".join(criterios)


def precalentar_dns(urls):
    """Resuelve el DNS de cada host UNA vez, sin medir, para que la primera
    petición medida no incluya la resolución de nombres."""
    import socket
    from urllib.parse import urlparse
    for u in urls:
        host = urlparse(u).hostname
        try:
            socket.getaddrinfo(host, 443)
        except Exception as e:
            print(f"  aviso: no se pudo resolver {host}: {e}")


def forzar_frio_lambda(cfg_plat, marcador):
    """Cambia POC_MARKER en la Lambda y espera a que quede Active/Successful."""
    fn = cfg_plat["aws_function_name"]
    region = cfg_plat["region"]
    cmd = [AWS_CLI, "lambda", "update-function-configuration",
           "--function-name", fn, "--region", region,
           "--environment", f"Variables={{POC_MARKER={marcador}}}"]
    r = subprocess.run(cmd, capture_output=True, text=True, shell=(os.name == "nt"))
    if r.returncode != 0:
        raise RuntimeError(f"update-function-configuration falló: {r.stderr.strip()}")
    # esperar a que termine la actualización
    for _ in range(60):
        q = subprocess.run([AWS_CLI, "lambda", "get-function-configuration",
                            "--function-name", fn, "--region", region,
                            "--query", "[State,LastUpdateStatus]", "--output", "text"],
                           capture_output=True, text=True, shell=(os.name == "nt"))
        if q.returncode == 0 and "Active" in q.stdout and "Successful" in q.stdout:
            return
        time.sleep(1)
    raise RuntimeError("La Lambda no volvió a estado Active/Successful en 60 s")


def forzar_frio_workers(cfg_plat):
    """Publica una versión nueva del Worker (wrangler.jsonc en la raíz de la
    PoC). Aunque el código sea idéntico, Cloudflare crea una versión nueva y
    la siguiente petición en cada máquina del PoP arranca un isolate nuevo
    (la función lo reporta con first_request=true). Bloquea hasta que
    wrangler confirma el despliegue (~5 s)."""
    cmd = ["npx", "wrangler", "deploy"]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ,
                       timeout=120, shell=(os.name == "nt"))
    if r.returncode != 0:
        raise RuntimeError(f"wrangler deploy falló: {r.stderr.strip()[-400:]}")
    if "Current Version ID" not in r.stdout:
        raise RuntimeError("wrangler deploy no confirmó una versión nueva")


def forzar_frio_cloudrun(cfg_plat, marcador):
    """Cambia POC_MARKER en el servicio de Cloud Run (--update-env-vars, no
    destructivo: no borra otras variables). Cualquier cambio de configuración
    crea una revisión nueva => instancia nueva (documentado por Google Cloud).

    A diferencia de Lambda y Workers, aquí NO se espera nada después del
    cambio, y el motivo es el ciclo de vida de Cloud Run: una revisión no
    recibe tráfico hasta que la plataforma la valida, y para validarla arranca
    un contenedor y le hace un health check. Si se espera a que la revisión
    quede lista y además se duerme unos segundos, la primera petición medida
    llega a ese contenedor ya arrancado y sale caliente (verificado el
    20-09-2026: uptime de 8638 ms en la petición #0). `gcloud run services
    update` sin --async ya retorna con la revisión sirviendo tráfico, así que
    la petición inmediatamente posterior es la que paga el arranque."""
    name = cfg_plat["gcloud_service_name"]
    region = cfg_plat["region"]
    project = cfg_plat["gcloud_project"]
    cmd = [GCLOUD_CLI, "run", "services", "update", name,
           "--region", region, "--project", project,
           "--update-env-vars", f"POC_MARKER={marcador}", "--quiet"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, shell=(os.name == "nt"))
    if r.returncode != 0:
        raise RuntimeError(f"gcloud run services update falló: {r.stderr.strip()[-400:]}")


def forzar_frio(cfg_plat, marcador):
    """Despacha al mecanismo de forzado declarado en config.json."""
    metodo = cfg_plat.get("metodo_forzado", "lambda_env")
    if metodo == "lambda_env":
        forzar_frio_lambda(cfg_plat, marcador)
    elif metodo == "wrangler_deploy":
        forzar_frio_workers(cfg_plat)
    elif metodo == "gcloud_env":
        forzar_frio_cloudrun(cfg_plat, marcador)
    else:
        raise RuntimeError(f"metodo_forzado desconocido: {metodo}")


def ciclo(plat, cfg_plat, cfg, modo, n_ciclo, writer, f, estado, quiet=False):
    """1 invocación candidata a fría + N calientes. Escribe cada fila al CSV."""
    n_cal = cfg["calientes_por_ciclo"]
    pausa = cfg["pausa_entre_calientes_s"]
    for k in range(1 + n_cal):
        lat, status, datos, err = invocar(cfg_plat["url"], cfg["timeout_http_s"])
        es_frio, crit = clasificar(datos, estado.get(plat),
                                   cfg_plat.get("criterio_frio", "instance_id"),
                                   latencia_ms=lat)
        if datos is not None and datos.get("instance_id"):
            estado[plat] = datos["instance_id"]
        fila = {
            "plataforma": plat, "modo": modo, "ciclo": n_ciclo, "n_en_ciclo": k,
            "timestamp_local": datetime.now().isoformat(timespec="milliseconds"),
            "latencia_ms": f"{lat:.1f}", "http_status": status,
            "instance_id": (datos or {}).get("instance_id", ""),
            "first_request": (datos or {}).get("first_request", ""),
            "uptime_ms": (datos or {}).get("uptime_ms", ""),
            "colo": (datos or {}).get("colo", ""),
            "request_id": (datos or {}).get("request_id", ""),
            "es_frio": es_frio if es_frio is not None else "",
            "criterio_frio": crit, "error": err or "",
        }
        writer.writerow(fila)
        f.flush()
        if not quiet:
            etiqueta = "FRÍO   " if es_frio else ("caliente" if es_frio is False else "error  ")
            print(f"  [{plat:18s}] {modo:8s} c{n_ciclo:02d} #{k}  {lat:8.1f} ms  {etiqueta}"
                  f"  id={fila['instance_id'][:8]}  up={fila['uptime_ms']}  {crit or err}")
        if k < n_cal:
            time.sleep(pausa)


def esperar(minutos):
    total = int(minutos * 60)
    print(f"  ... inactividad {minutos} min ", end="", flush=True)
    for s in range(total):
        time.sleep(1)
        if s % 60 == 59:
            print(".", end="", flush=True)
    print(" listo")


def main():
    ap = argparse.ArgumentParser(description="PoC TI-05: medición de cold start y latencia")
    ap.add_argument("--prueba", action="store_true", help="corrida corta de verificación (~3 min)")
    ap.add_argument("--forzado", type=int, default=0, help="N ciclos forzados")
    ap.add_argument("--natural", type=int, default=0, help="N ciclos naturales")
    ap.add_argument("--espera", type=float, default=15, help="minutos de inactividad (natural)")
    ap.add_argument("--solo", default=None, help="medir solo esta plataforma")
    ap.add_argument("--csv", default=None, help="ruta CSV fija (por defecto: data/mediciones_<fecha-hora>_<modo>.csv)")
    args = ap.parse_args()

    cfg = cargar_config()
    plats = cfg["plataformas"]
    pendientes = [p for p, cp in plats.items() if str(cp.get("url", "")).startswith("PENDIENTE")]
    for p in pendientes:
        print(f"aviso: {p} omitida (url pendiente en config.json)")
        del plats[p]
    if not plats:
        sys.exit("Ninguna plataforma tiene URL configurada (todas PENDIENTE).")
    if args.solo:
        if args.solo not in plats:
            sys.exit(f"Plataforma desconocida: {args.solo}. Opciones: {list(plats)}")
        plats = {args.solo: plats[args.solo]}

    if args.prueba:
        n_forz, n_nat, espera = 2, 1, 1.0
        print("MODO PRUEBA: 1 ciclo natural (1 min de espera) + 2 ciclos forzados.")
    else:
        n_forz, n_nat, espera = args.forzado, args.natural, args.espera
        if n_forz == 0 and n_nat == 0:
            ap.error("indica --prueba, --forzado N o --natural N")

    inicio = datetime.now()
    if args.csv:
        ruta_csv = args.csv
    else:
        # Un archivo por corrida: data/mediciones_YYYYMMDD-HHMM_<modo>.csv
        etiqueta = "prueba" if args.prueba else "+".join(
            m for m, n in (("natural", n_nat), ("forzado", n_forz)) if n > 0)
        ruta_csv = f"data/mediciones_{inicio.strftime('%Y%m%d-%H%M')}_{etiqueta}.csv"
    f, writer = abrir_csv(ruta_csv)
    estado = {}  # último instance_id visto por plataforma
    print(f"Inicio: {inicio.isoformat(timespec='seconds')}  CSV: {ruta_csv}")
    print(f"Plataformas: {', '.join(plats)}")
    if n_forz and any(cp.get("metodo_forzado", "lambda_env") == "lambda_env"
                      for cp in plats.values() if cp.get("forzable")):
        print(f"AWS CLI: {AWS_CLI}")
    if n_forz and any(cp.get("metodo_forzado") == "gcloud_env"
                      for cp in plats.values() if cp.get("forzable")):
        print(f"gcloud CLI: {GCLOUD_CLI}")
    print("No abrir las URLs en el navegador mientras corre.")
    precalentar_dns([cp["url"] for cp in plats.values()])
    print()

    try:
        # ---------- natural ----------
        for c in range(1, n_nat + 1):
            print(f"[natural] ciclo {c}/{n_nat}")
            # Se espera ANTES de cada invocación fría, incluido el primer
            # ciclo, para que todas partan de inactividad real.
            esperar(espera)
            for plat, cp in plats.items():
                ciclo(plat, cp, cfg, "natural", c, writer, f, estado)

        # ---------- forzado ----------
        marcador_base = int(time.time())
        for c in range(1, n_forz + 1):
            print(f"[forzado] ciclo {c}/{n_forz}")
            for plat, cp in plats.items():
                if cp.get("forzable"):
                    try:
                        forzar_frio(cp, marcador_base + c)
                        # Margen de propagación: en Lambda y Workers el forzado
                        # devuelve cuando el proveedor acepta el cambio, no
                        # cuando ya está activo en el punto que atiende la
                        # petición. En la corrida del 19-09-2026, con 2 s, 1 de
                        # 25 ciclos de Workers midió todavía contra un isolate
                        # de la versión anterior. Cloud Run declara 0: allí la
                        # revisión ya está sirviendo cuando el comando retorna.
                        time.sleep(cp.get("espera_tras_forzado_s", ESPERA_TRAS_FORZADO_S))
                    except Exception as e:
                        print(f"  !! no se pudo forzar frío en {plat}: {e}")
                ciclo(plat, cp, cfg, "forzado", c, writer, f, estado)
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Lo medido hasta ahora quedó en el CSV.")
    finally:
        f.close()
        fin = datetime.now()
        print(f"\nFin: {fin.isoformat(timespec='seconds')}  duración {fin - inicio}")


if __name__ == "__main__":
    main()
