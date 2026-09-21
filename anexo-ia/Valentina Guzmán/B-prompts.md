# Anexo A — Parte B: prompts utilizados (2.4, criterios de 3.2, 3.1 "Datos sin servidor", Anexo D, cuestionario)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Valentina Guzman.
**Secciones cubiertas:** 2.4 Diseño orientado a eventos; apertura de 3.2 (criterios de comparación: costo, latencia, complejidad operacional); 3.1 Alternativas adicionales — lista "Datos sin servidor" (candidatos verificados: PlanetScale, Turso); Anexo D, fila "Datos sin servidor"; 4 preguntas del cuestionario sobre estas secciones.
**Nivel declarado por sección:**
- 2.4 Diseño orientado a eventos: **nivel 2** en la búsqueda inicial y verificación de fuentes (NotebookLM operado a través de Claude por MCP, cuaderno "Serverless" del grupo, con instrucciones de citación textual y localizador obligatorios) y **nivel 1** en corrección de estilo del borrador final (skill "humanizer": reescribe la forma, no agrega hechos). El análisis comparativo entre modelos y el párrafo de cierre "cuándo conviene" son de redacción y decisión propia, verificados contra la fuente oficial antes de citarse — por el punto 6.1 de las Indicaciones, esa parte no admite nivel superior a 1.
- Apertura de 3.2 (criterios costo/latencia/complejidad operacional): **nivel 2** en la misma búsqueda/verificación por NotebookLM; la definición y justificación de los tres criterios, y la decisión de dejar la complejidad operacional sin puntaje numérico, son de autoría propia (parte del análisis comparativo protegido por el punto 6.1).
- 3.1 "Datos sin servidor" (PlanetScale, Turso) y Anexo D: **nivel 2** en la verificación de los candidatos en su documentación oficial vía NotebookLM; la frase de "qué aporta cada candidato" y la decisión de pasarlos al integrante 7 son de autoría propia.
- Cuestionario (4 preguntas de estas secciones): **nivel 1** — redacción propia; se usó IA únicamente para revisar que las preguntas no fueran demasiado triviales o demasiado específicas y, en algunas, para estilo (humanizer). Ninguna respuesta ni justificación fue redactada por IA.
**Herramientas:** NotebookLM (Google), cuaderno de trabajo "Serverless" del grupo, operado a través de Claude por MCP, con los modelos `claude-opus-5` (alto) y `claude-sonnet-5` (alto) según la sesión.
**Período:** 20-09-2026.

Enlace al cuaderno de gemini notebook: [enlace a cuaderno](https://notebook.google.com/notebook/a2038a46-2a51-4a91-a29e-4c1a344e5d0f)
Los prompts se transcriben literalmente, tal como fueron escritos (incluidos errores de tipeo), en orden cronológico, agrupados por sesión. Las cuatro sesiones se registraron íntegras, sin resumir, a medida que ocurrieron (nota al pie de cada archivo fuente: "Transcripción exacta e íntegra... sin resumir").

---

# Sesiones con NotebookLM (búsqueda y verificación de fuentes, vía Claude/MCP)

## Sesión 1 — Claude + NotebookLM (MCP), cuaderno "Serverless" — huecos generales / revisión cruzada de las cuatro secciones


Prompts de la persona en esta sesión: 17.


#### Prompt 1 — Turno 1 — Usuario


````text
<pasted_content id="6c2c">
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

PASO 1 — LEER LAS REGLAS
Recupera y lee completa la fuente "Investigación README FIRST" del cuaderno
"Serverless". Si tienes una copia local del mismo archivo .md, léela desde ahí:
es el mismo documento y es más rápido.

Su estructura es:
  - Al inicio: la INSTRUCCIÓN OBLIGATORIA de citación (bloques A a E).
  - En el medio: una ficha de diagnóstico por fuente, de siete puntos.
  - Al FINAL del documento: cuatro tablas que clasifican las 40 fuentes por
    tipo, con una columna "Nota" que fija restricciones de uso por fuente.

Ese documento NO es fuente de contenido. Es el índice y el reglamento: te dice
qué fuentes existen, cómo están clasificadas y qué se puede citar de cada una.
El contenido sale de las fuentes completas del cuaderno, no de él.
Sus reglas mandan sobre cualquier otra consideración y sobre tu conocimiento previo.

PASO 2 — PLANIFICAR ANTES DE RESPONDER
Para cada pregunta, declara primero qué fuentes del cuaderno vas a usar. Por cada
una indica su número de ficha y transcribe su columna "Nota" de la tabla
correspondiente. Si la nota marca una cifra o afirmación como no citable, no la
uses ni siquiera parafraseada: la fuente se queda, el dato puntual se cae.
Si necesitas una fuente que no está en el cuaderno, dilo. No la sustituyas por
conocimiento propio ni por búsqueda web.

PASO 3 — RECUPERACIÓN DELEGADA A NOTEBOOKLM

No traigas la fuente completa a tu contexto. En vez de eso, pídele a NotebookLM
que lea la fuente completa y te devuelva la cita ya transcrita. Formula la
consulta al MCP en estos términos:

  "Lee COMPLETA la fuente [nombre del archivo] del cuaderno. Responde [pregunta].
   Por cada afirmación indica:
   (a) el nombre exacto del archivo de donde sale;
   (b) el localizador más preciso que el propio documento contenga: número y
       título de sección, capítulo, página impresa o encabezado;
   (c) la cita textual entre comillas, transcrita literalmente en el idioma
       original, incluyendo el contexto anterior y posterior suficiente para
       que se entienda de qué parte del documento salió y qué está afirmando
       —no una frase suelta, sino el pasaje completo;
   (d) si el documento matiza, condiciona o contradice esa afirmación en otra
       parte, transcribe también ese pasaje;
   (e) además de la cita, devuelve el PASAJE REAL COMPLETO en un bloque aparte,
       transcrito palabra por palabra tal como aparece en el documento:
       respetando mayúsculas, puntuación, cifras, unidades, nombres de
       parámetros y saltos de párrafo. Si el pasaje ocupa varios párrafos,
       transcríbelos todos. Si omites algo intermedio, márcalo con [...] y
       nunca al inicio ni al final del pasaje. Ese bloque debe poder leerse
       solo y entenderse sin la respuesta.
   No resumas. No parafrasees dentro de las comillas. Si no puedes localizar
   la afirmación en el texto, dilo."

REGLAS AL RECIBIR LA RESPUESTA
1. Si NotebookLM devuelve una afirmación sin cita textual, o con una cita que
   parece resumen en vez de transcripción, NO la uses: vuelve a preguntar
   pidiendo la transcripción literal.
2. Si devuelve la cita pero sin localizador, consérvala y marca la ubicación
   como "no declarada por la fuente". Nunca inventes sección, capítulo ni página.
3. Traer el texto de la fuente a tu propio contexto SOLO en estos casos:
   - la afirmación contiene una cifra, un porcentaje, un precio o una medición;
   - es una definición que se va a transcribir literal en el informe;
   - NotebookLM dio dos respuestas distintas sobre lo mismo;
   - la cita recibida no permite saber de qué parte del documento salió.
   En esos casos, verifica el pasaje tú mismo y dilo: "verificado contra el
   texto completo".
4. Toda cita no verificada por ti va marcada como "según NotebookLM, sin
   verificación directa".
5. La respuesta y el texto de la fuente van SIEMPRE separados. Primero la
   respuesta redactada; después, en bloque aparte y entre comillas, el pasaje
   real. Nunca mezclarlos en el mismo párrafo ni intercalar palabras propias
   dentro de las comillas.
6. Si necesitas aclarar algo dentro de una cita, hazlo entre corchetes y en
   tu propio nombre: "[...] el broker [de Kafka] asigna [...]". Todo lo que
   esté entre comillas y sin corchetes tiene que estar literal en la fuente.

PASO 4 — FORMATO DE SALIDA (repetir por cada pregunta)

### Pregunta N: [repetir la pregunta]

**Fuentes usadas.** [nº de ficha + nombre del archivo + su nota de la tabla,
por cada fuente que vas a usar en esta pregunta]

**Respuesta.** [respuesta directa, redactada con tus palabras, sin relleno.
Aquí no van comillas: esto es la síntesis, la prueba viene abajo]

**Evidencia.** Por cada afirmación de la respuesta:

  1. Afirmación: [la afirmación concreta que se está respaldando]
  2. Fuente: [nombre exacto del archivo + número de ficha del README]
  3. Ubicación: [sección, capítulo, página o encabezado | "no declarada
     por la fuente"]
  4. Texto real de la fuente:

     > "[transcripción literal e íntegra del pasaje, con el contexto anterior
     > y posterior necesario para saber de qué parte del documento salió y
     > qué está afirmando. Varios párrafos si corresponde. Sin editar, sin
     > resumir, sin corregir.]"

  5. Traducción (si aplica): [marcada como traducción propia, fuera de las
     comillas]
  6. Matices en otra parte del documento (si los hay): [ubicación + cita
     textual del pasaje que condiciona o contradice lo anterior]
  7. Verificación: [verificado contra el texto completo] | [según NotebookLM,
     sin verificación directa]

**Detalles que no se pueden pasar por alto.** Versión del documento, fecha de
publicación o actualización, valores por defecto, condiciones, excepciones y
limitaciones que el propio texto declare.

**Interpretación propia.** [Solo si la hay, marcada como tal. Lo que no está
literal en la fuente va aquí, nunca mezclado con la evidencia.]

PASO 5 — CIERRE (una sola vez, al final de todas las preguntas)

## Referencias (BibTeX)
Una entrada por cada fuente efectivamente citada en estas respuestas — no de todo
el cuaderno, no de fuentes consultadas pero no citadas.
Tipos: @article (revista con revisión por pares, con doi) · @inproceedings
(congreso, con booktitle y doi) · @techreport (estándar o especificación, con
institution y versión) · @online (documentación oficial, con url y urldate).
No inventes campos: si un dato no aparece en la fuente, omite el campo y anótalo
debajo del bloque como "dato no declarado en la fuente". urldate en AAAA-MM-DD.
Si hay DOI, cita por DOI y no por URL de repositorio o agregador.

═══════════════════════════════════════════
PREGUNTA:
Aplica esto a los 6 candidatos: los 4 que ya trae la ficha (Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1) más al menos 2 de la lista a verificar (PlanetScale, Turso, Upstash, CockroachDB Serverless, MongoDB Atlas Serverless, Firestore). Para cada uno, en este orden:

Fuente y fecha de verificación. ¿En qué documentación oficial o calculadora oficial del proveedor se verificó cada dato (URL, fecha de consulta)? Si algún dato no está publicado por el proveedor, ¿se declaró expresamente "solo por cotización" en vez de citar una cifra de tercero?
═══════════════════════════════════════════
</pasted_content id="6c2c">

---
````


#### Prompt 2 — Turno 3 — Usuario


````text
NO, anda dejando ese tipo de comentarios en un md nuevo en el escritorio (haz un archivo que se llame "comentarios 3.1")

---
````


#### Prompt 3 — Turno 5 — Usuario


````text
<pasted_content id="6c2c">
[Mismo protocolo completo del Turno 1 — CONTEXTO, PASO 1 a PASO 5 — con la pregunta final:]

PREGUNTA:
Aplica esto a los 6 candidatos: los 4 que ya trae la ficha (Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1) más al menos 2 de la lista a verificar (PlanetScale, Turso, Upstash, CockroachDB Serverless, MongoDB Atlas Serverless, Firestore). Para cada uno, en este orden:

0. (RESPONDIDO ANTERIORMENTE)
1. Modelo de precios. ¿Cuál es la unidad de cobro exacta (por solicitud, por GB-mes de almacenamiento, por unidad de cómputo/IOPS, por vCPU-segundo, etc.)? ¿Qué incluye el free tier (límites, si expira, si pide tarjeta) y cuáles son los tramos de precio siguientes? Cita cada cifra con producto, moneda, región, fecha de consulta y si es precio de lista o cotización (formato del punto 6 de la guía)
</pasted_content id="6c2c">

---
````


#### Prompt 4 — Turno 7 — Usuario


````text
<pasted_content id="6c2c">
[Mismo protocolo completo — CONTEXTO, PASO 1 a PASO 5 — con la pregunta final:]

PREGUNTA:
Aplica esto a los 6 candidatos: los 4 que ya trae la ficha (Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1) más al menos 2 de la lista a verificar (PlanetScale, Turso, Upstash, CockroachDB Serverless, MongoDB Atlas Serverless, Firestore). Para cada uno, en este orden:

0. (RESPONDIDO ANTERIORMENTE)
1. (RESPONDIDO ANTERIORMENTE)
2. Arquitectura. ¿En cuál de las cuatro categorías entra (relacional distribuida, NoSQL documental, key-value, SQLite distribuido) y con qué motor o protocolo es compatible (p. ej. Postgres, MySQL, propio)? ¿Qué modelo de consistencia y de replicación usa? Si es un caso híbrido o no encaja limpiamente en una categoría, decirlo y justificar la clasificación elegida.
</pasted_content id="6c2c">

---
````


#### Prompt 5 — Turno 9 — Usuario


````text
<pasted_content id="6c2c">
[Mismo protocolo completo — con la pregunta final:]

PREGUNTA:
Aplica esto a los 6 candidatos [...]. Para cada uno, en este orden:

0. (RESPONDIDO ANTERIORMENTE)
1. (RESPONDIDO ANTERIORMENTE)
2. (RESPONDIDO ANTERIORMENTE)
3. Vigencia. ¿Sigue vigente tal como se describe, o fue descontinuado, renombrado o fusionado con otro plan? ¿Cuándo ocurrió el cambio y por qué (fuente oficial y fecha)? Si sigue vigente pero en preview/beta, indicarlo.
</pasted_content id="6c2c">

---
````


#### Prompt 6 — Turno 11 — Usuario


````text
<pasted_content id="6c2c">
[Mismo protocolo completo — con la pregunta final:]

PREGUNTA:
Aplica esto a los 6 candidatos [...]. Para cada uno, en este orden:

0. (RESPONDIDO ANTERIORMENTE)
1. (RESPONDIDO ANTERIORMENTE)
2. (RESPONDIDO ANTERIORMENTE)
3. (RESPONDIDO ANTERIORMENTE)
4. Límites técnicos. ¿Qué límites declara el proveedor en: tamaño máximo de almacenamiento, número máximo de conexiones concurrentes, regiones disponibles (cuántas y cuáles), tamaño máximo de payload/solicitud, y algún límite de rendimiento o SLA de latencia publicado? Indicar si hay opción de residencia de datos en una región específica.
</pasted_content id="6c2c">

---
````


#### Prompt 7 — Turno 13 — Usuario


````text
<pasted_content id="6c2c">
[Mismo protocolo completo — con la pregunta final:]

PREGUNTA:
Aplica esto a los 6 candidatos [...]. Para cada uno, en este orden:

0. (RESPONDIDO ANTERIORMENTE)
1. (RESPONDIDO ANTERIORMENTE)
2. (RESPONDIDO ANTERIORMENTE)
3. (RESPONDIDO ANTERIORMENTE)
4. (RESPONDIDO ANTERIORMENTE)
5. Justificación para la comparación. Mapear explícitamente el aporte de esta alternativa a los tres criterios que definen las columnas del cuadro 3.2 (costo, latencia, complejidad operacional): ¿en cuál de esos ejes se diferencia de los otros candidatos? Indicar además: (a) si es una de las 4 ya nombradas en la ficha o una alternativa adicional aportada por el grupo; (b) si entra como fila al cuadro 3.2 o se descarta, y por qué.
</pasted_content id="6c2c">

---
````


#### Prompt 8 — Turno 15 — Usuario


````text
quiero que tú interpretes todo, para guiarme al menos

---
````


#### Prompt 9 — Turno 17 — Usuario


````text
si

---
````


#### Prompt 10 — Turno 19 — Usuario (respuesta a la pregunta de aclaración)


````text
Your questions have been answered: "Dijiste "sí" a la pregunta de cierre, pero ofrecí dos caminos distintos. ¿Cuál prefieres?"="Ambas cosas". You can now continue with these answers in mind.

---
````


#### Prompt 11 — Turno 21 — Usuario


````text
<pasted_content id="6c2c">
necesito que verifiques las nuevas fuentes, hay que revisar si son válidas.

# PROTOCOLO DE VALIDACIÓN DE FUENTES

## Rol
Actúas como evaluador de fuentes bajo una guía estricta: una referencia inexistente o
una cifra sin respaldo se evalúa como ERROR GRAVE, y una cifra sin fecha de consulta
no se considera válida. Ante la duda, descarta.

## Entrada
Te entregaré una o varias fuentes candidatas (URL, título, autoría, tipo de documento,
y la afirmación o dato que se pretende sostener con ella).

## Tarea
Aplica los 8 pasos EN ORDEN a cada fuente. Detente en cuanto una fuente se caiga
(ver Regla de corte). No inventes información: si un dato necesario para evaluar
(autoría, fecha, metodología) no está disponible, eso cuenta como ausencia, no como
"probablemente sí".

---

### Paso 1 — Filtro de tipo (elimina rápido, antes de leer nada más)
Clasifica la fuente:
- PREFERENTE (sigue de largo): oficial del proveedor, estándar (NIST / ISO / IETF /
  CNCF / OWASP / Apache SF), académica revisada por pares.
- ADMISIBLE, solo si lo declaras explícitamente en el texto: informe de industria o
  encuesta, documentación técnica de terceros, blog de ingeniería reconocido.
- DESCARTE INMEDIATO, sin excepción: comparativa de un proveedor sobre su propia
  categoría, artículo sin autoría verificable, contenido de agregador sin fuente
  original.

### Paso 2 — Sesgo de proveedor
¿La fuente compara su propio producto contra la competencia, dentro del mismo texto?
Si sí → DESCARTADA como evidencia comparativa, aunque sea oficial y primaria.
Única salvedad: se puede usar para un hecho fechado puntual (ej. "el producto X se
descontinuó el [fecha]"), nunca para sostener una comparación de rendimiento,
superioridad o posicionamiento.

### Paso 3 — Autoría verificable
¿Puedes nombrar a una persona u organización responsable del contenido?
Si no hay ningún nombre identificable (blog "del equipo", sin autor, sin organización
clara) → DESCARTADA.

### Paso 4 — Metodología (solo si cayó en "informe de industria / encuesta" en Paso 1)
¿Declara tamaño de muestra Y metodología?
Si falta cualquiera de las dos → DESCARTADA (no cumple la condición de admisión).
Si declara una pero no la otra → se marca ZONA DE MÁXIMA CAUTELA: se puede mencionar,
pero nunca como respaldo único de una afirmación central.

### Paso 5 — Origen del dato: primaria o secundaria
Esto CLASIFICA, no descarta por sí solo. Pregunta: ¿el documento es donde el dato o la
definición aparece por primera vez, o está reportando lo que otro ya publicó?
Una fuente secundaria limpia (pasó Pasos 1–4) sigue siendo citable; para datos muy
específicos, rastrea e indica la fuente primaria que cita.

### Paso 6 — Verificabilidad de cada afirmación puntual
Evalúa por separado CADA dato que se pretende citar, no la fuente en bloque.
Una fuente puede pasar los Pasos 1–5 y aun así contener una afirmación suelta sin
respaldo dentro de su propio texto (cifras redondas de marketing, "sub-second",
"200+ capacidades", "2M+ de X", cifras de casos de éxito en material comercial).
Regla: si no puedes encontrar el pasaje exacto que respalda el dato al abrir el
documento tú misma, ese dato específico NO se cita. La fuente sobrevive; el dato no.

### Paso 7 — Si es cifra o precio: las cinco reglas de precio
Toda cifra de precio debe declarar: producto, moneda, región, fecha de consulta, y si
es precio de lista o cotización.
Sin fecha de consulta → NO VÁLIDA, sin excepción.
Además: los precios se levantan una sola vez, de forma centralizada (cuadro 3.2). Si
una sección necesita un precio, se solicita al responsable de ese cuadro; no se busca
por cuenta propia.
Este paso aplica ENCIMA de cualquier cifra, aunque la fuente haya pasado todo lo
anterior.

### Paso 8 — Redundancia (no descarta; prioriza esfuerzo)
Si ya existe una fuente oficial o académica limpia que respalda el mismo punto, no
apiles más. Prioriza fuentes que llenen huecos reales de evidencia por sobre reforzar
puntos ya cerrados.

---

## REGLA DE CORTE RÁPIDA
- Falla Paso 1, 2 o 3 → la fuente entera se cae. No sigas evaluando.
- Pasa esos tres pero falla Paso 4 (siendo informe de industria) → se cae entera.
- Pasa todo lo anterior pero falla Paso 6 en una afirmación puntual → la fuente se
  queda, se cae solo ese dato.
- Paso 7 se aplica a toda cifra, con independencia de los pasos previos.

---

## FORMATO DE SALIDA (una ficha por fuente)

**Fuente N — [título / URL]**
- Tipo (Paso 1): [preferente / admisible / descarte] — justificación en una línea
- Sesgo de proveedor (Paso 2): [sí / no] — efecto
- Autoría (Paso 3): [nombre identificado / ausente]
- Metodología (Paso 4): [N/A / muestra + metodología declaradas / falta cuál]
- Origen (Paso 5): [primaria / secundaria → fuente primaria que cita]
- Afirmaciones puntuales (Paso 6): lista de datos a citar, cada uno marcado
  [RESPALDADO en pasaje X] o [SIN RESPALDO → no citar]
- Cifras/precios (Paso 7): [N/A / cumple las 5 reglas / falta: ___]
- Redundancia (Paso 8): [llena un hueco / duplica evidencia ya cerrada]

**VEREDICTO:** ADMITIDA / ADMITIDA CON RESERVAS (especificar qué datos se caen) /
DESCARTADA (indicar en qué paso y por qué)
**Uso permitido:** [para qué afirmación exacta puede citarse, y para cuál no]

Al final, entrega un resumen: fuentes admitidas, fuentes caídas con el paso que las
tumbó, y huecos de evidencia que siguen sin cubiertos.
</pasted_content id="6c2c">

---
````


#### Prompt 12 — Turno 23 — Usuario


````text
haz la búsqueda de las que falten. deben pasar todos los filtros

---
````


#### Prompt 13 — Turno 25 — Usuario


````text
qué nos estaría faltando para concretar todo?

---
````


#### Prompt 14 — Turno 27 — Usuario


````text
<pasted_content id="6c2c">
[Documento completo: PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO — ESCUELA DE INFORMÁTICA — ICI-5444 Taller de Formulación de Proyectos Informáticos — Trabajo de Investigación 2026 — Indicaciones a cumplir y fichas de los temas asignados — Documento FEP00.3.26 Versión del 3 de agosto de 2026 — Antonio Moya Villegas (antonio.moya@pucv.cl)

Secciones 1 a 8 completas: objetivo y alcance, entrega/formato/exposición, cuestionario de evaluación de conocimientos, aporte propio del grupo, precios y fuentes, declaración de uso de inteligencia artificial (con niveles 0-3 y anexo obligatorio), asignación de 12 temas por empresa, y las 12 fichas completas de los temas TI-01 a TI-12 — incluida la ficha TI-05 "Serverless y computación en el borde" asignada a la empresa TERABYTE, con sus subtemas obligatorios, tecnologías a comparar (incluyendo la lista "Datos sin servidor: Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1, y otros que el grupo debe identificar") y entregables específicos.

Anexo final: Formulario de declaración de uso de inteligencia artificial, con sección A (declaración por sección del informe), B (prompts utilizados), C (evidencia trazable) y D (firma de los integrantes).]

completa todo teniendo en cuenta las instrucciones
</pasted_content id="6c2c">

---
````


#### Prompt 15 — Turno 29 — Usuario


````text
<pasted_content id="6c2c">
[Documento completo: "TERABYTE · TI-05 Serverless y computación en el borde — Guía del equipo: estructura, división y reglas obligatorias"

Incluye: 1) qué tienen que responder (comparar 3 modelos de ejecución + edge vs. always-on en costo/latencia/complejidad operacional); 2) índice completo del informe (portada, resumen ejecutivo, introducción, secciones 1 a 5, conclusiones, referencias, anexos); 3) presupuesto de extensión en páginas/palabras por sección; 4) división del trabajo entre 9 integrantes con tabla detallada de responsabilidades y dependencias entre secciones — incluyendo la fila:

| 5 | Valentina Guzman | 2.4 Diseño orientado a eventos · Criterios de comparación (apertura de 3.2) | Colas, pub/sub, idempotencia, entrega al menos una vez, orquestación vs. coreografía. Define y justifica los criterios (costo, latencia, complejidad operacional) que son las columnas del cuadro; los acuerda con 6 y 7 antes de que llenen la tabla |

5) sección 5 con las 5 listas de "otros" (FaaS, contenedores sin servidor, cómputo en el borde, código abierto, datos sin servidor) y sus exploradores asignados — incluyendo la fila "Datos sin servidor" con Integrante 5 (2.4) y 4 (2.3) como exploradores, y los candidatos a verificar: PlanetScale, Turso, Upstash, CockroachDB Serverless, MongoDB Atlas Serverless, Firestore; 6) reglas obligatorias sobre precios; 7) reglas obligatorias sobre fuentes; 8) reglas obligatorias sobre inteligencia artificial (niveles, anexo, consecuencias); 9) cuestionario de 30 preguntas; 10) presentación oral; 11) lo que se evalúa peor.]

mi rol es el rol 5. que me falta exactamente?
</pasted_content id="6c2c">

---
````


#### Prompt 16 — Turno 31 — Usuario


````text
<pasted_content id="6c2c">
Aquí está el contenido textual completo de la sección 3.2

[Bloque LaTeX completo: comentario de responsables (Valentina — criterios; Rodolfo — AWS y Azure, consolida y escribe el análisis; Claudio y Daniel — Google, Cloudflare, Fastly, Deno/Vercel/Netlify, open source), presupuesto de extensión, subsección "Criterios y cuadro comparativo de plataformas" con: párrafo de apertura, tabla de 3 criterios (Costo y modelo de cobro, Latencia y aislamiento, Complejidad operacional) con columnas "Por qué importa" y "Cómo se mide en el cuadro"; Tabla 3.2a (Criterios arquitectónicos, operativos y económicos) con 12 filas de plataformas (AWS Lambda, Azure Functions Flex Consumption, Google Cloud Run functions, Google Cloud Run servicios, AWS Fargate/ECS, Azure Container Apps, Cloudflare Workers Paid, Fastly Compute, AWS Lambda@Edge/CloudFront, EC2 reservada ECS t3.medium, Oracle OCI Functions, Azion Edge Functions) con columnas Plataforma/Modelo/Aislamiento/Unidad de cobro y piso/Precio de lista fechado/Cold start/Mitigación/Qué opera el equipo/Estado-Límite rediseño; Tabla 3.2b (Límites técnicos y tarifas de egreso de datos) con las mismas 12 plataformas y columnas de tiempo máximo, memoria/vCPU, payload, concurrencia, egreso; Tabla 3.2c (Ecosistema de plataformas de código abierto) con 6 proyectos (Knative Serving, OpenFaaS, KEDA, Fermyon SpinKube, wasmCloud, Fission) y columnas de modelo, aislamiento, escala 0, defaults, acreditación CNCF; notas metodológicas (a) a (d) sobre complejidad operacional, arranque en frío, Lambda@Edge/CloudFront consolidados, y respaldo teórico del aislamiento en el borde citando a Schwarzl et al. sobre Spectre; y el párrafo de análisis comparativo final sobre costos fijos encubiertos de mitigación de cold start, la bifurcación económica del cómputo en el borde, la complejidad operacional trasladada a ingeniería de red, y el riesgo de dependencia del proveedor ejemplificado con el cierre de AWS App Runner a nuevos clientes en 2026.]

## Todas las decisiones tomadas sobre 3.2

Reconstruidas de `propuesta-estructura-3.2.md`, `esqueleto-3.2a-3.2b.md`, `Tablas-3.2-Definitivas.md` y `mis-filas-3.2.md`:

[28 decisiones numeradas, agrupadas en: Alcance y estructura (1-6, incluyendo la decisión 5: "Las bases de datos sin servidor no van en 3.2 (Aurora, DynamoDB, Neon, D1 y sus alternativas): se tratan en 3.1 y en 2.4/2.6."); Complejidad operacional — el criterio sin métrica estándar (7-11); Reglas de datos aplicadas a todas las celdas (12-18); Arranque en frío — columna compartida con 4.1 (19-21); Filas y responsables definidos (22-26, incluyendo la decisión 26: "Responsables: Rodolfo — filas 1, 2, 5, 6, 9 y 10; Claudio y Daniel — filas 3, 4, 7, 8, 11, 12 + Tabla 3.2c + tabla ampliada del anexo; Vicente — columna de cold start; Francisca — configuración de la fila ancla; Valentina — párrafo y tabla de criterios."); Análisis comparativo (27-28).]
</pasted_content id="6c2c">

---
````


#### Prompt 17 — Turno 33 — Usuario


````text
guarda toda esta conversación con lujo de detalles en un md en el escritorio, no la quiero resumida, la quiero exacta, con todo. el archivo se debe llamar "lo que puede llegar a faltar.md"

---
````


## Sesión 2 — Claude + NotebookLM (MCP) — Bloque 2 bis (garantía de entrega; descartado del cuadro 3.2, ver nota)


Prompts de la persona en esta sesión: 11.


#### Prompt 18 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

PASO 1 — LEER LAS REGLAS
Recupera y lee completa la fuente "Investigación README FIRST" del cuaderno
"Serverless". Si tienes una copia local del mismo archivo .md, léela desde ahí:
es el mismo documento y es más rápido.

Su estructura es:
  - Al inicio: la INSTRUCCIÓN OBLIGATORIA de citación (bloques A a E).
  - En el medio: una ficha de diagnóstico por fuente, de siete puntos.
  - Al FINAL del documento: cuatro tablas que clasifican las 40 fuentes por
    tipo, con una columna "Nota" que fija restricciones de uso por fuente.

Ese documento NO es fuente de contenido. Es el índice y el reglamento: te dice
qué fuentes existen, cómo están clasificadas y qué se puede citar de cada una.
El contenido sale de las fuentes completas del cuaderno, no de él.
Sus reglas mandan sobre cualquier otra consideración y sobre tu conocimiento previo.

PASO 2 — PLANIFICAR ANTES DE RESPONDER
Para cada pregunta, declara primero qué fuentes del cuaderno vas a usar. Por cada
una indica su número de ficha y transcribe su columna "Nota" de la tabla
correspondiente. Si la nota marca una cifra o afirmación como no citable, no la
uses ni siquiera parafraseada: la fuente se queda, el dato puntual se cae.
Si necesitas una fuente que no está en el cuaderno, dilo. No la sustituyas por
conocimiento propio ni por búsqueda web.

PASO 3 — RECUPERACIÓN DELEGADA A NOTEBOOKLM

No traigas la fuente completa a tu contexto. En vez de eso, pídele a NotebookLM
que lea la fuente completa y te devuelva la cita ya transcrita. Formula la
consulta al MCP en estos términos:

  "Lee COMPLETA la fuente [nombre del archivo] del cuaderno. Responde [pregunta].
   Por cada afirmación indica:
   (a) el nombre exacto del archivo de donde sale;
   (b) el localizador más preciso que el propio documento contenga: número y
       título de sección, capítulo, página impresa o encabezado;
   (c) la cita textual entre comillas, transcrita literalmente en el idioma
       original, incluyendo el contexto anterior y posterior suficiente para
       que se entienda de qué parte del documento salió y qué está afirmando
       —no una frase suelta, sino el pasaje completo;
   (d) si el documento matiza, condiciona o contradice esa afirmación en otra
       parte, transcribe también ese pasaje;
   (e) además de la cita, devuelve el PASAJE REAL COMPLETO en un bloque aparte,
       transcrito palabra por palabra tal como aparece en el documento:
       respetando mayúsculas, puntuación, cifras, unidades, nombres de
       parámetros y saltos de párrafo. Si el pasaje ocupa varios párrafos,
       transcríbelos todos. Si omites algo intermedio, márcalo con [...] y
       nunca al inicio ni al final del pasaje. Ese bloque debe poder leerse
       solo y entenderse sin la respuesta.
   No resumas. No parafrasees dentro de las comillas. Si no puedes localizar
   la afirmación en el texto, dilo."

REGLAS AL RECIBIR LA RESPUESTA
1. Si NotebookLM devuelve una afirmación sin cita textual, o con una cita que
   parece resumen en vez de transcripción, NO la uses: vuelve a preguntar
   pidiendo la transcripción literal.
2. Si devuelve la cita pero sin localizador, consérvala y marca la ubicación
   como "no declarada por la fuente". Nunca inventes sección, capítulo ni página.
3. Traer el texto de la fuente a tu propio contexto SOLO en estos casos:
   - la afirmación contiene una cifra, un porcentaje, un precio o una medición;
   - es una definición que se va a transcribir literal en el informe;
   - NotebookLM dio dos respuestas distintas sobre lo mismo;
   - la cita recibida no permite saber de qué parte del documento salió.
   En esos casos, verifica el pasaje tú mismo y dilo: "verificado contra el
   texto completo".
4. Toda cita no verificada por ti va marcada como "según NotebookLM, sin
   verificación directa".
5. La respuesta y el texto de la fuente van SIEMPRE separados. Primero la
   respuesta redactada; después, en bloque aparte y entre comillas, el pasaje
   real. Nunca mezclarlos en el mismo párrafo ni intercalar palabras propias
   dentro de las comillas.
6. Si necesitas aclarar algo dentro de una cita, hazlo entre corchetes y en
   tu propio nombre: "[...] el broker [de Kafka] asigna [...]". Todo lo que
   esté entre comillas y sin corchetes tiene que estar literal en la fuente.

PASO 4 — FORMATO DE SALIDA (repetir por cada pregunta)

### Pregunta N: [repetir la pregunta]

**Fuentes usadas.** [nº de ficha + nombre del archivo + su nota de la tabla,
por cada fuente que vas a usar en esta pregunta]

**Respuesta.** [respuesta directa, redactada con tus palabras, sin relleno.
Aquí no van comillas: esto es la síntesis, la prueba viene abajo]

**Evidencia.** Por cada afirmación de la respuesta:

  1. Afirmación: [la afirmación concreta que se está respaldando]
  2. Fuente: [nombre exacto del archivo + número de ficha del README]
  3. Ubicación: [sección, capítulo, página o encabezado | "no declarada
     por la fuente"]
  4. Texto real de la fuente:

     > "[transcripción literal e íntegra del pasaje, con el contexto anterior
     > y posterior necesario para saber de qué parte del documento salió y
     > qué está afirmando. Varios párrafos si corresponde. Sin editar, sin
     > resumir, sin corregir.]"

  5. Traducción (si aplica): [marcada como traducción propia, fuera de las
     comillas]
  6. Matices en otra parte del documento (si los hay): [ubicación + cita
     textual del pasaje que condiciona o contradice lo anterior]
  7. Verificación: [verificado contra el texto completo] | [según NotebookLM,
     sin verificación directa]

**Detalles que no se pueden pasar por alto.** Versión del documento, fecha de
publicación o actualización, valores por defecto, condiciones, excepciones y
limitaciones que el propio texto declare.

**Interpretación propia.** [Solo si la hay, marcada como tal. Lo que no está
literal en la fuente va aquí, nunca mezclado con la evidencia.]

PASO 5 — CIERRE (una sola vez, al final de todas las preguntas)

## Referencias (BibTeX)
Una entrada por cada fuente efectivamente citada en estas respuestas — no de todo
el cuaderno, no de fuentes consultadas pero no citadas.
Tipos: @article (revista con revisión por pares, con doi) · @inproceedings
(congreso, con booktitle y doi) · @techreport (estándar o especificación, con
institution y versión) · @online (documentación oficial, con url y urldate).
No inventes campos: si un dato no aparece en la fuente, omite el campo y anótalo
debajo del bloque como "dato no declarado en la fuente". urldate en AAAA-MM-DD.
Si hay DOI, cita por DOI y no por URL de repositorio o agregador.

═══════════════════════════════════════════
PREGUNTA:
5. Para el Bloque 2 bis: ¿qué garantía de entrega da cada tecnología del cuadro?
═══════════════════════════════════════════
```
````


#### Prompt 19 — Interacción 2 — El usuario entrega el contexto y el memo de Daniel sobre el Bloque 2 bis


````text

````


#### Prompt 20 — Usuario (primer bloque pegado)


````text
```
Contexto: cómo está organizado el cuadro

El cuadro comparativo de 3.2 no es una sola tabla gigante — lo dividimos en bloques separados, uno por criterio, para que se lea de corrido:

Bloque 1 — Costo
Bloque 2 — Latencia
Bloque 2 bis — Garantía de entrega ← este
Bloque 3 — Complejidad operacional
Qué es específicamente

El Bloque 2 bis es una tabla nueva, aparte de la de Latencia, que compara las ocho plataformas del cuadro según:

Garantía nativa — si cada plataforma entrega al menos una vez, exactamente una vez, o a lo más una vez.
Duplicados posibles — si esa garantía puede producir mensajes repetidos.
Si la garantía más fuerte cuesta o tarda más — el cruce con costo y latencia (el caso de AWS Step Functions Standard vs. Express es el ejemplo).
Por qué existe como bloque aparte y no como fila de Latencia

Porque no es lo mismo medir cuánto tarda un evento en llegar (latencia) que medir cuántas veces puede llegar o si puede perderse (garantía de entrega). Son dos preguntas distintas, aunque estén relacionadas. Además, es el bloque que conecta directamente el cuadro de 3.2 con tu sección 2.4 — es donde tu contenido sobre entrega al menos una vez / exactamente una vez / a lo más una vez deja de ser solo explicación teórica en el capítulo 2 y se convierte en dato comparable en la tabla del capítulo 3.
```
````


#### Prompt 21 — Usuario (segundo bloque pegado, mismo mensaje)


````text
```
ten en cuenta la info entregada y los esqueletos de las tablas, en el contexto se explica qué es el bloque 2 bis
```
````


#### Prompt 22 — Usuario (tercer bloque pegado, mismo mensaje — memo completo de Daniel)


````text
```
# Propuesta de estructura para 3.2 · Cuadro comparativo

Para: Rodolfo (consolida), Valentina (criterios), Claudio (mitad Google/edge/OSS con Daniel).
De: Daniel. Fecha: 2026-09-20.

Esto es organización del trabajo, no contenido del informe. Los párrafos de criterios (Valentina) y de análisis del cuadro (Rodolfo) los escribe cada uno a mano; aquí solo acordamos qué tabla llenamos y cómo, para no levantar datos dos veces ni con columnas distintas.

## 1. Decisiones que propongo cerrar hoy

1. **Los criterios son los tres de la ficha**: costo, latencia y complejidad operacional. No se agregan otros. Las columnas del cuadro son los campos que hacen medible cada criterio; los límites técnicos que exige la ficha van en una segunda tabla compacta.
2. **Filas = plataformas, columnas = campos** (no transpuesta). Con doce plataformas la versión transpuesta no cabe.
3. **Doce filas**: dos o más plataformas por cada uno de los cuatro modelos de ejecución (FaaS, contenedor sin servidor, borde, siempre encendido) más las alternativas de 3.1 que califiquen. **La fila de instancia siempre encendida es obligatoria**: es el "frente a qué" de la ficha y el ancla del punto de equilibrio de 4.2.
4. **Dos tablas en el cuerpo**, ambas en página horizontal: Tabla 3.2a (criterios, 9 columnas) y Tabla 3.2b (límites técnicos y egreso, 6 columnas). La tabla ampliada con URL y fecha de cada celda va al anexo como respaldo.
5. **Las bases de datos sin servidor no van en 3.2a/3.2b** (sus columnas son otras). Se tratan en 3.1 y en 2.4/2.6; si sobra espacio, tabla chica aparte.

## 2. Tabla 3.2a · Criterios (9 columnas)

| # | Columna | Criterio | Qué se anota | De dónde sale |
|---|---|---|---|---|
| 1 | Plataforma | identificación | nombre oficial del producto | — |
| 2 | Modelo | identificación | exactamente uno de: funciones como servicio · contenedores sin servidor · cómputo en el borde · instancias siempre encendidas | vocabulario de la ficha |
| 3 | Aislamiento | latencia | microVM / contenedor / aislador V8 / Wasm / VM dedicada | documentación oficial del proveedor (no por analogía) |
| 4 | Unidad de cobro y piso mensual | costo | unidad(es) con base temporal (GB-s, vCPU-s, tiempo de CPU, invocación, instancia-hora) y si existe cargo fijo mensual o escala a cero | página oficial de precios |
| 5 | Precio de lista | costo | cifra + producto, USD, región, tramo, fecha de consulta, capa gratuita, "lista" o "solo por cotización" | página o calculadora oficial |
| 6 | Arranque en frío | latencia | p50 / p95 en ms con la fuente entre paréntesis: "(4.1)" para las plataformas de la PoC; para las demás, una única medición publicada con autor y año, o "sin medición" | sección 4.1 (Vicente) o un solo paper acordado |
| 7 | Mitigación del arranque en frío | latencia | mecanismo oficial (concurrencia aprovisionada, SnapStart, instancias mínimas, plan Premium/Flex, no aplica) y **si se factura aparte** | documentación oficial |
| 8 | Qué opera el equipo | complejidad operacional | lista cerrada de responsabilidades que quedan del lado del cliente (ver sección 4) | modelo de responsabilidad compartida del proveedor |
| 9 | Estado y límite que fuerza rediseño | complejidad operacional | si el estado debe externalizarse (y a qué servicio) y cuál límite obliga a partir el trabajo (ej. timeout, payload) | documentación oficial de límites |

## 3. Tabla 3.2b · Límites técnicos y egreso (6 columnas)

| # | Columna | Qué se anota |
|---|---|---|
| 1 | Plataforma | igual que 3.2a |
| 2 | Tiempo máximo de ejecución | valor y unidad; si depende del plan, el del plan cotizado en 3.2a |
| 3 | Memoria / vCPU | rango mínimo–máximo |
| 4 | Payload de entrada / salida | valores; si sincrónico y asincrónico difieren, ambos |
| 5 | Concurrencia / escalado | límite de concurrencia por defecto y forma de escalado (a cero sí/no, máximo de instancias) |
| 6 | Egreso de datos | unidad y precio fechado, tramo gratuito, o "sin cargo" si el proveedor lo declara |

Todo lo que Rodolfo ya levantó y no cabe en estas 15 columnas no se pierde: va a la tabla ampliada del anexo.

## 4. Cómo se mide la complejidad operacional (para tener certeza)

**Lo que hay que decir en el informe, con honestidad:** no existe en la literatura una métrica estandarizada de complejidad operacional. Los surveys la describen cualitativamente; la única evidencia empírica cercana es que una fracción relevante de adoptantes elige serverless para evitar trabajo operativo (Eismann et al., 2021) y que las herramientas de prueba y despliegue son inmaduras (Leitner et al., 2019). Inventar una escala numérica sería una métrica ad hoc indefendible.

**Lo que hacemos en su lugar:** operacionalizar el criterio por **hechos verificables en documentación oficial**, sin puntuación en la celda. El juicio comparativo (qué modelo es más o menos complejo de operar y para qué carga) va en el párrafo de análisis, argumentado a partir de esos hechos y firmado como valoración del grupo.

Tres campos, todos con fuente:

**Campo A · Qué opera el equipo (columna 8).** Se llena con una lista cerrada, la misma para todas las filas, marcando lo que queda del lado del cliente:

- sistema operativo y parcheo
- runtime / dependencias de la aplicación
- planificación de capacidad
- escalado (configuración o manual)
- red (VPC, balanceo, certificados)
- despliegue y versionado
- observabilidad y alertas
- recuperación ante fallos (reintentos, colas de errores)

La celda dice, por ejemplo, "runtime, despliegue, observabilidad, recuperación" y nada más. Comparar filas es leer cuántos y cuáles ítems quedan; no se escribe un número ni un nivel.

**Cómo se declara esta lista, con exactitud.** La lista **no está publicada como tal en ninguna fuente**: es una construcción del grupo derivada de (a) los modelos de responsabilidad compartida que publican los proveedores, que están escritos desde la seguridad (quién protege qué) y a nivel de modelo IaaS/PaaS/FaaS, no de producto, y (b) la comparación en prosa del whitepaper del CNCF, que es la única que enumera responsabilidades operativas explícitas. Así hay que decirlo en la nota de la tabla y en el párrafo de criterios: "lista de responsabilidades construida por el grupo a partir de X, Y, Z y aplicada a cada producto con su documentación oficial". Es aporte propio declarado, no un estándar.

Fuentes verificadas el 2026-09-20 (abiertas y confirmadas; falta que quien las cite las lea completas):
- AWS, *Security Overview of AWS Lambda*, sección "The shared responsibility model": AWS gestiona infraestructura, sistema operativo y plataforma; el cliente, su código, IAM y las imágenes en ECR. URL: https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/the-shared-responsibility-model.html
- Microsoft, *Shared responsibility in the cloud*: matriz de diez filas (datos, configuración, identidades, dispositivos, aplicaciones, controles de red, sistema operativo, hosts, red física, datacenter) por on-premises/IaaS/PaaS/SaaS; nombra Azure Functions como PaaS; **no nombra Container Apps**. URL: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
- Google, *Shared responsibilities and shared fate on Google Cloud*: divide por IaaS/PaaS/SaaS/FaaS; nombra Compute Engine (IaaS) y Cloud Run functions (FaaS); en FaaS el cliente conserva datos, protección del cliente, controles de aplicación e IAM. URL: https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
- CNCF Serverless Whitepaper v1.0, sección "Serverless vs. Other Cloud Native Technologies": en CaaS el desarrollador gestiona sistema operativo y parches, balanceo, capacidad, escalado, logging y monitoreo; FaaS abstrae sistema operativo, runtime y ciclo de vida del contenedor. Es prosa, no matriz. URL: https://github.com/cncf/wg-serverless/blob/master/whitepapers/serverless-overview/README.md
- Castro et al. (2019), *The Rise of Serverless Computing*, CACM, Tabla 1: compara IaaS/PaaS/SaaS/BaaS por nivel de control del desarrollador. Útil como marco, no enumera responsabilidades operativas.

**Límites de este respaldo, para no sobrevender la columna.** Para Cloudflare, Fastly, Deno, Vercel y Netlify no se encontró un documento de responsabilidad compartida equivalente; esas celdas se llenan desde la documentación de arquitectura de cada uno y quedan marcadas en la tabla ampliada como "sin modelo de responsabilidad publicado". Para los proyectos open source, todo queda del lado del equipo salvo lo que provea el clúster gestionado donde corran, y eso se declara.

**Campo B · Estado externo obligatorio (columna 9, primera parte).** Sí/no y a qué servicio hay que externalizar el estado (base de datos, caché, almacenamiento de objetos, Durable Objects). Sale de la documentación oficial que describe el ciclo de vida del entorno de ejecución (por ejemplo, que la instancia puede ser reemplazada entre invocaciones).

**Campo C · Límite que fuerza rediseño (columna 9, segunda parte).** Cuál de los límites de la Tabla 3.2b obliga a partir el trabajo o a cambiar de arquitectura para una carga típica (ejemplo: timeout de 15 minutos para trabajos largos, payload de pocos MB para archivos, 50 ms de CPU para cómputo pesado). Es un hecho de la documentación con una consecuencia declarada, no una opinión.

**Cómo se usa en el análisis.** El párrafo de Rodolfo puede decir "las plataformas de borde dejan menos responsabilidades al equipo pero imponen los límites más restrictivos; la instancia siempre encendida es la única sin límite de tiempo ni de payload y la que más responsabilidades conserva". Eso es comparación no evidente, sostenida por celdas verificables, y es lo que la pauta valora.

## 5. Reglas para llenar celdas

- Toda cifra: producto, moneda, región, fecha de consulta, tipo (lista/cotización). Sin fecha no vale.
- Región: **us-east-1** para AWS (ya fijada por Rodolfo); **us-east4** para Google (o us-central1, pero una sola y declarada); **East US** para Azure; **"global"** para Cloudflare, Fastly, Deno, Vercel y Netlify cuando el precio no depende de región.
- Fuentes de cifras: solo página o calculadora oficial. Los CSV de los agentes (`archivosTemporal/fuentes_agent/`) dan las URLs; la cifra la lee la persona en la página y la anota con la fecha en que la leyó.
- Si algo no está publicado: "solo por cotización" (precio) o "no documentado" (límite). Nunca vacío sin explicación.
- Open source (Knative, OpenFaaS, KEDA, Spin, wasmCloud): precio "no aplica (autoalojado)"; límites = valores por defecto configurables con la página de configuración; el costo real es el clúster, y eso se dice en el análisis.
- Columna 6 (arranque en frío) queda vacía hasta que Vicente entregue 4.1. Para las plataformas fuera de la PoC, acordar entre los tres **un solo** paper del que se toman las cifras, con año, y decirlo en la nota de la tabla.

## 6. Quién hace qué

| Quién | Qué |
|---|---|
| Valentina | Redacta el párrafo de criterios (a mano) con la operacionalización de las secciones 2 y 4; tabla chica de criterios del `main.tex` |
| Rodolfo | Filas AWS y Azure en 3.2a y 3.2b; fila de instancia siempre encendida (EC2 reservada o Compute Engine con CUD, la que se use en 4.2, acordado con Francisca); consolida las dos mitades; escribe el análisis (a mano) |
| Claudio y Daniel | Filas Google, Cloudflare, Fastly, Deno, Vercel, Netlify, open source; filas de alternativas que entren desde 3.1 |
| Vicente | Entrega p50/p95 de 4.1 para la columna 6 |
| Todos | Cada celda con URL y fecha en la planilla de respaldo (`trabajo/3.2-cuadro/`) |

## 7. Pendientes que bloquean

- Valentina confirma (o corrige) la operacionalización de la sección 4. Sin eso no se llena la columna 8.
- Rodolfo y Francisca acuerdan qué configuración always-on se cotiza (misma para el cuadro y para 4.2).
- Los tres acordamos el paper único para la columna 6 en plataformas sin PoC.
- Las cinco fuentes de la sección 4 ya fueron abiertas y confirmadas (2026-09-20); quien llene la columna 8 debe leerlas completas antes de citarlas y registrarlas en el Excel.
```
````


#### Prompt 23 — Usuario


````text
```
guarda toda esta conversación con lujo de detalles en un md en el escritorio, no la quiero  resumida, la quiero exacta, con todo. el archivo se debe llamar "seccion3.2"
```
````


#### Prompt 24 — Usuario (mensaje 1, cortado)


````text
```
la decisión tomada fue:
```
````


#### Prompt 25 — Usuario (mensaje 2, continuación con la lista de plataformas)


````text
```
Tablas 3.2a y 3.2b (Comerciales y de referencia)

AWS Lambda
Azure Functions (Flex Consumption)
Google Cloud Run functions
Google Cloud Run (servicios)
AWS Fargate (ECS)
Azure Container Apps
Cloudflare Workers (Paid)
Fastly Compute
AWS Lambda@Edge / CloudFront Functions
Amazon EC2 reservada (ECS t3.medium)
Oracle Cloud Infrastructure (OCI) Functions
Azion Edge Functions

Tabla 3.2c (Ecosistema de código abierto)

Knative Serving
OpenFaaS
KEDA
Fermyon SpinKube
wasmCloud
Fission

Tabla Ampliada del Anexo (Borde adicional)

Deno Deploy
Vercel
Netlify
```
````


#### Prompt 26 — Interacción 5 — El usuario pide re-ejecutar la Pregunta 5 con el protocolo completo, ya con la lista de plataformas confirmada


````text

````


#### Prompt 27 — Usuario


````text
```
necesito que hagas lo siguiente-----

CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

[... mismo bloque de instrucciones PASO 1 a PASO 5 que en las interacciones anteriores ...]

═══════════════════════════════════════════
PREGUNTA:
5. Para el Bloque 2 bis: ¿qué garantía de entrega da cada tecnología del cuadro?
═══════════════════════════════════════════
```
````


#### Prompt 28 — Usuario


````text
```
entregame todas las interacciones sobre el bloque 2 bis en un md, quiero que incluyas todo, el md se debe llamar "bloque2bis"
```
````


## Sesión 3 — Claude + NotebookLM (MCP) — Criterios de comparación (apertura de 3.2)


Prompts de la persona en esta sesión: 7.


#### Prompt 29 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

PASO 1 — LEER LAS REGLAS
Recupera y lee completa la fuente "Investigación README FIRST" del cuaderno
"Serverless". Si tienes una copia local del mismo archivo .md, léela desde ahí:
es el mismo documento y es más rápido.

Su estructura es:
  - Al inicio: la INSTRUCCIÓN OBLIGATORIA de citación (bloques A a E).
  - En el medio: una ficha de diagnóstico por fuente, de siete puntos.
  - Al FINAL del documento: cuatro tablas que clasifican las 40 fuentes por
    tipo, con una columna "Nota" que fija restricciones de uso por fuente.

Ese documento NO es fuente de contenido. Es el índice y el reglamento: te dice
qué fuentes existen, cómo están clasificadas y qué se puede citar de cada una.
El contenido sale de las fuentes completas del cuaderno, no de él.
Sus reglas mandan sobre cualquier otra consideración y sobre tu conocimiento previo.

PASO 2 — PLANIFICAR ANTES DE RESPONDER
Para cada pregunta, declara primero qué fuentes del cuaderno vas a usar. Por cada
una indica su número de ficha y transcribe su columna "Nota" de la tabla
correspondiente. Si la nota marca una cifra o afirmación como no citable, no la
uses ni siquiera parafraseada: la fuente se queda, el dato puntual se cae.
Si necesitas una fuente que no está en el cuaderno, dilo. No la sustituyas por
conocimiento propio ni por búsqueda web.

PASO 3 — RECUPERACIÓN DELEGADA A NOTEBOOKLM

No traigas la fuente completa a tu contexto. En vez de eso, pídele a NotebookLM
que lea la fuente completa y te devuelva la cita ya transcrita. Formula la
consulta al MCP en estos términos:

  "Lee COMPLETA la fuente [nombre del archivo] del cuaderno. Responde [pregunta].
   Por cada afirmación indica:
   (a) el nombre exacto del archivo de donde sale;
   (b) el localizador más preciso que el propio documento contenga: número y
       título de sección, capítulo, página impresa o encabezado;
   (c) la cita textual entre comillas, transcrita literalmente en el idioma
       original, incluyendo el contexto anterior y posterior suficiente para
       que se entienda de qué parte del documento salió y qué está afirmando
       —no una frase suelta, sino el pasaje completo;
   (d) si el documento matiza, condiciona o contradice esa afirmación en otra
       parte, transcribe también ese pasaje;
   (e) además de la cita, devuelve el PASAJE REAL COMPLETO en un bloque aparte,
       transcrito palabra por palabra tal como aparece en el documento:
       respetando mayúsculas, puntuación, cifras, unidades, nombres de
       parámetros y saltos de párrafo. Si el pasaje ocupa varios párrafos,
       transcríbelos todos. Si omites algo intermedio, márcalo con [...] y
       nunca al inicio ni al final del pasaje. Ese bloque debe poder leerse
       solo y entenderse sin la respuesta.
   No resumas. No parafrasees dentro de las comillas. Si no puedes localizar
   la afirmación en el texto, dilo."

REGLAS AL RECIBIR LA RESPUESTA
1. Si NotebookLM devuelve una afirmación sin cita textual, o con una cita que
   parece resumen en vez de transcripción, NO la uses: vuelve a preguntar
   pidiendo la transcripción literal.
2. Si devuelve la cita pero sin localizador, consérvala y marca la ubicación
   como "no declarada por la fuente". Nunca inventes sección, capítulo ni página.
3. Traer el texto de la fuente a tu propio contexto SOLO en estos casos:
   - la afirmación contiene una cifra, un porcentaje, un precio o una medición;
   - es una definición que se va a transcribir literal en el informe;
   - NotebookLM dio dos respuestas distintas sobre lo mismo;
   - la cita recibida no permite saber de qué parte del documento salió.
   En esos casos, verifica el pasaje tú mismo y dilo: "verificado contra el
   texto completo".
4. Toda cita no verificada por ti va marcada como "según NotebookLM, sin
   verificación directa".
5. La respuesta y el texto de la fuente van SIEMPRE separados. Primero la
   respuesta redactada; después, en bloque aparte y entre comillas, el pasaje
   real. Nunca mezclarlos en el mismo párrafo ni intercalar palabras propias
   dentro de las comillas.
6. Si necesitas aclarar algo dentro de una cita, hazlo entre corchetes y en
   tu propio nombre: "[...] el broker [de Kafka] asigna [...]". Todo lo que
   esté entre comillas y sin corchetes tiene que estar literal en la fuente.

PASO 4 — FORMATO DE SALIDA (repetir por cada pregunta)

### Pregunta N: [repetir la pregunta]

**Fuentes usadas.** [nº de ficha + nombre del archivo + su nota de la tabla,
por cada fuente que vas a usar en esta pregunta]

**Respuesta.** [respuesta directa, redactada con tus palabras, sin relleno.
Aquí no van comillas: esto es la síntesis, la prueba viene abajo]

**Evidencia.** Por cada afirmación de la respuesta:

  1. Afirmación: [la afirmación concreta que se está respaldando]
  2. Fuente: [nombre exacto del archivo + número de ficha del README]
  3. Ubicación: [sección, capítulo, página o encabezado | "no declarada
     por la fuente"]
  4. Texto real de la fuente:

     > "[transcripción literal e íntegra del pasaje, con el contexto anterior
     > y posterior necesario para saber de qué parte del documento salió y
     > qué está afirmando. Varios párrafos si corresponde. Sin editar, sin
     > resumir, sin corregir.]"

  5. Traducción (si aplica): [marcada como traducción propia, fuera de las
     comillas]
  6. Matices en otra parte del documento (si los hay): [ubicación + cita
     textual del pasaje que condiciona o contradice lo anterior]
  7. Verificación: [verificado contra el texto completo] | [según NotebookLM,
     sin verificación directa]

**Detalles que no se pueden pasar por alto.** Versión del documento, fecha de
publicación o actualización, valores por defecto, condiciones, excepciones y
limitaciones que el propio texto declare.

**Interpretación propia.** [Solo si la hay, marcada como tal. Lo que no está
literal en la fuente va aquí, nunca mezclado con la evidencia.]

PASO 5 — CIERRE (una sola vez, al final de todas las preguntas)

## Referencias (BibTeX)
Una entrada por cada fuente efectivamente citada en estas respuestas — no de todo
el cuaderno, no de fuentes consultadas pero no citadas.
Tipos: @article (revista con revisión por pares, con doi) · @inproceedings
(congreso, con booktitle y doi) · @techreport (estándar o especificación, con
institution y versión) · @online (documentación oficial, con url y urldate).
No inventes campos: si un dato no aparece en la fuente, omite el campo y anótalo
debajo del bloque como "dato no declarado en la fuente". urldate en AAAA-MM-DD.
Si hay DOI, cita por DOI y no por URL de repositorio o agregador.

═══════════════════════════════════════════
PREGUNTA:
1. ¿Cómo se define "costo" de forma comparable entre los cuatro modelos?

═══════════════════════════════════════════
```
````


#### Prompt 30 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

[... mismo bloque de instrucciones PASO 1 a PASO 5 que en el Turno 1 ...]

═══════════════════════════════════════════
PREGUNTA:
2. ¿Cómo se define "latencia" de forma comparable — arranque en frío declarado o percentil?a

═══════════════════════════════════════════
```
````


#### Prompt 31 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
[... mismo bloque de instrucciones PASO 1 a PASO 5 que en los turnos anteriores ...]

═══════════════════════════════════════════
PREGUNTA:
3. ¿Cómo se define "complejidad operacional" de forma defendible, no solo como opinión del grupo?
═══════════════════════════════════════════
```
````


#### Prompt 32 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
[... mismo bloque de instrucciones PASO 1 a PASO 5 que en los turnos anteriores ...]

═══════════════════════════════════════════
PREGUNTA:
4. ¿En qué formato necesitan Rodolfo y Claudio que entregues los criterios para llenar el cuadro?
═══════════════════════════════════════════
```
````


#### Prompt 33 — Usuario


````text
```
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
[... mismo bloque de instrucciones PASO 1 a PASO 5 que en los turnos anteriores ...]

═══════════════════════════════════════════
PREGUNTA:
5. Para el Bloque 2 bis: ¿qué garantía de entrega da cada tecnología del cuadro?
═══════════════════════════════════════════
```
````


#### Prompt 34 — Usuario


````text
```
Contexto: cómo está organizado el cuadro

El cuadro comparativo de 3.2 no es una sola tabla gigante — lo dividimos en bloques separados, uno por criterio, para que se lea de corrido:

Bloque 1 — Costo
Bloque 2 — Latencia
Bloque 2 bis — Garantía de entrega ← este
Bloque 3 — Complejidad operacional
Qué es específicamente

El Bloque 2 bis es una tabla nueva, aparte de la de Latencia, que compara las ocho plataformas del cuadro según:

Garantía nativa — si cada plataforma entrega al menos una vez, exactamente una vez, o a lo más una vez.
Duplicados posibles — si esa garantía puede producir mensajes repetidos.
Si la garantía más fuerte cuesta o tarda más — el cruce con costo y latencia (el caso de AWS Step Functions Standard vs. Express es el ejemplo).
Por qué existe como bloque aparte y no como fila de Latencia

Porque no es lo mismo medir cuánto tarda un evento en llegar (latencia) que medir cuántas veces puede llegar o si puede perderse (garantía de entrega). Son dos preguntas distintas, aunque estén relacionadas. Además, es el bloque que conecta directamente el cuadro de 3.2 con tu sección 2.4 — es donde tu contenido sobre entrega al menos una vez / exactamente una vez / a lo más una vez deja de ser solo explicación teórica en el capítulo 2 y se convierte en dato comparable en la tabla del capítulo 3.
```

y, en un segundo bloque pegado en el mismo mensaje:

```
ten en cuenta la info entregada y los esqueletos de las tablas, en el contexto se explica qué es el bloque 2 bis
```

y, en un tercer bloque pegado en el mismo mensaje:

```
# Propuesta de estructura para 3.2 · Cuadro comparativo

Para: Rodolfo (consolida), Valentina (criterios), Claudio (mitad Google/edge/OSS con Daniel).
De: Daniel. Fecha: 2026-09-20.

Esto es organización del trabajo, no contenido del informe. Los párrafos de criterios (Valentina) y de análisis del cuadro (Rodolfo) los escribe cada uno a mano; aquí solo acordamos qué tabla llenamos y cómo, para no levantar datos dos veces ni con columnas distintas.

## 1. Decisiones que propongo cerrar hoy

1. **Los criterios son los tres de la ficha**: costo, latencia y complejidad operacional. No se agregan otros. Las columnas del cuadro son los campos que hacen medible cada criterio; los límites técnicos que exige la ficha van en una segunda tabla compacta.
2. **Filas = plataformas, columnas = campos** (no transpuesta). Con doce plataformas la versión transpuesta no cabe.
3. **Doce filas**: dos o más plataformas por cada uno de los cuatro modelos de ejecución (FaaS, contenedor sin servidor, borde, siempre encendido) más las alternativas de 3.1 que califiquen. **La fila de instancia siempre encendida es obligatoria**: es el "frente a qué" de la ficha y el ancla del punto de equilibrio de 4.2.
4. **Dos tablas en el cuerpo**, ambas en página horizontal: Tabla 3.2a (criterios, 9 columnas) y Tabla 3.2b (límites técnicos y egreso, 6 columnas). La tabla ampliada con URL y fecha de cada celda va al anexo como respaldo.
5. **Las bases de datos sin servidor no van en 3.2a/3.2b** (sus columnas son otras). Se tratan en 3.1 y en 2.4/2.6; si sobra espacio, tabla chica aparte.

## 2. Tabla 3.2a · Criterios (9 columnas)

| # | Columna | Criterio | Qué se anota | De dónde sale |
|---|---|---|---|---|
| 1 | Plataforma | identificación | nombre oficial del producto | — |
| 2 | Modelo | identificación | exactamente uno de: funciones como servicio · contenedores sin servidor · cómputo en el borde · instancias siempre encendidas | vocabulario de la ficha |
| 3 | Aislamiento | latencia | microVM / contenedor / aislador V8 / Wasm / VM dedicada | documentación oficial del proveedor (no por analogía) |
| 4 | Unidad de cobro y piso mensual | costo | unidad(es) con base temporal (GB-s, vCPU-s, tiempo de CPU, invocación, instancia-hora) y si existe cargo fijo mensual o escala a cero | página oficial de precios |
| 5 | Precio de lista | costo | cifra + producto, USD, región, tramo, fecha de consulta, capa gratuita, "lista" o "solo por cotización" | página o calculadora oficial |
| 6 | Arranque en frío | latencia | p50 / p95 en ms con la fuente entre paréntesis: "(4.1)" para las plataformas de la PoC; para las demás, una única medición publicada con autor y año, o "sin medición" | sección 4.1 (Vicente) o un solo paper acordado |
| 7 | Mitigación del arranque en frío | latencia | mecanismo oficial (concurrencia aprovisionada, SnapStart, instancias mínimas, plan Premium/Flex, no aplica) y **si se factura aparte** | documentación oficial |
| 8 | Qué opera el equipo | complejidad operacional | lista cerrada de responsabilidades que quedan del lado del cliente (ver sección 4) | modelo de responsabilidad compartida del proveedor |
| 9 | Estado y límite que fuerza rediseño | complejidad operacional | si el estado debe externalizarse (y a qué servicio) y cuál límite obliga a partir el trabajo (ej. timeout, payload) | documentación oficial de límites |

## 3. Tabla 3.2b · Límites técnicos y egreso (6 columnas)

| # | Columna | Qué se anota |
|---|---|---|
| 1 | Plataforma | igual que 3.2a |
| 2 | Tiempo máximo de ejecución | valor y unidad; si depende del plan, el del plan cotizado en 3.2a |
| 3 | Memoria / vCPU | rango mínimo–máximo |
| 4 | Payload de entrada / salida | valores; si sincrónico y asincrónico difieren, ambos |
| 5 | Concurrencia / escalado | límite de concurrencia por defecto y forma de escalado (a cero sí/no, máximo de instancias) |
| 6 | Egreso de datos | unidad y precio fechado, tramo gratuito, o "sin cargo" si el proveedor lo declara |

Todo lo que Rodolfo ya levantó y no cabe en estas 15 columnas no se pierde: va a la tabla ampliada del anexo.

## 4. Cómo se mide la complejidad operacional (para tener certeza)

**Lo que hay que decir en el informe, con honestidad:** no existe en la literatura una métrica estandarizada de complejidad operacional. Los surveys la describen cualitativamente; la única evidencia empírica cercana es que una fracción relevante de adoptantes elige serverless para evitar trabajo operativo (Eismann et al., 2021) y que las herramientas de prueba y despliegue son inmaduras (Leitner et al., 2019). Inventar una escala numérica sería una métrica ad hoc indefendible.

**Lo que hacemos en su lugar:** operacionalizar el criterio por **hechos verificables en documentación oficial**, sin puntuación en la celda. El juicio comparativo (qué modelo es más o menos complejo de operar y para qué carga) va en el párrafo de análisis, argumentado a partir de esos hechos y firmado como valoración del grupo.

Tres campos, todos con fuente:

**Campo A · Qué opera el equipo (columna 8).** Se llena con una lista cerrada, la misma para todas las filas, marcando lo que queda del lado del cliente:

- sistema operativo y parcheo
- runtime / dependencias de la aplicación
- planificación de capacidad
- escalado (configuración o manual)
- red (VPC, balanceo, certificados)
- despliegue y versionado
- observabilidad y alertas
- recuperación ante fallos (reintentos, colas de errores)

La celda dice, por ejemplo, "runtime, despliegue, observabilidad, recuperación" y nada más. Comparar filas es leer cuántos y cuáles ítems quedan; no se escribe un número ni un nivel.

**Cómo se declara esta lista, con exactitud.** La lista **no está publicada como tal en ninguna fuente**: es una construcción del grupo derivada de (a) los modelos de responsabilidad compartida que publican los proveedores, que están escritos desde la seguridad (quién protege qué) y a nivel de modelo IaaS/PaaS/FaaS, no de producto, y (b) la comparación en prosa del whitepaper del CNCF, que es la única que enumera responsabilidades operativas explícitas. Así hay que decirlo en la nota de la tabla y en el párrafo de criterios: "lista de responsabilidades construida por el grupo a partir de X, Y, Z y aplicada a cada producto con su documentación oficial". Es aporte propio declarado, no un estándar.

Fuentes verificadas el 2026-09-20 (abiertas y confirmadas; falta que quien las cite las lea completas):
- AWS, *Security Overview of AWS Lambda*, sección "The shared responsibility model": AWS gestiona infraestructura, sistema operativo y plataforma; el cliente, su código, IAM y las imágenes en ECR. URL: https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/the-shared-responsibility-model.html
- Microsoft, *Shared responsibility in the cloud*: matriz de diez filas (datos, configuración, identidades, dispositivos, aplicaciones, controles de red, sistema operativo, hosts, red física, datacenter) por on-premises/IaaS/PaaS/SaaS; nombra Azure Functions como PaaS; **no nombra Container Apps**. URL: https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
- Google, *Shared responsibilities and shared fate on Google Cloud*: divide por IaaS/PaaS/SaaS/FaaS; nombra Compute Engine (IaaS) y Cloud Run functions (FaaS); en FaaS el cliente conserva datos, protección del cliente, controles de aplicación e IAM. URL: https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
- CNCF Serverless Whitepaper v1.0, sección "Serverless vs. Other Cloud Native Technologies": en CaaS el desarrollador gestiona sistema operativo y parches, balanceo, capacidad, escalado, logging y monitoreo; FaaS abstrae sistema operativo, runtime y ciclo de vida del contenedor. Es prosa, no matriz. URL: https://github.com/cncf/wg-serverless/blob/master/whitepapers/serverless-overview/README.md
- Castro et al. (2019), *The Rise of Serverless Computing*, CACM, Tabla 1: compara IaaS/PaaS/SaaS/BaaS por nivel de control del desarrollador. Útil como marco, no enumera responsabilidades operativas.

**Límites de este respaldo, para no sobrevender la columna.** Para Cloudflare, Fastly, Deno, Vercel y Netlify no se encontró un documento de responsabilidad compartida equivalente; esas celdas se llenan desde la documentación de arquitectura de cada uno y quedan marcadas en la tabla ampliada como "sin modelo de responsabilidad publicado". Para los proyectos open source, todo queda del lado del equipo salvo lo que provea el clúster gestionado donde corran, y eso se declara.

**Campo B · Estado externo obligatorio (columna 9, primera parte).** Sí/no y a qué servicio hay que externalizar el estado (base de datos, caché, almacenamiento de objetos, Durable Objects). Sale de la documentación oficial que describe el ciclo de vida del entorno de ejecución (por ejemplo, que la instancia puede ser reemplazada entre invocaciones).

**Campo C · Límite que fuerza rediseño (columna 9, segunda parte).** Cuál de los límites de la Tabla 3.2b obliga a partir el trabajo o a cambiar de arquitectura para una carga típica (ejemplo: timeout de 15 minutos para trabajos largos, payload de pocos MB para archivos, 50 ms de CPU para cómputo pesado). Es un hecho de la documentación con una consecuencia declarada, no una opinión.

**Cómo se usa en el análisis.** El párrafo de Rodolfo puede decir "las plataformas de borde dejan menos responsabilidades al equipo pero imponen los límites más restrictivos; la instancia siempre encendida es la única sin límite de tiempo ni de payload y la que más responsabilidades conserva". Eso es comparación no evidente, sostenida por celdas verificables, y es lo que la pauta valora.

## 5. Reglas para llenar celdas

- Toda cifra: producto, moneda, región, fecha de consulta, tipo (lista/cotización). Sin fecha no vale.
- Región: **us-east-1** para AWS (ya fijada por Rodolfo); **us-east4** para Google (o us-central1, pero una sola y declarada); **East US** para Azure; **"global"** para Cloudflare, Fastly, Deno, Vercel y Netlify cuando el precio no depende de región.
- Fuentes de cifras: solo página o calculadora oficial. Los CSV de los agentes (`archivosTemporal/fuentes_agent/`) dan las URLs; la cifra la lee la persona en la página y la anota con la fecha en que la leyó.
- Si algo no está publicado: "solo por cotización" (precio) o "no documentado" (límite). Nunca vacío sin explicación.
- Open source (Knative, OpenFaaS, KEDA, Spin, wasmCloud): precio "no aplica (autoalojado)"; límites = valores por defecto configurables con la página de configuración; el costo real es el clúster, y eso se dice en el análisis.
- Columna 6 (arranque en frío) queda vacía hasta que Vicente entregue 4.1. Para las plataformas fuera de la PoC, acordar entre los tres **un solo** paper del que se toman las cifras, con año, y decirlo en la nota de la tabla.

## 6. Quién hace qué

| Quién | Qué |
|---|---|
| Valentina | Redacta el párrafo de criterios (a mano) con la operacionalización de las secciones 2 y 4; tabla chica de criterios del `main.tex` |
| Rodolfo | Filas AWS y Azure en 3.2a y 3.2b; fila de instancia siempre encendida (EC2 reservada o Compute Engine con CUD, la que se use en 4.2, acordado con Francisca); consolida las dos mitades; escribe el análisis (a mano) |
| Claudio y Daniel | Filas Google, Cloudflare, Fastly, Deno, Vercel, Netlify, open source; filas de alternativas que entren desde 3.1 |
| Vicente | Entrega p50/p95 de 4.1 para la columna 6 |
| Todos | Cada celda con URL y fecha en la planilla de respaldo (`trabajo/3.2-cuadro/`) |

## 7. Pendientes que bloquean

- Valentina confirma (o corrige) la operacionalización de la sección 4. Sin eso no se llena la columna 8.
- Rodolfo y Francisca acuerdan qué configuración always-on se cotiza (misma para el cuadro y para 4.2).
- Los tres acordamos el paper único para la columna 6 en plataformas sin PoC.
- Las cinco fuentes de la sección 4 ya fueron abiertas y confirmadas (2026-09-20); quien llene la columna 8 debe leerlas completas antes de citarlas y registrarlas en el Excel.
```
````


#### Prompt 35 — Usuario


````text
```
guarda toda esta conversación con lujo de detalles en un md en el escritorio, no la quiero  resumida, la quiero exacta, con todo. el archivo se debe llamar "seccion3.2"
```
````


## Sesión 4 — Claude + NotebookLM (MCP) — Sección 2.4 (diseño orientado a eventos)


Prompts de la persona en esta sesión: 11.


#### Prompt 36 — TURNO 1 — Mensaje del usuario (instrucciones + Pregunta 1)


````text
CONTEXTO
Tienes acceso a NotebookLM por MCP. El cuaderno de trabajo es "Serverless".
Si no sabes qué herramientas expone ese MCP, lístalas antes de hacer nada.
Si el MCP no responde o el cuaderno "Serverless" no aparece, DETENTE y dímelo:
no respondas de memoria.

PASO 1 — LEER LAS REGLAS
Recupera y lee completa la fuente "Investigación README FIRST" del cuaderno
"Serverless". Si tienes una copia local del mismo archivo .md, léela desde ahí:
es el mismo documento y es más rápido.

Su estructura es:
  - Al inicio: la INSTRUCCIÓN OBLIGATORIA de citación (bloques A a E).
  - En el medio: una ficha de diagnóstico por fuente, de siete puntos.
  - Al FINAL del documento: cuatro tablas que clasifican las 40 fuentes por
    tipo, con una columna "Nota" que fija restricciones de uso por fuente.

Ese documento NO es fuente de contenido. Es el índice y el reglamento: te dice
qué fuentes existen, cómo están clasificadas y qué se puede citar de cada una.
El contenido sale de las fuentes completas del cuaderno, no de él.
Sus reglas mandan sobre cualquier otra consideración y sobre tu conocimiento previo.

PASO 2 — PLANIFICAR ANTES DE RESPONDER
Para cada pregunta, declara primero qué fuentes del cuaderno vas a usar. Por cada
una indica su número de ficha y transcribe su columna "Nota" de la tabla
correspondiente. Si la nota marca una cifra o afirmación como no citable, no la
uses ni siquiera parafraseada: la fuente se queda, el dato puntual se cae.
Si necesitas una fuente que no está en el cuaderno, dilo. No la sustituyas por
conocimiento propio ni por búsqueda web.

PASO 3 — RECUPERACIÓN DELEGADA A NOTEBOOKLM

No traigas la fuente completa a tu contexto. En vez de eso, pídele a NotebookLM
que lea la fuente completa y te devuelva la cita ya transcrita. Formula la
consulta al MCP en estos términos:

  "Lee COMPLETA la fuente [nombre del archivo] del cuaderno. Responde [pregunta].
   Por cada afirmación indica:
   (a) el nombre exacto del archivo de donde sale;
   (b) el localizador más preciso que el propio documento contenga: número y
       título de sección, capítulo, página impresa o encabezado;
   (c) la cita textual entre comillas, transcrita literalmente en el idioma
       original, incluyendo el contexto anterior y posterior suficiente para
       que se entienda de qué parte del documento salió y qué está afirmando
       —no una frase suelta, sino el pasaje completo;
   (d) si el documento matiza, condiciona o contradice esa afirmación en otra
       parte, transcribe también ese pasaje;
   (e) además de la cita, devuelve el PASAJE REAL COMPLETO en un bloque aparte,
       transcrito palabra por palabra tal como aparece en el documento:
       respetando mayúsculas, puntuación, cifras, unidades, nombres de
       parámetros y saltos de párrafo. Si el pasaje ocupa varios párrafos,
       transcríbelos todos. Si omites algo intermedio, márcalo con [...] y
       nunca al inicio ni al final del pasaje. Ese bloque debe poder leerse
       solo y entenderse sin la respuesta.
   No resumas. No parafrasees dentro de las comillas. Si no puedes localizar
   la afirmación en el texto, dilo."

REGLAS AL RECIBIR LA RESPUESTA
1. Si NotebookLM devuelve una afirmación sin cita textual, o con una cita que
   parece resumen en vez de transcripción, NO la uses: vuelve a preguntar
   pidiendo la transcripción literal.
2. Si devuelve la cita pero sin localizador, consérvala y marca la ubicación
   como "no declarada por la fuente". Nunca inventes sección, capítulo ni página.
3. Traer el texto de la fuente a tu propio contexto SOLO en estos casos:
   - la afirmación contiene una cifra, un porcentaje, un precio o una medición;
   - es una definición que se va a transcribir literal en el informe;
   - NotebookLM dio dos respuestas distintas sobre lo mismo;
   - la cita recibida no permite saber de qué parte del documento salió.
   En esos casos, verifica el pasaje tú mismo y dilo: "verificado contra el
   texto completo".
4. Toda cita no verificada por ti va marcada como "según NotebookLM, sin
   verificación directa".
5. La respuesta y el texto de la fuente van SIEMPRE separados. Primero la
   respuesta redactada; después, en bloque aparte y entre comillas, el pasaje
   real. Nunca mezclarlos en el mismo párrafo ni intercalar palabras propias
   dentro de las comillas.
6. Si necesitas aclarar algo dentro de una cita, hazlo entre corchetes y en
   tu propio nombre: "[...] el broker [de Kafka] asigna [...]". Todo lo que
   esté entre comillas y sin corchetes tiene que estar literal en la fuente.

PASO 4 — FORMATO DE SALIDA (repetir por cada pregunta)

### Pregunta N: [repetir la pregunta]

**Fuentes usadas.** [nº de ficha + nombre del archivo + su nota de la tabla,
por cada fuente que vas a usar en esta pregunta]

**Respuesta.** [respuesta directa, redactada con tus palabras, sin relleno.
Aquí no van comillas: esto es la síntesis, la prueba viene abajo]

**Evidencia.** Por cada afirmación de la respuesta:

  1. Afirmación: [la afirmación concreta que se está respaldando]
  2. Fuente: [nombre exacto del archivo + número de ficha del README]
  3. Ubicación: [sección, capítulo, página o encabezado | "no declarada
     por la fuente"]
  4. Texto real de la fuente:

     > "[transcripción literal e íntegra del pasaje, con el contexto anterior
     > y posterior necesario para saber de qué parte del documento salió y
     > qué está afirmando. Varios párrafos si corresponde. Sin editar, sin
     > resumir, sin corregir.]"

  5. Traducción (si aplica): [marcada como traducción propia, fuera de las
     comillas]
  6. Matices en otra parte del documento (si los hay): [ubicación + cita
     textual del pasaje que condiciona o contradice lo anterior]
  7. Verificación: [verificado contra el texto completo] | [según NotebookLM,
     sin verificación directa]

**Detalles que no se pueden pasar por alto.** Versión del documento, fecha de
publicación o actualización, valores por defecto, condiciones, excepciones y
limitaciones que el propio texto declare.

**Interpretación propia.** [Solo si la hay, marcada como tal. Lo que no está
literal en la fuente va aquí, nunca mezclado con la evidencia.]

PASO 5 — CIERRE (una sola vez, al final de todas las preguntas)

## Referencias (BibTeX)
Una entrada por cada fuente efectivamente citada en estas respuestas — no de todo
el cuaderno, no de fuentes consultadas pero no citadas.
Tipos: @article (revista con revisión por pares, con doi) · @inproceedings
(congreso, con booktitle y doi) · @techreport (estándar o especificación, con
institution y versión) · @online (documentación oficial, con url y urldate).
No inventes campos: si un dato no aparece en la fuente, omite el campo y anótalo
debajo del bloque como "dato no declarado en la fuente". urldate en AAAA-MM-DD.
Si hay DOI, cita por DOI y no por URL de repositorio o agregador.

═══════════════════════════════════════════
PREGUNTAS:

1. ¿Qué es una arquitectura orientada a eventos?═══════════════════════════════════════════


---
````


#### Prompt 37 — TURNO 2 - Mensaje del usuario


````text
(Mismas instrucciones CONTEXTO / PASO 1 a PASO 5 del Turno 1, reproducidas integras arriba; el usuario las repite de forma identica en cada turno, cambiando solo la seccion final PREGUNTA)

===========================================
PREGUNTA:
2. Cual es la diferencia entre colas (punto a punto) y pub/sub (broadcast)?
===========================================

---
````


#### Prompt 38 — TURNO 3 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
3. Que es idempotencia y por que importa cuando hay reintentos automaticos?
===========================================

---
````


#### Prompt 39 — TURNO 4 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
4. Como se define formalmente cada una de las tres semanticas de entrega (at-most-once / at-least-once / exactly-once)?
===========================================

---
````


#### Prompt 40 — TURNO 5 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
5. Como garantiza -o no- cada tecnologia concreta esas semanticas?
===========================================

---
````


#### Prompt 41 — TURNO 6 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
6. Que es orquestacion vs. coreografia, con un ejemplo de cada patron?
===========================================

---
````


#### Prompt 42 — TURNO 7 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
7. Como se conecta nativamente FaaS a eventos? Cual es el mecanismo tecnico?
===========================================

---
````


#### Prompt 43 — TURNO 8 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
8. Como consumen eventos los contenedores sin servidor?
===========================================

---
````


#### Prompt 44 — TURNO 9 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
9. Como maneja el computo en el borde los eventos, dado que su modelo es mas cercano a solicitud/respuesta?
===========================================

---
````


#### Prompt 45 — TURNO 10 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
10. Como luce un consumidor de eventos en una instancia siempre encendida?
===========================================

---
````


#### Prompt 46 — TURNO 11 - Mensaje del usuario


````text
(Mismas instrucciones estandar del Turno 1)

===========================================
PREGUNTA:
11. Dado todo lo anterior, bajo que condiciones de carga y tipo de evento conviene cada modelo?
===========================================

(NOTA: mientras el asistente investigaba esta pregunta 11, el usuario envio un mensaje adicional en medio del turno: "guarda toda esta conversacion con lujo de detalles en un md en el escritorio, no la quiero resumida, la quiero exacta, con todo. el archivo se debe llamar 'seccion2.4'". Este mismo archivo que estas leyendo es la respuesta a ese pedido.)

---
````

