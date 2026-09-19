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
| 1 | **Daniel (Jefe)** | Resumen ejecutivo · Introducción con párrafo de aporte  · Anexo IA · integración final y entrega | Al final escribe intro y resumen con el material de todos, unifica estilo, junta las 9 declaraciones de IA, arma el PDF y envía |
| 2 | Matías Reyes | 1 Marco teórico · 2.1 Modelos de ejecución y aislamiento | Definiciones desde CNCF y literatura académica. V8 isolates (Cloudflare), microVM Firecracker (AWS), contenedores/gVisor (Google) desde documentación oficial y papers |
| 3 | Isidora Cisternas | 2.2 Arranque en frío · 2.5 WebAssembly y WASI | Causas del cold start y mitigaciones (SnapStart, provisioned concurrency, min instances, Premium plan) desde docs y papers. WASI desde W3C / Bytecode Alliance; Fermyon Spin, wasmCloud, Wasmtime. Cierra 2.2 citando los resultados de 4.1 |
| 4 | Francisca Abarca | 2.3 Facturación por consumo · 4.2 Modelo de costos | Unidades de cobro (GB-s, vCPU-s, tiempo de CPU vs. tiempo de reloj, invocaciones, egress) desde docs oficiales. Planilla que compara una arquitectura sin servidor con una de **contenedores siempre encendidos** (por ejemplo ECS sobre EC2 o GKE con nodos reservados), con supuestos declarados y el **volumen de equilibrio en solicitudes por mes**, usando los precios del cuadro 3.2 |
| 5 | Valentina Guzman | 2.4 Diseño orientado a eventos · Criterios de comparación (apertura de 3.2) | Colas, pub/sub, idempotencia, entrega al menos una vez, orquestación vs. coreografía. Define y justifica los criterios (costo, latencia, complejidad operacional) que son las columnas del cuadro; los acuerda con 6 y 7 antes de que llenen la tabla |
| 6 | Rodolfo Fernández | 3.2 Cuadro comparativo: AWS y Azure · consolidación de la tabla | Límites técnicos y precio de lista fechado de Lambda, Fargate, App Runner, Lambda&#64;Edge, CloudFront Functions, Azure Functions, Container Apps, Aurora Serverless, DynamoDB. Une las dos mitades y escribe el análisis del cuadro |
| 7 | Claudio Toledo & Daniel Miranda | 3.2 Cuadro comparativo: Google, Cloudflare, Fastly, Deno/Vercel/Netlify, open source · **3.1 Alternativas adicionales** | Su mitad de la tabla. Recibe los candidatos "otros" de todas las secciones, verifica y redacta las 5 listas ampliadas con justificación; decide cuáles entran como filas al cuadro |
| 8 | Vicente Arratia | 4.1 Prueba de concepto | Despliega una función trivial en 2 o 3 plataformas del cuadro (Lambda, Cloud Run, Cloudflare Workers; free tier). Script que mide cold start vs. warm. Tabla, gráficos, metodología y limitaciones. Código y datos crudos a anexo |
| 9 | Fabian Solís | 4.3 Caso TERABYTE · 5 Tendencias y riesgos · **2.6 Límites y dependencia del proveedor** | Aplica el modelo de costos y la latencia medida al proyecto de licitación del grupo, y discute explícitamente el punto que la ficha pide llevar a la propuesta: el paso de CAPEX a OPEX puro y **el riesgo de una factura que crece con el éxito del sistema**. Tendencias con fuentes serias, cada una con su contraevidencia; casos públicos de equipos que abandonaron serverless por costo o complejidad. Redacta 2.6 (timeouts, payload, manejo de estado, portabilidad, lock-in) como sección propia.|

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
| Funciones como servicio | AWS Lambda, Google Cloud Run functions, Azure Functions | Integrante 2 (2.1) y 6 (3.2) | Oracle Cloud Functions (basado en el proyecto abierto Fn: abre discusión de portabilidad), Alibaba Function Compute (modelo de precios distinto), ...