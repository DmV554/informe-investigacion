# Guía para agentes de búsqueda de fuentes · TERABYTE · TI-05

Trabajo de investigación ICI-5444 (PUCV). Tema TI-05: Serverless y computación en el borde. Esta guía la usa un agente de investigación (o varios, uno por bloque) con acceso al repositorio `informe-investigacion` y al Drive `Investigacion_FEP`.

## 0. Tu rol en una frase

Encuentras, verificas y registras **fuentes candidatas** para secciones concretas del informe. No escribes el informe, no resumes para el informe, no produces cifras ni conclusiones. El grupo lee cada fuente en el original y decide si la usa. Tu salida se declara en el Anexo A del informe como "búsqueda inicial de fuentes que luego se verifican en el original" (nivel 2 de uso de IA), así que todo lo que entregues tiene que ser trazable.

Lee antes de empezar, en este orden:

1. `indicaciones/indicaciones_trabajo_de_investigacion_2026.md`, secciones 4, 5 y 6 (aporte propio, precios y fuentes, IA) y la ficha TI-05 en la sección 8.
2. `Terabyte-Guia-Equipo.md`, secciones 2 (índice), 5 (alternativas adicionales), 6 (precios) y 7 (fuentes).
3. `archivosTemporal/Referencias Investigación.xlsx`, hoja "Fuentes": las 47 fuentes que ya tenemos. **No las vuelvas a proponer.**
4. `informe/main.tex`: los comentarios `%%` de cada bloque dicen qué contenido necesita cada sección.

## 1. Reglas que no se negocian

**Nunca inventes una referencia.** Cada fuente que registres debe tener una URL o DOI que tú mismo hayas abierto y que resuelva al documento que dices que es. Si no logras abrirlo, no lo registres como encontrado: regístralo en la lista de "no verificadas" con lo que sabes. Una referencia inexistente en el informe se evalúa como error grave y compromete a las nueve personas del grupo.

**Registra la fecha de consulta de todo**, formato `AAAA-MM-DD`. Para páginas de precios y de límites es obligatorio además anotar producto exacto, moneda, región y si es precio de lista o "solo por cotización". Una cifra sin fecha no vale.

**Clasifica la admisibilidad de cada fuente** con estas tres categorías, que salen del punto 5 de las Indicaciones:

- `PREFERENTE`: documentación oficial del proveedor; especificaciones y estándares (W3C, CNCF, NIST, ISO, IETF, ETSI, Apache); artículos revisados por pares; libros académicos; bases de datos de la biblioteca PUCV.
- `ADMISIBLE-DECLARANDO`: informes de industria y encuestas anuales **solo si publican muestra y metodología** (anota ambas); documentación técnica de terceros; blogs de ingeniería de empresas reconocidas con autor identificable.
- `NO-ADMISIBLE`: comparativas publicadas por un proveedor sobre su propia categoría (Cloudflare comparando Workers con Lambda, AWS comparando Lambda con Cloud Run); artículos sin autor verificable; agregadores y sitios de SEO; reportes de mercado sin metodología pública; preprints sin revisión (estos van aparte, marcados `PREPRINT`, y solo como apoyo, nunca como única fuente).

Si una fuente es `NO-ADMISIBLE` pero te sirvió para descubrir otra, anota la buena y descarta la mala.

**Prefiere lo reciente para lo que cambia y lo clásico para lo que no.** Límites, precios y estado de productos: solo 2025-2026, y verifica que la página no tenga aviso de deprecación. Conceptos, definiciones y evidencia empírica fundacional: el año no descalifica, pero anota si el paper mide una plataforma que ha cambiado desde entonces.

**Resuelve el año de publicación con un criterio único**: el año del número de la revista o de las actas de la conferencia, no el de publicación en línea anticipada. Si difieren, anota ambos en observaciones.

**Escribe en español**, salvo títulos y citas textuales, que van en su idioma original.

## 2. Formato de salida

Entrega dos archivos por bloque de trabajo, en `trabajo/fuentes/`:

### 2.1 `candidatas-<bloque>.csv`

Una fila por fuente, separador `;`, codificación UTF-8, **mismas columnas que la hoja "Fuentes" del Excel** más las nuevas marcadas con asterisco:

```
N°;Nombre de la fuente;Autores;Año;Tipo;Link de acceso;Sección del informe;Clave BibTeX;Subtema / observaciones;Admisibilidad*;Dato que respalda*;Fecha de consulta*;Cómo la verificaste*;Prioridad*
```

- `Tipo`: usa exactamente uno de: `Paper revisado por pares`, `Libro`, `Estándar / especificación`, `Documentación oficial de proveedor`, `Informe de industria`, `Blog de ingeniería`, `Preprint (no revisado por pares)`.
- `Sección del informe`: una o varias de la lista oficial (hoja "Secciones" del Excel): `1 Marco teórico`, `2.1 Modelos de ejecución y aislamiento`, `2.2 Arranque en frío`, `2.3 Facturación por consumo y punto de equilibrio`, `2.4 Diseño orientado a eventos`, `2.5 WebAssembly y WASI como entorno de borde`, `2.6 Límites técnicos y dependencia del proveedor`, `3.1 Alternativas adicionales`, `3.2 Criterios y cuadro`, `4.1 PoC`, `4.2 Modelo de costos`, `4.3 Caso TERABYTE`, `5 Tendencias y riesgos`. Separa varias con coma.
- `Clave BibTeX`: `apellidoprimerautorAAAApalabraclave`, en minúsculas y sin acentos (`jonas2019berkeley`, `aws2026fargatepricing`).
- `Dato que respalda`: qué afirmación concreta de esa sección puede respaldar esta fuente, en una frase. No es un resumen del documento.
- `Cómo la verificaste`: `DOI resuelve al PDF`, `URL abierta, título y autores coinciden`, `página oficial, sin aviso de deprecación`, etc.
- `Prioridad`: `ALTA` si cubre un hueco de los listados en la sección 3 de esta guía; `MEDIA` si complementa; `BAJA` si es opcional.

### 2.2 `candidatas-<bloque>.bib`

Una entrada BibTeX por fila del CSV, para `biblatex` con estilo APA (`@article`, `@inproceedings`, `@online`, `@report`, `@book`). Campos mínimos: `author`, `title`, `year`, y según el tipo `journal`/`booktitle`, `volume`, `number`, `pages`, `doi` o `url`. Para toda `@online`: `urldate` obligatorio. Para páginas de precios agrega `note = {Producto X, USD, región Y, precio de lista, consultado el AAAA-MM-DD}`.

### 2.3 Al final de cada bloque

Una lista corta en el mismo CSV o en un `.md` aparte con: (a) fuentes que buscaste y **no encontraste o no pudiste verificar**, con lo que intentaste; (b) fuentes ya en el Excel que detectaste con problemas (enlace roto, año dudoso, producto descontinuado).

## 3. Qué falta, por sección

Esto es el corazón de la guía. Para cada sección se indica qué ya tenemos (para que no lo repitas) y qué falta. Los títulos que aparecen entre comillas son referencias que el equipo cree que existen y que **debes localizar y verificar**; si alguna no existe o el título difiere, corrígelo en tu registro.

### 1 Marco teórico y conceptual

Tenemos: Castro 2019, Wen 2023, Shafiei 2022, Li 2022 primer, Cassel 2022, Xie 2021.

Falta la definición canónica y la de edge:

- **CNCF Serverless Whitepaper** (Cloud Native Computing Foundation, Serverless Working Group, v1.0). Buscar en el repositorio `cncf/wg-serverless` de GitHub. Es la definición de serverless más citada por la industria y falta por completo.
- **NIST SP 800-145**, "The NIST Definition of Cloud Computing", para anclar IaaS/PaaS/FaaS al vocabulario estándar.
- Definición estándar de edge computing: **ETSI GS MEC 003** (Multi-access Edge Computing framework and reference architecture), en el portal de ETSI. Además un paper fundacional de edge: Satyanarayanan, "The Emergence of Edge Computing" (IEEE Computer, 2017) o Shi et al., "Edge Computing: Vision and Challenges" (IEEE Internet of Things Journal, 2016).
- Las tres visiones clásicas que faltan y que sirven a varias secciones a la vez:
  - Jonas et al., "Cloud Programming Simplified: A Berkeley View on Serverless Computing" (UC Berkeley EECS technical report, 2019). Visión optimista.
  - Hellerstein et al., "Serverless Computing: One Step Forward, Two Steps Back" (CIDR 2019). Visión crítica; es evidencia contradictoria para la sección 5.
  - Adzic y Chatley, "Serverless computing: economic and architectural impact" (ESEC/FSE 2017). Análisis económico original; sirve a 2.3 y 4.2.

### 2.1 Modelos de ejecución y aislamiento

Tenemos: Firecracker (NSDI 2020), Wang 2022 (runC/gVisor/Kata).

Falta la documentación oficial de los tres mecanismos de aislamiento que la ficha nombra, para poder describirlos desde la fuente:

- Cloudflare, documentación de Workers sobre cómo funcionan los isolates de V8 (página "How Workers works" o equivalente en `developers.cloudflare.com`).
- Google, documentación de gVisor (`gvisor.dev`) y la página de Cloud Run que describe su entorno de ejecución (sandbox de primera y segunda generación).
- AWS, documentación de Firecracker (`firecracker-microvm.github.io`) y la página de Lambda sobre el entorno de ejecución.
- Opcional, un paper que compare aislamientos con medición: Wang et al., "Peeking Behind the Curtains of Serverless Platforms" (USENIX ATC 2018).

### 2.2 Arranque en frío

Tenemos: Golec 2025, Ghorbian 2024, Ustiugov 2021 (snapshots). Está bien cubierto académicamente.

Falta la documentación oficial de cada mitigación que la ficha pide (concurrencia aprovisionada, instantáneas, entornos livianos):

- AWS Lambda: páginas oficiales de **SnapStart** y de **Provisioned Concurrency**, con sus límites y su costo.
- Google Cloud Run: página de **instancias mínimas** (min instances) y la página sobre arranque en frío / startup CPU boost.
- Azure Functions: página de planes de hosting con **Flex Consumption** y **Premium** (instancias pre-calentadas / always ready).
- Cloudflare: página oficial que describa el arranque de un Worker (cuidado: si es un texto comparándose con Lambda es `NO-ADMISIBLE`; si es documentación de cómo funciona su plataforma, es `PREFERENTE`).
- Un paper empírico sobre factores del cold start: Manner et al., "Cold Start Influencing Factors in Function as a Service" (IEEE/ACM UCC Companion 2018).

### 2.3 Facturación por consumo · 4.2 Modelo de costos

Tenemos: Ghorbian 2026 (pricing survey), Hamza 2024, Liu & Niu 2024, Eismann 2021, AWS Lambda Pricing, Cloud Run Pricing.

Este es el bloque con el hueco más grave: **no existe ninguna fuente de precio del modelo always-on**, así que el punto de equilibrio no se puede calcular. Falta:

- **Always-on, cómputo**: página oficial de precios de **Amazon EC2** (bajo demanda) y de **Savings Plans / Reserved Instances**; página de precios de **Google Compute Engine** y de sus **Committed Use Discounts**. Anotar región `us-east-1` o `us-east4` (o la que use el cuadro 3.2; consultarlo con Rodolfo) y fecha.
- **Always-on, orquestación de contenedores**: precio del plano de control de **Amazon ECS** (gratuito o no) y de **GKE** (tarifa por clúster/hora), porque la comparación de la ficha es "contenedores siempre encendidos".
- **Salida de datos**: página oficial de **AWS Data Transfer** (egress a Internet por GB, con el tramo gratuito) y de **Google Cloud Network pricing**. También la política de egress de Cloudflare Workers (si no cobra egress, la página oficial que lo diga).
- **Precios serverless que faltan para el cuadro** (ver 3.2 abajo).
- Académico: Eivy, "Be Wary of the Economics of 'Serverless' Cloud Computing" (IEEE Cloud Computing, 2017). Análisis clásico del punto de equilibrio.

### 2.4 Diseño orientado a eventos

Tenemos: Zhang 2020 (Beldi), y nada más. Es la sección peor cubierta.

- **Especificación CloudEvents** (CNCF, `cloudevents.io`), versión vigente.
- Documentación oficial sobre semánticas de entrega: **Amazon SQS** (colas estándar "al menos una vez" vs. FIFO "exactamente una vez"), **Amazon SNS**, **Amazon EventBridge**, **Google Cloud Pub/Sub** (garantía de entrega al menos una vez), **Azure Service Bus** o **Event Grid**.
- Documentación oficial sobre idempotencia en funciones: la página de AWS Lambda sobre cómo hacer funciones idempotentes (o la del proyecto Powertools for AWS Lambda, que es de AWS).
- Orquestación frente a coreografía desde documentación oficial: **AWS Step Functions** y **Azure Durable Functions** (orquestación); guías de arquitectura de AWS o Microsoft que expliquen la diferencia entre orquestación y coreografía (por ejemplo, el patrón "Choreography" en Azure Architecture Center).
- Académico: al menos un paper revisado por pares sobre workflows o composición de funciones serverless. Candidatos a verificar: López et al., "Comparison of FaaS Orchestration Systems" (IEEE/ACM UCC Companion 2018); Baldini et al., "The Serverless Trilemma: Function Composition for Serverless Computing" (Onward! 2017).

### 2.5 WebAssembly y WASI

Tenemos: Kjorveziroski 2023, Gackstatter 2022, Besozzi 2025 (preprint), W3C Wasm core, WASI.

- **Corregir la fila 16 del Excel**: el título dice "Release 3.0" pero la URL apunta a `wasm-core-2`. Localizar la URL correcta de la versión vigente de la especificación core del W3C y registrar cuál es.
- **WASI**: la página oficial de la versión vigente (WASI 0.2 / Preview 2 o posterior) en `wasi.dev` o en el repositorio `WebAssembly/WASI`, y la nota de la Bytecode Alliance que la anunció, con fecha.
- Documentación oficial de los runtimes y frameworks que la ficha nombra: **Wasmtime** (`wasmtime.dev`), **Fermyon Spin** y **SpinKube** (proyecto sandbox del CNCF: registrar el enlace del CNCF que lo acredite), **wasmCloud** (proyecto del CNCF: ídem).
- Académico fundacional: Haas et al., "Bringing the Web up to Speed with WebAssembly" (PLDI 2017).

### 2.6 Límites técnicos y dependencia del proveedor

Tenemos: QuickFaaS 2022, y las páginas de límites de Lambda, Cloud Run, Azure Functions, Fastly, Deno, Cloudflare.

- Páginas oficiales de límites que faltan (las mismas que necesita 3.2, ver abajo).
- Documentación oficial de **Knative** (`knative.dev`) como capa estándar sobre Kubernetes, y su acreditación como proyecto del CNCF.
- Académico sobre portabilidad y lock-in: Yussupov et al., "Facing the Unplanned Migration of Serverless Applications: A Study on Portability Problems, Solutions, and Dead Ends" (IEEE/ACM UCC 2019); Opara-Martins et al., "Critical analysis of vendor lock-in and its impact on cloud computing migration" (Journal of Cloud Computing, 2016).

### 3.1 Alternativas adicionales · Anexo D

El grupo evalúa candidatos para las cinco listas de la ficha (ver `trabajo/3.1-alternativas/registro-busqueda.md`). Para **cada candidato** de esa lista necesitamos tres URLs oficiales con fecha: la página del producto, la página de precios y la página de límites o cuotas; y **un chequeo explícito de estado**: si el producto tiene aviso de deprecación, cambio de nombre o cambio de modelo, regístralo con la URL del aviso. Descubrir que un candidato está descontinuado es un resultado válido y valioso.

Además, dos fuentes de descubrimiento que el grupo citará como método de búsqueda:

- El **CNCF Landscape**, categoría serverless (plataformas hosted, instalables, frameworks): URL y fecha de consulta.
- Las tablas de plataformas de los surveys que ya tenemos (Wen 2023, Hassan 2021, Li 2022): no hay que buscarlas, pero si encuentras un survey 2024-2026 con una tabla comparativa de plataformas más actual, regístralo.

No propongas candidatos nuevos por tu cuenta salvo que aparezcan en el CNCF Landscape o en un survey revisado por pares; en ese caso regístralos en una lista aparte "candidatos detectados" con la fuente donde los viste.

### 3.2 Criterios y cuadro comparativo

Para cada una de estas plataformas necesitamos la página oficial de **límites/cuotas** y la de **precios**, con fecha. Marca las que ya están en el Excel como "ya registrada" y verifica que el enlace siga vivo:

| Plataforma | Límites | Precios |
|---|---|---|
| AWS Lambda | ya registrada (fila 18) | ya registrada (fila 25) |
| Google Cloud Run functions | falta | falta (¿misma página que Cloud Run?) |
| Azure Functions | ya registrada (fila 22) | falta |
| Google Cloud Run | parcial (filas 20-21) | ya registrada (fila 26) |
| AWS Fargate | falta | falta |
| Azure Container Apps | falta | falta |
| AWS App Runner | falta | falta |
| Cloudflare Workers (+ Durable Objects, D1, R2) | ya registrada (fila 19) | falta |
| Fastly Compute | ya registrada (fila 23) | falta |
| AWS Lambda@Edge y CloudFront Functions | falta | falta |
| Vercel Functions | falta | falta |
| Netlify Functions | falta | falta |
| Deno Deploy | ya registrada (fila 24) | misma página |
| Knative, OpenFaaS, KEDA | documentación de configuración de límites (timeouts, concurrencia) | no aplica (declararlo) |
| Fermyon Spin / SpinKube, wasmCloud, Wasmtime | ídem | no aplica |

Además, la página de **regiones** de cada proveedor que confirme si existe región en Chile o Sudamérica (AWS South America São Paulo, Google Cloud Santiago, Azure Brazil South; y la lista de ubicaciones de red de Cloudflare y Fastly), porque afecta latencia y el caso TERABYTE.

### 4.1 Prueba de concepto

Tenemos: SeBS 2021, Scheuner 2020, Wang 2022. Metodología cubierta.

- Documentación oficial de los tres proveedores donde se despliega la PoC (Lambda, Cloud Run, Cloudflare Workers) sobre **cómo identificar un arranque en frío** en sus registros o métricas (por ejemplo, el campo `Init Duration` en los logs de Lambda; la métrica de instancias/arranques en Cloud Run; lo equivalente en Workers).
- Documentación oficial de las **capas gratuitas** de los tres, con fecha, para declarar el costo de la PoC.

### 4.3 Caso TERABYTE

No requiere fuentes externas nuevas. Si encuentras la **AWS Well-Architected Framework, Serverless Applications Lens** (documento oficial de AWS) o su equivalente de Google/Azure, regístralo como `MEDIA`: sirve para justificar decisiones de arquitectura en la propuesta.

### 5 Tendencias y riesgos

Tenemos: Toosi 2025 (editorial), Bhise 2025 (dudoso), y cuatro reportes de mercado (Mordor, Grand View, Research and Markets) que **no cumplen** el requisito de metodología pública y se van a descartar.

Reemplazarlos por:

- **CNCF Annual Survey**, edición más reciente, con la página que declare tamaño de muestra y metodología (sin eso es `NO-ADMISIBLE`).
- **Datadog, "The State of Serverless"**, edición más reciente, con su sección de metodología (Datadog es proveedor de observabilidad, no de serverless, así que no es una comparativa sobre su propia categoría; igual va como `ADMISIBLE-DECLARANDO`).
- Si existe, una encuesta de desarrolladores con metodología pública que pregunte por adopción de serverless (Stack Overflow Developer Survey, JetBrains State of Developer Ecosystem) en su edición más reciente.
- **Casos públicos de equipos que abandonaron o redujeron serverless por costo o complejidad**, máximo dos, verificados en la fuente original (blog de ingeniería con autor y fecha). Candidato conocido a verificar: el artículo del equipo de Amazon Prime Video (2023) sobre el rediseño de su servicio de monitoreo de calidad de audio/video, de una arquitectura de funciones y Step Functions a un monolito, con la reducción de costo que declararon. Registrar autor, fecha y URL original en `aws.amazon.com` o el blog de Prime Video Tech; no citar los artículos de terceros que lo comentan.
- Evidencia contradictoria académica: Hellerstein 2019 (ya pedido arriba) y, si lo encuentras, un paper revisado por pares 2023-2026 que discuta límites o costos ocultos de serverless con datos.

### Datos sin servidor (lista de la ficha, cruza 2.4, 2.6, 3.1 y 3.2)

Hoy hay **cero fuentes**. Falta la documentación oficial (producto, precios, límites, fecha) de: **Amazon Aurora Serverless v2**, **Amazon DynamoDB en modo bajo demanda**, **Neon**, **Cloudflare D1**; y lo mismo para los candidatos del registro de 3.1 en esa lista.

## 4. División en varios agentes

Si se reparte el trabajo, estos cuatro bloques son independientes entre sí y cada uno entrega su propio par CSV + BIB:

| Bloque | Contenido | Secciones que alimenta |
|---|---|---|
| **A · Académico** | Todo lo marcado como paper, libro o estándar en la sección 3 de esta guía: definiciones canónicas (CNCF, NIST, ETSI), las tres visiones clásicas, y los papers de 2.1, 2.2, 2.3, 2.4, 2.5, 2.6. | 1, 2.1-2.6, 5 |
| **B · Límites y precios** | Toda la documentación oficial de límites, precios, regiones y capas gratuitas de la tabla de 3.2; más los precios always-on (EC2, Compute Engine, ECS/GKE) y de egress. Es el bloque con más filas y el que más exige fecha, moneda y región en cada una. | 2.3, 2.6, 3.2, 4.1, 4.2 |
| **C · Alternativas y datos serverless** | Para cada candidato del `registro-busqueda.md`: producto, precios, límites y estado de vigencia. CNCF Landscape. Toda la lista de datos sin servidor. | 3.1, Anexo D, 3.2 |
| **D · Eventos, Wasm e industria** | Documentación oficial de 2.4 (colas, pub/sub, idempotencia, orquestación) y 2.5 (W3C, WASI, runtimes); las encuestas con metodología y los casos públicos de la sección 5. | 2.4, 2.5, 5 |

Cada agente lee las secciones 0 a 2 completas y solo la parte de la sección 3 que le toca. Al terminar, el grupo consolida los cuatro CSV en la hoja "Fuentes" del Excel y los cuatro BIB en `informe/referencias.bib`, **después** de abrir cada fuente en el original.

## 5. Lo que no debes hacer

- No escribas párrafos para el informe ni "resúmenes útiles" de las fuentes. Una frase de "dato que respalda" por fuente y nada más.
- No estimes, redondees ni conviertas precios. Copia la cifra tal como aparece, con su unidad, y registra la URL y la fecha. El cálculo lo hace el grupo.
- No completes campos que no pudiste verificar con "probablemente" o con valores plausibles. Déjalos vacíos y anótalo en la lista de no verificadas.
- No uses como fuente artículos de Medium, dev.to, sitios de comparativas o el blog de un proveedor comparándose con la competencia. Si te sirven para descubrir la fuente oficial, usa la oficial.
- No repitas fuentes que ya están en el Excel. Si crees que una fila del Excel tiene un error, anótalo en la lista de problemas detectados en vez de crear una fila nueva.
