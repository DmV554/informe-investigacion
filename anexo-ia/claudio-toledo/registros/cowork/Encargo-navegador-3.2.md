# Encargo para el agente de navegador · Tablas 3.2
### TERABYTE · TI-05 · 20-09-2026

Documento autocontenido: se puede pegar completo.

---

## Contexto

Informe académico universitario sobre computación sin servidor y en el borde. Estoy a cargo
de una mitad del cuadro comparativo de plataformas: **Google, Cloudflare, Fastly, Deno y
código abierto**. La otra mitad (AWS y Azure) la levanta un compañero.

Necesito **datos de documentación oficial** para llenar tres tablas. No necesito análisis,
recomendaciones ni comparaciones: solo los datos, con su URL y su fecha.

---

## REGLAS QUE NO SE PUEDEN SALTAR

Las impone el curso y deciden si un dato sirve o se descarta.

**1 · Solo documentación oficial.** El sitio de documentación del proveedor o del proyecto.
No sirven blogs de terceros, comparativas, agregadores, foros comunitarios ni artículos sin
autor identificable.

**2 · Toda cifra necesita fecha de consulta.** Sin fecha, la cifra no es válida.

**3 · Distingue valor por defecto de valor máximo.** Si la página dice "Default", ese no es
el límite del producto. Necesito el máximo, y si solo hay valor por defecto, decirlo así.

**4 · No sirve que un proveedor hable bien de sí mismo.** "Somos los más rápidos" o
"independencia real del proveedor" no son evidencia. Sí sirve que **documente un mecanismo o
un límite**. Es la diferencia entre descripción técnica y autopromoción.

**5 · Tampoco sirve que un proyecto compare a sus competidores.** Por ejemplo, la página de
Fission que se compara con Knative: pista sí, fuente no.

**6 · Si algo no está publicado, dilo.** «No publicado», «solo por cotización» o «no
documentado» son respuestas válidas y útiles. **Nunca completes con estimaciones.**

**7 · Región.** Para Google usa **us-east4** y decláralo en la celda. Para las plataformas de
borde, si el precio no depende de región, escribe **«global»**.

**8 · Una fila = un plan cotizado.** Si la plataforma tiene varios planes, usa el que indico
y decláralo.

---

## LOS CAMPOS QUE HAY QUE LLENAR

Catorce campos por plataforma, repartidos en dos tablas. Más tres columnas de trazabilidad.

| # | Campo | Qué se anota |
|---|---|---|
| 1 | Plataforma | nombre oficial **+ plan cotizado** |
| 2 | Modelo | uno de: funciones como servicio · contenedores sin servidor · cómputo en el borde |
| 3 | **Aislamiento** | microVM / contenedor / isolate de V8 / Wasm / VM dedicada. **Según la documentación, no por analogía** |
| 4 | **Unidad de cobro y piso mensual** | unidad con su base temporal (GB-s, vCPU-s, tiempo de CPU, invocación) y **si hay cargo fijo mensual** o escala a cero |
| 5 | **Precio de lista** | cifra + producto, USD, región, tramo de volumen, fecha, **capa gratuita**, y «lista» o «solo por cotización» |
| 6 | Arranque en frío | **DEJAR VACÍO.** Lo cubre otra persona |
| 7 | **Mitigación de arranque en frío** | mecanismo oficial (concurrencia aprovisionada, instancias mínimas, refuerzo de CPU) **y si se factura aparte** |
| 8 | **Qué opera el equipo** | marcar de esta lista cerrada lo que queda del lado del cliente: sistema operativo y parcheo · runtime y dependencias · planificación de capacidad · escalado · red (VPC, balanceo, certificados) · despliegue y versionado · observabilidad y alertas · recuperación ante fallos. **Sin puntuación ni nivel** |
| 9 | **Estado externo y límite que fuerza rediseño** | si el estado debe externalizarse y a qué servicio; y cuál límite obliga a partir el trabajo |
| 10 | **Tiempo máximo de ejecución** | valor y unidad. **Si hay techo distinto según el tipo de disparador, decirlo** |
| 11 | **Memoria / vCPU** | rango mínimo–máximo |
| 12 | **Payload entrada / salida** | si síncrono y asíncrono difieren, ambos |
| 13 | **Concurrencia / escalado** | límite por defecto, si escala a cero, máximo de instancias |
| 14 | **Egreso de datos** | unidad y precio fechado, tramo gratuito, o «sin cargo» si el proveedor lo declara |

**Trazabilidad, obligatoria:** URL de límites (con fecha) · URL de precios (con fecha) · URL
de responsabilidad compartida o arquitectura (con fecha).

---

# PLATAFORMAS

## Prioridad 1 · Van en el cuerpo del informe

### 1 · Cloudflare Workers — plan **Paid**

`developers.cloudflare.com/workers/platform/limits`
`developers.cloudflare.com/workers/platform/pricing`

**Trampas conocidas:**
- **Tiempo de CPU y duración total de la solicitud NO son lo mismo.** Anota los dos y di
  cuál es cuál
- El plan pago tiene **cargo mínimo mensual por cuenta**. Ese dato es clave para el campo 4:
  rompe el supuesto de que escalar a cero es pagar cero
- El aislamiento son isolates de V8: **confírmalo en la documentación**, no lo des por hecho
- Para el campo 9: ¿obliga a externalizar el estado a Durable Objects, D1 o R2?

### 2 · Google Cloud Run — **servicios, facturación por solicitud**

`cloud.google.com/run/quotas`
`cloud.google.com/run/docs/configuring/request-timeout`
`cloud.google.com/run/docs/configuring/services/memory-limits`
`cloud.google.com/run/docs/configuring/cpu`
`cloud.google.com/run/pricing`

**Trampas conocidas:**
- El **refuerzo de CPU al arranque se cobra durante el arranque**. Confírmalo: va en el campo
  7 con el «sí se factura» explícito
- Región **us-east4**
- «Concurrencia» significa dos cosas: solicitudes simultáneas **por instancia**, e
  **instancias máximas**. Anota las dos

### 3 · Google Cloud Run functions

**Es un producto distinto de Cloud Run.** Las páginas de arriba no sirven.

- Encuentra su documentación de límites y de precios
- **Confirma cómo se llama hoy comercialmente**, porque antes fue "Cloud Functions"

### 4 · Fastly Compute

`docs.fastly.com/products/compute-resource-limits`
`fastly.com/pricing`

**Trampas conocidas:**
- **Fastly sí publica precios de uso por tramos.** Solo los paquetes Advantage y Ultimate son
  por cotización, y hay **tarifas heredadas para cuentas anteriores a noviembre de 2025**
- **La celda de precio debe decir qué régimen se cita**
- Campo 14: en una CDN el tráfico es el negocio, así que el egreso probablemente tenga
  contenido relevante

---

## Prioridad 2 · Tabla de código abierto

Estas cinco van en una tabla aparte, con **columnas distintas**. No tienen precio ni arranque
en frío medido.

**Campos para estas cinco:** Proyecto · Modelo que implementa · **Aislamiento** · **Escala a
cero (sí/no, por defecto)** · **Timeout y concurrencia por defecto (configurables)** · Qué
opera el equipo · **Acreditación CNCF**.

> El campo «qué opera el equipo» ya está resuelto para las cinco: *todo salvo lo que provea el
> clúster gestionado*. **No hace falta investigarlo.**

### 5 · Knative Serving · 6 · OpenFaaS · 7 · KEDA · 8 · Fermyon Spin / SpinKube · 9 · wasmCloud

**Lo que más necesito es la acreditación.** Para cada uno:

1. ¿Está en el **CNCF Landscape**? ¿En qué categoría?
2. ¿Cuál es su **nivel de madurez**: Sandbox, Incubating o Graduated? ¿Desde qué fecha?
3. Si **no** es proyecto CNCF, dilo explícitamente y di bajo qué gobernanza está

`landscape.cncf.io` · `cncf.io/projects/`

**Ya verificado, no lo repitas:** OpenFaaS **no es proyecto CNCF**.

**Además, por proyecto:**
- **Aislamiento**: contenedor, Wasm, u otro, según su documentación
- **Escala a cero**: sí o no, por defecto
- **Timeout y concurrencia por defecto**, diciendo que son configurables
- **KEDA no ejecuta código**, escala cargas de otros. La celda de aislamiento debe decirlo así
- **OpenFaaS: ¿existe una variante de despliegue sin Kubernetes?** Si existe, nómbrala. Es
  importante porque tengo una fuente de 2022 que afirma que exige Kubernetes

---

## Prioridad 3 · Van al anexo, solo si alcanza

### 10 · Deno Deploy · 11 · Vercel Functions (Fluid compute) · 12 · Netlify Functions

Mismos catorce campos de la prioridad 1.

`docs.deno.com/deploy` — trae límites y precio en la misma página
`vercel.com/docs/functions/limitations` · `vercel.com/pricing`
`docs.netlify.com/functions/overview` · `netlify.com/pricing`

---

## FORMATO DE RESPUESTA

CSV separado por **punto y coma**, con estas 19 columnas en este orden exacto:

```
Plataforma;Modelo (ficha);[3.2a] Aislamiento;[3.2a] Unidad de cobro y piso mensual;[3.2a] Precio de lista (producto, USD, región, tramo, fecha, capa gratuita, lista/cotización);[3.2a] Arranque en frío p50/p95 (fuente: 4.1 o paper único);[3.2a] Mitigación cold start (¿se factura aparte?);[3.2a] Qué opera el equipo (lista cerrada);[3.2a] Estado externo obligatorio / límite que fuerza rediseño;[3.2b] Tiempo máx. ejecución;[3.2b] Memoria / vCPU;[3.2b] Payload in/out;[3.2b] Concurrencia / escalado;[3.2b] Egreso de datos (precio fechado);URL límites (fecha);URL precios (fecha);URL responsabilidad compartida / arquitectura (fecha);Verificado por / fecha;Notas
```

- Si una celda lleva punto y coma en su contenido, entrecomíllala
- La columna de arranque en frío va **vacía**
- En «Notas» pon: contradicciones entre páginas, datos que parezcan de marketing, valores por
  defecto que se puedan confundir con máximos, y cualquier cosa que no hayas podido verificar

**Y aparte del CSV, una lista corta de:**
1. Datos que **no** pudiste encontrar, por plataforma
2. Contradicciones entre la página comercial y la documentación
3. Cifras que viste pero que **no son admisibles** según las reglas, y por qué

---

## Lo que NO necesito

- Análisis, recomendaciones o comparaciones entre plataformas
- Cifras de arranque en frío (las cubre otra persona)
- Plataformas nuevas: la lista está cerrada
- Comparativas de terceros o de proveedores sobre su propia categoría
- Cifras de cuota de mercado o adopción
