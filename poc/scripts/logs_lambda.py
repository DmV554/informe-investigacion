#!/usr/bin/env python3
"""
PoC TI-05 · TERABYTE · Extrae las líneas REPORT de CloudWatch para la Lambda
y las cruza con data/mediciones.csv por RequestId.

Por qué
-------
La línea REPORT trae, medido por AWS y sin red de por medio:
  Duration        tiempo del handler
  Billed Duration tiempo cobrado (incluye la inicialización en el frío)
  Init Duration   SOLO en el primer request de cada instancia = arranque en frío
Cruzarla con la latencia medida desde el cliente permite descomponer el
total en inicialización + ejecución + red.

Uso
---
  python scripts/logs_lambda.py
      Lee todos los data/mediciones_*.csv (o los que indique --csv), toma la
      ventana de tiempo de las filas de aws-lambda, baja los REPORT de esa
      ventana y escribe data/lambda_report.csv y data/lambda_join.csv.

Requiere AWS CLI configurada.
"""

import csv
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone


def _resolver_aws_cli():
    """Misma resolución que medir.py: POC_AWS_CLI, "aws", "aws.exe" (WSL) o la
    ruta de instalación habitual en Windows."""
    candidatos = [os.environ.get("POC_AWS_CLI"), shutil.which("aws"), shutil.which("aws.exe"),
                  "/mnt/c/Program Files/Amazon/AWSCLIV2/aws.exe"]
    for c in candidatos:
        if c and os.path.isfile(c):
            return c
    return "aws"


AWS_CLI = _resolver_aws_cli()

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(RAIZ, "config.json")

RE_REPORT = re.compile(
    r"REPORT RequestId: (?P<rid>[0-9a-f-]+)\s+Duration: (?P<dur>[\d.]+) ms\s+"
    r"Billed Duration: (?P<billed>\d+) ms\s+Memory Size: (?P<mem>\d+) MB\s+"
    r"Max Memory Used: (?P<maxmem>\d+) MB(?:\s+Init Duration: (?P<init>[\d.]+) ms)?"
)


def cargar_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def leer_mediciones(patrones):
    """Concatena los CSV de data/ (por defecto data/mediciones_*.csv)."""
    import glob
    rutas = []
    for pat in patrones:
        rutas += sorted(glob.glob(os.path.join(RAIZ, pat)))
    if not rutas:
        sys.exit(f"No se encontraron CSV para {patrones}")
    rutas = [r for r in rutas if not os.path.basename(r).startswith(("lambda_", "mediciones_lambda_join"))]
    filas = []
    for ruta in rutas:
        with open(ruta, encoding="utf-8") as f:
            filas += list(csv.DictReader(f))
    print("CSV leídos:", ", ".join(os.path.relpath(r, RAIZ) for r in rutas))
    return filas


def ventana(filas_lambda):
    ts = [datetime.fromisoformat(r["timestamp_local"]) for r in filas_lambda]
    ini = min(ts) - timedelta(minutes=2)
    fin = max(ts) + timedelta(minutes=2)
    # los timestamps del CSV son hora local naive; se convierten a epoch ms
    # asumiendo la zona local del sistema
    to_ms = lambda d: int(d.astimezone(timezone.utc).timestamp() * 1000)
    return to_ms(ini.astimezone()), to_ms(fin.astimezone())


def bajar_reports(log_group, region, t_ini_ms, t_fin_ms):
    eventos = []
    token = None
    while True:
        cmd = [AWS_CLI, "logs", "filter-log-events", "--log-group-name", log_group,
               "--region", region, "--filter-pattern", "REPORT",
               "--start-time", str(t_ini_ms), "--end-time", str(t_fin_ms),
               "--output", "json"]
        if token:
            cmd += ["--next-token", token]
        r = subprocess.run(cmd, capture_output=True, text=True, shell=(os.name == "nt"))
        if r.returncode != 0:
            sys.exit(f"aws logs filter-log-events falló: {r.stderr.strip()}")
        data = json.loads(r.stdout or "{}")
        eventos += data.get("events", [])
        token = data.get("nextToken")
        # CloudWatch puede devolver páginas vacías con token; se sigue hasta
        # que no haya token.
        if not token:
            break
    return eventos


def parsear(eventos):
    filas = []
    for ev in eventos:
        m = RE_REPORT.search(ev.get("message", ""))
        if not m:
            continue
        filas.append({
            "request_id": m["rid"],
            "log_stream": ev.get("logStreamName", ""),
            "ts_cloudwatch": datetime.fromtimestamp(ev["timestamp"] / 1000, tz=timezone.utc).isoformat(),
            "duration_ms": m["dur"],
            "billed_ms": m["billed"],
            "memory_mb": m["mem"],
            "max_memory_mb": m["maxmem"],
            "init_duration_ms": m["init"] or "",
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
    plat = cfg["plataformas"]["aws-lambda"]
    med = leer_mediciones(args.csv)
    filas_lambda = [r for r in med if r["plataforma"] == "aws-lambda" and r["request_id"]]
    if not filas_lambda:
        sys.exit("No hay filas de aws-lambda con request_id en el CSV.")

    t_ini, t_fin = ventana(filas_lambda)
    print(f"Bajando REPORT de {plat['aws_log_group']} entre "
          f"{datetime.fromtimestamp(t_ini/1000)} y {datetime.fromtimestamp(t_fin/1000)} (hora local)")
    reports = parsear(bajar_reports(plat["aws_log_group"], plat["region"], t_ini, t_fin))
    print(f"REPORT encontrados: {len(reports)}  (con Init Duration: "
          f"{sum(1 for r in reports if r['init_duration_ms'])})")

    p1 = escribir("data/lambda_report.csv", reports, list(reports[0].keys()) if reports else
                  ["request_id"])
    print(f"-> {p1}")

    por_rid = {r["request_id"]: r for r in reports}
    join = []
    sin_match = 0
    for r in filas_lambda:
        rep = por_rid.get(r["request_id"])
        if rep is None:
            sin_match += 1
            rep = {}
        fila = dict(r)
        fila.update({
            "cw_duration_ms": rep.get("duration_ms", ""),
            "cw_billed_ms": rep.get("billed_ms", ""),
            "cw_init_duration_ms": rep.get("init_duration_ms", ""),
            "cw_log_stream": rep.get("log_stream", ""),
        })
        # latencia medida desde el cliente menos lo que AWS reporta como
        # (init + duration) = aproximación de red + overhead de la plataforma
        try:
            interno = float(rep.get("duration_ms") or 0) + float(rep.get("init_duration_ms") or 0)
            fila["resto_red_plataforma_ms"] = f"{float(r['latencia_ms']) - interno:.1f}" if rep else ""
        except ValueError:
            fila["resto_red_plataforma_ms"] = ""
        join.append(fila)

    cols = list(join[0].keys())
    p2 = escribir("data/lambda_join.csv", join, cols)
    print(f"-> {p2}   (filas sin REPORT correspondiente: {sin_match}; "
          f"si es >0, espera un minuto y vuelve a correr: los logs demoran en llegar)")

    # Chequeo de consistencia: frío según el cliente vs. Init Duration según AWS
    coincide = sum(1 for f in join if (f["es_frio"] == "True") == bool(f["cw_init_duration_ms"]))
    print(f"Consistencia frío(cliente) vs Init Duration(AWS): {coincide}/{len(join)} filas coinciden")


if __name__ == "__main__":
    main()
