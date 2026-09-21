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
