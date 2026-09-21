# Anexo A — Parte B: prompts utilizados (3.2, filas AWS y Azure)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Rodolfo Antonio Fernández Vera.
**Secciones cubiertas:** 3.2 Cuadro comparativo: filas de AWS y Azure de las Tablas 3.2a y 3.2b (AWS Lambda; Azure Functions, Flex Consumption; AWS Fargate; Azure Container Apps; AWS Lambda@Edge + CloudFront Functions) y fila ancla de instancia siempre encendida (EC2 t3.medium sobre ECS, compartida con Francisca Abarca). No cubre el análisis comparativo de 3.2 (ver más abajo).
**Nivel declarado por sección:**
- 3.2 Cuadro comparativo, filas AWS y Azure: **nivel 3**. La IA abrió la documentación y las páginas de precios oficiales de cada proveedor, extrajo las cifras y límites con su URL, región, moneda y fecha de consulta, redactó las celdas, hizo un pase de verificación contra las fuentes (v1 → v2), cerró pendientes documentales y armó la planilla de verificación. El autor fijó las reglas de trabajo (región us-east-1 / East US, USD, precio de lista, solo fuente oficial, "no documentado" o "solo por cotización" en vez de completar por analogía), definió el alcance de cada sesión, dejó fuera de la IA la columna de arranque en frío y la fila siempre encendida mientras el equipo no las acordara, y decidió las 11 discrepancias que la verificación detectó (incluidas las dos de criterio: rango de vCPU y memoria de Fargate, y precio de CloudFront Functions). **Ninguna cifra fue producida por el modelo:** cada una se leyó en la página oficial del proveedor y quedó citada con su fecha (punto 6.1). 

- 3.2 Análisis comparativo (dos párrafos) y justificación de criterios: **no declarados por este integrante.** Los dos párrafos del texto final los redactó Claudio Toledo (commit `7c50b74`, 20-09-2026) y el párrafo de criterios es de Valentina Guzmán; cada uno los declara en su fila. En las sesiones de este integrante la IA sí escribió un **borrador de análisis** de unas 250 palabras (sesión 1, rondas 1 y 2), que no se usó como texto del informe. 

- Apoyo de estudio y organización (guía de lectura de los tres papers base, validación cruzada de cifras con los papers, segunda opinión sobre la revisión de Claudio, orientación sobre el anexo y consolidación de este registro): **nivel 2**. No produjo texto del informe.
**Herramientas:**
- Claude (Anthropic), chat en claude.ai dentro del Proyecto "FEP Investigación Rodo", varias conversaciones; al menos una atendida por Claude Sonnet 5 (`claude-sonnet-5`). El modelo de las conversaciones de las rondas 1 a 4 no quedó registrado.
- Claude (Anthropic), sesiones de trabajo con vínculo al computador del autor (app de escritorio), modelo configurado `claude-opus-5`, con navegador integrado para leer páginas de precios con JavaScript.
- Gemini 3.8 Flash (Google), revisión de documentos técnicos oficiales en la ronda 2, consultas particulares sobre ficha, documentos, etc.
**Período:** 18-09-2026 a 19-09-2026.

Los prompts se presentan en orden cronológico, agrupados por sesión. Hay dos tipos de registro, y cada sesión dice cuál tiene:

- **Transcripción hecha por la IA (sesiones 4, 6, 7 y 8).** La propia sesión copió los prompts desde su historial, con las erratas del original. El autor advierte que estas transcripciones las generó Claude y pueden no ser textuales en todos sus detalles; el texto exacto es el del enlace de cada conversación, que prevalece sobre esta copia. El prompt de la sesión 8 es el mensaje enviado en esa misma sesión.
- **Reconstrucción (sesiones 1, 2, 3 y 5).** El texto literal no se conservó en ningún archivo disponible. Se reconstruye a partir de las bitácoras que esas sesiones guardaron en el Proyecto (`claude/bitacora_sesion_3.2_2026-09-18.md`, `claude/conciliacion_criterios_valentina_claudio_2026-09-19.md`, `claude/estado_criterios_3.2_2026-09-20.md`); el texto exacto queda en el enlace de la conversación indicado en `C-evidencia.md`.

---

## Sesión 1 — Claude (chat, Proyecto "FEP Investigación Rodo"), 18-09 a 19-09-2026

**Enlace o exportación:** No fue posible realizar la exportación, ni en la interfaz de web ni en la interfaz de la aplicacion de escritorio permite exportar la conversación. Registro indirecto: `claude/bitacora_sesion_3.2_2026-09-18.md`.
**Secciones a las que sirvió:** 3.2 (datos de las filas AWS y Azure, primera versión); apoyo de estudio (guía de lectura de papers).

*Reconstrucción, sin texto literal.* Pedidos del autor, en orden:

1. Armar la matriz de datos de AWS y Azure para 3.2 sin esperar los criterios definitivos del equipo, con región us-east-1 / East US, USD y precio de lista. Alcance acordado: la IA investiga y arma la matriz de datos y un borrador de análisis; el autor reescribe el análisis y la justificación de criterios. Resultado: `Borrador_3.2_Cuadro_AWS_Azure.md` (9 servicios, pendientes de verificación, borrador de análisis y registro de trazabilidad).
2. Entregar texto listo para copiar en el Google Doc compartido del equipo; el autor decidió editarlo él mismo, sin conector.
3. (Ronda 2) Incorporar la revisión que el autor hizo con Gemini 5 sobre documentación oficial (ver sesión 2): precio Arm de Lambda, cargos de Provisioned Concurrency y SnapStart, límite de 230 s HTTP de Azure Functions, límites de payload de Azure; descartar como fuente primaria las referencias 31 y 33.
4. (Ronda 3) Cerrar los precios de Azure Functions, Azure Container Apps y CloudFront Functions leyendo las páginas oficiales con el navegador integrado. Hallazgo no pedido: AWS App Runner cerrado a nuevos clientes.
5. (Ronda 4) Revisar los tres papers base **sin redactar el análisis a partir de ellos** y armar una guía de lectura personal. Resultado: `Guia_Lectura_Papers_Base.md` (incluye el hallazgo de autores cruzados en los nombres de archivo de dos papers).

## Sesión 2 — Gemini 3.8 Flash (Google), 18-09 a 19-09-2026

**Enlace o exportación:** https://share.gemini.google/t8dzZiPXFUbG. Resultado conservado: `Referencias Excel/ResultadoInvestigacionGemini.md` (carpeta local del autor).
**Secciones a las que sirvió:** 3.2 (revisión de cifras y límites de AWS y Azure).

*Reconstrucción, sin texto literal.* El autor pidió revisar documentos técnicos oficiales (referencias 32 *AWS Lambda Developer Guide*, 18 *AWS Lambda Quotas*, 22 *Azure Functions scale and hosting*, 25 precios de AWS Lambda) y dos de apoyo (31 Cloudflare Learning Center y 33 InventiveHQ), y consolidar lo encontrado para contrastarlo con la matriz. Las conclusiones se incorporaron en la sesión 1, ronda 2. Se utilizo para realizar consultas particulares.


## Sesión 3 — Claude Sonnet 5 (chat, Proyecto "FEP Investigación Rodo"), 19-09 a 21-09-2026

**Enlace o exportación:** *[POR COMPLETAR]*. Registro: `claude/Consolidado_Uso_IA_Seccion_3.2.md` (§2 y §3), escrito por esta misma sesión.
**Tipo de registro:** transcripción hecha por la IA.
**Secciones a las que sirvió:** apoyo de estudio para 3.2 (validación cruzada con papers, segunda opinión sobre la revisión de Claudio); registro para este anexo.

1. Y crees que el contenido de estos papers sea coherente con lo encontrado en la tabla comparativa?
2. *[Adjuntos: 2 imágenes de una carpeta de Google Drive y un CSV]* Si, procede con ese parrafo. Antes de proceder a la lectura planeo verificar la tabla completa, pero queria que me ayudaras a priorizar, y que el tiempo es poco y ya pronto quiero comenzar a ver seminario. Otra observacion... *[parte del texto no conservada en el registro: describe el sistema de "fuentes-candidatas" en Drive que Daniel usa con un bot de Grok para la trazabilidad de fuentes]* No se si afectara d alguna forma en nuestro trabajo, pero te lo dejo ahi para conversarlo luego.
3. *[Pega íntegro el documento de Claudio Toledo "Revision-tabla-3.2-para-Rodolfo.md"]* Antes de continuar con la tabla, converse con mi compañero Claudio de la tabla y los criterios, y por ahora me dejo esta retroalimentacion, te lo adjunto en el mensaje. De todas maneras, te doy mi opinion de esta revision: 1. Sobre las 5 preguntas, las 4 primeras estaria de acuerdo a lo que señala claudio, quedaria ver tu opinion 2. Sobre las quinta y lo de valentina, lo unico que dejaría en sus manos sería el tema de complejidad operacional, que eso prefiero que lo defina ella. Estos cambios repercuten bastante en nuestros avances, de hecho arme una planilla con otro agente 'Checklist_Verificacion_3.2_AWS_Azure.xlsx' para ir verificando, y probablemente igual la deba que modificar, pero asi estamos trabajando todos en la misma sintonia. Que opinas.
4. Dame un prompt detallado para continuar esta sesion en una nueva (será dentro de este proyecto). La idea es que tenga informacion que no se encuentre en ningún documento, que sea más bien comentarios o hallazgos encontrados en conversaciones entre tu y yo. Propon el prompt, y te lo corregire o aceptare.
5. Eso te iba a mencionar sobre ese documento de conciliacion. AUN NO ES DEFINITIVO, estamos a la espera de obtener los criterios definitivos por parte de valentina, asi que ese documento es solo una guia, aun que para tu informacion ya se lo hice llegar a valentina. No he tomado ninguna decision contigo por ahora, para que lo tengas claro.
6. *[Pega íntegros `main.tex` y `Borrador_3.2_Tablas_A_B_v3_resuelto_2026-09-20.md`]* Recopila todo lo que te he solicitado dentro de un solo .md, los prompts, las decisiones mias y los resultados tuyos. Ya estamos en la fase final, ya se ha consolidado la tabla (peudes revisar el main.tex, donde se aprecian dichas tablas ya completadas.) Te adjunte tambien el borrador que realice con otra sesion. Todo esto lo hago con el proposito de completar luego la seccion de declaracion de uso de IA que se solicita. Recopila todo lo que puedas, y luego genera y guarda un .md en la raiz del proyecto. Puede que no tengas acceso a la carpeta local ya que ahora estoy desde el notebook.

## Sesión 5 — Claude Sonnet 5 (chat, Proyecto "FEP Investigación Rodo"), 20-09-2026, 01:43 a ~04:20

**Enlace o exportación:** *[POR COMPLETAR]*. Registro indirecto: `claude/estado_criterios_3.2_2026-09-20.md`.
**Secciones a las que sirvió:** 3.2 (datos de las filas AWS y Azure en la estructura 3.2a/3.2b; resolución de discrepancias).

*Reconstrucción, sin texto literal.* Pedidos del autor, en orden:

1. (01:43) Revisar la propuesta de criterios de Valentina Guzmán y el acuerdo provisorio entre Rodolfo, Claudio y Valentina.
2. (02:16–02:24) Revisar la propuesta de estructura de 3.2 de Daniel Miranda; el autor confirma seguirla (filas = plataformas, Tablas 3.2a y 3.2b, complejidad operacional por hechos verificables).
3. (02:24–03:00) Reconstruir las 7 filas de AWS y Azure en la nueva estructura con los datos ya verificados de la sesión 1. Resultado: `Borrador_3.2_Tablas_A_B_Daniel_2026-09-20.md`, con pendientes explícitos; la sesión entregó además el prompt que el autor usó en la sesión 6.
4. (~04:11) "acepto las que menciona la v2": aplicar las 11 discrepancias detectadas por la sesión 6. Resultado: `Borrador_3.2_Tablas_A_B_v3_resuelto_2026-09-20.md`, versión que el autor entregó a Claudio Toledo para consolidar. Su registro de trazabilidad dice: "las 11 decisiones de esta entrada son las de Rodolfo, no de la IA".
5. (~04:20) Plan de tres pasos (cruce de fuentes con la planilla maestra del equipo, actualización de la copia en Drive, priorización de plataformas) y un prompt para el agente Grok de Daniel. (OBSERVACION: Dicho agente de grok no se pudo recopilar correctamente sus prompts debido a que este pertenecia a un trial de prueba de 3 días, el cual finalizo y no se permitio el acceso posterior al chat)

## Sesión 6 — Claude (sesión con vínculo al computador), `claude-opus-5`, 20-09-2026 (desde las 02:49) y 21-09-2026 (16:29)

**Enlace o exportación:** https://claude.ai/code/session_012KA1rRMu2EgdCf7HUgRr9T (accesible con la cuenta del autor).
**Tipo de registro:** transcripción hecha por la IA.
**Secciones a las que sirvió:** 3.2 (verificación de cifras contra fuentes oficiales, cierre de pendientes, planilla de verificación); registro para este anexo.

1. *[Adjuntos: selección de la carpeta local `...\FEP\Investigación`; el PDF de pautas del curso llegó automáticamente como archivo del Proyecto]*

> Necesito que hagas dos cosas en orden, sobre el trabajo de la sección 3.2 (TERABYTE TI-05). Entrega del informe: mañana lunes 21-09-2026, así que prioriza.
> Reglas que aplican a todo lo que seleccus a continuación (no negociables):
>
> * Toda cifra: producto, moneda, región, fecha de consulta, tipo (lista/cotización). Sin fecha no es válida.
> * Fuente: solo documentación o calculadora oficial del proveedor. Nunca terceros, blogs o agregadores para cuotas duras ni precios. Solo trabajar con fuente ya declarada en los documentos, si es necesario investigar fuentes extras, declararlo y dejarlo pendiente.
> * Si algo no está publicado: escribe "no documentado" (límites) o "solo por cotización" (precios) — nunca lo dejes vacío ni lo completes por analogía con otro servicio.
> * Si necesitas más contexto de las reglas del curso, están en `indicaciones_trabajo_de_investigaci_n_2026_terabyte.md` (punto 5) en la misma carpeta — no debería hacer falta para esta tarea puntual.
>
> PASO 1 — Completa lo investigable con las fuentes que ya tenemos
> Trabaja sobre `Borrador_3.2_Tablas_A_B_Daniel_2026-09-20.md` (Tablas 3.2a y 3.2b, 7 plataformas AWS/Azure).
> A. Verifica lo que ya está. Para cada cifra ya presente en las tablas, abre la fuente oficial citada al pie ([F1]-[F5]) y confirma que el valor sigue vigente hoy. Si cambió desde el 18-09-2026, anota el valor nuevo con la fecha de hoy. Puedes basarte ademas en las fuentes declaradas en Borrador_3.2_Cuadro_AWS_Azure.md
> B. Completa estos pendientes concretos, solo con fuentes oficiales:
>
> 1. Modelo de aislamiento de AWS Fargate, AWS App Runner, Azure Functions y Azure Container Apps (documentación oficial de cada uno).
> 2. Egreso de datos para las 7 plataformas — busca en AWS Data Transfer Pricing y Azure Bandwidth Pricing oficiales (no uses las cifras generales de InventiveHQ, ya marcadas como no admisibles).
> 3. Memoria real de AWS Lambda@Edge — documentación específica de Lambda@Edge, no asumida por analogía con Lambda estándar.
> 4. Región/notación de precio de AWS CloudFront Functions — ¿depende de una región de origen o es de red global?
> 5. Fecha de consulta de AWS Fargate Pricing (marcada como no registrada — hoy sirve).
> 6. Lee completas las 5 fuentes de responsabilidad compartida ya citadas en [D1] (AWS, Microsoft, CNCF) y refina con cita precisa las celdas "Qué opera el equipo" y "Estado y límite que fuerza rediseño" de las 7 filas — deja explícito cuándo es cita directa y cuándo es extrapolación declarada (como ya está marcado para Azure Container Apps, que Microsoft no nombra).
>
> NO toques: la columna "Arranque en frío" (bloqueada — pendiente de que el equipo acuerde un único paper o de que Vicente entregue 4.1) ni la fila "Instancia siempre encendida". Déjalas tal como están.
> PASO 2 — Actualiza el Excel con estos cambios
> Con el Paso 1 resuelto (o marcado explícitamente "no documentado"), actualiza `Checklist_Verificacion_3.2_AWS_Azure.xlsx` para reflejar la estructura completa de las Tablas 3.2a (9 campos) y 3.2b (6 campos) por servicio — ya no es solo el desglose de precio de la vez anterior, ahora son todas las columnas: aislamiento, unidad de cobro y piso mensual, precio de lista, mitigación de arranque en frío, qué opera el equipo, estado y límite que fuerza rediseño, tiempo máximo, memoria/vCPU, payload, concurrencia/escalado, egreso de datos.
>
> * Mantén intacto lo que ya funciona: el desplegable de estado por ítem y las fórmulas de la hoja de resumen.
> * Para cada ítem que actualices o agregues, deja el estado en "pendiente de verificación manual" (o el equivalente que ya use el desplegable) — no marques nada como verificado en forma definitiva, porque falta que yo lo revise.
> * No agregues datos para "Arranque en frío" ni para "Instancia siempre encendida" — quedan en blanco/pendientes tal como están en el borrador.
>
> Cuando termines, avísame qué quedó "no documentado" para que yo decida si busco por otro lado antes de la entrega de mañana.
>
> SI ES MUCHO TRABAJO PARA UN ÚNICO OUTPUT, TRABAJA EN BLOQUES. Lo dejo a tu criterio.

2. (21-09-2026, 16:29) Necesito que documentes este chat dentro del archivo del contexto Consolidado_Uso_IA_Seccion_3.2.md, para documentar de forma completa el uso de IA. Sigue el formato de este documento, comprendelo primero para documentar correctamente para qué se uso está sesión. No generes un archivo nuevo, modifica el existente.

## Sesión 7 — Claude (sesión con vínculo al computador), `claude-opus-5`, 21-09-2026, 13:59 a 16:51

**Enlace o exportación:** https://claude.ai/code/session_018wzY8A6UkW8yufR8xzBzMe (accesible con la cuenta del autor).
**Tipo de registro:** transcripción hecha por la IA.
**Secciones a las que sirvió:** ninguna sección del informe: lectura de la 3.2 ya consolidada por Claudio y orientación sobre el cuestionario y el anexo. La sesión no redactó texto, no produjo cifras ni preguntas y no modificó archivos del informe.

1. *[Adjuntos: selección de la carpeta del repositorio; PDF de pautas del curso como archivo del Proyecto]* Revisa las indicaciones del trabajo junto con la Guia de division del equipo. Son los documentos fundamentales para trabajar.

   Mi compañero consolido mi tabla con la suya y tambien ya realizo la redaccion como tal de estas (Soy Rodolfo). Puedes ver el resultado en los ultimos commits realizados en esta rama, podrás ver la tabla consolidada final junto con los parrafod redactados.

   Una vez hayas leido y comprendido el avance hasta ahora, me comentas. Evita buscar errores o discrepancias, enfocate en comprender lo que ya hay.
2. Que revisaras del texto? que texto estas hablando?

   Y la integracion se encargara de hacerla mi compañera Isidora. Ahora mi intencion es saber si en base a mi seccion (que sería tabla 3.2 AWS - AZURE) debo realizar preguntas el cuestionario de 30 preguntas. Mis compañeros ya estan avanzando en eso en este documento_

   [enlace al Google Doc del cuestionario del equipo]
3. *[Adjuntos: `Borrador_3.2_Tablas_A_B_v3_resuelto_2026-09-20.md` y una captura de la lista de chats del Proyecto]* Perfecto, antes de comenzar, queria ver como podia resolver por mi parte el tema del anexo de IA. Tengo entendido que es más o menos individual por integrante, y que se coloca un anexo al final, o varios. En ese caso yo estuve trabajando contigo bastante rato, especificamente para realizar la tabla 3.2 preliminar de AWS y AZURE (te la adjuntare para que la revises, es la que le entregue a claudio para que haga la consolidacion y los parrafos finales).

   Como puedes ver en la imagen poseo esos chats, en los cuales estuve en algunos solamente trabajando específicamente en la tabla, deberia revisar. No se como debería preparar esta seccion en el informe.

   Que dices que haga primero, ver el tema de la IA, o ver el tema de las preguntas?
4. Cambio de planes, nos preocuparemos sobre el anexo de IA. Cuando isidora termine de integrar todas las ramas, daniel hará un commit con una forma de poner todo lo relativo a la IA, con unos ajustes en el anexo y una guía de cómo llenar. Asi después cada uno mete todo rápidamente siguiendo esa pauta.

   Como no sabemos aun como será la estructura que seguira, no se que podriamos hacer mientras. La pregutas las realizara una unica persona en base al documentoc ompleto consolidado, ya no es tarea nuestra.

   Respecto ala viso de nivel de la 3.2, Estoy de acuerdo si es nivel 3, tiene sentido y es lo mas honesto.
5. Ya se ha consolidado por ahora el uso de la IA, estuve organizandome con el resto de sesiones y recopilando prompts, decisiones, etc. Complementalo con lo que se realizo acá para tambien. El documento se encuentra en la carpeta \claude, se llama Consolidado_Uso_IA_Seccion_3.2.md.

   Analiza su estructura antes de redactar.

## Sesión 8 — Claude (sesión con vínculo al computador), `claude-opus-5`, 21-09-2026, 17:01

**Enlace o exportación:** https://claude.ai/code/session_01Vpj62xautciMCM9uM36cTG (accesible con la cuenta del autor).
**Secciones a las que sirvió:** este anexo (armado de `B-prompts.md` y `C-evidencia.md` a partir del consolidado; formato, nivel 2). No tocó contenido del informe.

1. *[Adjunto: selección de la carpeta del repositorio]* Necesito que leas la carpeta "anexo-ia", tienes acceso directo a ella. Necesito completar por mi parte la declaracion de IA. En esa carpeta se encuentra un README, leelo para comprender las instrucciones de como completar dicho anexo individualmente.

   Puedes apoyarte principalmente en el archivo Consolidado_Uso_IA_Seccion_3.2.md, donde intente dejar todas las sesiones registradas, con sus respectivos prompts (ojo, estos prompts son generados por claude, pero se basan en prompts reales mios).
