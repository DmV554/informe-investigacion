# Anexo A — Parte C: evidencia trazable (3.2, filas AWS y Azure)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Rodolfo Antonio Fernández Vera.
**Secciones cubiertas:** 3.2 Cuadro comparativo (filas AWS y Azure de las Tablas 3.2a y 3.2b).

## 1. Conversaciones

| # | Herramienta | Fechas | Enlace | Exportación en `registros/` | Secciones |
|---|---|---|---|---|---|
| 1 | Claude (chat, Proyecto "FEP Investigación Rodo"), modelo no registrado | 18-09 a 19-09-2026 | No fue posible realizar la exportación en la interfaz de web ni en la interfaz de la aplicacion de escritorio, simplemente no da la opción y se desconoce la razón | *[pendiente]* | 3.2 (matriz AWS/Azure, rondas 1 a 3); guía de lectura de papers (ronda 4) |
| 2 | Gemini 5 (Google) | 18-09 a 19-09-2026 | https://share.gemini.google/t8dzZiPXFUbG | *[pendiente]* | 3.2 (revisión de documentación oficial, ronda 2) |
| 3 | Claude (chat, Proyecto "FEP Investigación Rodo") | 19-09-2026 | No fue posible realizar la exportación en la interfaz de web ni en la interfaz de la aplicacion de escritorio, simplemente no da la opción y se desconoce la razón | *[pendiente]* | 3.2 (propuesta de columnas, no aprobada) |
| 4 | Claude Sonnet 5 (chat, Proyecto "FEP Investigación Rodo") | 19-09 a 21-09-2026 | No fue posible realizar la exportación en la interfaz de web ni en la interfaz de la aplicacion de escritorio, simplemente no da la opción y se desconoce la razón | *[pendiente]* | apoyo de estudio para 3.2; registro del anexo |
| 5 | Claude Sonnet 5 (chat, Proyecto "FEP Investigación Rodo") | 20-09-2026, 01:43 a ~04:20 | No fue posible realizar la exportación en la interfaz de web ni en la interfaz de la aplicacion de escritorio, simplemente no da la opción y se desconoce la razón | *[pendiente]* | 3.2 (tablas 3.2a/3.2b v1 y v3) |
| 6 | Claude, sesión con vínculo al computador, `claude-opus-5` | 20-09-2026 y 21-09-2026 | https://claude.ai/code/session_012KA1rRMu2EgdCf7HUgRr9T (accesible con la cuenta del autor) | *[pendiente]* | 3.2 (verificación v2, planilla de verificación); registro del anexo |
| 7 | Claude, sesión con vínculo al computador, `claude-opus-5` | 21-09-2026 | https://claude.ai/code/session_018wzY8A6UkW8yufR8xzBzMe (accesible con la cuenta del autor) | *[pendiente]* | orientación; registro del anexo (sin contenido del informe) |
| 8 | Claude, sesión con vínculo al computador, `claude-opus-5` | 21-09-2026 | https://claude.ai/code/session_01Vpj62xautciMCM9uM36cTG (accesible con la cuenta del autor) | *[pendiente]* | este anexo (formato) |

**Chats del Proyecto.** La barra lateral de claude.ai muestra, entre otros, estos chats del Proyecto: "Tabla 3.2 AWS-Azure cuestionario", "Sección 3.2 TERABYTE TI-05 tablas", "Matriz de conciliación y estructura de c…", "Conciliacion Correcciones", "VERIFICACION TABLA", "Sesion principal", "Plantilla informe". *[POR COMPLETAR por Rodolfo: asignar cada chat a su número de sesión de la tabla y reemplazar los enlaces pendientes por el enlace de "compartir" de cada uno, para que el profesor pueda abrirlos.]*

**Registro consolidado.** El documento `claude/Consolidado_Uso_IA_Seccion_3.2.md` del Proyecto reúne, por sesión, los prompts, las decisiones del autor, lo que produjo la IA y sus limitaciones declaradas. Lo escribieron las sesiones 4, 6 y 7. *[Sugerido: guardar una copia en `registros/Consolidado_Uso_IA_Seccion_3.2.md`.]*

**Archivos de trabajo producidos con IA** (carpeta local del autor, `...\FEP\Investigación\`), que muestran la evolución de las filas AWS/Azure hasta la versión entregada a Claudio Toledo:

| Archivo | Sesión | Estado |
|---|---|---|
| `Borrador_3.2_Cuadro_AWS_Azure.md` | 1 (rondas 1 a 3) y 4 | primera matriz de 9 servicios; superada |
| `Guia_Lectura_Papers_Base.md` | 1 (ronda 4) | guía de lectura personal; no es texto del informe |
| `Borrador_3.2_Tablas_A_B_Daniel_2026-09-20.md` | 5 | v1 en estructura 3.2a/3.2b |
| `Borrador_3.2_Tablas_A_B_v2_verificado_2026-09-20.md` | 6 | v2 verificada contra fuentes; 11 discrepancias |
| `Borrador_3.2_Tablas_A_B_v3_resuelto_2026-09-20.md` | 5 | v3 con las decisiones del autor; entregada a Claudio |
| `Checklist_Verificacion_3.2_AWS_Azure.xlsx` | creada con "otro agente" *[sesión por confirmar]*; reconstruida en la 6 | planilla de verificación (192 ítems) |

*[Sugerido: copiar la v1, la v2, la v3 y la planilla en `registros/` para que la evolución quede en el repositorio.]*

## 2. Historial de versiones (commits)

El autor no hizo commits propios en el repositorio. Sus filas entraron al informe en los commits de consolidación de Claudio Toledo en la rama `3.2-Cloud-Fastly-Deno`, integrada en `main` el 21-09-2026:

- `2fb598c` 20-09-2026 22:28 — Claudio Toledo — feat-documentation: seccion parte 3.2a y 3.2b (incluye `trabajo/3.2-cuadro/mis-filas-3.2.md` con las filas del autor y `Tablas-3.2-Definitivas.md`)
- `7c50b74` 20-09-2026 23:22 — Claudio Toledo — feat-docs: Se agregan los parrafos de la seccion 3.2 y documentacion de las tablas (ajusta las celdas de Azure Functions y Fargate, en línea con la v3 del autor)
- `ed5e9ab` 21-09-2026 16:32 — Daniel Miranda — Merge origin/3.2-Cloud-Fastly-Deno en main

La evolución previa de las filas (v1 → v2 → v3) no está en el repositorio; está en los archivos de trabajo de la sección 1.

## 3. Qué produjo la IA y qué produjo la persona

**3.2 Cuadro comparativo, filas AWS y Azure (nivel 3).** La IA leyó la documentación y las páginas de precios oficiales de AWS y Azure (con el navegador integrado cuando la página cargaba con JavaScript, fijando región y moneda en el selector), extrajo cada cifra con su URL, región y fecha de consulta y redactó las celdas. En un segundo pase reabrió cada fuente, cerró pendientes (aislamiento, egreso de datos de las 7 plataformas, memoria de Lambda@Edge, región de CloudFront Functions) y señaló 11 discrepancias. El autor fijó las reglas de trabajo y el alcance de cada sesión, decidió las 11 discrepancias y los dos criterios de juicio (rango de Fargate según la documentación de ECS; 0,10 USD por millón para CloudFront Functions), y entregó la v3 a Claudio Toledo para la consolidación. Limitaciones declaradas por la propia IA: la conversión por hora del precio de Fargate (×3600) la hizo la IA; algunas citas de documentación se obtuvieron con lectura web automatizada y deben confirmarse textualmente en la página; la v2 incorporó fuentes oficiales nuevas (F6, F10, subpáginas de CloudFront) sin dejarlas pendientes, lo que el autor aceptó al aprobar la v3. *[POR CONFIRMAR por Rodolfo: alcance de su revisión en la fuente original.]*

**Lo que no hizo la IA.** Ninguna cifra, cita o referencia del informe proviene del modelo: todas se leyeron en la documentación oficial del proveedor. El análisis comparativo de 3.2 no es de este integrante (lo redactó Claudio Toledo, commit `7c50b74`), y el borrador de análisis que la IA escribió en la sesión 1 no se usó como texto del informe *[POR CONFIRMAR por Rodolfo: que no se entregó a Claudio como base]*. La IA no redactó preguntas del cuestionario: la sesión 7 se negó a hacerlo por el punto 6.1, y el equipo después asignó el cuestionario a una sola persona.
