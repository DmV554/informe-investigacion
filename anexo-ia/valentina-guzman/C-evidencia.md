# Anexo A — Parte C: evidencia trazable (2.4, criterios de 3.2, 3.1 "Datos sin servidor", Anexo D, cuestionario)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Valentina Guzman.
**Secciones cubiertas:** las mismas de `B-prompts.md`.

## 1. Conversacioness

| # | Herramienta | Fechas | Enlace / exportación | Secciones |
|---|---|---|---|---|
| 1-4 | NotebookLM (Google), cuaderno "Serverless" del grupo, operado a través de Claude por MCP (`claude-opus-5` alto / `claude-sonnet-5` alto) | 20-09-2026 | Sin enlace propio: NotebookLM se consultó desde dentro de una sesión de Claude, no genera un enlace de sesión compartible por su cuenta. La evidencia es la **transcripción literal e íntegra** de cada una de las cuatro conversaciones, ya incorporada completa en `B-prompts.md`: cada prompt propio numerado, y en cada archivo fuente original consta además la respuesta completa del asistente con cita textual, localizador y referencia a la fuente del cuaderno. Los cuatro archivos originales (`lo_que_puede_llegar_a_faltar.md`, `bloque2bis.md`, `seccion3.2.md`, `seccion2.4.md`) se conservan tal cual se exportaron y quedan disponibles a requerimiento del profesor. |

**Nota sobre el uso de un skill de la cuenta ("humanizer").** Se usó en la corrección de estilo del borrador de 2.4 y de algunas preguntas del cuestionario: reescribe la forma del texto sin agregar hechos, cifras ni citas nuevas. Se declara como apoyo de nivel 1 (corrección de estilo), consistente con el punto 6.1 de las Indicaciones.

## 2. Historial de versiones (commits)

Commits de la integrante en el repositorio del grupo (`git log --author=Valentina`), integrados en `main` el 21-09-2026:

| Commit | Fecha | Descripción |
|---|---|---|
| `b944e27` | 21-09-2026 | Nueva rama. Se añade punto 2.4 |
| `dc1d458` | 21-09-2026 | Se cambia el primer párrafo (criterios de 3.2) y se agregan referencias al .bib |
| `f1efb97` | 21-09-2026 | anexo IA |
| `698198e` | 21-09-2026 | anexo IA valentina final |

## 3. Qué produjo la IA y qué produjo la persona

**2.4 Diseño orientado a eventos.** La búsqueda y verificación de las fuentes citadas (colas, pub/sub, idempotencia, las tres semánticas de entrega, orquestación vs. coreografía) se hizo con NotebookLM sobre el cuaderno "Serverless" del grupo, exigiendo en cada caso cita textual y localizador contra la fuente original antes de aceptar la afirmación. El análisis comparativo entre modelos de ejecución y el párrafo de cierre "en qué casos conviene cada uno" son de redacción y decisión propia: por el punto 6.1 de las Indicaciones, esa parte del informe no admite nivel de IA superior a 1, y aquí se mantuvo en nivel 0-1 (estilo únicamente).

**Criterios de comparación (apertura de 3.2).** Los tres criterios —costo, latencia, complejidad operacional— y la decisión de dejar la complejidad operacional sin puntaje numérico (por no existir una métrica estandarizada, según lo verificado en las fuentes) son de autoría propia, acordados con Rodolfo (6) y Claudio/Daniel (7) antes de que llenaran el cuadro. La IA se usó solo para verificar en las fuentes del cuaderno que la falta de una métrica estandarizada de complejidad operacional fuera un hallazgo real y no una suposición.

**3.1 "Datos sin servidor" y Anexo D.** PlanetScale y Turso se verificaron en su documentación oficial (vía NotebookLM, con cita textual). La frase de "qué aporta cada uno a la comparación" es de redacción propia; la decisión de pasarlos al integrante 7 (Claudio/Daniel Miranda) para que decida su inclusión en el cuadro 3.2 también lo es.

**Cuestionario.** Las 4 preguntas y sus justificaciones son de redacción 100% humana. La IA se usó únicamente para revisar que las preguntas no apuntaran a un detalle demasiado trivial (por ejemplo, una tabla específica) ni fueran demasiado específicas de más, y para estilo (humanizer) en algunas.

**Lo que no hizo la IA.** Ninguna cifra, precio o afirmación de las secciones propias se tomó de la IA sin abrir la fuente oficial que NotebookLM citó. Las decisiones de qué entra, qué se descarta (por ejemplo, el Bloque 2 bis no se llenó como estaba diseñado originalmente — ver Sesión 2 en `B-prompts.md` para el detalle de por qué) y la redacción final del análisis comparativo son de autoría humana.
