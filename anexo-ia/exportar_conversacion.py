#!/usr/bin/env python3
"""
Exporta una sesión de Claude Code a Markdown legible, a partir del registro
JSONL que la herramienta guarda en ~/.claude/projects/<proyecto>/<sesion>.jsonl.

Genera dos archivos:
  prompts.md       solo las instrucciones escritas por la persona, numeradas y
                   con fecha y hora (para la parte B del anexo de declaración).
  conversacion.md  la conversación completa: instrucciones de la persona,
                   respuestas del modelo y un resumen de cada herramienta
                   ejecutada (para la parte C, evidencia trazable).

Uso
---
  python3 exportar_conversacion.py                      # sesión más reciente del proyecto
  python3 exportar_conversacion.py --jsonl <ruta>       # una sesión concreta
  python3 exportar_conversacion.py --salida <carpeta>
"""

import argparse
import glob
import json
import os
from datetime import datetime

PROYECTO_POR_DEFECTO = os.path.expanduser(
    "~/.claude/projects/-home-rev-repos-informe-investigacion"
)


def hora_local(iso):
    """Convierte el timestamp UTC del registro a hora local legible."""
    if not iso:
        return ""
    try:
        return (datetime.fromisoformat(iso.replace("Z", "+00:00"))
                .astimezone().strftime("%d-%m-%Y %H:%M"))
    except ValueError:
        return iso


def texto_de(contenido):
    """El contenido puede ser una cadena o una lista de bloques tipados."""
    if isinstance(contenido, str):
        return contenido.strip()
    if not isinstance(contenido, list):
        return ""
    partes = []
    for bloque in contenido:
        if isinstance(bloque, dict) and bloque.get("type") == "text":
            partes.append(bloque.get("text", "").strip())
    return "\n\n".join(p for p in partes if p)


def es_prompt_humano(evento):
    """Descarta resultados de herramientas, recordatorios del sistema y
    mensajes de subagentes: deja solo lo que la persona escribió."""
    if evento.get("type") != "user" or evento.get("isSidechain"):
        return False
    if evento.get("userType") not in (None, "external"):
        return False
    contenido = evento.get("message", {}).get("content")
    if isinstance(contenido, list) and any(
        isinstance(b, dict) and b.get("type") == "tool_result" for b in contenido
    ):
        return False
    texto = texto_de(contenido)
    if not texto or texto.startswith("<system-reminder>"):
        return False
    # Los comandos locales de la herramienta (/model, /effort, /context…) se
    # registran como eventos de usuario, pero no son instrucciones al modelo.
    if any(m in texto for m in ("<local-command-caveat>", "<command-name>",
                                "<local-command-stdout>")):
        return False
    # Eventos que la herramienta inyecta como "usuario" pero que no escribió
    # la persona: avisos de tareas en segundo plano, el archivo de una imagen
    # adjunta (el texto del prompt va en otro evento) y el cuerpo de una
    # habilidad cargada.
    if texto.startswith(("<task-notification>", "[Image: source:",
                         "Base directory for this skill:", "## Context Usage")):
        return False
    return True


def herramientas_de(evento):
    """Nombres de las herramientas invocadas en un mensaje del modelo."""
    contenido = evento.get("message", {}).get("content")
    if not isinstance(contenido, list):
        return []
    return [b.get("name", "?") for b in contenido
            if isinstance(b, dict) and b.get("type") == "tool_use"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jsonl", default=None, help="registro de la sesión a exportar")
    ap.add_argument("--proyecto", default=PROYECTO_POR_DEFECTO)
    ap.add_argument("--salida", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--hasta", default=None,
                    help="excluye los eventos desde esta hora local (DD-MM-YYYY HH:MM) en adelante")
    args = ap.parse_args()

    ruta = args.jsonl
    if not ruta:
        candidatos = sorted(glob.glob(os.path.join(args.proyecto, "*.jsonl")),
                            key=os.path.getmtime)
        if not candidatos:
            raise SystemExit(f"No hay registros de sesión en {args.proyecto}")
        ruta = candidatos[-1]

    eventos = []
    for linea in open(ruta, encoding="utf-8"):
        try:
            eventos.append(json.loads(linea))
        except json.JSONDecodeError:
            continue  # líneas truncadas por un cierre abrupto

    if args.hasta:
        eventos = [e for e in eventos
                   if not e.get("timestamp") or hora_local(e["timestamp"]) < args.hasta
                   or hora_local(e["timestamp"])[:10] != args.hasta[:10]
                   and hora_local(e["timestamp"]) < args.hasta]
    modelos = sorted({e.get("message", {}).get("model") for e in eventos
                      if e.get("type") == "assistant" and e.get("message", {}).get("model")})

    sesion = next((e.get("sessionId") for e in eventos if e.get("sessionId")), "?")
    version = next((e.get("version") for e in eventos if e.get("version")), "?")
    fechas = [e.get("timestamp") for e in eventos if e.get("timestamp")]
    encabezado = (
        f"- Herramienta: Claude Code {version}\n"
        f"- Identificador de sesión: `{sesion}`\n"
        f"- Registro de origen: `{os.path.basename(ruta)}`\n"
        f"- Modelos: {', '.join(modelos) if modelos else '?'}\n"
        f"- Inicio: {hora_local(min(fechas)) if fechas else '?'}\n"
        f"- Fin: {hora_local(max(fechas)) if fechas else '?'}\n"
    )

    os.makedirs(args.salida, exist_ok=True)

    # ---- prompts.md ----
    prompts = [e for e in eventos if es_prompt_humano(e)]
    with open(os.path.join(args.salida, "prompts.md"), "w", encoding="utf-8") as f:
        f.write("# Prompts utilizados — sección 4.1 (prueba de concepto)\n\n")
        f.write(encabezado)
        f.write(f"- Total de instrucciones de la persona: {len(prompts)}\n\n")
        f.write("Transcripción literal, en orden cronológico, tal como fueron escritas.\n\n---\n\n")
        for i, e in enumerate(prompts, 1):
            f.write(f"## Prompt {i} — {hora_local(e.get('timestamp'))}\n\n")
            f.write("```text\n" + texto_de(e["message"]["content"]) + "\n```\n\n")

    # ---- conversacion.md ----
    with open(os.path.join(args.salida, "conversacion.md"), "w", encoding="utf-8") as f:
        f.write("# Conversación completa — sección 4.1 (prueba de concepto)\n\n")
        f.write(encabezado)
        f.write("\nDe cada intervención del modelo se transcribe el texto y se listan las\n"
                "herramientas que ejecutó (lectura y escritura de archivos, comandos y\n"
                "consultas a documentación). La salida de esas herramientas no se incluye\n"
                "por extensión; el registro original la conserva íntegra.\n\n---\n\n")
        n = 0
        for e in eventos:
            if es_prompt_humano(e):
                n += 1
                f.write(f"## Persona — prompt {n} — {hora_local(e.get('timestamp'))}\n\n")
                f.write("```text\n" + texto_de(e["message"]["content"]) + "\n```\n\n")
            elif e.get("type") == "assistant" and not e.get("isSidechain"):
                texto = texto_de(e.get("message", {}).get("content"))
                usos = herramientas_de(e)
                if not texto and not usos:
                    continue
                f.write(f"### Claude Code — {hora_local(e.get('timestamp'))}\n\n")
                if texto:
                    f.write(texto + "\n\n")
                if usos:
                    f.write(f"*Herramientas ejecutadas: {', '.join(usos)}*\n\n")

    print(f"Sesión: {sesion}  ({len(prompts)} instrucciones de la persona)")
    print(f"-> {os.path.join(args.salida, 'prompts.md')}")
    print(f"-> {os.path.join(args.salida, 'conversacion.md')}")


if __name__ == "__main__":
    main()
