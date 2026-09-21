# Encargo para el agente de navegador
### Trabajo de investigación · TERABYTE · TI-05 · 20-09-2026

Documento autocontenido: se puede pegar completo.

---

## Contexto

Informe académico universitario sobre computación sin servidor y en el borde. Estoy a cargo
de la sección **3.1 Alternativas adicionales**: identificar plataformas que la ficha del
curso no nombra, y justificar qué aporta cada una a la comparación.

Ya tengo diez alternativas elegidas y verificadas. **No busques alternativas nuevas.** Lo que
necesito son cinco cosas puntuales, en orden de prioridad.

---

## REGLAS QUE NO SE PUEDEN SALTAR

Las impone el curso y decidien si un dato sirve o no.

**1 · Solo documentación oficial.** La fuente válida es el sitio de documentación del
proveedor o del proyecto. No sirven blogs de terceros, comparativas, agregadores ni
artículos sin autor identificable.

**2 · Toda cifra necesita fecha de consulta.** Sin fecha, la cifra no es válida.

**3 · No sirve que un proveedor hable bien de sí mismo.** Una frase como "somos los más
rápidos" o "verdadera independencia del proveedor" no es admisible como evidencia. Sí es
admisible que el proveedor **documente qué mecanismo implementa** o **qué límite tiene**.
Es la diferencia entre descripción técnica y autopromoción.

**4 · Tampoco sirve que un proyecto compare a sus competidores.** Por ejemplo, la página de
Fission que se compara con Knative y OpenFaaS: sirve como pista, no como fuente sobre
Knative ni OpenFaaS.

**5 · Distingue valor por defecto de valor máximo.** Si una página dice "Default Value",
ese no es el límite del producto. Necesito el máximo.

**6 · Si algo no está publicado, dilo.** "No publicado" o "solo por cotización" son respuestas
válidas y útiles. No completes con estimaciones.

**Formato de respuesta por cada dato:** el dato, la URL exacta donde aparece, y la fecha de
consulta.

---

## TAREA 1 · Azure Front Door Edge Actions · puede invalidar un descarte

`https://learn.microsoft.com/en-us/azure/frontdoor/edge-actions`

**Situación:** descarté Azure Front Door porque su motor de reglas solo aplica condiciones y
acciones predefinidas, sin ejecutar código del usuario. Pero existe **Edge Actions**, que al
parecer sí ejecuta JavaScript en los puntos de presencia.

**Responde:**

1. ¿Edge Actions ejecuta código escrito por el usuario? ¿En qué lenguaje?
2. ¿Está en **vista previa** o es de disponibilidad general? Si es preview, ¿hay fecha
   anunciada de disponibilidad general?
3. Límites documentados: tamaño de código, tiempo de ejecución, memoria, versiones,
   cantidad de recursos por suscripción.
4. ¿Tiene precio publicado, o se cobra dentro de Front Door?
5. ¿Es un producto distinto del motor de reglas, o una función dentro del mismo?

**Por qué importa:** si Edge Actions ejecuta código de verdad, mi descarte está mal formulado
y habría que separarlo: descartar el motor de reglas y evaluar Edge Actions aparte.

---

## TAREA 2 · Paper "The State of FaaS"

`https://arxiv.org/abs/2408.03021`
Ekwe-Ekwe, Nnamdi; Amos, Lucas · IEEE CLOUD 2024 · DOI 10.1109/CLOUD62652.2024.00055

Paper revisado por pares que analiza proveedores FaaS públicos.

**Responde:**

1. **La lista completa de proveedores que analiza.** Solo los nombres.
2. ¿Alguno **no** está en estas cinco listas de la ficha?
   - FaaS: AWS Lambda, Google Cloud Run functions, Azure Functions
   - Contenedores sin servidor: Cloud Run, AWS Fargate, Azure Container Apps, AWS App Runner
   - Borde: Cloudflare Workers, Fastly Compute, Lambda@Edge, CloudFront Functions, Vercel,
     Netlify, Deno Deploy
   - Código abierto: Knative, OpenFaaS, KEDA, Fermyon Spin/SpinKube, wasmCloud, Wasmtime
   - Datos: Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1
3. ¿Qué **criterios de comparación** usa entre proveedores?
4. ¿Qué dice específicamente de **Oracle Functions, Alibaba Function Compute e IBM**, con
   número de página?
5. **Confirma la publicación formal**: ¿existe la versión de IEEE CLOUD 2024 con ese DOI?
   Necesito citar la publicada, no el preprint de arXiv.

---

## TAREA 3 · Madurez en la CNCF de Fission y Nuclio

**El dato que busco:** el nivel de madurez oficial de cada proyecto —Sandbox, Incubating o
Graduated— y la fecha en que lo alcanzó.

**Empieza por:**
- `https://landscape.cncf.io/?group=serverless`
- `https://www.cncf.io/projects/`

**Responde:**

1. ¿**Fission** está en el CNCF Landscape? ¿En qué categoría y con qué nivel de madurez?
2. ¿**Nuclio** está? Misma pregunta.
3. Para comparar, confirma el nivel de estos cuatro, que sí están en la ficha del curso:
   **Knative, KEDA, wasmCloud, WasmEdge**.

**Si Fission o Nuclio no aparecen en la CNCF, dilo explícitamente.** Esa ausencia es un dato
comparable: sería una diferencia de gobernanza frente a los que sí están.

---

## TAREA 4 · Firestore

- `https://firebase.google.com/docs/firestore`
- `https://cloud.google.com/firestore/pricing`
- `https://cloud.google.com/firestore/docs/quotas`

Es la única candidata de mi lista de datos sin servidor que no alcancé a verificar.

**Responde:**

1. Modelo de cobro: ¿qué unidades cobra exactamente?
2. Cuotas gratuitas diarias.
3. Límites: tamaño de documento, escrituras por segundo, y cualquier otro tope relevante.
4. ¿El precio varía por región?
5. **La pregunta que decide:** ¿en qué se diferencia de **DynamoDB bajo demanda** y de
   **Cloudflare D1**, que ya están en la ficha? Si no hay una diferencia clara y documentada,
   dilo: entonces no entra.

---

## TAREA 5 · Confirmación de seis datos

Estos datos los tengo de la planilla de un compañero y necesito confirmarlos en la fuente.
**Por cada uno: confirma o corrige, con la URL exacta y la fecha.**

| # | Dato a confirmar | URL |
|---|---|---|
| 1 | El precio de OCI Functions usa **tablas globales y no varía por región** | `https://www.oracle.com/cloud/price-list/` |
| 2 | Scaleway Functions: **EUR 0,000005 por GB-s** y **EUR 0,000015 por 100 solicitudes**, con capa gratuita de **400.000 GB-s** y **1.000.000 de solicitudes** al mes | `https://www.scaleway.com/en/pricing/serverless/` |
| 3 | Fly.io: **CPU compartida con 6,25 % de base más ráfaga**, y **las cuotas de máquinas por organización no tienen tabla pública fija** (se ajustan por correo) | `https://fly.io/docs/machines/cpu-performance/` |
| 4 | Railway: límites de uso por plan | `https://docs.railway.com/reference/usage-limits` |
| 5 | Supabase: planes Free, Pro, Team y Enterprise, con invocaciones de Edge Functions **incluidas en el plan** más excedentes | `https://supabase.com/pricing` |
| 6 | Turso: planes y cuotas | `https://turso.tech/pricing` · `https://docs.turso.tech/help/usage-and-billing` |

> Para el número 3, lo que más me interesa confirmar es la **ausencia** de una tabla pública
> de cuotas. Si Fly.io no publica cuántas máquinas permite por cuenta, eso es un dato de
> complejidad operacional que sirve para el informe.

---

## Lo que NO necesito

- Alternativas nuevas: las cinco listas ya están cerradas con dos cada una
- Opiniones sobre cuál plataforma es mejor
- Comparativas de terceros o de proveedores sobre su propia categoría
- Cifras de cuota de mercado o de adopción sin fuente primaria verificable
