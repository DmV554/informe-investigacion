# Esqueleto de las tablas 3.2a y 3.2b · doce filas

Fecha: 2026-09-20. Responsables por fila: **R** = Rodolfo · **DC** = Daniel y Claudio · **V** = Vicente (columna cold start) · **F** = Francisca (configuración always-on, acordada con R).

Reglas comunes: toda cifra con producto, moneda, región, fecha de consulta y tipo (lista / solo por cotización). Regiones: AWS us-east-1 · Google us-east4 · Azure East US · borde "global". Una fila = un plan cotizado (declarado en la celda de plataforma). Lo que no cabe aquí va a la tabla ampliada del anexo con URL y fecha por celda. Las celdas ya escritas son las que se deducen del modelo, no de una página; el resto se lee en documentación oficial.

## Tabla 3.2a · Criterios (9 columnas)

| # | Resp. | Plataforma (plan cotizado) | Modelo | Aislamiento | Unidad de cobro y piso mensual | Precio de lista fechado | Arranque en frío (fuente) | Mitigación (¿se factura aparte?) | Qué opera el equipo | Estado externo / límite que fuerza rediseño |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | R · V | AWS Lambda | funciones como servicio | | | | (4.1) | | | |
| 2 | R | Azure Functions (Flex Consumption) | funciones como servicio | | | | sin medición propia o paper único | | | |
| 3 | DC | Google Cloud Run functions | funciones como servicio | | | | sin medición propia o paper único | | | |
| 4 | DC · V | Google Cloud Run (servicios, facturación por solicitud) | contenedores sin servidor | | | | (4.1) | | | |
| 5 | R | AWS Fargate (sobre ECS) | contenedores sin servidor | | | | sin medición propia o paper único | | | |
| 6 | R | Azure Container Apps (Consumption) | contenedores sin servidor | | | | sin medición propia o paper único | | | |
| 7 | DC · V | Cloudflare Workers (Paid) | cómputo en el borde | | | | (4.1) | | | |
| 8 | DC | Fastly Compute | cómputo en el borde | | | | sin medición propia o paper único | | | |
| 9 | R | AWS Lambda@Edge + CloudFront Functions (fila conjunta) | cómputo en el borde | | | | sin medición propia o paper único | | | |
| 10 | R · F | Contenedor sobre EC2 con instancia reservada, orquestado por ECS (tamaño: el mismo de 4.2) | instancias siempre encendidas | VM dedicada; sin aislamiento por invocación | instancia-hora (o segundo); piso = instancia encendida el mes completo; no escala a cero | bajo demanda y con compromiso a 1 y 3 años, ambos fechados | no aplica (instancia encendida) | no aplica | SO y parcheo, runtime, capacidad, escalado, red, despliegue, observabilidad, recuperación | estado puede residir en la instancia; sin límite de tiempo ni de payload de plataforma |
| 11 | DC | *(alternativa desde 3.1)* | *(modelo de la alternativa)* | | | | sin medición propia o paper único | | | |
| 12 | DC | *(alternativa desde 3.1)* | *(modelo de la alternativa)* | | | | sin medición propia o paper único | | | |

Notas de la tabla (van al pie en el informe): (a) columna "Qué opera el equipo": lista de responsabilidades construida por el grupo a partir de los modelos de responsabilidad compartida de AWS, Microsoft y Google y del whitepaper del CNCF, aplicada a cada producto con su documentación oficial; (b) columna "Arranque en frío": "(4.1)" remite a las mediciones propias; para las demás filas se usa una única fuente publicada, citada con año, o se declara "sin medición propia"; (c) fila 9: Lambda@Edge y CloudFront Functions se presentan juntas por ser la oferta de borde del mismo proveedor; donde difieren, la celda indica ambos valores.

## Tabla 3.2b · Límites técnicos y egreso (6 columnas)

| # | Resp. | Plataforma | Tiempo máximo de ejecución | Memoria / vCPU | Payload entrada / salida | Concurrencia / escalado | Egreso de datos (precio fechado) |
|---|---|---|---|---|---|---|---|
| 1 | R | AWS Lambda | | | | | |
| 2 | R | Azure Functions (Flex Consumption) | | | | | |
| 3 | DC | Google Cloud Run functions | | | | | |
| 4 | DC | Google Cloud Run (servicios) | | | | | |
| 5 | R | AWS Fargate (sobre ECS) | | | | | |
| 6 | R | Azure Container Apps (Consumption) | | | | | |
| 7 | DC | Cloudflare Workers (Paid) | | | | | |
| 8 | DC | Fastly Compute | | | | | |
| 9 | R | AWS Lambda@Edge + CloudFront Functions | | | | | |
| 10 | R · F | Contenedor sobre EC2 reservada (ECS) | sin límite de plataforma | el de la instancia cotizada (fijo) | sin límite de plataforma | la que soporte la instancia; escalado manual o por grupo de autoescalado (no a cero) | tarifa de salida a Internet de EC2, fechada |
| 11 | DC | *(alternativa desde 3.1)* | | | | | |
| 12 | DC | *(alternativa desde 3.1)* | | | | | |

## Tabla 3.2c · Plataformas de código abierto (tabla chica, misma sección o anexo)

Estas no van en 3.2a porque no tienen precio ni cold start medido; se comparan por lo que sí las distingue y alimentan 2.6 (portabilidad). Responsables: **DC**.

| # | Proyecto | Modelo que implementa | Aislamiento | Escala a cero (sí/no, por defecto) | Timeout y concurrencia por defecto (configurables) | Qué opera el equipo | Acreditación (CNCF u otra, verificada) |
|---|---|---|---|---|---|---|---|
| 1 | Knative Serving | funciones / contenedores sobre Kubernetes | contenedor | | | todo salvo lo que provea el clúster gestionado | |
| 2 | OpenFaaS | funciones sobre Kubernetes | contenedor | | | ídem | **no es proyecto CNCF** |
| 3 | KEDA | autoescalado a cero para cargas en Kubernetes | (no ejecuta código; escala otros) | | | ídem | |
| 4 | Fermyon Spin / SpinKube | funciones Wasm | Wasm | | | ídem | |
| 5 | wasmCloud | componentes Wasm distribuidos | Wasm | | | ídem | |
| 6 | *(alternativa OSS desde 3.1, si entra)* | | | | | ídem | |

## Fuera de las tablas y dónde queda

- Deno Deploy, Vercel Functions, Netlify Functions, AWS App Runner: tabla ampliada del anexo con las columnas de 3.2a y 3.2b; el análisis puede citarlas.
- Bases de datos sin servidor (Aurora Serverless, DynamoDB bajo demanda, Neon, D1 y alternativas de 3.1): se tratan en 3.1 y en 2.4 / 2.6; no van en 3.2.
- Todo dato levantado que no quepa en estas columnas: tabla ampliada del anexo, con URL y fecha por celda.

## Orden de trabajo

1. R y F acuerdan hoy la configuración de la fila 10 (proveedor, tamaño de instancia, tipo de compromiso). Sin eso no hay ancla.
2. R y DC levantan sus filas en 3.2a y 3.2b en paralelo, en la planilla de respaldo con URL y fecha por celda. La columna de cold start queda vacía salvo la nota de fuente.
3. DC cierra 3.1 y decide qué dos alternativas ocupan las filas 11 y 12.
4. V entrega p50/p95 para las filas 1, 4 y 7. Los tres acuerdan el paper único para las demás o dejan "sin medición propia".
5. R consolida, revisa unidades comparables entre filas (tiempo de CPU vs tiempo de reloj; facturación por solicitud vs por instancia) y escribe el análisis a mano.
