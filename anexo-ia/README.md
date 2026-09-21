# Anexo A · Declaración de uso de inteligencia artificial — evidencia trazable

Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE (Empresa 6), ICI-5444, PUCV.

Esta carpeta es la **evidencia** que respalda el Anexo A del informe (`informe/main.tex`, bloque `>>> ANEXO A`). El Anexo A impreso contiene la declaración por sección e integrante (parte A), el índice de esta carpeta (parte B), la referencia al repositorio y su commit de entrega (parte C) y las firmas (parte D). Los prompts completos y las conversaciones viven aquí, no en el PDF.

Base normativa: punto 6 de las *Indicaciones del Trabajo de Investigación 2026* (FEP00.3.26). En resumen: el nivel se declara **por sección**, no global; se indican herramienta y versión; para niveles 2 y 3 se entregan los **prompts efectivamente empleados** y **evidencia trazable** (enlace o exportación de la conversación y el historial de versiones); **cada integrante declara lo suyo**; y en las secciones del punto 6.1 (análisis comparativo y criterios, conclusiones, párrafo de aporte, discusión crítica, cuestionario, y toda cifra, cita o referencia) el nivel solo puede ser 0 o 1.

## Estándar del grupo

### Estructura

```
anexo-ia/
  README.md                      ← este archivo: estándar + índice (se imprime en el Anexo A)
  _plantilla/                    ← copiar para empezar
      B-prompts.md
      C-evidencia.md
  _herramientas/
      exportar_conversacion.py   ← exporta una sesión de Claude Code (jsonl) a markdown
  <nombre-apellido>/             ← una carpeta por integrante, en minúsculas y con guion
      B-prompts.md               ← todos sus prompts, cronológicos, agrupados por sesión y herramienta
      C-evidencia.md             ← enlaces o exportaciones de conversaciones + commits de sus ramas
      registros/                 ← exportaciones (md, pdf, json) de cada conversación
```

Cada integrante crea **su propia carpeta** y no toca las de los demás. Quien no usó IA en ninguna sección (nivel 0 en todo) igual crea su carpeta con un `B-prompts.md` que lo declare en una línea; el anexo es obligatorio aunque el nivel sea 0.

### Qué va en cada archivo

`B-prompts.md` empieza con una cabecera fija: trabajo, secciones cubiertas, nivel declarado por sección (con una frase de qué hizo la IA y qué hizo la persona), herramientas con versión o modelo, período. Después, los prompts **literales**, numerados y en orden cronológico, agrupados por sesión; cada sesión con herramienta, enlace y fechas. Si una parte del texto literal no se conservó, se dice expresamente y se reconstruye a partir del registro disponible, marcándola como reconstrucción. No se resumen ni se "limpian" los prompts.

`C-evidencia.md` lista, por sesión, el enlace a la conversación (si la herramienta lo da) y el archivo exportado en `registros/`; y la lista de commits de las ramas del integrante (`git log --oneline` de su rama o de los archivos que tocó), que es el historial de versiones que pide el punto 6.3. Si la exportación completa es muy larga, se guarda igual en `registros/` y en `C-evidencia.md` se indexa.

### Reglas

1. **Un registro por uso, no por herramienta.** Si una misma conversación sirvió a dos secciones, se registra una vez y se indican ambas secciones.
2. **Los agentes de búsqueda o verificación también se declaran** (nivel 2), aunque el texto final sea humano: el prompt que se les dio es el prompt efectivamente empleado.
3. **Nivel por sección, coherente con el 6.1.** En las secciones protegidas el nivel declarado es 0 o 1; si una conversación tocó una de ellas, en `B-prompts.md` se explica qué parte fue apoyo de formato o estilo (nivel 1) y qué quedó fuera del texto.
4. **Nada de credenciales ni datos personales de terceros** en las exportaciones (revisar antes de subir).
5. **Fecha de cierre.** El índice de abajo se congela con el commit de entrega; ese hash se escribe en la parte C del Anexo A.

### Cómo exportar una conversación

- **Claude (Cowork o chat web):** Configuración → Privacidad → Exportar datos; llega un enlace por correo. También sirve el enlace de la sesión (`https://claude.ai/code/session_...`), indicando que es accesible con la cuenta del usuario.
- **Claude Code:** `python3 anexo-ia/_herramientas/exportar_conversacion.py --sesion <archivo.jsonl> --salida <carpeta>` genera `prompts.md` y `conversacion.md`.
- **Otras herramientas (ChatGPT, Grok, Gemini, Copilot):** usar la exportación nativa o el enlace de "compartir"; si no existe, copiar la conversación completa a un `.md` y declarar que es copia manual.

## Índice (se imprime en el Anexo A, parte B)

| # | Integrante | Sección(es) | Nivel | Herramientas | Archivos |
|---|---|---|---|---|---|
| 1 | Vicente Arratia | 4.1 Prueba de concepto; Anexo B | 2 | Claude (Cowork, `claude-fable-5-1`); Claude Code 2.1.278 (`claude-opus-5`, `claude-fable-5-1`) | `vicente-arratia/B-prompts.md`, `vicente-arratia/C-evidencia.md`, `vicente-arratia/registros/`, `vicente-arratia/cowork/` |
| 2 | Daniel Miranda | 3.1 Alternativas adicionales; Anexo D; plantilla LaTeX y organización del repositorio; Anexo A (estándar) | 2 (búsqueda y verificación de fuentes, formato, organización); 1 (corrección de estilo en 3.1) | Claude (Cowork, `claude-fable-5-1`); agente de investigación externo (Grok, xAI) para búsqueda y verificación de fuentes | `daniel-miranda/B-prompts.md`, `daniel-miranda/C-evidencia.md`, `daniel-miranda/registros/` |
| 3 | *(integrante)* | *(secciones)* | *(0–3 por sección)* | *(herramienta y versión)* | `<nombre-apellido>/…` |

Cada integrante agrega su fila al hacer su commit. Las filas se ordenan por número de sección principal.
