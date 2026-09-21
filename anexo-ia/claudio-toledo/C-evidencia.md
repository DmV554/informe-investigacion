# Anexo A — Parte C: evidencia trazable (3.1, 3.2 y bibliografía)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Claudio Patricio Toledo Mac-lean.
**Secciones cubiertas:** 3.1 Alternativas adicionales (búsqueda y verificación de candidatos); 3.2 Cuadro comparativo (mitad Google, Cloudflare, Fastly, Deno/Vercel/Netlify y código abierto, más la consolidación de la mitad de AWS y Azure); bibliografía de las fuentes a mi cargo.

## 1. Conversaciones

| # | Herramienta | Fechas | Enlace | Exportación en `registros/` | Secciones |
|---|---|---|---|---|---|
| 1 | Claude Code 2.1.271 (`claude-opus-5`), sesión `d4406eea-e25d-4bef-a2fe-4e0b7442cca2` | 18-09-2026 02:46 a 19-09-2026 14:58 | sin enlace estable (herramienta local) | `claude-code-sesion-d4406eea-prompts.md`, `claude-code-sesion-d4406eea-conversacion.md` | Bibliografía; apoyo a 3.1 y 3.2 |
| 2 | Claude Code 2.1.278 (`claude-opus-5`), sesión `cf21efe1-8c94-4839-9cd4-c78d63bcdf68` | 19-09-2026 12:28 a 20-09-2026 21:36 | sin enlace estable (herramienta local) | `claude-code-sesion-cf21efe1-prompts.md`, `claude-code-sesion-cf21efe1-conversacion.md` | 3.1; 3.2; organización del trabajo |
| 3 | Claude (Cowork / aplicación de escritorio) usada como agente de navegador | 20-09-2026 | *(pendiente: enlace o exportación de la conversación)* | `cowork/` (los cinco encargos pegados) y `cowork/salidas/` (lo que devolvió) | 3.1 y 3.2, levantamiento de datos en documentación oficial |

Las exportaciones de las sesiones de Claude Code se generaron con `anexo-ia/_herramientas/exportar_conversacion.py` a partir del registro interno que la herramienta guarda de cada sesión (`~/.claude/projects/<proyecto>/<sesión>.jsonl`). El archivo `-prompts.md` contiene solo lo que escribió la persona; el `-conversacion.md`, además, las respuestas del modelo y la lista de herramientas que ejecutó en cada paso.

Pendiente de completar antes de la entrega: el enlace o la exportación de la conversación de Cowork (fila 3) y la confirmación del modelo y la versión de esa herramienta.

## 2. Historial de versiones (commits del integrante)

Rama propia: `3.2-Cloud-Fastly-Deno`. Salida de `git log --oneline --author="Claudio"`:

- `2fb598c` 20-09-2026 22:28 — feat-documentation: seccion parte 3.2a y 3.2b
  (`informe/main.tex`, `informe/referencias.bib`, `trabajo/3.2-cuadro/Tablas-3.2-Definitivas.md`, `trabajo/3.2-cuadro/mis-filas-3.2.md`, `trabajo/3.2-cuadro/mitad-google-cloudflare-fastly-deno-oss.csv`, `.gitignore`)
- `7c50b74` 20-09-2026 23:22 — feat-docs: Se agregan los parrafos de la seccion 3.2 y documentacion de las tablas
  (`informe/main.tex`, `trabajo/3.2-cuadro/Tablas-3.2-Definitivas.md`)

Ninguno de los dos mensajes de commit lleva coautoría de IA: los commits se hicieron a mano y la declaración del uso es la que consta en este anexo. El historial completo de la rama, con el estado de cada archivo antes y después, está en el repositorio del grupo (https://github.com/DmV554/informe-investigacion) y se reconstruye con `git log --follow informe/main.tex`.

## 3. Qué produjo la IA y qué produjo la persona

**3.1 Alternativas adicionales.** La IA ordenó el esquema de la sección, armó los listados de plataformas candidatas a revisar, estructuró los criterios de inclusión y descarte que después consolidó Daniel Miranda, y redactó los encargos que se le pegaron al agente de navegador. La verificación de cada candidata en la documentación oficial (existencia del producto, límites publicados, precio de lista o solo cotización, estado del proyecto) y la decisión sobre cuáles proponer son propias, y están registradas en `registros/cowork/salidas/`. El texto de 3.1 que aparece en el informe y la selección final de las diez alternativas son de Daniel Miranda, que declara su propia fila.

**3.2 Cuadro comparativo, filas a mi cargo (Google, Cloudflare, Fastly, Deno/Vercel/Netlify y código abierto).** La IA buscó en la documentación oficial y transcribió a las tablas de trabajo los límites de tiempo, memoria, *payload*, concurrencia, egreso y los precios de lista, siempre acompañados de la URL y la fecha de consulta; también armó la estructura de las tablas 3.2a, 3.2b y 3.2c a partir del esqueleto del grupo. La revisión celda por celda contra la página oficial, la elección de qué plataformas entran y en qué fila, y la armonización con la mitad de AWS y Azure son propias. Ninguna cifra del cuadro proviene de lo que el modelo supiera: todas salen de la fuente citada.

**3.2 Cuadro comparativo, dos párrafos de análisis.** De autoría humana. Se escribieron a partir del borrador v3 de Rodolfo Fernández y de la validación cruzada de las filas, y reemplazan el `% TODO (Rodolfo)` de `informe/main.tex` en el commit `7c50b74`. Ese texto no aparece en ninguna de las transcripciones de las sesiones de esta carpeta, que se conservan íntegras y pueden revisarse.

**3.2, volcado a LaTeX.** Apoyo de formato: el paso de las tablas de markdown a los entornos `longtable` de la plantilla `inf-pucv` y la comprobación de que el documento compilara. No alteró el contenido de las celdas ni el texto de los párrafos.

**Bibliografía de las fuentes a mi cargo.** La IA leyó los PDF, tradujo al español los *abstracts*, dio el formato de fila de la planilla del grupo y comparó fortalezas y debilidades entre artículos para apoyar la decisión de cuáles usar. Los DOI y las entradas BibTeX se tomaron de Crossref y de los propios PDF. Qué artículo entra en qué sección, y cuáles se descartan, es decisión propia: consta en `DatosChatsAnteriores/Revision-papers.md` y `Analisis-pros-contras.md`, fuera del repositorio.

**Este Anexo A.** La IA revisó las tres sesiones, exportó los registros a `registros/` y redactó el borrador de esta declaración. Los niveles declarados, lo que queda pendiente y la firma son decisión del integrante.
