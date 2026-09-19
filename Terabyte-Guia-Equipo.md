# TERABYTE · TI-05 Serverless y computación en el borde
## Guía del equipo: estructura, división y reglas obligatorias

Fuentes de esta guía: *Indicaciones Trabajo de Investigación 2026* (FEP00.3.26) y *Pautas del Curso* (FEP00.1.26). Cuando los dos documentos chocan, manda el de Indicaciones por ser el específico del trabajo.

---

## 1. Qué tenemos que responder

La ficha pide **comparar** tres modelos de ejecución (funciones como servicio, contenedores sin servidor y cómputo en el borde) **contra el modelo de instancias siempre encendidas**, y determinar **en qué condiciones de carga conviene cada uno en tres dimensiones: costo, latencia y complejidad operacional**.

Esto define cómo se escribe cada sección: no es un catálogo de productos, es un análisis comparativo. Cada sección debe terminar respondiendo, para su tema, "¿en qué casos conviene una cosa y en qué casos la otra?". Las conclusiones responden la pregunta completa con una recomendación explícita con la que el grupo se compromete.

**Entrega:** informe de 10 a 15 páginas (PDF e impreso) + presentación (PPT o PDF) + cuestionario de 30 preguntas + anexo de declaración de IA. Todo se entrega el **lunes 21 de septiembre de 2026**. Nombre de los archivos (informe y presentación): `6 - TERABYTE - TI-05`. Asunto del correo: `[ICI544] - 6 - TERABYTE - TI-05`. Entrega fuera de plazo, incompleta o sin el anexo de IA **no se recibe conforme**.

**Nota:** 70 % informe y caso práctico, 30 % presentación oral. En la exposición el profesor decide quién habla, cuándo se detiene y quién sigue: **todos deben poder exponer cualquier sección**.

---

## 2. Índice del informe

```
Portada
Resumen ejecutivo
Introducción y contexto
   (último párrafo obligatorio: qué proviene de la ficha y qué es aporte del grupo)
1  Marco teórico y conceptual                          (máximo 1 página)
2  Desarrollo y análisis técnico
   2.1 Modelos de ejecución y aislamiento
   2.2 Arranque en frío: causas, medición y mitigaciones
   2.3 Facturación por consumo y punto de equilibrio
   2.4 Diseño orientado a eventos
   2.5 WebAssembly y WASI como entorno de borde
   2.6 Límites técnicos y dependencia del proveedor
3  Análisis comparativo de tecnologías y productos
   3.1 Alternativas adicionales                        (las 5 listas de la ficha ampliadas)
   3.2 Criterios y cuadro comparativo de plataformas   (mínimo 6 plataformas, límites técnicos, precios fechados)
4  Caso de estudio e implementación práctica
   4.1 Prueba de concepto: arranque en frío y latencia (código, metodología, resultados)
   4.2 Modelo de costos y volumen de equilibrio        (planilla)
   4.3 Aplicación al caso de licitación de TERABYTE
5  Tendencias y riesgos
Conclusiones y recomendación
Referencias bibliográficas                             (mínimo 10 académicas + técnicas)
Anexo A: Declaración de uso de inteligencia artificial (9 firmas)
Anexos B en adelante: código y mediciones de la PoC, planilla de costos, búsqueda documentada de alternativas
Documento adjunto: Cuestionario de evaluación (30 preguntas)
```

**Los tres entregables de la ficha** están en **3.2** (cuadro comparativo), **4.1** (prueba de concepto) y **4.2** (modelo de costos). Son tres entregables independientes (el "o bien" de la ficha aplica solo a la PoC: propia o análisis de mediciones publicadas), pero deben compartir un mismo escenario: las plataformas donde corre la PoC están entre las del cuadro, la arquitectura que se cotiza en el modelo de costos usa una de esas plataformas con los precios del cuadro, y el caso TERABYTE usa el punto de equilibrio y la latencia medida. Cada entregable responde a una dimensión del alcance: cuadro → límites y complejidad operacional; PoC → latencia; modelo → costo.

---

## 3. Presupuesto de extensión (para cerrar en 15 páginas)

Una página de texto corrido son unas 450 palabras; con tabla o figura, menos. **Cada uno escribe dentro de su presupuesto desde el primer borrador.** El detalle (código, mediciones crudas, planilla completa, búsqueda documentada) va a anexos; el cuerpo dice el resultado y remite al anexo.

| Sección | Páginas | Palabras | Lo que no va |
|---|---|---|---|
| Resumen ejecutivo | 0,5 | 200 | Contexto ni definiciones; solo resultado, número de equilibrio y recomendación |
| Introducción + párrafo de aporte | 0,75 | 350 | Historia del cloud |
| 1 Marco teórico | 1 | 450 | Explicar qué es un contenedor, una VM o la nube |
| 2.1 a 2.6 | 0,75 c/u (4,5) | 300–350 c/u | Descripciones de productos, capturas, listas de características. Tres párrafos: concepto, comparación entre modelos, "cuándo conviene" |
| 3.1 Alternativas adicionales | 0,75 | 300 | La búsqueda documentada completa (anexo). En el cuerpo: tabla de 10 filas y dos párrafos |
| 3.2 Criterios y cuadro | 1,25 | 250 + tabla | Prosa que repita la tabla. Criterios en un párrafo y tabla chica; cuadro en una página horizontal; análisis en dos párrafos |
| 4.1 PoC | 1,25 | 350 + gráfico | Código y paso a paso (anexo). Metodología en un párrafo, gráfico, tabla resumen, interpretación |
| 4.2 Modelo de costos | 1 | 300 + gráfico | Planilla completa (anexo). Supuestos en tabla, gráfico de equilibrio, el número |
| 4.3 Caso TERABYTE | 0,75 | 350 | Redescribir el proyecto; solo el volumen estimado y qué modelo conviene |
| 5 Tendencias y riesgos | 1 | 450 | Frases sin fuente; más de dos casos |
| Conclusiones y recomendación | 1 | 450 | Resumir el informe; responder la pregunta de la ficha y comprometerse |
| **Total** | **~13,75** | | Holgura de ~1 página para títulos, figuras y espacios |

---

## 4. División del trabajo

| # | Integrante | Secciones que redacta | Qué hace concretamente |
|---|---|---|---|
| 1 | **Daniel (Jefe)** | Resumen ejecutivo · Introducción con párrafo de aporte · Anexo IA · integración final y entrega | Redacta 2.6 (timeouts, payload, manejo de estado, portabilidad, lock-in) como sección propia. Al final escribe intro y resumen con el material de todos, unifica estilo, junta las 9 declaraciones de IA, arma el PDF y envía |
| 2 | Matias Reyes | 1 Marco teórico · 2.1 Modelos de ejecución y aislamiento | Definiciones desde CNCF y literatura académica. V8 isolates (Cloudflare), microVM Firecracker (AWS), contenedores/gVisor (Google) desde documentación oficial y papers |
| 3 | Isidora Cisternas | 2.2 Arranque en frío · 2.5 WebAssembly y WASI | Causas del cold start y mitigaciones (SnapStart, provisioned concurrency, min instances, Premium plan) desde docs y papers. WASI desde W3C / Bytecode Alliance; Fermyon Spin, wasmCloud, Wasmtime. Cierra 2.2 citando los resultados de 4.1 |
| 4 | Francisca Abarca | 2.3 Facturación por consumo · 4.2 Modelo de costos | Unidades de cobro (GB-s, vCPU-s, tiempo de CPU vs. tiempo de reloj, invocaciones, egress) desde docs oficiales. Planilla que compara una arquitectura sin servidor con una de **contenedores siempre encendidos** (por ejemplo ECS sobre EC2 o GKE con nodos reservados), con supuestos declarados y el **volumen de equilibrio en solicitudes por mes**, usando los precios del cuadro 3.2 |
| 5 | Valentina Guzman | 2.4 Diseño orientado a eventos · Criterios de comparación (apertura de 3.2) | Colas, pub/sub, idempotencia, entrega al menos una vez, orquestación vs. coreografía. Define y justifica los criterios (costo, latencia, complejidad operacional) que son las columnas del cuadro; los acuerda con 6 y 7 antes de que llenen la tabla |
| 6 | Rodolfo Fernandez | 3.2 Cuadro comparativo: AWS y Azure · consolidación de la tabla | Límites técnicos y precio de lista fechado de Lambda, Fargate, App Runner, Lambda@Edge, CloudFront Functions, Azure Functions, Container Apps, Aurora Serverless, DynamoDB. Une las dos mitades y escribe el análisis del cuadro |
| 7 | Claudio Toledo & Daniel Miranda | 3.2 Cuadro comparativo: Google, Cloudflare, Fastly, Deno/Vercel/Netlify, open source · **3.1 Alternativas adicionales** | Su mitad de la tabla. Recibe los candidatos "otros" de todas las secciones, verifica y redacta las 5 listas ampliadas con justificación; decide cuáles entran como filas al cuadro |
| 8 | Vicente Arratia | 4.1 Prueba de concepto | Despliega una función trivial en 2 o 3 plataformas del cuadro (Lambda, Cloud Run, Cloudflare Workers; free tier). Script que mide cold start vs. warm. Tabla, gráficos, metodología y limitaciones. Código y datos crudos a anexo |
| 9 | Fabian Solis | 4.3 Caso TERABYTE · 5 Tendencias y riesgos | Aplica el modelo de costos y la latencia medida al proyecto de licitación del grupo, y discute explícitamente el punto que la ficha pide llevar a la propuesta: el paso de CAPEX a OPEX puro y **el riesgo de una factura que crece con el éxito del sistema**. Tendencias con fuentes serias, cada una con su contraevidencia; casos públicos de equipos que abandonaron serverless por costo o complejidad |

**Transversal, todos:**
- Aportar al menos 1 o 2 fuentes académicas de su sección a la planilla común (así se llega a las 10 mínimas).
- Tomar papers base de la vale del drive, revisar los PAPERS que correspondan a su sección.
- Detectar candidatos para "alternativas adicionales" en su tema y pasarlos al integrante 7.
- Redactar a mano 3 o 4 preguntas del cuestionario sobre su propia sección. (Opcional-hacer al final)
- Conclusiones, recomendación y presentación se hacen en grupo.

### Cómo funcionan las dependencias entre secciones

Cada persona **investiga y redacta su sección completa desde sus propias fuentes**; nadie espera a otro para empezar ni escribe sobre el trabajo de otro. Una dependencia es solo un **dato puntual que se produce en un único lugar del informe y que otra sección cita con referencia cruzada** en vez de producirlo de nuevo. Si el dato aún no existe cuando se redacta, se deja el hueco marcado y se completa después.

- **3.2 produce los precios; 2.3, 4.2 y 4.3 los citan.** Quien escribe 2.3 explica desde documentación oficial cómo cobra cada modelo (eso es su contenido propio); cuando necesita una cifra concreta usa la del cuadro, con su fecha, y remite a la tabla. Razón: toda cifra debe llevar producto, moneda, región, fecha y tipo; si tres personas buscan el mismo precio en días distintos, el informe termina con cifras distintas para lo mismo. Una sola fuente de precios, verificada por 6 y 7, citada por todos.
- **4.1 produce las mediciones; 2.2 las cita.** Quien escribe 2.2 explica causas y mitigaciones del cold start desde papers y docs (90 % de la sección) y cierra con una frase del tipo *"las mediciones propias del grupo (sección 4.1) confirman este orden de magnitud"*.
- **Los criterios (integrante 5) definen las columnas del cuadro (6 y 7).** Se acuerdan antes de llenar la tabla.
- **4.2 produce el volumen de equilibrio; 4.3 lo aplica al proyecto TERABYTE.**
- **3.1 decide qué alternativas adicionales entran como filas al cuadro 3.2.** El integrante 7 hace ambas, así que no hay traspaso.
- **2.6 se complementa con 3.1 y 2.5**: lock-in y portabilidad se apoyan en las alternativas open source y en WASI (referencias cruzadas, no contenido compartido).
- **5 se complementa con 4.2**: los casos de retorno a always-on se explican con el punto de equilibrio.
- **Conclusiones dependen de todo; introducción y resumen se escriben al final.**

---

## 5. Los "otros": alternativas adicionales obligatorias (sección 3.1)

La fila de la ficha se titula **"Tecnologías, productos y proveedores a comparar"** y tiene **cinco listas**, cada una terminada en «y otros que el grupo debe identificar». El punto 4 de las Indicaciones convierte eso en exigencia: por cada lista, **al menos dos alternativas relevantes que no figuren en ella, indicando qué aportan y por qué merecen entrar en la comparación**. Son mínimo 10 tecnologías adicionales justificadas, y **forman parte del conjunto que se compara**: las que califiquen entran como filas del cuadro 3.2.

Si tras buscar se concluye que no hay más para alguna lista, hay que **declararlo expresamente y documentar la búsqueda** (fuentes consultadas, criterios de descarte y fecha). No decir nada se evalúa como ficha incompleta.

Lo que se evalúa no es la lista larga, sino la frase de justificación: *"entra porque aporta X a la comparación"*. Una alternativa sin justificación no cuenta.

Cada lista tiene un **explorador** (la sección donde naturalmente aparece) que busca y verifica candidatos, y el **integrante 7 consolida** todo en 3.1.

| Lista de la ficha | Ya nombra | Explorador (quién busca) | Candidatos a verificar en su documentación oficial |
|---|---|---|---|
| Funciones como servicio | AWS Lambda, Google Cloud Run functions, Azure Functions | Integrante 2 (2.1) y 6 (3.2) | Oracle Cloud Functions (basado en el proyecto abierto Fn: abre discusión de portabilidad), Alibaba Function Compute (modelo de precios distinto), IBM Cloud Code Engine, Scaleway Serverless Functions |
| Contenedores sin servidor | Cloud Run, AWS Fargate, Azure Container Apps, AWS App Runner | Integrante 2 (2.1) y 7 (3.2) | Fly.io, Railway, Render, Scaleway Serverless Containers, Koyeb |
| Cómputo en el borde | Cloudflare Workers, Fastly Compute, Lambda@Edge, CloudFront Functions, Vercel, Netlify, Deno Deploy | Integrante 3 (2.5) y 7 (3.2) | Akamai EdgeWorkers, Supabase Edge Functions, Bunny Edge Scripting, Azure Front Door rules engine (verificar si califica) |
| Código abierto | Knative, OpenFaaS, KEDA, Fermyon Spin / SpinKube, wasmCloud, Wasmtime | Integrante 3 (2.5) y Daniel (2.6) | Apache OpenWhisk, Fission, Nuclio, Fn Project, WasmEdge |
| Datos sin servidor | Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1 | Integrante 5 (2.4) y 4 (2.3) | PlanetScale, Turso, Upstash, CockroachDB Serverless, MongoDB Atlas Serverless, Firestore |

Advertencia: algunos candidatos pueden estar descontinuados o haber cambiado de modelo. Descubrirlo y descartarlo con fecha y fuente **también es aporte** y se documenta en 3.1 y su anexo.

**Además de las listas**, el aporte propio incluye: subtemas, riesgos o casos que la ficha no menciona (justificados), la PoC con mediciones propias (4.1), la aplicación al caso de licitación de TERABYTE (4.3), evidencia contradictoria bien tratada (5) y una recomendación comprometida (conclusiones). Todo esto se enumera en el **párrafo final de la introducción**, que el profesor usa como referencia para evaluar el análisis crítico.

---

## 6. Reglas obligatorias sobre PRECIOS (punto 5 de Indicaciones)

Aplican a **toda cifra** que aparezca en el informe, en cualquier sección.

1. Toda cifra debe indicar: **producto, moneda, región, fecha de consulta, y si es precio de lista o cotización**. Una cifra sin fecha **no se considera válida**.
2. Los precios se verifican en la **página oficial o calculadora oficial del proveedor**, no en artículos de terceros. Las cifras de la ficha son solo referencia de orden de magnitud.
3. Si un proveedor no publica precios, se escribe **«solo por cotización»**. No se citan cifras de terceros sin verificar.
4. Los precios se levantan **una sola vez en el cuadro 3.2** (integrantes 6 y 7). Las secciones 2.3, 4.2 y 4.3 citan esa tabla. Si alguien necesita un precio que no está, lo pide a 6 o 7, no lo busca aparte.
5. Formato sugerido para citar en el texto: *AWS Lambda, us-east-1, USD 0,0000166667 por GB-segundo, precio de lista, consultado el 18-09-2026 en la calculadora oficial de AWS.*

## 7. Reglas obligatorias sobre FUENTES (punto 5 de Indicaciones + Pautas)

1. **Mínimo 10 fuentes académicas** (papers revisados por pares, libros, estándares) más las fuentes técnicas. Cada integrante aporta al menos 1 o 2 académicas de su sección.
2. **Fuentes preferentes (lista textual del PDF):** documentación oficial del proveedor; especificaciones y estándares (NIST, ISO, IETF, CNCF, OWASP, Apache Software Foundation); textos legales en su fuente oficial; artículos revisados por pares; bases de datos del Sistema de Bibliotecas PUCV. Para WASI, la especificación del W3C / Bytecode Alliance es un estándar del mismo tipo y se cita como tal.
3. **Admisibles solo declarándolo en el texto:** informes de industria y encuestas anuales (indicando muestra y metodología), documentación técnica de terceros, blogs de ingeniería reconocidos. Ejemplo: *"según el informe anual de la CNCF (encuesta a N organizaciones, metodología X)…"*.
4. **No admisibles como fuente primaria:** comparativas publicadas por un proveedor sobre su propia categoría (un artículo de Cloudflare comparando Workers con Lambda, por ejemplo), artículos sin autoría verificable, contenido de agregadores sin fuente original.
5. **Toda referencia se abre y se verifica en el original** antes de citarla. Una referencia inexistente o una cifra sin respaldo se evalúa como **error grave**.
6. Registrar cada fuente en la **planilla común** en el momento de consultarla: sección · dato que respalda · autor/organización · título · URL · tipo (académica / oficial / industria / blog) · fecha de consulta.
7. El análisis no puede ser copia extraída de Internet: **se chequeará**.

## 8. Reglas obligatorias sobre INTELIGENCIA ARTIFICIAL (punto 6 de Indicaciones)

### Dónde NO se admite IA (autoría 100 % humana, defendible oralmente sin el texto)
- El análisis comparativo y la justificación de los criterios utilizados (3.2 y, por extensión, la parte comparativa de cada sección del capítulo 2).
- Las conclusiones y recomendaciones.
- El párrafo de aporte propio (introducción) y la discusión crítica de la evidencia (5).
- La redacción de las 30 preguntas del cuestionario y de sus justificaciones.
- **La producción de cifras, citas o referencias: se obtienen de la fuente, no del modelo.** Nunca pedirle una cifra, un precio o una referencia a una IA para ponerla en el informe.

### Dónde SÍ se admite, declarándolo
Búsqueda inicial de fuentes que luego se verifican en el original, traducción, corrección gramatical y de estilo, apoyo de formato y diagramación, generación de código auxiliar identificado como tal (por ejemplo, el script de medición de la PoC).

### Niveles (cada integrante declara el suyo, por sección)
- **Nivel 0:** sin IA.
- **Nivel 1:** corrección, estilo, traducción, sinónimos. El autor controla argumentos y estructura.
- **Nivel 2:** estructurar esquemas, lluvia de ideas, resumir bibliografía, fragmentos de código de apoyo. El análisis es del autor.
- **Nivel 3:** la IA redacta secciones completas o genera argumentos centrales. Requiere revisión profunda y declaración explícita. **En las secciones prohibidas no es nivel 3, es falta a la probidad.**



### Anexo de declaración (obligatorio aunque todos declaren nivel 0)
El formulario viene al final del PDF de Indicaciones y tiene cuatro partes:
- **A. Declaración por sección:** nivel 0-3 **por cada sección del informe**, no un nivel global, con herramienta y versión usada. El formulario ya trae filas para resumen ejecutivo, conclusiones y recomendaciones, **el cuestionario de 30 preguntas y la presentación (diapositivas)**: la declaración cubre también esos dos entregables, no solo el cuerpo del informe.
- **B. Prompts utilizados (niveles 2 y 3):** los prompts efectivamente empleados, indicando a qué sección corresponde cada uno.
- **C. Evidencia trazable (niveles 2 y 3):** enlace o exportación de las conversaciones, historial de versiones del documento o repositorio con commits. Verificar que el profesor pueda acceder.
- **D. Firma de los integrantes:** nombre completo, **nivel máximo declarado** y firma de cada uno. **Nadie declara por otro.** El formulario trae 6 filas: agregar 3 para los 9.

### Consecuencias
- Declarar correctamente **no baja la nota**. Se evalúa la calidad y autoría del análisis, no la abstinencia.
- Omitir la declaración, declarar un nivel menor al real o presentar contenido generado en secciones prohibidas es **falta a la probidad académica** y **alcanza a todo el grupo**, salvo que se acredite responsabilidad individual.
- Sin anexo, el informe se evalúa como entrega incompleta.

### Práctica obligatoria del equipo
- Todo se escribe en **un único Google Doc** (o Word con control de cambios) desde el inicio: el historial de versiones es la evidencia.
- Quien use IA en cualquier nivel **guarda desde ahora** los prompts y los enlaces a las conversaciones, identificando a qué sección corresponden.

---

## 9. Cuestionario de 30 preguntas (punto 3 de Indicaciones)

- 30 preguntas sobre aspectos clave del tema, con **respuesta correcta y breve justificación** cada una.
- Mezcla de formatos: selección múltiple, verdadero/falso, completar, respuesta corta.
- Cubrir teoría y aplicaciones prácticas.
- Dificultad: **12 básicas, 12 intermedias, 6 avanzadas** (40/40/20).
- Incluir preguntas de comprensión, aplicación y análisis crítico.
- **Índice temático** que clasifique cada pregunta según la sección del informe.
- **Redacción 100 % humana.** Cada integrante escribe 3 o 4 de su sección; Daniel arma el índice temático y ajusta la proporción.
- Probablemente sirve de base al control corto que se aplica a los otros grupos durante nuestra exposición.

---

## 10. Presentación oral (30 % de la nota, rúbrica de las Pautas)

- Contenido y dominio 40 % · Material visual 20 % · Comunicación 20 % · Tiempo y estructura 10 %.
- El material visual premia gráficos y diagramas relevantes y castiga el exceso de texto: los gráficos de la PoC (4.1), del punto de equilibrio (4.2) y el diagrama de arquitectura son las láminas clave.
- El profesor decide quién empieza, cuándo se detiene y quién sigue. Todos dominan todo.
- Inasistencia injustificada a la exposición: nota 1,0.

---

## 11. Lo que se evalúa peor (para no perder tiempo en ello)

- La extensión. "Un informe largo sin aporte propio se evalúa peor que uno breve con análisis genuino y verificable."
- Descripciones de productos copiadas de la documentación sin comparación ni análisis.
- Cifras sin fecha, referencias no verificadas, comparativas de proveedores usadas como fuente primaria.
- Listas de "otros" sin justificación, o el punto omitido sin declararlo.
