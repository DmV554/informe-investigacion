#!/usr/bin/env python3
"""
PoC TI-05 · TERABYTE · Extrae los logs de solicitud de Cloud Run y los cruza
con data/mediciones_*.csv por trace id.

Por qué
-------
Es opcional (validación cruzada, análoga a logs_lambda.py pero con el dato
que expone Cloud Run). Cada log de solicitud (logName terminado en
"requests") trae, medido por Google y sin red de por medio:
  httpRequest.latency      latencia del lado del servidor
  httpRequest.status       código HTTP
  labels.instanceId        instancia de Cloud Run que respondió
  resource.labels.revision_name  revisión que respondió
El `trace` del log se arma a partir del header X-Cloud-Trace-Context que
manda el cliente (medir.py no lo manda hoy; si no hay trace, el cruce por id
no es posible y solo sirve el resumen por ventana de tiempo). El cruce
primario de esta PoC es por `request_id` cuando la función lo expuso en la
respuesta y quedó en el CSV de mediciones.

Requiere gcloud CLI autenticada y rol roles/logging.viewer sobre el proyecto.

Uso
---
  python scripts/logs_cloudrun.py
      Lee todos los data/mediciones_*.csv (excluye salidas previas y
      cualquier archivo que empiece con "cloudrun_"), toma la ventana de
      tiempo de las filas de google-cloud-run, baja los logs de esa ventana
      y escribe data/cloudrun_report.csv y data/cloudrun_join.csv.
"""

import csv
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(RAIZ, "config.json")


def _resolver_gcloud_cli():
    """Misma resolución que medir.py: POC_GCLOUD_CLI, "gcloud" o "gcloud.cmd"
    (WSL con la CLI instalada en Windows)."""
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


def leer_mediciones(patrones):
    """Concatena los CSV de data/ (por defecto data/mediciones_*.csv),
    excluyendo salidas previas de este mismo script y de logs_lambda.py."""
    import glob
    rutas = []
    for pat in patrones:
        rutas += sorted(glob.glob(os.path.join(RAIZ, pat)))
    if not rutas:
        sys.exit(f"No se encontraron CSV para {patrones}")
    rutas = [r for r in rutas if not os.path.basename(r).startswith(
        ("lambda_", "mediciones_lambda_join", "cloudrun_"))]
    filas = []
    for ruta in rutas:
        with open(ruta, encoding="utf-8") as f:
            filas += list(csv.DictReader(f))
    print("CSV leídos:", ", ".join(os.path.relpath(r, RAIZ) for r in rutas))
    return filas


def ventana(filas_cr):
    """Ventana ±2 min alrededor de las filas de Cloud Run. timestamp_local es
    hora local naive; se convierte a UTC ISO con astimezone() (usa la zona
    horaria del sistema que corrió medir.py)."""
    ts = [datetime.fromisoformat(r["timestamp_local"]) for r in filas_cr]
    ini = (min(ts) - timedelta(minutes=2)).astimezone()
    fin = (max(ts) + timedelta(minutes=2)).astimezone()
    to_iso_utc = lambda d: d.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    return to_iso_utc(ini), to_iso_utc(fin)


def bajar_logs(service_name, project, t_ini_iso, t_fin_iso):
    filtro = (
        'resource.type="cloud_run_revision" AND '
        f'resource.labels.service_name="{service_name}" AND '
        'logName:"requests" AND '
        f'timestamp>="{t_ini_iso}" AND timestamp<="{t_fin_iso}"'
    )
    cmd = [GCLOUD_CLI, "logging", "read", filtro, "--project", project,
           "--format", "json", "--limit", "5000", "--order", "asc"]
    r = subprocess.run(cmd, capture_output=True, text=True, shell=(os.name == "nt"))
    if r.returncode != 0:
        sys.exit(f"gcloud logging read falló: {r.stderr.strip()}")
    try:
        return json.loads(r.stdout or "[]")
    except json.JSONDecodeError as e:
        sys.exit(f"Salida de gcloud logging read no es JSON válido: {e}")


def _latencia_ms(valor):
    """httpRequest.latency viene como cadena tipo "0.012345s"."""
    if not valor:
        return ""
    try:
        return f"{float(str(valor).rstrip('s')) * 1000:.3f}"
    except ValueError:
        return ""


def parsear(entradas):
    filas = []
    for e in entradas:
        trace = e.get("trace") or ""
        trace_id = trace.split("/")[-1] if trace else ""
        http_req = e.get("httpRequest", {}) or {}
        filas.append({
            "trace_id": trace_id,
            "timestamp": e.get("timestamp", ""),
            "cr_latency_ms": _latencia_ms(http_req.get("latency")),
            "cr_status": http_req.get("status", ""),
            "cr_instance_id": (e.get("labels") or {}).get("instanceId", ""),
            "cr_revision": (e.get("resource", {}).get("labels") or {}).get("revision_name", ""),
        })
    return filas


def escribir(ruta, filas, columnas):
    ruta_abs = os.path.join(RAIZ, ruta)
    with open(ruta_abs, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        w.writerows(filas)
    return ruta_abs


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", nargs="*", default=["data/mediciones_*.csv"],
                    help="uno o más CSV de mediciones (acepta comodines)")
    args = ap.parse_args()
    cfg = cargar_config()
    plat = cfg["plataformas"]["google-cloud-run"]
    service_name = plat["gcloud_service_name"]
    project = plat["gcloud_project"]

    med = leer_mediciones(args.csv)
    filas_cr = [r for r in med if r["plataforma"] == "google-cloud-run" and r.get("request_id")]
    if not filas_cr:
        sys.exit("No hay filas de google-cloud-run con request_id en el CSV.")

    t_ini, t_fin = ventana(filas_cr)
    print(f"Bajando logs de solicitud de {service_name} entre {t_ini} y {t_fin} (UTC)")
    logs = parsear(bajar_logs(service_name, project, t_ini, t_fin))
    print(f"Logs de solicitud encontrados: {len(logs)}")

    p1 = escribir("data/cloudrun_report.csv", logs,
                  list(logs[0].keys()) if logs else ["trace_id"])
    print(f"-> {p1}")

    por_trace = {r["trace_id"]: r for r in logs if r["trace_id"]}
    join = []
    sin_match = 0
    for r in filas_cr:
        log = por_trace.get(r["request_id"])
        if log is None:
            sin_match += 1
            log = {}
        fila = dict(r)
        fila.update({
            "cr_latency_ms": log.get("cr_latency_ms", ""),
            "cr_status": log.get("cr_status", ""),
            "cr_instance_id": log.get("cr_instance_id", ""),
            "cr_revision": log.get("cr_revision", ""),
        })
        try:
            fila["resto_red_plataforma_ms"] = (
                f"{float(r['latencia_ms']) - float(log['cr_latency_ms']):.1f}"
                if log.get("cr_latency_ms") else ""
            )
        except ValueError:
            fila["resto_red_plataforma_ms"] = ""
        join.append(fila)

    cols = list(join[0].keys())
    p2 = escribir("data/cloudrun_join.csv", join, cols)
    print(f"-> {p2}   (filas sin log correspondiente: {sin_match}; "
          f"si es >0, espera y vuelve a correr: los logs demoran en llegar)")

    # Chequeo de consistencia: para filas frías (es_frio == "True"), ¿cambió
    # cr_instance_id respecto a la fila anterior de Cloud Run?
    anterior = None
    frias_evaluadas = 0
    frias_consistentes = 0
    for fila in join:
        actual = fila.get("cr_instance_id") or None
        if fila.get("es_frio") == "True":
            frias_evaluadas += 1
            if anterior is not None and actual is not None and actual != anterior:
                frias_consistentes += 1
        if actual is not None:
            anterior = actual
    print(f"Consistencia frío(cliente) vs cambio de cr_instance_id: "
          f"{frias_consistentes}/{frias_evaluadas} filas frías coinciden")


if __name__ == "__main__":
    main()
