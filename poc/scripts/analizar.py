#!/usr/bin/env python3
"""
PoC TI-05 · TERABYTE · Resumen estadístico y gráfico de data/mediciones.csv.

Produce
-------
  results/resumen.csv        p50 / p95 / media / n por plataforma × modo × estado
  results/resumen_latex.txt  filas listas para pegar en la tabla poc-resumen de main.tex
  results/poc-coldstart.png  gráfico (si matplotlib está instalado: pip install matplotlib)

Uso
---
  python scripts/analizar.py
  python scripts/analizar.py --csv data/mediciones_20260919-1850_natural.csv data/mediciones_2026*_forzado.csv
"""

import argparse
import csv
import os
import statistics
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOMBRES = {"aws-lambda": "AWS Lambda", "cloudflare-workers": "Cloudflare Workers",
           "google-cloud-run": "Google Cloud Run"}


def _forzables():
    import json
    try:
        with open(os.path.join(RAIZ, "config.json"), encoding="utf-8") as f:
            cfg = json.load(f)
        return {k for k, v in cfg["plataformas"].items() if v.get("forzable")}
    except Exception:
        return {"aws-lambda"}


FORZABLES = _forzables()


def pct(vals, p):
    if not vals:
        return None
    s = sorted(vals)
    k = (len(s) - 1) * p / 100
    lo, hi = int(k), min(int(k) + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def leer_csvs(patrones):
    """Lee y concatena los CSV indicados (o data/mediciones_*.csv por defecto)."""
    import glob
    patrones = patrones or ["data/mediciones_*.csv"]
    rutas = []
    for pat in patrones:
        rutas += sorted(glob.glob(os.path.join(RAIZ, pat)))
    # nunca leer salidas de logs_lambda.py (contienen filas duplicadas de Lambda)
    rutas = [r for r in rutas if not os.path.basename(r).startswith(("lambda_", "mediciones_lambda_join"))]
    if not rutas:
        raise SystemExit(f"No se encontraron CSV para {patrones}")
    filas = []
    for ruta in rutas:
        with open(ruta, encoding="utf-8") as f:
            filas += [r for r in csv.DictReader(f) if r["error"] == "" and r["latencia_ms"]]
    print("Archivos leídos:")
    for r in rutas:
        print("  -", os.path.relpath(r, RAIZ))
    print(f"Filas válidas: {len(filas)}\n")
    return filas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", nargs="*", default=None,
                    help="uno o más CSV (acepta comodines). Por defecto: data/mediciones_*.csv")
    args = ap.parse_args()

    filas = leer_csvs(args.csv)

    # (plataforma, modo, estado) -> [latencias]
    grupos = defaultdict(list)
    grupos_todo = defaultdict(list)  # (plataforma, estado) juntando modos
    for r in filas:
        estado = "frio" if r["es_frio"] == "True" else "caliente"
        lat = float(r["latencia_ms"])
        # El modo "forzado" solo se aplica a plataformas con "forzable": true en
        # config.json (Lambda vía POC_MARKER, Workers vía wrangler deploy). Las
        # demás se miden en la misma ventana pero sin forzar nada: sus filas se
        # agrupan como "observado" para no sugerir un forzado que no existe.
        modo = r["modo"] if r["plataforma"] in FORZABLES else "observado"
        grupos[(r["plataforma"], modo, estado)].append(lat)
        grupos_todo[(r["plataforma"], estado)].append(lat)

    os.makedirs(os.path.join(RAIZ, "results"), exist_ok=True)

    # ---- resumen.csv ----
    out = []
    for (plat, modo, est), v in sorted(grupos.items()):
        out.append({"plataforma": plat, "modo": modo, "estado": est, "n": len(v),
                    "p50_ms": f"{pct(v,50):.1f}", "p95_ms": f"{pct(v,95):.1f}",
                    "media_ms": f"{statistics.mean(v):.1f}",
                    "min_ms": f"{min(v):.1f}", "max_ms": f"{max(v):.1f}"})
    for (plat, est), v in sorted(grupos_todo.items()):
        out.append({"plataforma": plat, "modo": "todos", "estado": est, "n": len(v),
                    "p50_ms": f"{pct(v,50):.1f}", "p95_ms": f"{pct(v,95):.1f}",
                    "media_ms": f"{statistics.mean(v):.1f}",
                    "min_ms": f"{min(v):.1f}", "max_ms": f"{max(v):.1f}"})
    with open(os.path.join(RAIZ, "results/resumen.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader(); w.writerows(out)

    # ---- tabla en pantalla ----
    print(f"{'plataforma':20s} {'modo':8s} {'estado':9s} {'n':>4s} {'p50':>8s} {'p95':>8s} {'media':>8s}")
    for o in out:
        print(f"{o['plataforma']:20s} {o['modo']:8s} {o['estado']:9s} {str(o['n']):>4s} "
              f"{o['p50_ms']:>8s} {o['p95_ms']:>8s} {o['media_ms']:>8s}")

    # ---- penalización de frío ----
    print("\nPenalización de arranque en frío (p50 frío - p50 caliente, todos los modos):")
    for plat in sorted({p for (p, _) in grupos_todo}):
        fr, ca = grupos_todo.get((plat, "frio"), []), grupos_todo.get((plat, "caliente"), [])
        if fr and ca:
            print(f"  {NOMBRES.get(plat, plat):20s} {pct(fr,50) - pct(ca,50):8.1f} ms")

    # ---- filas LaTeX para la tabla poc-resumen de main.tex ----
    lineas = []
    for plat in sorted({p for (p, _) in grupos_todo}):
        fr, ca = grupos_todo.get((plat, "frio"), []), grupos_todo.get((plat, "caliente"), [])
        if not fr or not ca:
            continue
        n_txt = f"n={len(fr)}/{len(ca)}"
        lineas.append(
            f"    \\filaTabla{{{NOMBRES.get(plat, plat)} & {pct(fr,50):.0f} & {pct(fr,95):.0f} & "
            f"{pct(ca,50):.0f} & {pct(ca,95):.0f} & {n_txt} / REGION / FECHA}}"
        )
    with open(os.path.join(RAIZ, "results/resumen_latex.txt"), "w", encoding="utf-8") as f:
        f.write("% Pegar dentro de \\tabla{...}{poc-resumen}{...}{ en main.tex; completar REGION/FECHA\n")
        f.write("\n".join(lineas) + "\n")
    print("\nFilas LaTeX -> results/resumen_latex.txt")

    # ---- gráfico ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.ticker
    except ImportError:
        print("matplotlib no instalado: sin gráfico (pip install matplotlib)")
        return

    plats = sorted({p for (p, _) in grupos_todo})
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    datos, etiquetas, colores, posiciones = [], [], [], []
    pos = 1.0
    for i, plat in enumerate(plats):
        for est, col in (("frio", "#c0504d"), ("caliente", "#4f81bd")):
            v = grupos_todo.get((plat, est), [])
            if v:
                datos.append(v)
                etiquetas.append(f"{NOMBRES.get(plat, plat)}\n{est} (n={len(v)})")
                colores.append(col)
                posiciones.append(pos)
                pos += 1.0
        pos += 0.6  # separación visual entre plataformas
    try:
        bp = ax.boxplot(datos, positions=posiciones, widths=0.7, tick_labels=etiquetas,
                        patch_artist=True, showfliers=True)
    except TypeError:  # matplotlib < 3.9
        bp = ax.boxplot(datos, positions=posiciones, widths=0.7, labels=etiquetas,
                        patch_artist=True, showfliers=True)
    for patch, col in zip(bp["boxes"], colores):
        patch.set_facecolor(col); patch.set_alpha(0.75)
    # mediana anotada sobre cada caja
    for x, v in zip(posiciones, datos):
        med = pct(v, 50)
        ax.annotate(f"{med:.0f} ms", (x + 0.38, med), textcoords="offset points", xytext=(4, -3),
                    ha="left", fontsize=8)
    ax.set_ylabel("Latencia total desde el cliente (ms)")
    ax.set_ylim(0, max(max(v) for v in datos) * 1.12)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax.set_title("Latencia en arranque en frío vs. caliente, por plataforma")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    ruta = os.path.join(RAIZ, "results/poc-coldstart.png")
    fig.savefig(ruta, dpi=160)
    print(f"Gráfico -> {ruta}")


if __name__ == "__main__":
    main()
