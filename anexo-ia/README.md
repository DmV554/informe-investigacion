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
      exportar_conversacion.py   ← opcional: exporta una sesión de Claude Code (jsonl) a markdown
  <nombre-apellido>/             ← una carpeta por integrante, en minúsculas y con guion
      B-prompts.md               ← todos sus prompts, cronológicos, agrupados por sesión y herramienta
      C-evidencia.md             ← enlaces a las conversaciones (si la herramienta los da) + commits del integrante
      registros/                 ← opcional: solo si el integrante conservó transcripciones
```

Cada integrante crea **su propia carpeta** y no toca las de los demás. Quien no usó IA en ninguna sección (nivel 0 en todo) igual declara nivel 0 en el Anexo A; la carpeta es obligatoria solo para niveles 2 y 3.

### Qué va en cada archivo

`B-prompts.md` empieza con una cabecera fija: trabajo, secciones cubiertas, nivel declarado por sección (con una frase de qué hizo la IA y qué hizo la persona), herramientas con versión o modelo, período. Después, los prompts **literales**, numerados y en orden cronológico, agrupados por sesión; cada sesión con herramienta, enlace (cuando existe) y fechas. Si una parte del texto literal no se conservó, se dice expresamente y se reconstruye a partir del registro disponible, marcándola como reconstrucción. No se resumen ni se "limpian" los prompts.

`C-evidencia.md` lista, por sesión, el enlace a la conversación cuando la herramienta lo provee (o la razón de que no exista), y la lista de commits del integrante (`git log --oneline --author=<nombre>`), que es el historial de versiones que pide el punto 6.3. La evidencia principal es el propio repositorio: los prompts literales versionados y el historial de `informe/main.tex`.

### Reglas

1. **Un registro por uso, no por herramienta.** Si una misma conversación sirvió a dos secciones, se registra una vez y se indican ambas secciones.
2. **Los agentes de búsqueda o verificación también se declaran** (nivel 2), aunque el texto final sea humano: el prompt que se les dio es el prompt efectivamente empleado.
3. **Nivel por sección, coherente con el 6.1.** En las secciones protegidas el nivel declarado es 0 o 1; si una conversación tocó una de ellas, en `B-prompts.md` se explica qué parte fue apoyo de formato o estilo (nivel 1) y qué quedó fuera del texto.
4. **Nada de credenciales ni datos personales de terceros** en los registros (revisar antes de subir).
5. **Fecha de cierre.** El índice de abajo se congela con el commit de entrega, etiquetado `entrega` en `main`; ese hash se escribe en la parte C del Anexo A.

## Índice (se imprime en el Anexo A, parte B)

Ordenado por número de sección principal. Nivel: el máximo declarado por el integrante, con el desglose entre paréntesis.

| # | Integrante | Sección(es) | Nivel | Herramientas | Archivos |
|---|---|---|---|---|---|
| 1 | Daniel Miranda | Resumen ejecutivo e introducción (borradores); 3.1 Alternativas adicionales; Anexo D; Anexo E (síntesis del cuadro); plantilla LaTeX, bibliografía y organización del repositorio; estándar del Anexo A; reducción de extensión (formato) | 2 (búsqueda y verificación de fuentes, borradores, formato, organización); 1 (estilo en 3.1) | Claude (Cowork, `claude-fable-5-1`); agente de investigación externo (Grok, xAI), sin registros accesibles | `daniel-miranda/B-prompts.md`, `daniel-miranda/C-evidencia.md` |
| 2 | Matías Reyes | 1 Marco teórico; 2.1 Modelos de ejecución y aislamiento | 2 (búsqueda de fuentes y revisión del borrador de 1); 1 (2.1 párrafos 1–2); 0 (2.1 párrafo 3) | Claude (Cowork, `claude-opus-5`) | `matias-reyes/B-prompts.md`, `matias-reyes/C-evidencia.md`, `matias-reyes/registros/` |
| 3 | Isidora Cisternas | 2.2 Arranque en frío; 2.5 WebAssembly y WASI | 3 (redacción asistida sobre borradores propios en 2.2 y 2.5); 2 (búsqueda de cifras); 0–1 (párrafo de cierre de 2.5) | Claude (chat web claude.ai, `claude-opus-5`) | `isidora-cisternas/B-prompts.md`, `isidora-cisternas/C-evidencia.md` |
| 4 | Francisca Abarca | 2.3 Facturación por consumo; 4.2 Modelo de costos; Anexo C | 2 (selección de fuentes, orden, estilo, script y tabla de sensibilidad); 1 (análisis, supuestos y decisiones) | Claude (chat web, Claude 3.5 Sonnet / Claude 3 Opus) | `francisca-abarca/B-prompts.md`, `francisca-abarca/C-evidencia.md` |
| 5 | Valentina Guzmán | 2.4 Diseño orientado a eventos; criterios de 3.2; 3.1 lista «Datos sin servidor» y Anexo D; 4 preguntas del cuestionario | 2 (búsqueda y verificación de fuentes con NotebookLM); 1 (estilo); 0–1 (análisis y criterios) | NotebookLM (Google) operado a través de Claude por MCP (`claude-opus-5`, `claude-sonnet-5`) | `valentina-guzman/B-prompts.md`, `valentina-guzman/C-evidencia.md` |
| 6 | Fabián Solís | 2.6 Límites y dependencia del proveedor; 4.3 Caso TERABYTE; 5 Tendencias y riesgos | 0 (sin uso de IA declarado; no hay carpeta) | — | — |
| 7 | Claudio Toledo | 3.1 (búsqueda y verificación de candidatos); 3.2 filas Google, borde y código abierto y consolidación; bibliografía de sus fuentes; cuestionario (Anexo Q) | 2 (búsqueda y verificación en documentación oficial, traducción de resúmenes, esquemas); 1 (volcado a LaTeX; redacción del cuestionario); 0 (dos párrafos de análisis de 3.2) | Claude Code 2.1.271–2.1.278 (`claude-opus-5`); Claude (Cowork) | `claudio-toledo/B-prompts.md`, `claudio-toledo/C-evidencia.md`, `claudio-toledo/registros/` |
| 8 | Rodolfo Fernández | 3.2 Cuadro comparativo, filas AWS y Azure | 3 (extracción de cifras y redacción de celdas desde documentación oficial, verificadas por el autor); 2 (apoyo de estudio y organización) | Claude (chat en Proyecto, `claude-sonnet-5`; sesiones de escritorio, `claude-opus-5`); Gemini (Google) | `rodolfo-fernandez/B-prompts.md`, `rodolfo-fernandez/C-evidencia.md` |
| 9 | Vicente Arratia | 4.1 Prueba de concepto; Anexo B | 2 (código auxiliar de la prueba, formato y transcripción a LaTeX) | Claude (Cowork, `claude-fable-5-1`); Claude Code 2.1.278 (`claude-opus-5`, `claude-fable-5-1`) | `vicente-arratia/B-prompts.md`, `vicente-arratia/C-evidencia.md`, `vicente-arratia/registros/`, `vicente-arratia/cowork/` |

Conclusiones y recomendación (todo el grupo): existe un borrador generado con IA sobre los hechos ya establecidos en el informe (declarado en `daniel-miranda/B-prompts.md`, prompt 62); el texto entregado lo revisa y reescribe el grupo, y su nivel final se declara en la parte A del Anexo A.
