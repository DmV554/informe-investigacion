# Anexo A — Parte C: evidencia trazable (3.1, Anexo D, plantilla y organización)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Daniel Ignacio Miranda Vázquez.
**Secciones cubiertas:** 3.1 Alternativas adicionales; Anexo D; plantilla LaTeX y organización del repositorio; estándar del Anexo A; estructura (no contenido) de 3.2.

## 1. Conversaciones

| # | Herramienta | Fechas | Enlace | Exportación en `registros/` | Secciones |
|---|---|---|---|---|---|
| 1 | Claude (Cowork), `claude-fable-5-1` | 19-09 a 21-09-2026 | https://claude.ai/code/session_01GKFjHaKv49e4JnUS1XjGv4 (accesible con la cuenta del usuario) | *[pendiente: exportación de datos de la cuenta, Configuración → Privacidad → Exportar datos]* | 3.1, Anexo D, plantilla, repositorio, estructura 3.2, Anexo A |
| 2 | Grok (xAI), agente de investigación | 19-09 a 20-09-2026 | sin enlace estable | *[TODO Daniel: exportar o copiar a `registros/grok-*.md`]* | búsqueda y verificación de fuentes para 3.1 y 3.2; guía de elección; estructuración de decisiones; corrección de estilo del borrador de 3.1 |

Los prompts de sistema entregados al agente externo están versionados en `trabajo/fuentes/guia-agentes-busqueda-fuentes.md` y `trabajo/3.1-alternativas/prompt-verificacion-candidatos.md`; sus salidas, en `archivosTemporal/fuentes_agent/`, `trabajo/fuentes/` y `trabajo/3.1-alternativas/`.

## 2. Historial de versiones (commits del integrante)

Rama `daniel/3.1-alternativas-anexo-d`, integrada en `main` el 21-09-2026, más correcciones posteriores al merge:

- `dcf6540` 19-09-2026 — Organización inicial y plantilla LaTeX/overleaf inicial
- `a45404d` 19-09-2026 — Indicaciones actualizadas, subida pautas de investigacion (ppt) y cambios de la plantilla overleaf (claude)
- `8c2b9f3` 20-09-2026 — 3.1 / Anexo D: criterios D.1, registro D.2-D.6 con citas, pool bib, estructura 3.2 y guías de trabajo
- `f550ffa` 20-09-2026 — Anexo D completo: criterios D.1 (I3 seis dimensiones, X2 retiro/archivo, desempate paso 5), registro D.2-D.6 con 32 candidatos y D.7
- `cf50cd5` 20-09-2026 — 3.1 Alternativas adicionales: texto y tabla; D.1 fuentes de descubrimiento; ref a anexos por letra
- `45e07f6` 21-09-2026 — referencias.bib: reparar entradas rotas por el merge (wen2023, ribeiro2026skyler), texto suelto y claves duplicadas
- *(este commit)* 21-09-2026 — anexo-ia: estándar del grupo, carpetas por integrante y Anexo A en main.tex

Los commits de la rama llevan la coautoría declarada (`Co-Authored-By: Claude …`) y el enlace a la sesión en el mensaje, de modo que cada cambio remite a la conversación que lo produjo.

## 3. Qué produjo la IA y qué produjo la persona

**3.1 Alternativas adicionales.** La búsqueda inicial de candidatos y la verificación de cifras y URLs en documentación oficial la hizo un agente externo a partir de prompts escritos con apoyo de Claude; cada dato usado en el informe fue reabierto por el autor en la fuente oficial (fecha de consulta 20-09-2026). Los criterios de inclusión y descarte (Tabla D.1) los redactó el autor; Claude revisó su consistencia (ambigüedades, casos límite, orden de aplicación) sin proponer criterios propios. La decisión de qué candidatos entran y los motivos cortos son del autor, discutidos con Claude, que señaló inconsistencias entre criterios y resultados (por ejemplo, la exclusión de un candidato que no aportaba una dimensión no cubierta por la ficha); el autor tomó cada decisión. Los dos párrafos y las diez frases de la Tabla 3.1 son borrador del autor con corrección ortográfica y de estilo por IA (nivel 1); Claude revisó forma (que cada frase justifique en vez de describir, extensión, citas y referencias cruzadas).

**Anexo D.** Estructura (D.1 a D.7) propuesta por Claude y aprobada por el autor. D.1 (criterios, orden de aplicación y regla de desempate) redactado por el autor y transcrito al TeX por Claude. D.2 a D.6: filas llenadas por Claude a partir de las decisiones y motivos cortos del autor y de los hechos verificados, sin agregar hechos nuevos; revisadas por el autor. Citas bibliográficas de las fuentes oficiales tomadas del `.bib` generado por el agente externo, con los campos `note` eliminados y los autores corporativos protegidos.

**Plantilla, repositorio y Anexo A.** Correcciones de la plantilla LaTeX (numeración de anexos, `\FloatBarrier`, `.latexmkrc`, `.gitignore`), reparación de `referencias.bib` tras el merge, estructura de carpetas `trabajo/` y `anexo-ia/`, plantillas y este estándar: apoyo de formato y organización (nivel 2), sin contenido del informe.

**Lo que no hizo la IA.** Ninguna cifra, cita o referencia del informe proviene del modelo: todas se leyeron en la fuente oficial o en el paper original. Ningún texto de las secciones del punto 6.1 (análisis comparativo de 3.2, conclusiones, párrafo de aporte, sección 5, cuestionario) fue redactado ni decidido por IA en estas sesiones.
