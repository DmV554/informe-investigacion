#!/usr/bin/env python3
"""
PoC TI-05 · TERABYTE · Extrae la métrica propia de Cloud Run
"run.googleapis.com/container/startup_latencies" (Cloud Monitoring) para la
ventana de tiempo de una corrida de mediciones.

Por qué
-------
Bajo el protocolo forzado, `gcloud run services update` no expone al cliente
un arranque en frío observable: la plataforma no enruta tráfico a una
revisión nueva hasta validarla, y para validarla ya arrancó un contenedor y
le hizo un health check (ver el criterio "uptime_menor_que_latencia" y el
comentario de `forzar_frio_cloudrun` en medir.py). Por eso, en la corrida
forzada, 0 de las peticiones del cliente quedan clasificadas como frías en
Cloud Run: el arranque ocurrió, pero antes de que el cliente mandara nada.

Cloud Run sí registra ese arranque del lado del proveedor, sin depender de
qué instancia atendió qué petición: la métrica de Cloud Monitoring
"container/startup_latencies" (tipo DISTRIBUTION, medida en ms) trae un
punto por arranque de contenedor iniciado en el servicio, con
`resource.labels.revision_name`. Este script baja esa métrica para la
ventana de la corrida y la deja en results/cloudrun_startup.csv, análoga en
propósito a logs_cloudrun.py (que cruza latencia de servidor por trace id)
pero con el dato de arranque que Cloud Run sí mide internamente.

Aviso del instrumento
----------------------
Esto mide el arranque del contenedor tal como lo ve la plataforma (creación
+ health check interno), NO la latencia de extremo a extremo que percibe el
cliente. Es comparable con el `Init Duration` de Lambda (línea REPORT de
CloudWatch, `logs_lambda.py`) solo con esa salvedad: ambos son el tiempo que
el proveedor atribuye a "poner en marcha el entorno de ejecución", medido
del lado del proveedor y no desde Chile.

`gcloud monitoring` NO tiene subcomando `time-series`; la métrica se lee con
la API REST de Cloud Monitoring (`GET
https://monitoring.googleapis.com/v3/projects/{project}/timeSeries`),
autenticada con el token de `gcloud auth print-access-token`.

Percentiles aproximados por buckets
------------------------------------
La API devuelve cada punto como una distribución de histograma exponencial
(`bucketOptions.exponentialBuckets` + `bucketCounts`), no las muestras
individuales. La media agregada (`aggregate_media_ms`) es exacta (promedio
ponderado por cantidad de arranques de cada punto). p50/p95 NO son exactos:
se aproximan ubicando el bucket acumulado correspondiente y usando el punto
medio geométrico del rango del bucket como valor representativo. Se declaran
como "aproximados por bucket" en el nombre de columna.

Uso
---
  python scripts/startup_cloudrun.py
      Lee todos los data/mediciones_*.csv, toma la ventana de las filas de
      google-cloud-run (±2 min por defecto) y escribe
      results/cloudrun_startup.csv.
  python scripts/startup_cloudrun.py --csv data/mediciones_20260921*_forzado.csv --margen-min 5

Requiere gcloud CLI autenticada y rol roles/monitoring.viewer sobre el
proyecto (ver functions/cloudrun/README.md, punto g).
"""

import argparse
import csv
import glob
import json
import math
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(RAIZ, "config.json")
MONITORING_URL = "https://monitoring.googleapis.com/v3/projects/{project}/timeSeries"


def _resolver_gcloud_cli():
    """Misma resolución que medir.py y logs_cloudrun.py: variable
    POC_GCLOUD_CLI, "gcloud" en PATH, "gcloud.cmd" en PATH (WSL con la CLI
    instalada en Windows) y, por último, el nombre desnudo."""
    env = os.environ.get("POC_GCLOUD_CLI")
    if env and os.path.isfile(env):
        return env
    candidatos = [shutil.which("gcloud"), shutil.which("gcloud.cmd")]
    for c in candidatos:
        if c:
            return c
    return "gcloud"


GCLOUD_CLI = _resolver_gcloud_cli()


def cargar_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def leer_filas_cloudrun(patrones):
    """Concatena los CSV de mediciones (por defecto data/mediciones_*.csv) y
    devuelve solo las filas de google-cloud-run. Excluye salidas de otros
    scripts, igual que analizar.py y logs_cloudrun.py."""
    rutas = []
    for pat in patrones:
        rutas += sorted(glob.glob(os.path.join(RAIZ, pat)))
    rutas = [r for r in rutas if not os.path.basename(r).startswith(
        ("lambda_", "mediciones_lambda_join", "cloudrun_"))]
    if not rutas:
        sys.exit(f"No se encontraron CSV para {patrones}")
    filas = []
    for ruta in rutas:
        with open(ruta, encoding="utf-8") as f:
            filas += list(csv.DictReader(f))
    print("CSV leídos:", ", ".join(os.path.relpath(r, RAIZ) for r in rutas))
    filas_cr = [r for r in filas if r.get("plataforma") == "google-cloud-run" and r.get("timestamp_local")]
    if not filas_cr:
        sys.exit("No hay filas de google-cloud-run con timestamp_local en el CSV.")
    return filas_cr


def ventana_utc(filas_cr, margen_min):
    """timestamp_local es hora local naive (la del computador que corrió
    medir.py); se convierte a UTC con astimezone(), igual que en
    logs_cloudrun.py."""
    ts = [datetime.fromisoformat(r["timestamp_local"]) for r in filas_cr]
    ini = (min(ts) - timedelta(minutes=margen_min)).astimezone(timezone.utc)
    fin = (max(ts) + timedelta(minutes=margen_min)).astimezone(timezone.utc)
    return ini, fin


def _rfc3339(dt_utc):
    return dt_utc.isoformat().replace("+00:00", "Z")


def obtener_token_acceso():
    cmd = [GCLOUD_CLI, "auth", "print-access-token"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30,
                            shell=(os.name == "nt"))
    except FileNotFoundError:
        sys.exit(f"No se encontró la CLI de gcloud ({GCLOUD_CLI}). Define POC_GCLOUD_CLI si no está en el PATH.")
    if r.returncode != 0 or not r.stdout.strip():
        sys.exit(f"gcloud auth print-access-token falló: {r.stderr.strip()}")
    return r.stdout.strip()


def consultar_startup_latencies(project, service_name, ini_utc, fin_utc, token):
    """Baja todas las series/puntos de
    run.googleapis.com/container/startup_latencies para el servicio y la
    ventana dados, siguiendo paginación si la hay. Devuelve la lista cruda de
    timeSeries (posiblemente vacía)."""
    filtro = (
        'metric.type="run.googleapis.com/container/startup_latencies" AND '
        f'resource.labels.service_name="{service_name}"'
    )
    series = []
    page_token = None
    while True:
        params = {
            "filter": filtro,
            "interval.startTime": _rfc3339(ini_utc),
            "interval.endTime": _rfc3339(fin_utc),
        }
        if page_token:
            params["pageToken"] = page_token
        url = MONITORING_URL.format(project=project) + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                cuerpo = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", errors="replace")
            sys.exit(f"Cloud Monitoring API devolvió HTTP {e.code}: {detalle[:500]}")
        except urllib.error.URLError as e:
            sys.exit(f"No se pudo contactar la API de Cloud Monitoring: {e}")
        series += cuerpo.get("timeSeries", [])
        page_token = cuerpo.get("nextPageToken")
        if not page_token:
            break
    return series


def _rango_bucket(i, scale, growth_factor, num_finite_buckets):
    """Límites [inferior, superior) del bucket i de un histograma exponencial
    (definición de Cloud Monitoring ExponentialBuckets):
      bucket 0             : [0, scale)
      bucket i (1..N)       : [scale*growth^(i-1), scale*growth^i)
      bucket N+1 (overflow) : [scale*growth^N, +inf)
    """
    if i == 0:
        return 0.0, scale
    if i <= num_finite_buckets:
        return scale * growth_factor ** (i - 1), scale * growth_factor ** i
    return scale * growth_factor ** num_finite_buckets, math.inf


def _valor_representativo_bucket(i, scale, growth_factor, num_finite_buckets):
    """Valor aproximado que representa al bucket i: punto medio geométrico
    (sqrt(lo*hi)) para buckets finitos y con lo>0; scale/2 para el bucket 0
    (lo=0, la media geométrica no está definida); el límite inferior para el
    bucket de desborde (no tiene límite superior)."""
    lo, hi = _rango_bucket(i, scale, growth_factor, num_finite_buckets)
    if i == 0:
        return scale / 2
    if math.isinf(hi):
        return lo
    return math.sqrt(lo * hi)


def percentiles_desde_buckets(bucket_counts, scale, growth_factor, num_finite_buckets, percentiles):
    """Aproxima percentiles a partir de un histograma de buckets exponenciales
    ya fusionado (sumado bucket a bucket entre todos los puntos de la
    ventana). No son exactos: cada percentil se aproxima con el valor
    representativo (ver _valor_representativo_bucket) del primer bucket cuyo
    conteo acumulado alcanza ese percentil de la masa total. Devuelve un
    dict {p: valor_ms} o {p: None} si no hay datos."""
    total = sum(bucket_counts)
    if total <= 0:
        return {p: None for p in percentiles}
    resultado = {}
    for p in percentiles:
        objetivo = total * p / 100
        acumulado = 0.0
        valor = None
        for i, c in enumerate(bucket_counts):
            acumulado += c
            if acumulado >= objetivo:
                valor = _valor_representativo_bucket(i, scale, growth_factor, num_finite_buckets)
                break
        if valor is None:  # objetivo no alcanzado por redondeo: último bucket no vacío
            for i in range(len(bucket_counts) - 1, -1, -1):
                if bucket_counts[i] > 0:
                    valor = _valor_representativo_bucket(i, scale, growth_factor, num_finite_buckets)
                    break
        resultado[p] = valor
    return resultado


def _fusionar_puntos(puntos):
    """Suma count, count*mean y bucketCounts (alineados por índice, rellenando
    con ceros el histograma más corto) de una lista de
    value.distributionValue. Asume que todos comparten la misma
    bucketOptions.exponentialBuckets (scale/growthFactor/numFiniteBuckets);
    si no es así se usa la del primer punto y se avisa por stderr."""
    if not puntos:
        return 0, 0.0, [], None
    primero = puntos[0]["bucketOptions"]["exponentialBuckets"]
    scale = float(primero["scale"])
    growth = float(primero["growthFactor"])
    n_finitos = int(primero["numFiniteBuckets"])
    largo = n_finitos + 2  # bucket 0 + N finitos + overflow
    fusion = [0] * largo
    total_count = 0
    suma_media_por_count = 0.0
    for dv in puntos:
        eb = dv["bucketOptions"]["exponentialBuckets"]
        if eb != primero:
            print("Aviso: puntos con bucketOptions distintas; se usa la del "
                  "primer punto para el histograma fusionado (percentiles "
                  "pueden perder precisión).", file=sys.stderr)
        # La API serializa los int64 (bucketCounts, count) como strings JSON.
        counts = [int(c) for c in dv.get("bucketCounts", [])]
        for i, c in enumerate(counts):
            if i < largo:
                fusion[i] += c
            else:
                fusion[-1] += c  # exceso cae al overflow
        cnt = int(dv.get("count", 0))
        total_count += cnt
        suma_media_por_count += cnt * float(dv.get("mean", 0.0))
    media = suma_media_por_count / total_count if total_count else 0.0
    return total_count, media, fusion, (scale, growth, n_finitos)


def resumir(series):
    """Devuelve (resumen_por_revision: {revision: dict}, resumen_total: dict).
    Cada dict trae n, media_ms, p50_ms, p95_ms."""
    por_revision = {}
    for serie in series:
        rev = (serie.get("resource", {}).get("labels") or {}).get("revision_name", "(desconocida)")
        puntos = [p["value"]["distributionValue"] for p in serie.get("points", [])
                  if "distributionValue" in p.get("value", {})]
        por_revision.setdefault(rev, []).extend(puntos)

    resumen_por_revision = {}
    todos_los_puntos = []
    for rev, puntos in por_revision.items():
        n, media, fusion, params = _fusionar_puntos(puntos)
        if params:
            pcts = percentiles_desde_buckets(fusion, params[0], params[1], params[2], [50, 95])
        else:
            pcts = {50: None, 95: None}
        resumen_por_revision[rev] = {"n": n, "media_ms": media, "p50_ms": pcts[50], "p95_ms": pcts[95]}
        todos_los_puntos.extend(puntos)

    n_tot, media_tot, fusion_tot, params_tot = _fusionar_puntos(todos_los_puntos)
    if params_tot:
        pcts_tot = percentiles_desde_buckets(fusion_tot, params_tot[0], params_tot[1], params_tot[2], [50, 95])
    else:
        pcts_tot = {50: None, 95: None}
    resumen_total = {"n": n_tot, "media_ms": media_tot, "p50_ms": pcts_tot[50], "p95_ms": pcts_tot[95]}
    return resumen_por_revision, resumen_total


def _fmt(v):
    return f"{v:.1f}" if isinstance(v, (int, float)) else "--"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", nargs="*", default=["data/mediciones_*.csv"],
                    help="uno o más CSV de mediciones (acepta comodines)")
    ap.add_argument("--margen-min", type=float, default=2,
                    help="minutos de margen antes/después de la ventana de Cloud Run (default: 2)")
    args = ap.parse_args()

    cfg = cargar_config()
    plat = cfg["plataformas"]["google-cloud-run"]
    project = plat["gcloud_project"]
    service_name = plat["gcloud_service_name"]

    filas_cr = leer_filas_cloudrun(args.csv)
    ini_utc, fin_utc = ventana_utc(filas_cr, args.margen_min)
    print(f"Ventana (UTC, ±{args.margen_min:g} min): {_rfc3339(ini_utc)} .. {_rfc3339(fin_utc)}")

    token = obtener_token_acceso()
    series = consultar_startup_latencies(project, service_name, ini_utc, fin_utc, token)
    if not series:
        sys.exit("La API de Cloud Monitoring no devolvió series para "
                  "container/startup_latencies en esa ventana (¿el servicio no "
                  "arrancó ningún contenedor nuevo, o falta roles/monitoring.viewer?).")

    por_revision, total = resumir(series)
    if total["n"] == 0:
        sys.exit("Se encontraron series pero sin arranques (count=0) en la ventana.")

    print(f"\n{'revisión':40s} {'n':>5s} {'media':>9s} {'p50~':>9s} {'p95~':>9s}")
    filas_out = []
    for rev, r in sorted(por_revision.items()):
        print(f"{rev:40s} {r['n']:5d} {_fmt(r['media_ms']):>9s} {_fmt(r['p50_ms']):>9s} {_fmt(r['p95_ms']):>9s}")
        filas_out.append({
            "ventana_inicio_utc": _rfc3339(ini_utc), "ventana_fin_utc": _rfc3339(fin_utc),
            "revision": rev, "n_arranques": r["n"], "media_ms": _fmt(r["media_ms"]),
            "p50_aprox_ms": _fmt(r["p50_ms"]), "p95_aprox_ms": _fmt(r["p95_ms"]),
        })
    print(f"{'TODAS':40s} {total['n']:5d} {_fmt(total['media_ms']):>9s} "
          f"{_fmt(total['p50_ms']):>9s} {_fmt(total['p95_ms']):>9s}")
    filas_out.append({
        "ventana_inicio_utc": _rfc3339(ini_utc), "ventana_fin_utc": _rfc3339(fin_utc),
        "revision": "TODAS", "n_arranques": total["n"], "media_ms": _fmt(total["media_ms"]),
        "p50_aprox_ms": _fmt(total["p50_ms"]), "p95_aprox_ms": _fmt(total["p95_ms"]),
    })

    os.makedirs(os.path.join(RAIZ, "results"), exist_ok=True)
    ruta = os.path.join(RAIZ, "results/cloudrun_startup.csv")
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ventana_inicio_utc", "ventana_fin_utc", "revision",
                                           "n_arranques", "media_ms", "p50_aprox_ms", "p95_aprox_ms"])
        w.writeheader()
        w.writerows(filas_out)
    print(f"\n-> {ruta}")


if __name__ == "__main__":
    main()
