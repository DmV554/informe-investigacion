#!/usr/bin/env python3
"""
Arma los dos documentos del anexo de declaración de uso de IA (sección 4.1 y
Anexo B del informe) a partir de los registros exportados:

  B-prompts.md      Parte B del Anexo A: todos los prompts de la persona, en
                    orden cronológico, agrupados por sesión y herramienta.
  C-evidencia.md    Parte C del Anexo A: las conversaciones completas
                    (registro de Cowork + las dos sesiones de Claude Code) y
                    la lista de commits del repositorio que permiten
                    reconstruir cómo se produjo el código y el texto.

Entradas (misma carpeta salvo que se indique otra):
  cowork/registro-conversacion-cowork.md   registro de la sesión Cowork
  <exp>/prompts.md, <exp>/conversacion.md  salida de exportar_conversacion.py
                                           por cada sesión de Claude Code

Uso
---
  python3 armar_anexo.py --sesion <carpeta_exportada> [--sesion ...]
"""

import argparse
import os
import re
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
COWORK = os.path.join(AQUI, "cowork", "registro-conversacion-cowork.md")


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def encabezado_sesion(prompts_md):
    """Las líneas '- Clave: valor' del encabezado que escribe el exportador."""
    lineas = []
    for l in prompts_md.splitlines()[1:]:
        if l.startswith("- "):
            lineas.append(l)
        elif lineas:
            break
    return "\n".join(lineas)


def bloques_prompts(prompts_md):
    """[(fecha, texto)] a partir de '## Prompt N — fecha' + bloque ```text.
    Se corta por encabezado y se toma hasta el ÚLTIMO cierre del bloque, por
    si el propio prompt contenía un bloque de código pegado."""
    salida = []
    trozos = re.split(r"^## Prompt \d+ — ", prompts_md, flags=re.M)[1:]
    for t in trozos:
        fecha, _, resto = t.partition("\n")
        ini = resto.find("```text\n")
        fin = resto.rfind("\n```")
        if ini < 0 or fin < 0:
            continue
        salida.append((fecha.strip(), resto[ini + len("```text\n"):fin]))
    return salida


def cowork_partes(md):
    """Devuelve (encabezado, parte_A, turnos_usuario_parte_B)."""
    ia = md.index("## Parte A")
    ib = md.index("## Parte B")
    encabezado = md[:ia].strip()
    parte_a = md[ia:ib].strip()
    parte_b = md[ib:]
    turnos = re.findall(r"^### \[([^\]\n]+)\] Usuario\n\n(.*?)(?=^### \[|\Z)", parte_b, re.S | re.M)
    return encabezado, parte_a, [(f, t.strip()) for f, t in turnos]


def demover(md):
    """Baja un nivel los títulos para que el documento tenga un solo H1, sin
    tocar las líneas que están dentro de bloques de código (allí un '#' es
    un comentario citado literalmente)."""
    salida, en_bloque = [], False
    for l in md.splitlines():
        if l.lstrip().startswith("```"):
            en_bloque = not en_bloque
        elif not en_bloque and re.match(r"^#{1,5} ", l):
            l = "#" + l
        salida.append(l)
    return "\n".join(salida)


def commits():
    try:
        return subprocess.run(
            ["git", "-C", RAIZ, "log", "--date=format:%d-%m-%Y %H:%M",
             "--pretty=format:- `%h` %ad — %s", "main..PoC", "--", "poc/", "informe/"],
            capture_output=True, text=True, check=True).stdout.strip()
    except Exception as e:  # sin git o sin la rama: se deja constancia
        return f"(no se pudo leer el historial: {e})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sesion", action="append", required=True,
                    help="carpeta con prompts.md y conversacion.md de una sesión de Claude Code")
    ap.add_argument("--salida", default=AQUI)
    args = ap.parse_args()

    cw_enc, cw_a, cw_turnos = cowork_partes(leer(COWORK))
    sesiones = []
    for carpeta in args.sesion:
        pm = leer(os.path.join(carpeta, "prompts.md"))
        cm = leer(os.path.join(carpeta, "conversacion.md"))
        sesiones.append((encabezado_sesion(pm), bloques_prompts(pm), cm))

    intro = (
        "**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, "
        "PUCV ICI-5444.\n"
        "**Secciones cubiertas:** 4.1 Prueba de concepto: arranque en frío y latencia; "
        "Anexo B: código y mediciones de la prueba de concepto.\n"
        "**Nivel declarado:** 2 (colaboración e ideación). La IA generó el código auxiliar de la "
        "prueba (funciones, script de medición, análisis y guías de despliegue), identificado como "
        "tal en el Anexo B, y participó en la discusión metodológica. Las decisiones de método las "
        "tomó el autor en cada caso (constan en los prompts); las mediciones provienen de la "
        "ejecución real del código; la interpretación, las limitaciones y toda conclusión son de "
        "redacción humana.\n"
        "**Herramientas:** Claude (Anthropic), modo Cowork, modelo `claude-fable-5-1`; "
        "Claude Code 2.1.278 con los modelos `claude-opus-5` y `claude-fable-5-1`.\n"
        "**Período:** 17-09-2026 a 21-09-2026.\n"
    )

    # ------------------------------------------------------------------ B
    b = ["# Anexo A — Parte B: prompts utilizados (sección 4.1 y Anexo B)\n", intro,
         "\nLos prompts se transcriben en orden cronológico, tal como fueron escritos, agrupados por "
         "sesión. La primera parte de la sesión de Cowork no conservó su texto literal (corte de "
         "contexto de la herramienta) y se presenta como reconstrucción; todo lo demás es literal.\n",
         "\n---\n", "\n## Sesión 1 — Claude (Cowork), 17-09 a 20-09-2026\n", "\n" + cw_enc.split("\n", 1)[1].strip() + "\n",
         "\n### 1.a Reconstrucción cronológica (sin texto literal)\n",
         "\n" + demover(cw_a.split("\n", 1)[1]).strip() + "\n",
         "\n### 1.b Prompts literales\n"]
    for i, (fecha, texto) in enumerate(cw_turnos, 1):
        b.append(f"\n#### Cowork — prompt {i} — {fecha}\n\n{texto}\n")
    for n, (enc, prompts, _) in enumerate(sesiones, 2):
        b.append(f"\n---\n\n## Sesión {n} — Claude Code\n\n{enc}\n- Prompts de la persona: {len(prompts)}\n")
        for i, (fecha, texto) in enumerate(prompts, 1):
            b.append(f"\n#### Sesión {n} — prompt {i} — {fecha}\n\n````text\n{texto}\n````\n")
    with open(os.path.join(args.salida, "B-prompts.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(b))

    # ------------------------------------------------------------------ C
    c = ["# Anexo A — Parte C: evidencia trazable (sección 4.1 y Anexo B)\n", intro,
         "\n## Índice\n",
         "\n1. Historial de versiones: commits de la rama `PoC` del repositorio del grupo.\n"
         "2. Registro de la sesión de Cowork (reconstrucción + transcripción literal).\n"]
    for n, (enc, prompts, _) in enumerate(sesiones, 2):
        c[-1] += f"{n + 1}. Conversación completa de la sesión {n} de Claude Code.\n"
    c.append("\nDe cada intervención del modelo se transcribe el texto y se listan las herramientas "
             "que ejecutó; la salida de esas herramientas (contenido de archivos, resultados de "
             "comandos) no se incluye por extensión y queda en los registros originales, "
             "disponibles a requerimiento.\n")
    c.append("\n---\n\n## 1. Historial de versiones (rama `PoC`, carpetas `poc/` e `informe/`)\n\n"
             + commits() + "\n")
    c.append("\n---\n\n## 2. Registro de la sesión de Cowork\n\n" + demover(leer(COWORK)).strip() + "\n")
    for n, (enc, prompts, conv) in enumerate(sesiones, 2):
        cuerpo = conv.split("---\n", 1)[1] if "---\n" in conv else conv
        c.append(f"\n---\n\n## {n + 1}. Conversación completa — sesión {n} de Claude Code\n\n{enc}\n\n"
                 + demover(cuerpo).strip() + "\n")
    with open(os.path.join(args.salida, "C-evidencia.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(c))

    print(f"-> {os.path.join(args.salida, 'B-prompts.md')}")
    print(f"-> {os.path.join(args.salida, 'C-evidencia.md')}")


if __name__ == "__main__":
    main()
