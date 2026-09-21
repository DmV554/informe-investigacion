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


N_MIN_PERCENTIL = 5  # muestras mínimas para reportar p50/p95 de un estado


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
        if (r["plataforma"] == "google-cloud-run" and r["modo"] == "forzado"
                and r["n_en_ciclo"] == "0" and r["es_frio"] != "True"):
            # Primera petición del ciclo en Cloud Run que NO resultó fría: la
            # plataforma ya tenía un contenedor despierto antes de que esta
            # petición saliera del cliente (con gcloud_env, el health check de
            # la revisión nueva; con cloudrun_salir, el reemplazo proactivo del
            # contenedor caído; ver criterio uptime_menor_que_latencia). No es
            # una muestra caliente "limpia" ni frío percibido por el cliente:
            # se separa en su propio estado para no contaminar "caliente".
            estado = "forzado-sin-frio"
        else:
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
        if ca and len(fr) < N_MIN_PERCENTIL:
            # Plataforma con muestras calientes pero sin frío visible desde el
            # cliente bajo el protocolo forzado (ver estado "forzado-sin-frio").
            print(f"  {NOMBRES.get(plat, plat):20s} sin frío visible desde el cliente "
                  f"(n={len(fr)} < {N_MIN_PERCENTIL})")
        elif fr and ca:
            print(f"  {NOMBRES.get(plat, plat):20s} {pct(fr,50) - pct(ca,50):8.1f} ms")

    # ---- filas LaTeX para la tabla poc-resumen de main.tex ----
    lineas = []
    for plat in sorted({p for (p, _) in grupos_todo}):
        fr, ca = grupos_todo.get((plat, "frio"), []), grupos_todo.get((plat, "caliente"), [])
        if not ca:
            # Sin muestras calientes no hay fila que mostrar (no ocurre hoy).
            continue
        # Un percentil sobre 1-4 observaciones no describe nada: si el frío
        # visible desde el cliente no llega a N_MIN_PERCENTIL muestras, la fila
        # deja las columnas de frío en blanco y anota cuántas hubo.
        if len(fr) >= N_MIN_PERCENTIL:
            n_txt = f"n={len(fr)}/{len(ca)}"
            lineas.append(
                f"    \\filaTabla{{{NOMBRES.get(plat, plat)} & {pct(fr,50):.0f} & {pct(fr,95):.0f} & "
                f"{pct(ca,50):.0f} & {pct(ca,95):.0f} & {n_txt} / REGION / FECHA}}"
            )
        else:
            # Frío no visible desde el cliente bajo el protocolo forzado (ver
            # estado "forzado-sin-frio" más arriba): se deja la fila con las
            # columnas de frío en blanco en vez de omitir la plataforma.
            n_txt = f"n={len(fr)}/{len(ca)}"
            lineas.append(
                f"    \\filaTabla{{{NOMBRES.get(plat, plat)} & -- & -- & "
                f"{pct(ca,50):.0f} & {pct(ca,95):.0f} & {n_txt} / REGION / FECHA}} "
                f"% frío no visible desde el cliente; ver results/cloudrun_startup.csv"
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

    # Un panel por plataforma con eje Y compartido: el nombre de la plataforma
    # va una sola vez como título del panel y las cajas se etiquetan solo
    # "frío"/"caliente", así ninguna etiqueta se pisa con la vecina. La
    # penalización (p50 frío − p50 caliente) va como subtítulo: es el dato que
    # la sección 4.1 comenta. Colores por estado (frío azul, caliente naranja);
    # la identidad la lleva el texto del eje, el color solo la refuerza.
    COLOR = {"frio": "#2a78d6", "caliente": "#eb6834"}
    TEXTO, TEXTO_2 = "#0b0b0b", "#52514e"
    NOTA = {
        "cloudflare-workers": "frío = isolate recién creado (first_request);\nel cliente no lo percibe",
        "google-cloud-run": "frío = contenedor creado por la petición\n(uptime < latencia)",
        "aws-lambda": "frío = entorno de ejecución nuevo\n(instance_id distinto)",
    }
    plats = sorted({p for (p, _) in grupos_todo})
    fig, axes = plt.subplots(1, len(plats), figsize=(9.2, 4.0), sharey=True)
    if len(plats) == 1:
        axes = [axes]
    y_max = max(max(v) for (_, e), v in grupos_todo.items() if e in COLOR)
    rng = __import__("random").Random(7)  # jitter reproducible para los puntos atípicos
    for ax, plat in zip(axes, plats):
        estados = [e for e in ("frio", "caliente") if grupos_todo.get((plat, e))]
        datos = [grupos_todo[(plat, e)] for e in estados]
        posiciones = [i * 1.35 for i in range(len(estados))]  # aire para la etiqueta de mediana
        bp = ax.boxplot(datos, positions=posiciones, widths=0.46, patch_artist=True,
                        showfliers=False, whis=1.5,
                        medianprops={"color": TEXTO, "linewidth": 1.6},
                        whiskerprops={"color": TEXTO_2, "linewidth": 1},
                        capprops={"color": TEXTO_2, "linewidth": 1},
                        boxprops={"linewidth": 0})
        for patch, e in zip(bp["boxes"], estados):
            patch.set_facecolor(COLOR[e]); patch.set_alpha(0.85)
        # Puntos atípicos: fuera de los bigotes (1.5·IQR), pequeños, con aro
        # blanco y jitter horizontal para que no se apilen unos sobre otros.
        for x, v, e in zip(posiciones, datos, estados):
            q1, q3 = pct(v, 25), pct(v, 75)
            lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
            atip = [y for y in v if y < lo or y > hi]
            if atip:
                xs = [x + rng.uniform(-0.12, 0.12) for _ in atip]
                ax.scatter(xs, atip, s=14, color=COLOR[e], edgecolors="white",
                           linewidths=0.8, zorder=3)
            # Mediana como única etiqueta directa, a la derecha de la caja.
            ax.annotate(f"{pct(v, 50):.0f} ms", (x + 0.25, pct(v, 50)),
                        textcoords="offset points", xytext=(4, 0), ha="left",
                        va="center", fontsize=8.5, color=TEXTO)
        ax.set_xticks(posiciones)
        ax.set_xticklabels([f"{e.replace('frio', 'frío')}\n(n={len(v)})"
                            for e, v in zip(estados, datos)], fontsize=9, color=TEXTO)
        ax.set_xlim(-0.6, posiciones[-1] + 0.95)
        fr, ca = grupos_todo.get((plat, "frio"), []), grupos_todo.get((plat, "caliente"), [])
        if len(fr) >= N_MIN_PERCENTIL and ca:
            sub = f"penalización p50: {pct(fr, 50) - pct(ca, 50):+.0f} ms"
        else:
            sub = "frío no visible desde el cliente"
        ax.set_title(f"{NOMBRES.get(plat, plat)}\n{sub}", fontsize=10.5, color=TEXTO,
                     loc="left", pad=8)
        ax.text(0.0, -0.24, NOTA.get(plat, ""), transform=ax.transAxes, fontsize=7.5,
                color=TEXTO_2, va="top", ha="left", style="italic")
        ax.grid(axis="y", color="#e6e5e1", linewidth=0.8)
        ax.set_axisbelow(True)
        for lado in ("top", "right"):
            ax.spines[lado].set_visible(False)
        for lado in ("left", "bottom"):
            ax.spines[lado].set_color("#c3c2b7")
        ax.tick_params(colors=TEXTO_2, length=0)
    axes[0].set_ylabel("Latencia total desde el cliente (ms)", color=TEXTO)
    axes[0].set_ylim(0, y_max * 1.10)
    axes[0].yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    fig.suptitle("Latencia en arranque en frío vs. caliente, por plataforma "
                 "(25 ciclos forzados, cliente en Chile)", fontsize=11.5, color=TEXTO, x=0.01,
                 ha="left", y=0.985)
    # Márgenes fijos en vez de tight_layout: las notas bajo cada panel y el
    # subtítulo de dos líneas hacían que tight_layout dejara demasiado aire.
    fig.subplots_adjust(left=0.085, right=0.985, top=0.78, bottom=0.27, wspace=0.28)
    ruta = os.path.join(RAIZ, "results/poc-coldstart.png")
    fig.savefig(ruta, dpi=200, facecolor="white")
    fig.savefig(ruta[:-4] + ".pdf", facecolor="white")
    print(f"Gráfico -> {ruta}")


if __name__ == "__main__":
    main()
