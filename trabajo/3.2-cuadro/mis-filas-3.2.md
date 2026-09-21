# Mis Filas · Sección 3.2 (Google, Cloudflare, Fastly, Alternativas 3.1 y Código Abierto)
### Responsable: Claudio (con Daniel) · TERABYTE · TI-05 · 20-09-2026

Documento de entrega y respaldo exclusivo para la rama `3.2-Cloud-Fastly-Deno`.
Contiene únicamente las filas asignadas a Claudio y Daniel (DC), con sus 14 campos reglamentarios, tabla de código abierto y anexo.

---

## 1. Filas del Cuerpo del Informe (Tablas 3.2a y 3.2b)

### Fila 3 · Google Cloud Run functions (antes Cloud Functions 2nd gen)
* **Modelo:** Funciones como servicio (FaaS)
* **[3.2a] Aislamiento:** gVisor en primera generación o microVM Linux en segunda generación. Una función es un servicio de Cloud Run desplegado desde código fuente y hereda su infraestructura interna de aislamiento.
* **[3.2a] Unidad de cobro y piso mensual:** vCPU-s, GiB-s y solicitudes por millón (tarifas de Cloud Run con facturación por solicitud). Sin cargo fijo mensual; escala a cero en reposo. Cloud Build y Artifact Registry se facturan por separado al compilar y desplegar.
* **[3.2a] Precio de lista fechado:** us-east4 (Tier 1), USD, 20-09-2026: CPU activa \$0.000024/vCPU-s; memoria activa \$0.0000025/GiB-s; solicitudes \$0.40/millón. Capa gratuita mensual: 180.000 vCPU-s, 360.000 GiB-s y 2 M de solicitudes. Precio de lista publicado.
* **[3.2a] Arranque en frío:** sin medición propia.
* **[3.2a] Mitigación cold start:** Instancias mínimas (facturadas a tarifa idle) y refuerzo de CPU al arranque (Startup CPU boost). SÍ se facturan.
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · despliegue y versionado · observabilidad y alertas* (inferido del contrato de servicio).
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio. Sistema de archivos local es efímero en RAM. Límite de rediseño: funciones dirigidas por eventos (API v2) tienen un techo estricto de 9 minutos (540 s), frente a los 60 minutos permitidos para HTTP.
* **[3.2b] Tiempo máx. ejecución:** Hasta 60 min (3600 s) para HTTP; hasta 9 min para eventos.
* **[3.2b] Memoria / vCPU:** Memoria por defecto 256 MiB; hasta 16 GiB de RAM con 4 vCPU según tabla de comparación de funciones.
* **[3.2b] Payload entrada / salida:** Solicitud y respuesta HTTP/1: 32 MiB. Sin límite bajo HTTP/2.
* **[3.2b] Concurrencia / escalado:** Hasta 1.000 solicitudes concurrentes por instancia de función. Escala a cero.
* **[3.2b] Egreso de datos:** Red Premium Tier: 1 GiB/mes gratis; luego \$0.12/GB hacia Norteamérica hasta 1.024 GiB. 20-09-2026.
* **Trazabilidad:** Límites en `https://docs.cloud.google.com/run/docs/functions/comparison` · Precios en `https://cloud.google.com/run/pricing`.

---

### Fila 4 · Google Cloud Run (servicios, facturación por solicitud)
* **Modelo:** Contenedores sin servidor
* **[3.2a] Aislamiento:** Sandbox gestionado: gVisor (primera generación) o microVM Linux completa (segunda generación). Por defecto el servicio no especifica entorno y Cloud Run lo asigna automáticamente.
* **[3.2a] Unidad de cobro y piso mensual:** vCPU-s y GiB-s de tiempo de instancia facturable (bloques de 100 ms) + solicitudes por millón. Sin cargo fijo mensual; escala a cero en reposo.
* **[3.2a] Precio de lista fechado:** us-east4 (Tier 1), USD, 20-09-2026: CPU activa \$0.000024/vCPU-s; CPU idle \$0.0000025/vCPU-s; memoria activa \$0.0000025/GiB-s; solicitudes \$0.40/millón. Capa gratuita compartida de Tier 1. Precio de lista publicado.
* **[3.2a] Arranque en frío:** `(4.1)` (medido empíricamente por Vicente Arratia).
* **[3.2a] Mitigación cold start:** Instancias mínimas (se facturan a tarifa idle en reposo) y Startup CPU boost (duplica vCPU durante el arranque y 10 s posteriores). SÍ se facturan.
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · red (VPC, balanceo, certificados) · despliegue y versionado · observabilidad y alertas* (inferido).
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio. El sistema de archivos escribible descuenta de la RAM de la instancia. Límite de rediseño: 60 min de timeout máximo por solicitud y 32 GiB / 8 vCPU por instancia; procesos batch más largos obligan a migrar a Cloud Run Jobs (hasta 168 h).
* **[3.2b] Tiempo máx. ejecución:** 300 s (5 min) por defecto; configurable hasta 3.600 s (60 min) por solicitud.
* **[3.2b] Memoria / vCPU:** Memoria default 512 MiB (mín. 128 MiB en gen 1, 512 MiB en gen 2; máx. 32 GiB). vCPU default 1 (mín. 0.08, máx. 8).
* **[3.2b] Payload entrada / salida:** Solicitud y respuesta HTTP/1: 32 MiB. Sin límite bajo streaming HTTP/2.
* **[3.2b] Concurrencia / escalado:** Concurrencia por instancia: 80 por defecto, configurable hasta 1.000. Máximo de instancias por revisión: 100 por defecto (ampliable vía cuota). Escala a cero.
* **[3.2b] Egreso de datos:** Red Premium Tier: 1 GiB/mes gratis; luego \$0.12/GB hacia Norteamérica (1–1.024 GiB). 20-09-2026.
* **Trazabilidad:** Límites en `https://docs.cloud.google.com/run/quotas` · Precios en `https://cloud.google.com/run/pricing`.

---

### Fila 7 · Cloudflare Workers (plan Paid, modelo Standard)
* **Modelo:** Cómputo en el borde
* **[3.2a] Aislamiento:** Isolates de V8 en un único proceso multi-tenant. La memoria de cada isolate está aislada y se crea dentro de un entorno ya existente, sin instanciar una VM por función.
* **[3.2a] Unidad de cobro y piso mensual:** Solicitudes (por millón) + tiempo de CPU (por millón de CPU-ms). La duración de reloj no se factura. **Piso mensual obligatorio: \$5.00 USD/mes por cuenta.** Escala a cero en cómputo pero no en costo mensual.
* **[3.2a] Precio de lista fechado:** global, USD, 20-09-2026: \$5.00/mes base (incluye 10 M solicitudes y 30 M CPU-ms); adicionales a \$0.30/millón req. y \$0.02/millón CPU-ms. Capa Free: 100.000 req./día y 10 ms CPU. Precio de lista publicado.
* **[3.2a] Arranque en frío:** `(4.1)` (medido empíricamente por Vicente Arratia).
* **[3.2a] Mitigación cold start:** No documenta SKU aprovisionado. Mecanismo estructural: arranque de isolate en entorno existente (< 5 ms); snapshot de memoria Wasm en Workers de Python al desplegar. Sin cargo aparte.
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · despliegue y versionado · observabilidad y alertas* (inferido; Cloudflare no publica matriz de responsabilidad compartida).
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio. Isolates pueden ser desalojados sin afinidad de cliente. Destinos oficiales: Durable Objects, Workers KV, D1, R2. Límite de rediseño: **128 MB de memoria por isolate (no configurable)** y 5 minutos de tiempo de CPU por solicitud.
* **[3.2b] Tiempo máx. ejecución:** Dos relojes: Tiempo de CPU máx. 5 min por HTTP (**30 s por defecto**). Duración de reloj: **SIN LÍMITE** en HTTP mientras el cliente continúe conectado; 15 min en Cron Triggers.
* **[3.2b] Memoria / vCPU:** 128 MB por isolate, idéntico en Free y Paid, no configurable. vCPU no expuesta.
* **[3.2b] Payload entrada / salida:** URL 16 KB; cabeceras req./resp. 128 KB total; cuerpo respuesta sin límite forzado; cuerpo solicitud según plan de cuenta (Free/Pro 100 MB, Business 200 MB, Enterprise hasta 5 GB).
* **[3.2b] Concurrencia / escalado:** Sin límite numérico publicado de req./s ni de instancias. Escala automáticamente a nivel global. Hasta 10.000 subsolicitudes por invocación en Paid.
* **[3.2b] Egreso de datos:** **SIN CARGO declarado por el proveedor:** transferencia de datos y rendimiento incluidos en el plan Paid sin facturación extra. 20-09-2026.
* **Trazabilidad:** Límites en `https://developers.cloudflare.com/workers/platform/limits/` · Precios en `https://developers.cloudflare.com/workers/platform/pricing/` · Arquitectura en `https://developers.cloudflare.com/workers/reference/how-workers-works/`.

---

### Fila 8 · Fastly Compute (régimen de uso por tramos, post 04-11-2025)
* **Modelo:** Cómputo en el borde
* **[3.2a] Aislamiento:** WebAssembly (WASI) sobre motor Wasmtime. Aislamiento estricto por solicitud con sandbox ligero de inicialización instantánea.
* **[3.2a] Unidad de cobro y piso mensual:** Compute Requests (por millón) + Compute vCPU-ms (por millón). Sin cargo fijo mensual en el régimen de tramos actual (el régimen heredado previo a nov 2025 tenía \$50 USD/mes).
* **[3.2a] Precio de lista fechado:** global, USD, 20-09-2026: Compute Requests: 10 M gratis, luego \$0.50 a \$0.20/M según volumen. vCPU-ms: 100 M gratis, luego \$0.05 a \$0.02/millón ms. Capa Free: 10 M req. y 100 M vCPU-ms/mes. Paquetes Starter \$500/mes; Advantage y Ultimate solo por cotización. Precio de lista publicado.
* **[3.2a] Arranque en frío:** sin medición propia.
* **[3.2a] Mitigación cold start:** No documenta concurrencia aprovisionada. Mecanismo estructural: compilación anticipada a Wasm e instanciación de entorno en microsegundos. Sin cargo aparte.
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · despliegue y versionado · observabilidad y alertas* (inferido).
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio (Config Store, KV Store, Secret Store, Cache APIs). Límites de rediseño: **50 ms de tiempo de CPU por ejecución**, 128 MB de heap (+ 1 MB stack) y 32 solicitudes salientes a backend por ejecución.
* **[3.2b] Tiempo máx. ejecución:** Dos números: Tiempo de CPU máx. **50 ms por ejecución**. Runtime de reloj total: **2 minutos por ejecución** (60 s en pruebas).
* **[3.2b] Memoria / vCPU:** 1 MB stack y 128 MB heap por ejecución, no configurable. vCPU se factura como milisegundos consumidos.
* **[3.2b] Payload entrada / salida:** Cabeceras req./resp. 128 KB c/u; URL 8.192 bytes; objeto en caché máx. 100 MB; paquete compilado máx. 100 MB. Cuerpo HTTP no publicado.
* **[3.2b] Concurrencia / escalado:** Una instancia por solicitud. Encadenamiento máx. de 20 saltos y 6 servicios únicos.
* **[3.2b] Egreso de datos:** **Tráfico de entrega (Full Site Delivery) se factura aparte:** 100 GB gratis/mes; luego Norteamérica y Europa \$0.12/GB y \$0.08/GB; Sudamérica \$0.19 y \$0.14/GB. 20-09-2026.
* **Trazabilidad:** Límites en `https://docs.fastly.com/products/compute-resource-limits` · Precios en `https://www.fastly.com/pricing`.

---

### Fila 11 · Oracle Cloud Infrastructure Functions (alternativa 3.1)
* **Modelo:** Funciones como servicio (FaaS)
* **[3.2a] Aislamiento:** Contenedor gestionado / microVM en infraestructura OCI aislada por función. Motor basado en el proyecto de código abierto Fn Project.
* **[3.2a] Unidad de cobro y piso mensual:** Invocaciones (por millón) + GB-s de tiempo de ejecución. Concurrencia aprovisionada en reposo facturada al 25 % de la tarifa de ejecución. Sin cargo fijo mensual; escala a cero.
* **[3.2a] Precio de lista fechado:** US East (Ashburn) / global, USD, 20-09-2026: Invocaciones: \$0.20 por millón (\$0.0000002/inv.); Ejecución: \$0.00001417/GB-s. Capa Always Free: 2 M de invocaciones y 400.000 GB-s al mes permanentes. Precio de lista publicado.
* **[3.2a] Arranque en frío:** sin medición propia.
* **[3.2a] Mitigación cold start:** Concurrencia aprovisionada (Provisioned Concurrency); SÍ se factura aparte a tarifa reducida (25 % de la tarifa de ejecución en idle; sin sobrecargo al procesar).
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · despliegue y versionado · observabilidad y alertas*.
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio (OCI Object Storage, Autonomous Database). Límites de rediseño: timeout síncrono 300 s (default 30 s); modo detached hasta 3.600 s; memoria fija en opciones de 128 a 3072 MB.
* **[3.2b] Tiempo máx. ejecución:** Síncrono máx. 300 s (default 30 s). Modo detached (asíncrono): configurable de 5 s a 3.600 s (60 min).
* **[3.2b] Memoria / vCPU:** Opciones fijas: 128, 256, 512, 1024, 2048, 3072 MB. vCPU dimensionada proporcionalmente.
* **[3.2b] Payload entrada / salida:** Solicitud y respuesta HTTP: 6 MB cada una.
* **[3.2b] Concurrencia / escalado:** 60 instancias concurrentes por availability domain por defecto (ampliable por soporte). Escala a cero.
* **[3.2b] Egreso de datos:** **Primeros 10 TB/mes gratis hacia internet**; luego \$0.0085/GB. Sin cargo entre servicios OCI en la misma región. 20-09-2026.
* **Trazabilidad:** Límites en `https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm` · Precios en `https://www.oracle.com/cloud/cloud-native/functions/`.

---

### Fila 12 · Azion Edge Functions (alternativa 3.1)
* **Modelo:** Cómputo en el borde
* **[3.2a] Aislamiento:** Isolates de V8 sobre Edge Runtime distribuido propio compatible con estándares web (W3C/WHATWG). Memoria aislada por función.
* **[3.2a] Unidad de cobro y piso mensual:** Compute time (por cada 1.000 s de CPU) + Invocaciones (por millón). Sin cargo fijo mensual en plan Starter; escala a cero.
* **[3.2a] Precio de lista fechado:** PoPs en Brasil/LATAM y global, USD, 20-09-2026: Compute time: \$0.072 por 1.000 s de CPU tras free tier; Invocaciones: \$0.30 por millón tras free tier. Capa gratuita mensual: 8 horas de compute (28.800 s) y 3 M de invocaciones al mes. Precio de lista publicado.
* **[3.2a] Arranque en frío:** sin medición propia.
* **[3.2a] Mitigación cold start:** Aislamiento ligero en V8 Isolate en nodos edge (< 2 s cold start documentado, típico ms). No documenta SKU de concurrencia aprovisionada.
* **[3.2a] Qué opera el equipo:** *runtime y dependencias · despliegue y versionado · observabilidad y alertas*.
* **[3.2a] Estado externo / Límite de rediseño:** SÍ, obligatorio (Edge Storage, Edge SQL, Network Layer). Límites de rediseño: **2 segundos de tiempo de CPU por solicitud** (marketing publicita 5 min de wall-clock); isolate máx. 512 MB; argumentos JSON 100 KB.
* **[3.2b] Tiempo máx. ejecución:** CPU time máx. **2 segundos por solicitud**. Duración de reloj (wall-clock): máx. 5 minutos (300 s).
* **[3.2b] Memoria / vCPU:** Hasta 512 MB por isolate de función. vCPU no expuesta.
* **[3.2b] Payload entrada / salida:** Argumentos JSON 100 KB. Tamaño de código de función: UI 6 MB, API 20 MB. Sub-requests: máx. 50.
* **[3.2b] Concurrencia / escalado:** Autoescalado continuo sobre la red distribuida de PoPs edge. Escala a cero.
* **[3.2b] Egreso de datos:** Tráfico Edge Network cobrado por GB según región (Brasil/LATAM \$0.06/GB en tiers iniciales, con 50 GB gratis al mes). 20-09-2026.
* **Trazabilidad:** Límites en `https://www.azion.com/en/documentation/products/edge-application/edge-functions/` · Precios en `https://www.azion.com/en/pricing/`.

---

## 2. Tabla 3.2c · Código Abierto (6 Proyectos)

1. **Knative Serving:** Contenedores en Kubernetes. Pod autoscaler KPA con escala a cero activa por defecto (30 s de gracia). Timeout default 300 s (`revision-timeout-seconds`), concurrencia ilimitada por defecto. **Graduado CNCF el 11-09-2025**.
2. **OpenFaaS:** Funciones en contenedores sobre K8s o host único (`faasd`). Escala a cero no por defecto (opt-in `com.openfaas.scale.zero: true`). Despliegue sin K8s documentado con containerd/CNI. **No es proyecto CNCF** (OpenFaaS Ltd.).
3. **KEDA:** Autoescalador dirigido por eventos para K8s. **No ejecuta código, escala cargas ajenas.** Escala a cero activa por diseño. Parámetros de sondeo (`pollingInterval` 30 s default). **Graduado CNCF el 22-08-2023**.
4. **Fermyon Spin / SpinKube:** Cómputo Wasm sobre Kubernetes (`SpinApp`). Ejecutores `containerd-shim-spin` o `Spintainer`. Escala a cero delegada en KEDA (no nativa en HPA). **Sandbox CNCF desde el 21-01-2025 (SpinKube)**.
5. **wasmCloud:** Componentes Wasm distribuidos sobre Wasmtime + Component Model. Escala a cero nativa por diseño (sin instancias inactivas). Concurrencia ilimitada por defecto. **Incubating CNCF desde el 08-11-2024**.
6. **Fission (alternativa 3.1):** Funciones en Kubernetes. Estrategia mixta: ejecutor `poolmgr` (warm pools precalentados de 3 pods para eliminar cold start) o `newdeploy` (escala a cero con `minScale: 0`). Router timeout default 300 s. **Código abierto mantenido por la comunidad (v1.27.0)**.

---

## 3. Tabla Ampliada del Anexo (3 Plataformas)

1. **Deno Deploy (plan Pro):** Borde. Suscripción \$20/mes + Active CPU (\$0.10/h) y Memory time (\$0.025/GiB-h). Apps inactivas se apagan a los 20–30 s. Memoria default 768 MB (máx. 4 GB). Egreso: 200 GiB incluidos.
2. **Vercel Functions (Fluid compute, Pro):** FaaS/Borde. Active CPU (\$0.128/h en iad1) + Provisioned Memory (\$0.0106/GB-h) + Invocaciones (\$0.60/M). Piso \$20/mes por asiento. Timeout 300 s default, máx. 800 s (1800 s beta). Memoria 1–2 vCPU / 2–4 GB.
3. **Netlify Functions:** FaaS/Borde. Modelo de créditos unificado (Pro \$20/mes con 3.000 créditos). Timeout síncrono 60 s no configurable; background 15 min; streaming 10 s. Memoria default 1024 MB.
