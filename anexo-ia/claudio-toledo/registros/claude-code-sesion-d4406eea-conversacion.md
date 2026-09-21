# Conversación completa — sesión del 18-09: revisión de fuentes y bibliografía

- Herramienta: Claude Code 2.1.271
- Identificador de sesión: `d4406eea-e25d-4bef-a2fe-4e0b7442cca2`
- Registro de origen: `d4406eea-e25d-4bef-a2fe-4e0b7442cca2.jsonl`
- Modelos: claude-opus-5
- Inicio: 18-09-2026 02:46
- Fin: 19-09-2026 14:58

De cada intervención del modelo se transcribe el texto y se listan las
herramientas que ejecutó (lectura y escritura de archivos, comandos y
consultas a documentación). La salida de esas herramientas no se incluye
por extensión; el registro original la conserva íntegra.

---

## Persona — prompt 1 — 18-09-2026 02:46

```text
okey quiero que analices los archivos, Soy claudio y tengo que empezar con el trabajo de investigacion, no se bien por donde comenzar, se que tengo que recabar articulos, pero no se muy como buscarlos, se que puedo buscarlos manualmente en web of cience, pero no se bien si me sirven ono para lo que es mi seccion
```

### Claude Code — 18-09-2026 02:46

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 02:46

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 02:46

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 02:46

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 02:46

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 02:47

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 02:47

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 02:47

Hola, Claudio. Leí los dos archivos: la guía del equipo y las Indicaciones del profesor (las 17 páginas). Esto es lo que te toca, qué fuentes necesitas y cómo buscarlas.

## ⚠️ Primero, dos alertas

1. **Hoy es viernes 18 y la entrega es el lunes 21 de septiembre.** Te quedan 3 días, y Daniel (el jefe) necesita tu parte antes para integrarla. Pregúntale hoy mismo cuál es tu plazo interno.
2. **Tu copia de la guía está cortada.** El archivo [TERABYTE-TI05-Guia-del-equipo_md.md](TERABYTE-TI05-Guia-del-equipo_md.md) termina a mitad de la tabla de la sección 5 (los "otros"), en la línea 123, con un "...". Esa tabla es justamente la que usas tú. Pide la versión completa.

## Qué te toca a ti (integrante 7, junto con Daniel Miranda)

| Entregable | Qué es |
|---|---|
| **3.2, tu mitad del cuadro** | Límites técnicos y precios con fecha de **Google Cloud Run (y Cloud Run functions), Cloudflare Workers/D1/R2, Fastly Compute, Deno Deploy, Vercel, Netlify y el open source** (Knative, OpenFaaS, KEDA, Spin, wasmCloud, Wasmtime) |
| **3.1 Alternativas adicionales** | Por cada una de las 5 listas de la ficha, **al menos 2 tecnologías que no estén nombradas**, con la frase *"entra porque aporta X a la comparación"*. En el cuerpo va una tabla de unas 10 filas y dos párrafos. La búsqueda documentada va al anexo. |

## La clave: casi nada de tu sección sale de Web of Science

Por eso te cuesta saber si los artículos te sirven. Tus fuentes se reparten así:

| Lo que necesitas | De dónde sale |
|---|---|
| Precios y límites (timeout, memoria, tamaño de la carga, regiones) | **Documentación oficial del proveedor.** Nunca de un paper, porque los precios cambian. Cada cifra lleva producto, moneda, región, fecha de consulta y si es precio de lista o cotización (Indicaciones, punto 5). |
| Si un proveedor no publica precio | Escribes "solo por cotización". No sirven cifras de blogs. |
| Alternativas nuevas (3.1) | Documentación oficial, más un registro de la búsqueda: dónde buscaste, qué descartaste, por qué y en qué fecha. Eso va al anexo. |
| **1 o 2 artículos académicos** (tu aporte a las 10 del grupo) | **Aquí sí entra Web of Science**, junto con Scopus, IEEE Xplore y ACM Digital Library desde la biblioteca PUCV. |

Los artículos te sirven para **respaldar los criterios de comparación** y para justificar por qué una plataforma merece entrar. No son la fuente de la tabla.

## Cómo buscar en Web of Science

Usa la búsqueda avanzada con `TS=` (busca en título, resumen y palabras clave):

```
TS=("serverless" OR "function-as-a-service" OR FaaS) AND TS=(benchmark* OR "performance evaluation" OR comparison)
```
```
TS=("serverless" OR "edge computing") AND TS=(WebAssembly OR "V8 isolate*" OR "edge function*")
```
```
TS=("open source") AND TS=(serverless) AND TS=(Knative OR OpenFaaS OR OpenWhisk OR framework*)
```

Filtra por **años 2019–2026** y por el área **Computer Science**. Ordena por número de citas para ver primero los trabajos base.

**Para saber si un artículo te sirve (unos 10 minutos por artículo):**
1. Lee el título y el resumen. ¿Compara plataformas de tu mitad (Cloud Run, Cloudflare, open source, edge)? Si no, descártalo.
2. Mira directamente las tablas y la conclusión. ¿Trae criterios o métricas que puedas usar como columnas o para justificar una alternativa?
3. ¿Está publicado en una revista o congreso con revisión por pares? arXiv sin publicar vale menos.
4. Si cumple las tres, anótalo en la planilla común con el DOI.

**Candidatos que conozco, para que los busques y verifiques tú.** Las reglas del curso dicen que una referencia inexistente es un error grave, así que confirma cada uno en la base antes de citarlo:
- Scheuner & Leitner, *Function-as-a-Service performance evaluation: A multivocal literature review*, Journal of Systems and Software (2020). Es una revisión de cómo se miden y comparan las plataformas.
- Copik et al., *SeBS: A Serverless Benchmark Suite*, Middleware 2021.
- Wang et al., *Peeking Behind the Curtains of Serverless Platforms*, USENIX ATC 2018.
- Li et al., *Understanding Open Source Serverless Platforms: Design Considerations and Performance*, WoSC 2019. Encaja con tu parte de open source.
- Gackstatter et al., *Pushing Serverless to the Edge with WebAssembly Runtimes*, CCGrid 2022. Encaja con edge y WASM.

## Candidatos para 3.1, a verificar en la documentación oficial

- **FaaS:** Oracle Functions (basado en el proyecto abierto Fn), Alibaba Function Compute, DigitalOcean Functions.
- **Contenedores sin servidor:** Azure Container Instances, IBM Code Engine, Fly.io Machines.
- **Edge:** Akamai EdgeWorkers, Supabase Edge Functions, Bunny Edge Scripting.
- **Open source:** Apache OpenWhisk, Fission, Nuclio. Kubeless se abandonó, y sirve como ejemplo de riesgo de dependencia.
- **Datos sin servidor:** Turso, Upstash, PlanetScale, Cosmos DB serverless.

Recibirás más candidatos de tus compañeros. Tu trabajo es decidir cuáles entran al cuadro y justificarlo.

## Plan sugerido para 3 días

- **Hoy:** acuerda con **Valentina** (criterios) y **Rodolfo** (la otra mitad) cuáles son las columnas del cuadro, antes de llenarlo. Arma una planilla con esas columnas, más una columna de *URL de la fuente* y otra de *fecha de consulta*.
- **Sábado:** llena tu mitad desde la documentación oficial y encuentra tus 1 o 2 papers.
- **Domingo:** redacta 3.1 y el anexo de la búsqueda. Entrégale todo a Daniel.

## Sobre el uso de IA

Buscar fuentes con IA está permitido si lo declaras y verificas todo en el original. Pero el **análisis comparativo y la justificación de qué entra y por qué los tienes que escribir tú**. Además, en la presentación el profesor puede pedirte que lo expliques. **Guarda esta conversación**, porque si declaras nivel 2 te sirve como evidencia para el anexo.

Si quieres, puedo seguir con cualquiera de estas cosas:
- **(a)** Armar la planilla Excel de tu mitad del cuadro con las columnas y los campos de fecha y fuente.
- **(b)** Buscar en la web las páginas oficiales de límites y precios de cada plataforma de tu lista, para que tú verifiques y anotes.
- **(c)** Comprobar que los papers candidatos existen y conseguir sus DOI.

## Persona — prompt 2 — 18-09-2026 03:10

```text
voy a estar revisando antes, estos articulos e ir revisando si aportan o no a cada seccion, ve dandome el formato de cada fila para cada paper que vayamos analizando
```

### Claude Code — 18-09-2026 03:11

Como las secciones 2.1 a 2.6 están juntas en una sola opción del desplegable, te propongo **una columna extra** a la derecha de "Sección del informe", que se llame **"Subsección y aporte"**. Así, quien escribe 2.2 encuentra sus papers sin abrir los de 2.4.

## Formato de cada fila

| Columna | Qué poner |
|---|---|
| **Sección del informe** | El texto exacto del desplegable, por ejemplo `2.1 a 2.6` |
| **Subsección y aporte** *(nueva)* | `2.x · qué dato o argumento aporta · página o tabla del paper` |
| **¿Revisada?** | Márcala **solo cuando lo hayas leído tú**: resumen, tablas y conclusión |
| **Revisado por** | `Claudio Toledo` |
| **Fecha de revisión** | `18/09/2026` (el día en que lo leíste) |

Si un paper no aporta nada, no lo borres: marca `¿Revisada?` y escribe en "Subsección y aporte" `Descartado: motivo`. Ese registro también sirve como búsqueda documentada.

Si un paper sirve para dos secciones, en el desplegable va la principal y la otra la anotas en "Subsección y aporte". En Google Sheets también puedes activar la selección múltiple del desplegable: editas la regla de validación y eliges "Permitir varias selecciones".

## Propuesta para los 14 que ya tienes

Esta clasificación la hice por el título y lo que conozco de cada paper. **Confírmala cuando los leas.** No marqué ninguno como revisado.

| N° | Sección del informe | Subsección y aporte (propuesta) |
|---|---|---|
| 1 | 2.1 a 2.6 | 2.1 · Firecracker: la microVM de AWS Lambda y cómo aísla cada función |
| 2 | 2.1 a 2.6 | 2.1 · Compara el costo en rendimiento del aislamiento entre runC, gVisor y Kata |
| 3 | 2.1 a 2.6 | 2.2 · Revisión sistemática del cold start: causas y taxonomía de mitigaciones |
| 4 | 2.1 a 2.6 | 2.2 · Revisión de enfoques de optimización del cold start (complementa al 3) |
| 5 | 2.1 a 2.6 | 2.2 · Snapshots de funciones como mitigación, la base conceptual de SnapStart. Sirve también para 4.1 |
| 6 | 4.2 Modelo de costos | 2.3 y 4.2 · Mecanismos de cobro en serverless (GB-s, invocaciones). Para Francisca |
| 7 | 1 Marco teórico | 1 · Qué es serverless y cuándo conviene. Útil también para los criterios de 3.2 |
| 8 | 4.2 Modelo de costos | 4.2 y 5 · Evidencia empírica de cómo crece el costo; apoya "la factura que crece con el éxito" |
| 9 | 2.1 a 2.6 | 2.4 y 2.6 · Flujos de trabajo con estado e idempotencia sobre funciones |
| 10 | 2.1 a 2.6 | 2.5 · WebAssembly como base del serverless de próxima generación |
| 11 | 2.1 a 2.6 | 2.5 y 3.1 · Runtimes WASM en el borde comparados con contenedores (arranque, tamaño) |
| 12 | 3.1 Alternativas adicionales | 2.5 y 3.1 · WASM frente a unikernels en el borde. **Es un preprint:** úsalo solo como apoyo y decláralo así |
| 13 | 3.1 Alternativas adicionales | 3.1 y 2.6 · Portabilidad entre plataformas FaaS; argumento contra el lock-in |
| 14 | 3.2 Criterios y cuadro | 3.2 · Benchmark que compara AWS, Azure y Google con una metodología explícita. Respalda los criterios del cuadro y la PoC de 4.1 |

## Lo que te sirve a ti

Para tus secciones (3.1 y 3.2), los más útiles son el **14 (SeBS)**, el **13 (QuickFaaS)** y el **11**. Con esos dos o tres cumples tu aporte de 1 o 2 fuentes académicas. Los demás son para tus compañeros, así que avísales que están en la planilla.

Verifica con especial cuidado el **6**, el **8** y el **12**: de memoria no puedo confirmar que existan con esos datos. Abre el DOI y revisa que coincidan el título, los autores y el año. El resto sí los conozco y los datos calzan.

Cuando leas cada paper, dime el N° y qué encontraste (o pega el resumen) y te devuelvo la fila lista para pegar.

## Persona — prompt 3 — 18-09-2026 03:22

```text
okey ahora, quiero que en base a los articulos que tenemos como pdf, vayamos 1 por 1 analizandolo, quiero que en un .md me dejes anotado el doi, y el .bib de cada articulo, quiero analizarlos por numero, asi que vayamaos de manera ascendente partiendo del 47
```

### Claude Code — 18-09-2026 03:22

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 03:23

Estoy leyendo el PDF del paper 47. Ya tengo verificados su DOI y su BibTeX. Me falta la sección 6, que compara plataformas comerciales y es la que más te interesa.

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 03:23

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 03:24

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 03:24

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 03:24

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 03:24

Listo: revisé el paper 47 y creé [Revision-papers.md](Revision-papers.md). Para cada paper voy a dejar ahí los datos, el BibTeX, la fila para la planilla y las notas de lectura con número de página.

El DOI y el BibTeX no los escribí de memoria. Los descargué de Crossref, el registro oficial de DOI, y los comparé con la primera página del PDF. La cita que usa el informe es la del PDF: artículo 220, septiembre de 2022.

## Paper 47: *The Serverless Computing Survey* (ACM Computing Surveys, 2022)

**Fila para la planilla:**

| Sección del informe | Subsección y aporte | ¿Revisada? | Revisado por | Fecha |
|---|---|---|---|---|
| 1 Marco teórico | 1 · Definición de serverless (FaaS + BaaS) y sus 5 rasgos (p. 2–3). También sirve para 2.1, 2.2, 2.4 y 2.6 | ☐ márcalo tú al verificar | Claudio Toledo | 18/09/2026 |

**En resumen:** es un survey con revisión por pares, de buena calidad, que sirve a casi todo el equipo:
- **Matías (1 y 2.1):** la definición de serverless y la Tabla 1, que compara el tiempo de arranque y el aislamiento de VM, Docker, gVisor, Kata, Firecracker y unikernel (p. 6).
- **Isidora (2.2):** las estrategias de pre-calentamiento y los factores del cold start, como el lenguaje y la memoria (p. 8–11 y 22).
- **Valentina (2.4):** los cuatro tipos de disparador (HTTP, cola, temporizador y evento) y el uso de colas (p. 19–20).
- **Fabián (2.6):** un argumento útil. Según el paper, **el lock-in real no está en la función, sino en las APIs de los servicios del proveedor** (p. 24–25).

**Para ti (3.1 y 3.2) aporta poco directamente:**
- La Tabla 4 (p. 23) compara Lambda, Google, Azure e IBM OpenWhisk, pero con datos anteriores a 2022. **No uses esos precios en el cuadro.** Puedes citarla como antecedente de qué criterios se comparan.
- Menciona plataformas open source que pueden servirte como candidatas para 3.1: OpenWhisk, Fission, OpenLambda y Kubeless.

**Hay un posible error en el paper:** en la Tabla 4, el precio de Azure aparece como $0,0000016 por GB-s, diez veces menos que los demás. Lo confirmé en la imagen de la página y no es un problema de lectura del PDF. Si alguien lo cita, tiene que verificarlo en la documentación de Azure. Es el tipo de evidencia contradictoria que el profesor valora.

## Siguientes papers

En la carpeta hay 7 PDF: los números 47, 46, 45, 44, 43, 38 y 1. Como el 47 es el último de tu lista, entendí que quieres bajar desde ahí, así que el siguiente sería el **46, "Demystifying the Cost of Serverless Computing"**. Ese le sirve a Francisca para 4.2. Si te referías a otro orden, dime.

Cuando termines de leer el 47, marca la casilla de revisada y avísame para seguir con el 46.

## Persona — prompt 4 — 18-09-2026 04:08

```text
ahora analiza a detalle cada paper, de la misma manera que el 47, guarda detalle y ten sumo cuidado con cada uno, y guarda en un .md lo que debo colocar en el excel
```

### Claude Code — 18-09-2026 04:08

Voy a extraer el texto de los 6 PDF restantes y bajar sus metadatos de Crossref.

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:08

Metadatos de los 6 confirmados en Crossref. Ahora leo el 46 completo.

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:08

Tabla I del 46 revisada: da $0,000016 por GB-s para Azure, lo que confirma que el valor del paper 47 es un error. Sigo con el 45.

### Claude Code — 18-09-2026 04:08

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

45 listo. Sigo con el 44 (Faashouse).

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

Encontré una inconsistencia en el 44: el resumen le atribuye a faasHouse las mejoras (46 % y 44 %) que en los resultados son del algoritmo "optimal". Lo verifico al redactar. Sigo con el 43.

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:09

Sigo con el 38 (editorial) y después con el 1 (Firecracker).

### Claude Code — 18-09-2026 04:09

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:10

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:10

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:10

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 04:10

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 04:12

Terminé de leer los 7 PDF. Ahora escribo el análisis completo y el archivo para la planilla.

### Claude Code — 18-09-2026 04:14

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:14

Ahora el archivo con lo que va en la planilla.

### Claude Code — 18-09-2026 04:14

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:14

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:14

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 04:14

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:15

Leí completos los 7 PDF de la carpeta (47, 46, 45, 44, 43, 38 y 1) y dejé todo en dos archivos:

- **[Revision-papers.md](Revision-papers.md):** el análisis detallado de cada paper. Incluye DOI, BibTeX, un veredicto, notas de lectura con número de página e integrante al que le sirve, y advertencias. Los DOI y BibTeX los saqué de Crossref, no de memoria. El paper 1 (Firecracker) no tiene DOI porque su editorial no los asigna.
- **[Planilla-filas.md](Planilla-filas.md):** lo que va en cada columna de tu planilla, más una tabla de a quién avisarle por cada paper. La casilla **¿Revisada?** la dejé sin marcar: márcala tú cuando compruebes las páginas citadas en el PDF.

## Cuánto te sirve cada uno

| N° | Para tu sección (3.1 / 3.2) | Para el grupo |
|---|---|---|
| **43** | **Alta.** Compara los frameworks open source OpenWhisk, OpenFaaS y Kubeless, y los clasifica según cuánto dependen de la nube | Alta |
| **46** | Media | **Muy alta.** Muestra que serverless parte más barato y termina más caro con demanda sostenida. Es la base del punto de equilibrio (Francisca) y de "la factura que crece con el éxito" (Fabián) |
| 44, 45 | Media: traen candidatos para 3.1 (KubeEdge, Azure IoT Edge, Serverledge, Faasm) | Baja |
| 47, 1 | Baja | Alta (Marco teórico y 2.1) |
| 38 | Solo como mapa para buscar otros artículos | Es un editorial: no lo cuentes entre las 10 referencias académicas |

## Problemas que encontré en los papers

Pueden servir como **aporte propio**, que el profesor valora. La redacción del análisis tiene que ser de ustedes.

1. **El 47 tiene un error de precio.** Da $0,0000016 por GB-s para Azure, y el 46 da $0,000016, diez veces más.
2. **El resumen del 44 no coincide con sus propios resultados.** Le atribuye a su algoritmo mejoras del 46 % y del 44 % que, según las tablas de resultados, son de otro algoritmo de referencia. Las cifras reales del suyo son 36 % y 30 %.
3. **El 43 se contradice y tiene datos de Lambda desactualizados.** En una página dice que la facturación es por milisegundos y en otra que es por bloques de 100 ms.
4. **La comparación de precios del 46 puede estar sesgada.** Dice que Lambda cuesta 3,5 a 5,6 veces más que una VM, pero compara Lambda en procesador x86 con una VM de procesador ARM.
5. **"Edge" significa dos cosas distintas.** En la ficha es la red de un proveedor, como Cloudflare Workers. En los papers 44 y 45 son nodos propios cerca de sensores (IoT). Conviene aclararlo en el Marco teórico y en 3.1.
6. **El paper 1 lo escribió AWS sobre su propio producto.** Sirve para describir cómo funciona, pero no para comparar, porque las Indicaciones no admiten como fuente primaria lo que un proveedor publica sobre su propia categoría.

## Lo que tienes que verificar tú

- **Kubeless y Project Riff:** creo que ambos proyectos se abandonaron después de 2021, pero no lo comprobé. Revisa sus repositorios en GitHub. Si es así, te sirve para justificar en 3.1 por qué no entran al cuadro.
- **Límites actuales de AWS Lambda** (facturación, memoria, vCPU): revísalos en la documentación oficial antes de citar lo que dicen el 43 y el 1.
- **Declaración de IA:** este análisis cuenta como nivel 2 (resumen de bibliografía) en el anexo. Guarda esta conversación como evidencia.

Si me pasas más PDF, los analizo con el mismo formato.

## Persona — prompt 5 — 18-09-2026 04:17

```text
me interesa que lo hagas como ese formato tal cual, a eso me referia, eso quiero mantenerlo para todos los articulos que revisemos
```

### Claude Code — 18-09-2026 04:17

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:18

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 04:18

Listo. Rehíce [Planilla-filas.md](Planilla-filas.md) con las mismas columnas de tu planilla y en el mismo orden, sin la columna extra:

**N° | Nombre de la fuente | Autores | Año | Tipo | Link de acceso | Sección del informe | ¿Revisada? | Revisado por | Fecha de revisión**

| N° | Sección del informe |
|---|---|
| 1 | 2.1 a 2.6 |
| 38 | 5 Tendencias y riesgos |
| 43 | 3.1 Alternativas adicionales |
| 44 | 3.1 Alternativas adicionales |
| 45 | 3.1 Alternativas adicionales |
| 46 | 4.2 Modelo de costos |
| 47 | 1 Marco teórico |

- **Sección del informe:** escribí el texto tal como aparece en el desplegable, así que puedes copiarlo directo.
- **¿Revisada?:** la dejé sin marcar; márcala tú cuando compruebes cada paper.
- **Revisado por:** en tu planilla, el 46 y el 47 ya dicen "Rodoboss (parcialmente)". Puse "Claudio Toledo", pero habla con Rodolfo antes de reemplazar su nombre.

El detalle de por qué cada paper va en esa sección (páginas, cifras, advertencias) sigue en [Revision-papers.md](Revision-papers.md). Guardé este formato para usarlo en todos los papers que revisemos de aquí en adelante.

## Persona — prompt 6 — 18-09-2026 04:19

```text
ahora al momento de colocar lo que es la seccion, quiero que me justifiques porque es esa seccion y no otra
```

### Claude Code — 18-09-2026 04:20

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 04:20

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 04:21

Agregué a [Planilla-filas.md](Planilla-filas.md) la sección **"Justificación de la sección"**. La puse debajo de la tabla para no cambiar sus columnas. Para cada paper explico por qué va en esa sección y por qué no en las otras que podrían parecer candidatas, con número de página.

**El criterio:** cada paper va donde su aporte no lo cubre ninguna otra fuente que tengamos.

| N° | Sección | Por qué esa y no otra |
|---|---|---|
| 1 | 2.1 a 2.6 | Trata del aislamiento por microVM, que es un subtema obligatorio de 2.1. No va en 3.2 porque no compara plataformas ni trae precios, y lo escribió AWS sobre su propio producto. |
| 38 | 5 Tendencias y riesgos | Lo único original es la lista de desafíos abiertos (p. 4). Lo técnico viene de otros artículos, que son los que hay que citar. |
| 43 | 3.1 Alternativas adicionales | Es el único que compara frameworks open source. OpenWhisk, Fission, Kubeless y Oracle Fn **no están en la lista de código abierto de la ficha**, así que cuentan como alternativas adicionales. Para 1 y 2.x el 47 ya cubre lo mismo con más detalle. |
| 44 | 3.1 Alternativas adicionales | Nombra KubeEdge y Azure Functions on IoT Edge, que no están en la lista de cómputo en el borde de la ficha. No va en 5 porque el tema de energía no es parte de la pregunta de la ficha. Su relevancia es baja: se puede descartar si aparece algo mejor. |
| 45 | 3.1 Alternativas adicionales | Lista frameworks de edge que la ficha no nombra (Serverledge, Faasm, Sledge…). No va en 4.2 porque su "precio" es un supuesto de simulación, no un precio real. |
| 46 | 4.2 Modelo de costos | Construye el modelo de costo serverless frente a IaaS con el punto de cruce, que es justo el entregable de 4.2. No va en 4.3 porque 4.3 solo usa el resultado de 4.2. |
| 47 | 1 Marco teórico | Trae la definición académica de serverless que pide la guía. Para las secciones 2.x hay fuentes más específicas. |

Revisé contra la ficha (página 9 de las Indicaciones) que esas alternativas no están nombradas en sus listas.

Desde ahora, cada paper que revisemos va a traer esta justificación junto con su fila.

## Persona — prompt 7 — 18-09-2026 14:29

```text
okey ahora agregue del 42 al 39, quiero que los revises y ademas, de las secciones, ahora pueden ser varias secciones, asi como se ve en la imagen, ayudame y llendo a detalle paper por paper, sin dejar detalles por alto, tambien quiero que me traduzcas el abstract de cada paper para poder comprender a lo que se trata
```

### Claude Code — 18-09-2026 14:29

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:29

La carpeta cambió: los PDF ahora se llaman por número ("43 Paper.pdf", etc.), y los del 38 y el 1 ya no están. Extraigo el texto de los nuevos y bajo sus metadatos.

### Claude Code — 18-09-2026 14:29

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:29

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:29

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:30

Estoy leyendo el 40, un survey de 29 páginas. Ya encontré dos contradicciones internas que voy a documentar. Reviso su conclusión y sigo con el 41.

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:30

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:31

Ahora el 41 (SASAP, 2025).

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:31

El 41 es una simulación en C++ sin despliegue real, y su resumen muestra solo las cifras favorables. Lo documento. Sigo con el 42.

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:31

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:32

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:32

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:32

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:32

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:33

Reviso en la imagen la Tabla IV del 46: el resumen dice "13,5 % de los usuarios" y quiero verificar de dónde sale esa cifra.

### Claude Code — 18-09-2026 14:33

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 14:33

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 14:34

Ya revisé los cuatro papers nuevos y verifiqué las tablas en las imágenes. Ahora escribo el análisis completo de los 11 papers, en orden ascendente.

### Claude Code — 18-09-2026 14:36

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 14:37

Ahora la planilla con las secciones múltiples y la justificación de cada una.

### Claude Code — 18-09-2026 14:37

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 14:37

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 14:38

Revisé los 4 papers nuevos (39 a 42) completos y actualicé los 11 a la selección múltiple de secciones:

- **[Revision-papers.md](Revision-papers.md):** los 11 papers en orden ascendente. Cada uno tiene su **abstract en español**, DOI, BibTeX (sacado de Crossref), veredicto, notas con página y advertencias.
  - Los abstracts del 39 y el 40 están traducidos completos porque tienen licencia abierta (CC BY). Los otros van en una traducción condensada que conserva todas las ideas y cifras, porque tienen derechos reservados.
- **[Planilla-filas.md](Planilla-filas.md):** la tabla con las columnas de tu planilla y varias secciones por paper, separadas por coma. Debajo, para cada paper, explico por qué entra cada sección y por qué no entran las otras candidatas.

## Secciones propuestas

| N° | Secciones |
|---|---|
| 1 | 2.1 a 2.6 |
| 38 | 5 Tendencias y riesgos |
| **39** | 1 Marco teórico, 2.1 a 2.6, 3.1 Alternativas adicionales, 5 Tendencias y riesgos |
| **40** | 1 Marco teórico, 3.1 Alternativas adicionales, 3.2 Criterios y cuadro, 4.2 Modelo de costos |
| **41** | 5 Tendencias y riesgos (candidato a descarte) |
| **42** | 1 Marco teórico, 2.1 a 2.6, 4.1 PoC, 4.2 Modelo de costos, 5 Tendencias y riesgos |
| 43 | 2.1 a 2.6, 3.1 Alternativas adicionales, 3.2 Criterios y cuadro |
| 44 | 3.1 Alternativas adicionales |
| 45 | 3.1 Alternativas adicionales |
| 46 | 2.1 a 2.6, 4.2 Modelo de costos, 4.3 Caso TERABYTE, 5 Tendencias y riesgos |
| 47 | 1 Marco teórico, 2.1 a 2.6 |

## Lo más importante de los papers nuevos

- **39 (edge, IoT):** es muy útil para ti. Nombra AWS Greengrass y Azure IoT Edge, que no están en la ficha. También cita dos revisiones de plataformas para edge que valen la pena buscar para 3.1: El Ioini 2020 y Palade 2019.
- **40:** trae criterios para elegir una plataforma, que le sirven a Valentina para las columnas del cuadro. Pero se contradice dos veces sobre cosas básicas: qué tipo de función sale más barata y si excluyó o no la literatura gris. Hay que verificar cada dato que se use.
- **41:** es solo una simulación, sin despliegue real. Su resumen muestra solo las cifras favorables; en los resultados, su algoritmo queda por debajo del que compara (73 % frente a 86 %) en cumplir los requisitos de cómputo. Recomiendo no contarlo entre las fuentes centrales.
- **42:** propone un esquema híbrido (VM de base con serverless para absorber los picos), que puede ser una tercera opción para la recomendación del grupo. También advierte que un ataque puede generarle un gran costo al dueño de la aplicación.

## Coincidencias y contradicciones entre papers

Dejé 16 en total al inicio de [Revision-papers.md](Revision-papers.md). Las dos más útiles:

- **Tres fuentes independientes coinciden** (40, 42 y 46): serverless es más barato con carga variable y más caro con carga estable. Es un respaldo fuerte para las conclusiones de 4.2 y 4.3.
- **Hay una contradicción útil para Fabián sobre los ataques.** El 40 dice que los ataques quedan "controlados" en serverless. El 39 y el 42 advierten que, justamente por el autoescalado, un ataque puede disparar la factura del dueño.

## Cosas a revisar en la planilla

- **Año del 41:** la planilla dice 2025, pero la revista lo cita como 2026 (volumen 29). Se publicó en línea en diciembre de 2025. Recomiendo poner 2026.
- **PDF que faltan:** el 38 y el 1 ya no están en la carpeta. Los análisis que tengo de ellos son de antes.
- **Secciones que ya estaban puestas:** en tu planilla vi celdas con "3.2 Criterios y cuadro" combinado con otras secciones. Compáralas con esta propuesta antes de reemplazarlas.

## Persona — prompt 8 — 18-09-2026 15:36

```text
quiero que en un .md, hagamos un analisis a detalle de cada paper, tomando en cuenta los pros y contras de cada uno
```

### Claude Code — 18-09-2026 15:37

Antes de escribir, reviso cuánto cubre el 47 sobre WebAssembly, V8 isolates y edge, y compruebo si el 39 y el 40 incluyen fechas de recepción y aceptación que sirvan para evaluarlos.

### Claude Code — 18-09-2026 15:37

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 15:39

*Herramientas ejecutadas: Write*

### Claude Code — 18-09-2026 15:39

Creé [Analisis-pros-contras.md](Analisis-pros-contras.md), con el análisis de pros y contras de los 11 papers.

## Cómo está armado

- **Cinco criterios**, basados en lo que las Indicaciones y la ficha piden a una fuente: rigor, actualidad, independencia del proveedor, pertinencia para la pregunta de la ficha y verificabilidad. Cada paper recibe Alta, Media o Baja en cada uno.
- **Una tabla resumen** con las notas y el veredicto de cada paper.
- **Por paper:** qué es, pros y contras con número de página, qué citar y qué no, y el veredicto final.

## Resultado

| Veredicto | Papers |
|---|---|
| **Central** | 39 (edge), 42 (definición), 43 (open source), 46 (costo), 47 (marco teórico) |
| **Apoyo** | 1 (lo escribió AWS: solo sirve para describir), 40 (verificar cada dato), 44 y 45 (apoyo menor) |
| **No citar / descartar** | 38 (editorial), 41 (simulación sintética que no responde la ficha) |

Para las 10 referencias académicas mínimas hay 6 seguras (39, 40, 42, 43, 46 y 47) y 3 con reservas (1, 44 y 45).

## Lo nuevo de este análisis

- **Al modelo del 46 le falta el costo del personal.** Compara solo el gasto en recursos y deja fuera a quienes administran las VM, que es justo la "complejidad operacional" de la ficha. El modelo de Francisca en 4.2 debería incluirlo.
- **Ningún paper cubre el edge de los proveedores (CDN).** Cloudflare Workers, Fastly, Vercel y Deno Deploy no aparecen, y la cobertura de V8 isolates y WebAssembly/WASI es mínima: el 47 no menciona WebAssembly ni una vez. Para tu mitad del cuadro y para 2.5 hacen falta otras fuentes. Un buen punto de partida es la revisión que cita el 39 (El Ioini et al., 2020).
- **El 39 pasó por una revisión muy rápida:** se aceptó menos de un mes después de enviarse.
- **El 42 es en parte de 2019:** tiene una versión anterior en arXiv, aunque la publicada incluye referencias de 2021.

**Ojo con la regla de IA:** este documento es para elegir fuentes. La discusión crítica de la evidencia que va en el informe la tienen que escribir ustedes (Indicaciones, punto 6.1). Lo dejé advertido al inicio del archivo.

## Persona — prompt 9 — 18-09-2026 15:42

```text
teniendo en cuenta este analisis, ahora hubo cambios en las secciones a las que aporta cada articulo que hemos analizado?
```

### Claude Code — 18-09-2026 15:42

Reviso las secciones de cada paper con los veredictos del análisis de pros y contras. Primero compruebo que ambos documentos digan lo mismo.

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Grep*

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:42

Ahora actualizo la planilla con los cambios de sección.

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:42

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

Ahora actualizo las justificaciones de los cinco papers que cambian.

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:43

Sí, cambiaron las secciones de 5 de los 11 papers. Ya actualicé la tabla y las justificaciones en [Planilla-filas.md](Planilla-filas.md).

## Cambios

| N° | Antes | Ahora | Por qué |
|---|---|---|---|
| **38** | 5 Tendencias y riesgos | *(vacío)* | El análisis concluyó que no se debe citar: es un editorial sin datos propios. Solo sirve para encontrar los artículos originales, y esos son los que se citan. |
| **40** | 1, 3.1, 3.2, 4.2 | **3.1, 3.2, 4.2** | Sale **1 Marco teórico**. Su Tabla 5 era el aporte al marco, pero sus filas de seguridad y depuración no tienen evidencia, y el paper se contradice. Lo sólido son las filas de costo, que ya entran por 4.2. Para el marco, el 47 y el 42 son más confiables. |
| **41** | 5 Tendencias y riesgos | *(vacío, descartado)* | No hay nada citable: es una simulación sintética, su resumen oculta que pierde contra el método que compara, y no toca la pregunta de la ficha. |
| **42** | 1, 2.1 a 2.6, 4.1, 4.2, 5 | **+ 4.3 Caso TERABYTE** | Trae dos argumentos directos para decidir qué modelo le conviene al proyecto: el esquema **híbrido VM + serverless** (p. 16) y que serverless conviene cuando las solicitudes son **esporádicas** (p. 9). |
| **46** | 2.1 a 2.6, 4.2, 4.3, 5 | **2.1 a 2.6, 4.2, 4.3** | Sale **5 Tendencias y riesgos**. El caso de USD 72.000 viene de un blog, así que Fabián debería citar el blog directamente. La subasta es una propuesta académica que ningún proveedor ofrece. Su argumento fuerte, el gasto que se dispara con demanda sostenida, ya entra por 4.3. |

**Sin cambios:** 1, 39, 43, 44, 45 y 47. El análisis confirmó su asignación. En el 44 queda la condición de que se puede reemplazar si aparece la documentación oficial de KubeEdge.

## Una corrección

Encontré una inconsistencia mía en el 45. En [Analisis-pros-contras.md](Analisis-pros-contras.md) había escrito que se podía citar su "riesgo de sobrepasar el presupuesto", pero en la planilla lo había excluido, con razón: esa cifra (4× el presupuesto) sale de una simulación con precios supuestos. Ya lo corregí y ahora los dos documentos dicen lo mismo: no se cita.

## En la planilla

- **38 y 41:** el desplegable no tiene una opción "descartado". Deja la celda de sección vacía, pero marca "¿Revisada?" igual, para que quede constancia de que los evaluaron. Eso también sirve como búsqueda documentada.
- **Quedan 9 papers con sección.** Para las 10 referencias académicas del grupo siguen valiendo 6 seguros (39, 40, 42, 43, 46 y 47) más 3 con reservas (1, 44 y 45). Faltan fuentes sobre el edge de los proveedores (Cloudflare, Fastly) y sobre WebAssembly (2.5).

## Persona — prompt 10 — 18-09-2026 15:49

```text
de igual manera como analizaste el 38 si no tengo acceso a el? tu puedes tener acceso a ese artiuculo? o estabas inventando?
```

### Claude Code — 18-09-2026 15:49

Buena pregunta. Reviso qué quedó guardado para mostrarte de dónde salió.

### Claude Code — 18-09-2026 15:50

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 15:50

No inventé nada. El 38 lo leí desde un PDF que estaba en tu carpeta.

## Qué pasó

1. **El PDF estaba en tu carpeta.** Cuando me pediste analizar los papers, en `PapersRevision/` había 7 PDF. Uno era `1-s2.0-S0167739X24005375-main.pdf`, que es el formato de nombre que usa ScienceDirect al descargar. Ese era el 38; probablemente alguien del grupo lo bajó con el acceso de la biblioteca PUCV.
2. **Extraje su texto en ese momento.** Lo convertí a texto y lo guardé en mi carpeta temporal a las 04:08 del 18 de septiembre. Ese archivo todavía existe y empieza así:
   ```
   Future Generation Computer Systems 164 (2025) 107573
   Serverless Computing for Next-generation Application Development
   https://doi.org/10.1016/j.future.2024.107573
   Available online 21 October 2024
   ```
3. **Después alguien reorganizó la carpeta.** Los PDF pasaron a llamarse "39.pdf", "43 Paper.pdf", etc., y el 38 y el 1 (Firecracker) ya no están. Acabo de buscarlos en todo "Visual Proyectos" y no aparecen.

Por eso en la tabla de la cola de revisión anoté: *"ya no está en la carpeta; analizado antes desde `1-s2.0-S0167739X24005375-main.pdf`"*.

## ¿Puedo acceder a artículos por mi cuenta?

**No.** No tengo acceso a ScienceDirect, IEEE Xplore ni a ninguna base con suscripción. Todo lo que analicé salió de los PDF que ustedes pusieron en la carpeta. Lo único que consulté en internet fueron los **metadatos públicos de Crossref** (título, autores, revista, volumen), para armar el DOI y el BibTeX. Crossref no entrega el contenido del artículo.

## Qué hacer con el 38 y el 1

Como el análisis de un paper hay que poder verificarlo contra el original, conviene recuperar esos PDF:

- **38:** búscalo en la **Papelera de reciclaje** o en Descargas. Si no está, descárgalo de nuevo desde ScienceDirect con el acceso de la biblioteca PUCV (DOI 10.1016/j.future.2024.107573). Igual, el análisis concluyó que no se cita.
- **1 (Firecracker):** es de acceso abierto, sin suscripción, en la página de USENIX: <https://www.usenix.org/conference/nsdi20/presentation/agache>.

Cuando los vuelvas a poner en la carpeta, compruebo que el texto coincida con lo que analicé.

## Persona — prompt 11 — 18-09-2026 15:54

```text
creo que ahi lo restaure, es ese? puedes revisar si lo es? si lo es analizalo para ver que seciones cubre este articulo
```

### Claude Code — 18-09-2026 15:54

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 15:54

Apareció `38.pdf`. Compruebo que sea el mismo artículo que analicé, comparando su texto con el que extraje en la mañana.

### Claude Code — 18-09-2026 15:54

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 15:55

*Herramientas ejecutadas: Grep*

### Claude Code — 18-09-2026 15:55

*Herramientas ejecutadas: Read*

### Claude Code — 18-09-2026 15:55

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:55

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:55

Ahora actualizo la planilla y el análisis de pros y contras para que digan lo mismo.

### Claude Code — 18-09-2026 15:55

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

Ahora el documento de pros y contras.

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

Busco en Crossref el DOI del artículo de Tusa et al., para que puedas descargarlo con el acceso de la biblioteca.

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

*Herramientas ejecutadas: Edit*

### Claude Code — 18-09-2026 15:56

Sí, es el mismo artículo. El texto del `38.pdf` que restauraste es idéntico al que extraje en la mañana: mismo hash MD5 y las mismas 344 líneas. El análisis anterior se hizo sobre el artículo real.

## Qué secciones cubre

Lo releí completo. Es un editorial: presenta un número especial de la revista y resume 17 artículos de otros autores. Por eso hay que distinguir dos cosas.

**Lo que se puede citar del editorial mismo → 5 Tendencias y riesgos**

Su contenido propio es la lista de desafíos abiertos que proponen los editores (p. 4). Dos puntos le sirven directo a Fabián:
- Los modelos de precio se complican con cargas impredecibles.
- Faltan garantías de latencia, y los editores proponen **enfoques híbridos**, igual que el esquema híbrido del paper 42.

Va como opinión experta y **no cuenta entre las 10 referencias académicas**.

**Lo que cubre a través de los 17 artículos que resume (hay que citar los originales)**

| Artículo | Sección | Relevancia |
|---|---|---|
| **Tusa et al.** (2024): **microservicios siempre encendidos frente a funciones serverless** en el edge | 2.1 a 2.6, 4.3, Conclusiones | **Alta.** Es justo la comparación de la ficha. Los microservicios tienen mejor latencia; serverless es más simple de desarrollar. DOI verificado: 10.1016/j.future.2024.02.006 |
| Fireman et al. (Prebaking, arranque hasta 25× más rápido) | 2.2 | Alta |
| Mathew et al. (lock-in en la orquestación, caso Garmin) | 2.6 y 2.4 | Alta |
| Tran y Kim (autoescalado de Knative) | **3.2**, tu fila open source | Media |
| Ristov et al. (CODE, despliegue en varios proveedores) | 2.6 | Media |
| Katevas et al. (benchmarking en el pipeline) | 4.1 y 4.2 | Media |
| Los otros 11 | — | Baja |

## Qué corregí

1. **Vuelve a "5 Tendencias y riesgos".** Antes lo había dejado sin sección porque su lista de desafíos parecía genérica. Al releerlo, vi que el punto de los enfoques híbridos y el de los precios con cargas impredecibles se conectan con la recomendación del grupo. Actualicé [Planilla-filas.md](Planilla-filas.md) y [Analisis-pros-contras.md](Analisis-pros-contras.md).
2. **Error mío con Knative:** antes lo puse en 3.1, pero Knative ya está en la lista "Código abierto" de la ficha. No es una alternativa adicional: va en tu fila open source de 3.2.
3. **Me había saltado a Tusa et al.** Es probablemente el artículo más valioso que menciona el editorial. Te recomiendo descargarlo desde ScienceDirect con el acceso de la biblioteca PUCV. Si es tan pertinente como parece, puede sumarse a las 10 referencias académicas y también servirle a Vicente como contraste para la PoC.

En [Revision-papers.md](Revision-papers.md) dejé el mapa completo de los 17 artículos con su página, sección y relevancia.

## Persona — prompt 12 — 18-09-2026 17:13

```text
tengo una duda en el plan de trabajo que tenemos lo desmas integrantes y demsa, hay una cantidad mas o menos a revisar por cada integrante?
```

### Claude Code — 18-09-2026 17:13

*Herramientas ejecutadas: Bash*

### Claude Code — 18-09-2026 17:13

No. La guía del equipo **no fija una cantidad de papers por integrante**. Lo revisé de nuevo y lo único que dice al respecto está en "Transversal, todos" (líneas 90–91):

> - Aportar **al menos 1 o 2 fuentes académicas de su sección** a la planilla común (así se llega a las 10 mínimas).
> - Tomar papers base de la vale del drive, revisar los PAPERS que correspondan **a su sección**.

Es decir:
- **El mínimo es de aporte, no de revisión.** Cada uno debe sumar 1 o 2 fuentes académicas propias de su sección. Con 9 integrantes se llega a las 10 que exige el informe.
- **El criterio para revisar es temático, no numérico.** Cada uno revisa los papers del drive que tocan su sección. No hay un reparto del tipo "tú del 1 al 10".

## Tres cosas que vale la pena aclarar con Daniel o con Vale

1. **Tu copia de la guía sigue cortada.** Termina en la línea 122, a mitad de la tabla de alternativas. Si hay un reparto de papers, podría estar en la parte que falta.
2. **Están revisando los mismos papers.** En tu planilla, el 46 y el 47 ya decían "Rodoboss (parcialmente)", y tú también los revisaste. Sin un reparto explícito, se está duplicando trabajo.
3. **¿Quién reparte la planilla?** Tiene al menos 47 papers. Si se dividieran en partes iguales serían unos 5 por persona, pero ese número lo calculé yo; **no está en el plan**.

## Cómo va tu parte

Revisaste 11 papers (1 y 38 al 47), más de lo que pide la guía. De esos, los que aportan a **tu** sección (3.1 y 3.2) son:
- **Centrales:** 39 (edge) y 43 (open source).
- **De apoyo:** 40 (criterios y plataformas), 44 y 45 (candidatos de edge), y del 38, el paper de Tran y Kim sobre Knative para tu fila de 3.2.

Con el 39 y el 43 ya cumples tu aporte de 1 o 2 fuentes académicas. Los análisis de los demás papers les sirven a tus compañeros: la tabla "A quién avisarle" de [Planilla-filas.md](Planilla-filas.md) dice qué le sirve a cada uno.

Para lo que te queda (llenar tu mitad del cuadro 3.2 y redactar 3.1), el cuello de botella ya no son los papers. Es la **documentación oficial** de Google Cloud Run, Cloudflare, Fastly, Vercel, Netlify, Deno Deploy y los proyectos open source, que ninguno de los 11 papers cubre.

## Persona — prompt 13 — 19-09-2026 14:54

```text
dentro de los papers consegui el 13, que tan util es para mi seccion?
```

### Claude Code — 19-09-2026 14:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:54

*Herramientas ejecutadas: Read*

### Claude Code — 19-09-2026 14:55

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:55

*Herramientas ejecutadas: Read*

### Claude Code — 19-09-2026 14:55

Estoy terminando de leer el 13 (QuickFaaS, 29 páginas). Ya tengo lo necesario. Ahora lo agrego a los tres documentos y te digo cuánto te sirve.

### Claude Code — 19-09-2026 14:55

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Read*

### Claude Code — 19-09-2026 14:56

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:57

Busco la fila del 13 en la planilla real del equipo.

### Claude Code — 19-09-2026 14:57

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 14:57

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 14:57

Ahora actualizo la fila del 13 en `Papers-relevantes-para-3.md`, porque su hipótesis quedó descartada.

### Claude Code — 19-09-2026 14:58

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 14:58

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 14:58

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 14:58

El 13 sirve **poco para tu sección**. Lo leí completo (29 páginas).

## Para 3.1: no aporta candidatos

En `Papers-relevantes-para-3.md` estaba como prioridad alta, con la hipótesis de que un paper sobre portabilidad tendría que nombrar varias plataformas FaaS. **No se cumplió:**

- Solo trabaja con **Azure Functions y Google Cloud Functions**, y las dos ya están en la lista 1 de la ficha.
- Lo que revisa en trabajos relacionados (p. 3–4) no son plataformas de ejecución. Son herramientas de despliegue (Terraform, Serverless Framework, Pulumi), un framework que ya está en la ficha (OpenFaaS) y dos prototipos de investigación.

Igual no es tiempo perdido: **va al Anexo D como fuente consultada sin candidatos nuevos**. Las Indicaciones exigen documentar la búsqueda.

## Para 3.2: un dato útil en tu fila open source

La crítica a OpenFaaS (p. 3–4) es un argumento concreto de **complejidad operacional**:
- La mayoría de los eventos internos de la nube (almacenamiento, bases de datos) no lo disparan directamente; casi todo se activa por HTTP.
- Exige un clúster de Kubernetes, algo inapropiado para una aplicación simple.

Complementa la clasificación del paper 43.

## A quién le sirve de verdad

- **Fabián (2.6):** explica las dos causas del lock-in en FaaS (firmas de función y bibliotecas propias de cada proveedor) y **mide cuánto cuesta evitarlo: solo +3,2 % a +3,8 % de cold start** (p. 20). También lo lleva a una buena fuente: Yussupov et al. (2019).
- **Vicente (4.1):** su metodología para medir cold start en GCP y Azure es un buen modelo. Además documenta problemas reales al medir; por ejemplo, **GCP registró menos de 10 de cada 100 invocaciones** en sus métricas (p. 24).

**Ojo:** promedia solo el mejor 75 % de los cold starts. Eso esconde los peores tiempos, que son justamente los que importan en un cold start. Sus tiempos no se deben citar como típicos.

## Dónde quedó guardado

Vi que reorganizaste la carpeta, así que no toqué los archivos de `DatosChatsAnteriores/`:

- **[Sesion-actual-19-09/Paper-13-QuickFaaS.md](../Sesion-actual-19-09/Paper-13-QuickFaaS.md):** análisis completo, abstract traducido, BibTeX, pros y contras, la fila de la planilla y la justificación de cada sección.
  - **Sección propuesta: 2.1 a 2.6, 3.2 Criterios y cuadro, 4.1 PoC.**
- **[Papers-relevantes-para-3.md](../Sesion-actual-19-09/Papers-relevantes-para-3.md):** marqué la hipótesis del 13 como descartada y lo agregué a los papers ya analizados.

En la planilla real, el 13 figura sin revisar y el apellido "Simão" aparece con un carácter dañado. Conviene corregirlo.

**Para tu lista de prioridad alta:** si buscas candidatos para 3.1, el que más promete ahora es el **35** (revisión sistemática de 164 artículos, con una tabla de límites por proveedor).

