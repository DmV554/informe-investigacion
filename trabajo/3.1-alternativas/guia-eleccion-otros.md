# Guía de elección — Alternativas adicionales (3.1)

**Propósito.** Ayudar al grupo a elegir **2 “otros” por lista** desde la pool ya revisada, comparando candidatos mano a mano con cifras y citas oficiales. **La decisión final de los 2 por lista sigue siendo del grupo**; este documento no recomienda ni rankea un par.

**Fecha:** 2026-09-20 (America/Santiago).  
**Fuentes base:** `pool-otros-revisados.md`, `verificacion-candidatos.md`, y (cuando hace falta una cadena de cita) las mismas URLs oficiales reabiertas el mismo día.  
**Fuera de comparación “otros”:** productos de ficha (Lambda, Cloud Run functions, Azure Functions, Cloud Run, Fargate, Container Apps, App Runner, CF Workers, Fastly, Lambda@Edge, CloudFront Functions, Vercel, Netlify, Deno, Knative, OpenFaaS, KEDA, Spin/SpinKube, wasmCloud, Wasmtime, Aurora Serverless, DynamoDB on-demand, Neon, D1).

Companion de citas tabuladas: `citas-pool-otros.csv` · BibTeX mínimo: `citas-pool-otros.bib`.

---

## Lista 1: FaaS

### Pool (6)

- Oracle OCI Functions
- Alibaba Function Compute (FC 3.0)
- IBM Code Engine (functions)
- Scaleway Serverless Functions
- Huawei Cloud FunctionGraph
- Tencent Cloud SCF

### Comparación mano a mano

| Candidato | Modelo / qué aporta | Unidad de cobro + cifra exacta | Capas gratis / free tier | Límites clave | Estado | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Oracle OCI Functions | FaaS OCI; provisioned concurrency al 25% idle | Invocación >2M: **US$0.0000002**/invocación; ejecución >400k GB-s: **US$0.00001417**/GB-s | **2M** invocaciones/mes + **400,000** GB-s/mes | Timeout sync máx **300 s**; detached **5–3600 s**; memoria fija **128–3072 MB**; payload req/resp **6 MB** | activo | [1][2] |
| Alibaba FC 3.0 | Facturación unificada por **CU** (vCPU/mem/invocaciones) | Pay-as-you-go por región: Tier 1 **USD 0.000020/CU** (desc. oficial Aug 27 2024–Aug 27 2026: **0.0000160/CU**); Tier 2 **0.000017** (desc. **0.0000136**); Tier 3 **0.000014** (desc. **0.0000112**) | Trial: **150,000 CU**/ciclo × **3** ciclos (primeros usuarios) | Memoria máx **32 GB**; runtime máx **86,400 s**; instancias default **300**/región | activo | [3][4] |
| IBM Code Engine (functions) | Functions dentro de Code Engine (límites distintos de apps/jobs) | Unidades: vCPU-s, GB-s, requests; ejemplo oficial (disclaimer “do not reflect current prices”): **$0.00003431**/vCPU-s, **$0.00000356**/GB-s, **$0.538**/millón requests | Escenario: **100,000** vCPU-s + **200,000** GB-s + **100,000** HTTP req/mes | Runtime functions **120 s**; memoria **48,000 MB**; inline code **100 KB**; body **5 MB** | activo; unit prices “current” no definitivos en página producto | [5] |
| Scaleway Serverless Functions | FaaS EU; precios en **EUR** (USD no publicado) | Recurso **€0.000005**/GB-s; requests **€0.000015**/100 req; provisioned **€0.000017**/GB-s (antes de impuestos) | **400,000** GB-s + **1,000,000** requests/mes/cuenta | Timeout **10 s–60 min**; escala máx **50**; concurrency **1**/instancia; payload **6 MiB**; memoria org **600 GiB** | activo | [6][7] |
| Huawei Cloud FunctionGraph | FaaS Huawei intl.; pay-per-use USD en ejemplos oficiales | Requests **$0.2 USD / 1M**; ejecución **$0.00001667 USD/GB-s**; reserved idle **$0.000005556/GB-s** | Primeros **1,000,000** req/mes + **400,000** GB-s | Memoria máx **10 GB**; duración máx **259,200 s**; sync payload **6 MB**; async **256 KB**; concurrentes/cuenta **100** (ticket para más); functions/cuenta **400** | activo (producto intl.) | [8][9] |
| Tencent Cloud SCF | SCF intl. con USD + basic package post free-tier | Resource **0.0000167 USD/GBs**; invocaciones **0.002 USD / 10,000**; idle provisioned **0.00000847 USD/GBs** | Primeros **3 meses**: 1M event + 1M HTTP, **1,000,000 GB** resource, **2 GB** outbound; luego basic **0.06 USD/day** (cupos 500k+500k / 100,000 GB / 2 GB) | Memoria **64–3072 MB**; timeout **1–900 s**; /tmp **512 MB**; sync **6 MB**; async **128 KB**; code+layers **500 MB** | activo (docs intl.) | [10][11] |

### Elementos diferenciadores e interesantes

**Oracle OCI Functions.** Combina free tier amplio (2M invocaciones + 400k GB-s) con provisioned concurrency cobrada al **25%** del execution time cuando está idle y sin cargo extra cuando se usa [1]. Los timeouts distinguen sync (**300 s**) y detached (**hasta 3600 s**) [2], útil frente a FaaS “solo HTTP corto”.

**Alibaba Function Compute 3.0.** El diferenciador es el **CU** unificado (vCPU, memoria e invocaciones convertidos a una unidad) con tiers regionales en USD también fuera de mainland (p. ej. Singapore / Virginia / Frankfurt) [3]. Timeout hasta **86,400 s** y memoria **32 GB** [4] empujan el techo operativo por encima de varios peers FaaS.

**IBM Code Engine (functions).** Los límites **120 s** / **100 KB** inline son explícitamente de la tabla *Function*, no de apps/jobs [5]. El free tier de unidades está documentado; las tarifas unitarias “current” no aparecen de forma definitiva en la página de producto (solo escenario con disclaimer) — relevante si el informe exige precio de lista cerrado.

**Scaleway Serverless Functions.** Único en la pool FaaS con lista pública en **EUR** y free tier 400k GB-s + 1M requests [6]. Concurrency **1** por instancia y escala **50** [7] marcan un modelo más “una petición por instancia”. USD: **no publicado** en la página de pricing serverless.

**Huawei Cloud FunctionGraph.** Peer Asia/intl. con free tier **1M req + 400k GB-s** y tarifas USD en ejemplos oficiales [8]. Destaca duración máxima **259,200 s** y memoria **10 GB** [9], más el modo reserved idle a tarifa reducida.

**Tencent Cloud SCF.** Publica USD intl. (resource, invocaciones, idle provisioned) y un esquema de **free tier 3 meses** seguido de **basic package 0.06 USD/day** [10]. Timeout hasta **900 s** y memoria hasta **3072 MB** [11]; cuotas de concurrency en MB regionales (p. ej. 64,000 MB en varias regiones intl.).

### Criterios sugeridos para elegir 2

- ¿Se necesita **precio de lista USD** cerrado vs aceptable **EUR** / escenario con disclaimer / “contact sales”?
- ¿Importa **free tier recurrente** (mensual) vs trial temporal (meses / ciclos CU)?
- ¿El caso de uso pide **timeouts largos** / detached / jobs-like, o solo HTTP corto?
- ¿Prioridad **región LATAM/EU/Asia** documentada y documentación intl. estable?
- ¿Se valora **provisioned concurrency / reserved idle** con tarifa publicada?
- ¿Compatibilidad narrativa con peers ya en ficha (hiperescalares) vs diversificación geográfica?

### Referencias (Lista 1)

1. https://www.oracle.com/cloud/cloud-native/functions/  
2. https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm  
3. https://www.alibabacloud.com/help/en/functioncompute/fc-3-0/product-overview/billing-overview-of-fc · https://www.alibabacloud.com/help/en/functioncompute/fc/product-overview/pay-as-you-go-billing-methods  
4. https://www.alibabacloud.com/help/en/functioncompute/fc-3-0/product-overview/limits-of-usage  
5. https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits · https://cloud.ibm.com/docs/codeengine?topic=codeengine-pricing · https://cloud.ibm.com/docs/account?topic=account-sample  
6. https://www.scaleway.com/en/pricing/serverless/  
7. https://www.scaleway.com/en/docs/serverless-functions/reference-content/functions-limitations/  
8. https://support.huaweicloud.com/intl/en-us/price-functiongraph/functiongraph_00_0011.html · https://support.huaweicloud.com/intl/en-us/price-functiongraph/functiongraph_00_0010.html  
9. https://support.huaweicloud.com/intl/en-us/productdesc-functiongraph/functiongraph_01_0150.html  
10. https://intl.cloud.tencent.com/document/product/583/12281 · https://intl.cloud.tencent.com/document/product/583/12282  
11. https://intl.cloud.tencent.com/document/product/583/11637  

---

## Lista 2: Contenedores

### Pool (6)

- Fly.io
- Railway
- Render
- Scaleway Serverless Containers
- Koyeb
- DigitalOcean App Platform

### Comparación mano a mano

| Candidato | Modelo / qué aporta | Unidad de cobro + cifra exacta | Capas gratis / free tier | Límites clave | Estado | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Fly.io | Machines por segundo (CPU/RAM); cargo rootfs en stopped | Ej. shared-cpu-1x / 256MB: **$0.00000075/s** ($0.0027/h, $1.94/mo); rootfs stopped **$0.15 / GB / 30 days**; egress NA/EU **$0.02/GB**, APAC/SA **$0.04**, Africa/India **$0.12** | No free tier fijo publicado en pricing (reservas/créditos fuera de scope) | Hard size/count/timeout de Machine: **no publicados** como cifras fijas en pricing | activo | [12] |
| Railway | Usage RAM/CPU/egress + fee de plan | RAM **$10/GB/mo**; CPU **$20/vCPU/mo**; egress **$0.05/GB**; volume **$0.15/GB/mo**; facturación por minuto | Free **$0/mo**; Hobby **$5/mo**; Pro **$20/mo** (fee hacia usage) | Límites por plan en docs usage-limits (complementarios) | activo | [13] |
| Render | PaaS web/containers; Free spin-down | Starter web **$7/month** (512 MB, 0.5 CPU); workspaces Hobby **$0** / Pro **$25** / Scale **$499** + compute | Free web: spin-down tras **15 min** sin tráfico inbound | Paid **no** spin-down / no scale-to-zero; Hobby máx **25** services, **5 GB** bandwidth (docs free/pricing) | activo | [14][15] |
| Scaleway Serverless Containers | Contenedores serverless EU (EUR) | Memoria **€0.000002/GB-s**; vCPU **€0.00001/vCPU-s** (antes de impuestos) | **400,000** GB-s + **200,000** vCPU-s/mes/cuenta | Timeout **10 s–60 min**; max scale **50**; concurrency **80**; memoria **128–12228 MB**; CPU **70–6000** mvCPU; scale-to-zero tras **15 min** | activo | [6][16] |
| Koyeb | Serverless containers; scale-to-zero; billing por segundo | Standard `nano`: **$0.000001/s** ($0.0036/h, $2.68/mo); Eco `eco-nano`: **$0.0000006/s**; Pro **$29/mo** (+$10 compute incluido); egress extra EU/US **$0.02/GB**, Asia **$0.04/GB** | Free Instance: **512 MB** RAM, **0.1** vCPU, **2 GB** SSD; **1**/org; scale-to-zero tras **1 h** sin tráfico | Free: 1 región (FRA o IAD), sin Workers/custom scaling/Volumes | activo | [17][18] |
| DigitalOcean App Platform | PaaS contenedores shared/dedicated | Desde **$5.00/mo** (`apps-s-1vcpu-0.5gb`, 512 MiB); billing **by the second**, mínimo **1 minute**; egress extra **$0.02/GiB** | Free solo **static sites** (hasta 3 apps; 1 GiB outbound/app) | Max **250** containers/app; request autoscaling máx **100**; FS efímero **4 GiB**; build timeout **1 h**. Scale to Zero: **private preview**, duerme a **10%** del precio; `after_seconds` **600–86400** | activo; Scale to Zero = private preview | [19][20] |

### Elementos diferenciadores e interesantes

**Fly.io.** Facturación fina por segundo de Machines started y un cargo explícito de **rootfs en stopped** ($0.15/GB/30 días) [12], más egress regional. Útil para contrastar “scale-to-zero aparente” vs coste de disco parado. Límites duros de tamaño/conteo/timeout **no** están como tabla fija en pricing.

**Railway.** Modelo híbrido **subscription + usage** (Hobby $5 / Pro $20 hacia el consumo) con RAM/CPU/egress unitarios claros [13]. No afirmar idle gratuito: se factura por minuto de compute según docs.

**Render.** El Free con spin-down a los **15 minutos** frente a planes paid que **no** hacen scale-to-zero [14][15] es un contraste didáctico para el informe. Starter paid desde **$7/month**.

**Scaleway Serverless Containers.** Misma familia EU que Functions, con free tier de memoria y vCPU y precios EUR publicados [6]. Concurrency **80**, scale **50**, scale-to-zero a los **15 min** [16].

**Koyeb.** Publica scale-to-zero, instancias Standard/Eco desde **~$0.0000006–0.000001/s**, Free Instance con sleep tras **1 h**, y plan Pro **$29/mo** [17][18]. Buen ancla “containers serverless managed” fuera de hiperescalares.

**DigitalOcean App Platform.** PaaS con precio de entrada **$5/mo** y billing por segundo [19]. **Scale to Zero** existe pero solo en **private preview**, facturando **10%** al dormir [20] — no tratarlo como GA automático.

### Criterios sugeridos para elegir 2

- ¿Se necesita **scale-to-zero GA** documentado vs spin-down Free-only vs preview?
- ¿Prioridad **precio público EUR** (Scaleway) vs **USD** unitario (Fly/Railway/Koyeb/DO)?
- ¿Modelo **solo usage** vs **plan fee + usage**?
- ¿Importa cargo por **disco parado** / rootfs (Fly) en el análisis de coste idle?
- ¿PaaS git-deploy simple (Render/DO/Railway) vs Machines/edge regions (Fly/Koyeb)?
- ¿Región EU / multi-región documentada para el caso LATAM-Chile del informe?

### Referencias (Lista 2)

12. https://fly.io/docs/about/pricing/  
13. https://docs.railway.com/pricing  
14. https://render.com/docs/free · https://render.com/docs/faq  
15. https://render.com/pricing  
16. https://www.scaleway.com/en/docs/serverless-containers/reference-content/containers-limitations/  
17. https://www.koyeb.com/pricing  
18. https://www.koyeb.com/docs/reference/instances  
19. https://docs.digitalocean.com/products/app-platform/details/pricing/ · https://docs.digitalocean.com/products/app-platform/details/limits/  
20. https://docs.digitalocean.com/products/app-platform/how-to/scale-to-zero/  

---

## Lista 3: Edge

### Pool (5)

- Akamai EdgeWorkers
- Supabase Edge Functions
- Bunny Edge Scripting
- Azion Edge Functions
- Fermyon Cloud (managed Spin)

### Comparación mano a mano

| Candidato | Modelo / qué aporta | Unidad de cobro + cifra exacta | Capas gratis / free tier | Límites clave | Estado | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Akamai EdgeWorkers | EdgeWorkers por tiers Basic/Dynamic/Enterprise | Cobro por events/mes vía Marketplace; **lista USD no pública** en techdocs | Free trial documentado (sin lista USD) | Memoria **1.5 / 2.5 / 4 MB**; CPU **10 / 20 / 70 ms**; wall **4 / 5.5 / 10 s** (Basic/Dynamic/Enterprise) | activo | [21][22] |
| Supabase Edge Functions | Edge Deno ligado a Postgres/RLS | **$2 / 1M** invocaciones sobre cuota del plan | Free **500,000**; Pro/Team **2M** invocaciones | Memoria **256 MB**; CPU **2 s**/request; worker lifetime Free **150 s** / Paid **400 s**; idle timeout **150 s** | activo | [23][24] |
| Bunny Edge Scripting | Scripting en CDN Bunny | **$0.20 / M** requests; **$0.02 / 1000 s** CPU; bandwidth CDN **aparte** | No free tier de scripting publicado en pricing scripting | CPU **30 s**/request; memoria **128 MB**; subrequests **50**; script **10 MB**; cold start **500 ms**; wall-clock total separado: **no publicado** | activo | [25][26] |
| Azion Edge Functions | Edge LATAM/Brazil-relevant; compute + invocations | Compute: primeras **8 h/mes** gratis, luego **$0.072 / 1,000 s**; Invocations: primeros **3M/mes** gratis, luego **$0.30 / M** (mismas tarifas en regiones listadas) | 8 h compute + 3M invocations/mes | Args **100 KB**; isolate **512 MB**; code UI **6 MB** / API **20 MB**; sub-requests **50**; CPU **2 s**; wall-clock **5 min**; cold start máx **2 s** | activo | [27][28] |
| Fermyon Cloud (managed Spin) | Hosting managed Wasm/Spin (Spin OSS = ficha, OUT) | Starter **$0/mo**; Growth **$19.38/mo**; Enterprise Custom | Starter: **5** apps, **100,000** req, **5 GB** egress, 1 región | Package **100 MB**; handler **30 s**; HTTP body **10 MB**; **1,000** req/s; Growth: **100** apps, **1M** req, **50 GB** egress | **open beta** (sin SLA) | [29][30] |

### Elementos diferenciadores e interesantes

**Akamai EdgeWorkers.** Límites por tier en **ms/MB** muy estrictos (CPU 10–70 ms) [21]; útil como extremo “edge ultra-corto”. Precio USD de lista **no** aparece en techdocs (Marketplace/trial) [22].

**Supabase Edge Functions.** Diferenciador de plataforma: edge Deno **acoplado a Postgres + RLS** [23][24], con cuotas de invocaciones por plan y CPU **2 s**. No es un CDN edge genérico.

**Bunny Edge Scripting.** Precio simple **$0.20/M** + CPU time, con CDN bandwidth separado [25]. CPU **30 s** y cold start **500 ms** [26] contrastan con límites de milisegundos de Akamai.

**Azion Edge Functions.** Peer con relevancia **LATAM/Brazil** y pricing USD regional homogéneo para Functions [27]. Reportar el matiz oficial: marketing “hasta 5 minutes CPU” vs tabla de límites **CPU 2 s** / wall-clock **5 min** [28].

**Fermyon Cloud.** Managed de apps **Spin/Wasm** en open beta sin SLA [29][30]; no confundir con Spin/SpinKube de ficha OSS. Planes Starter/Growth con cupos de requests y egress.

### Criterios sugeridos para elegir 2

- ¿Se necesita **precio USD público** vs aceptable quote/Marketplace (Akamai)?
- ¿Prioridad **presencia LATAM/edge regional** (Azion) vs CDN global genérico (Bunny) vs plataforma BaaS (Supabase)?
- ¿Límites de ejecución en **ms** vs **segundos** vs **minutos** wall-clock?
- ¿Caso Wasm/Spin managed (Fermyon) vs JS/TS edge scripting?
- ¿Estado **GA** vs **open beta** / sin SLA aceptable para el informe?
- ¿Acoplamiento a DB/RLS (Supabase) como ventaja o como acoplamiento indeseado?

### Referencias (Lista 3)

21. https://techdocs.akamai.com/edgeworkers/docs/resource-tier-limitations  
22. https://techdocs.akamai.com/edgeworkers/docs/reporting-and-billing · https://techdocs.akamai.com/edgeworkers/docs/edgeworkers-free-trial  
23. https://supabase.com/docs/guides/functions/limits  
24. https://supabase.com/docs/guides/platform/manage-your-usage/edge-function-invocations  
25. https://bunny.net/docs/scripting/pricing  
26. https://bunny.net/docs/scripting/limits  
27. https://www.azion.com/en/documentation/products/pricing/  
28. https://www.azion.com/en/documentation/products/build/applications/functions/  
29. https://www.fermyon.com/pricing · https://developer.fermyon.com/cloud/index  
30. https://developer.fermyon.com/cloud/faq  

---

## Lista 4: OSS

### Pool (6)

- Apache OpenWhisk
- Fission
- Nuclio
- Fn Project
- WasmEdge
- Direktiv

### Comparación mano a mano

| Candidato | Modelo / qué aporta | Unidad de cobro + cifra exacta | Capas gratis / free tier | Límites clave (defaults / diseño) | Estado | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Apache OpenWhisk | FaaS OSS histórico Apache | N/A (self-hosted) | N/A | Defaults: timeout **60,000 ms** (rango 100–300,000); memory **256 MB** (128–512); code **48 MB**; concurrent namespace **100**; minuteRate **120**; result/params **1 MB** | activo (Apache) | [31] |
| Fission | FaaS sobre Kubernetes; executors poolmgr / newdeploy / container | N/A (OSS) | N/A | poolmgr `--poolsize` default **3**; newdeploy/container: scale-to-zero con `minScale: 0`; poolmgr: reap por `idletimeout` (no minScale:0) | activo; release **v1.27.0** (~2026-06-22) | [32] |
| Nuclio | Serverless high-performance; triggers (Kafka, HTTP, etc.) | N/A (OSS) | N/A | Kafka: **una partición / una réplica**; arquitectura con entidad **dealer**; triggers: Cron, Event Hub, HTTP, Kafka, Kinesis, MQTT, NATS, JetStream, RabbitMQ, v3ioStream | activo; release listado **1.17.8** (~2026-09-10) | [33] |
| Fn Project | Motor OSS detrás de OCI Functions | N/A (OSS) | N/A | Límites SaaS: N/A (operador); relación documentada con OCI Functions (“powered by Fn Project”) | activo | [34] |
| WasmEdge | Runtime Wasm edge/cloud (CNCF sandbox) | N/A (OSS) | N/A | No es FaaS completo por sí solo; runtime/embeddable | activo (CNCF sandbox) | [35] |
| Direktiv | Flow engine serverless event-driven sobre K8s/Knative (YAML) | N/A (OSS self-hosted; sin precios managed en docs consultadas) | N/A | Límites tipo SaaS: **no publicados** (dependen del cluster); listado en CNCF landscape.yml | activo (repo no archive); chart **direktiv-0.10.0** (~2025-10-21); tag app **v0.8.10** (notas 2024-12-12) | [36] |

### Elementos diferenciadores e interesantes

**Apache OpenWhisk.** Referencia histórica FaaS OSS con defaults publicados (60 s / 256 MB / 48 MB code) [31]; útil como baseline portable frente a managed. Límites de despliegues productivos (p. ej. clouds) pueden ser mayores — el doc lo advierte.

**Fission.** Diferenciador claro en **modelo de executor**: poolmgr con pool caliente default 3 vs newdeploy/container con `minScale: 0` [32]. Release reciente v1.27.0 (~2026-06-22).

**Nuclio.** Enfoque high-performance y contrato Kafka **partition → single replica** + componente **dealer** [33]. Buena pieza si el informe habla de streaming/triggers, no solo HTTP.

**Fn Project.** Valor comparativo: es el **motor open source** detrás de OCI Functions [34], puente OSS↔managed en la misma familia que ya aparece en pool FaaS.

**WasmEdge.** Runtime Wasm (CNCF sandbox) [35], no plataforma FaaS completa: aporta la capa de ejecución Wasm frente a frameworks FaaS/K8s de la misma lista.

**Direktiv.** Orquestación de **flows YAML** event-driven sobre K8s/Knative [36]; entrada en landscape CNCF (sin afirmar graduated/incubating). Pricing managed: no publicado en docs consultadas.

### Criterios sugeridos para elegir 2

- ¿Se busca **FaaS completo** (OpenWhisk/Fission/Nuclio/Fn) vs **runtime** (WasmEdge) vs **orquestación de flows** (Direktiv)?
- ¿Prioridad **scale-to-zero K8s** documentado (Fission newdeploy) vs pool caliente (poolmgr)?
- ¿Caso **streaming/Kafka** (Nuclio) vs HTTP actions clásicas (OpenWhisk)?
- ¿Narrativa de **continuidad managed** (Fn ↔ OCI Functions) útil para el informe?
- ¿Madurez percibida: proyecto Apache / releases 2026 / listado landscape sin membership CNCF de proyecto?
- ¿Operación self-hosted aceptable (todos) — ninguno aporta precio managed en esta pool?

### Referencias (Lista 4)

31. https://github.com/apache/openwhisk/blob/master/docs/reference.md · https://openwhisk.apache.org/  
32. https://fission.io/docs/concepts/executors/ · https://github.com/fission/fission/releases  
33. https://docs.nuclio.io/en/stable/reference/triggers/ · https://docs.nuclio.io/en/stable/reference/triggers/kafka.html · https://github.com/nuclio/nuclio/releases  
34. https://fnproject.io/ · https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm  
35. https://wasmedge.org/ · https://www.cncf.io/projects/wasmedge/  
36. https://www.direktiv.io/ · https://docs.direktiv.io/ · https://github.com/direktiv/direktiv  

---

## Lista 5: Datos

### Pool (6)

- PlanetScale
- Turso
- Upstash Redis
- CockroachDB Cloud / Basic
- MongoDB Atlas (Serverless → Flex) — *nota de descarte/migración*
- Firestore

### Comparación mano a mano

| Candidato | Modelo / qué aporta | Unidad de cobro + cifra exacta | Capas gratis / free tier | Límites clave | Estado | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| PlanetScale | MySQL/Vitess/Neki/Postgres managed (ya no “Hobby serverless” gratis) | Postgres non-HA PS-5 desde **$5/mo**; HA PS-5 **$15/mo** (us-east-1); Vitess/Neki cluster-based (p. ej. Neki PS-10 arm64 **$30/mo**) | Hobby **deprecado**: upgrade deadline **2024-04-08**; sin plan más pequeño que base PS-10 históricamente citado en FAQ | Precios varían por cloud/región; storage/backups/egress aparte del SKU | activo (modelo cluster actual) | [37][38] |
| Turso | libSQL/SQLite edge-oriented; rows read/written | Free **$0/mo**; Developer desde **$4.99/mo** (display anual); overages p. ej. storage **$0.75/GB**, rows read **$1/Billion**, rows written **$1/Million** | Free: **100** DBs, **5 GB** storage, **500M** rows read/mes, **10M** rows written/mes | Self-host libSQL posible; quotas pueden dejar DB **BLOCKED** | activo | [39] |
| Upstash Redis | Redis serverless pay-per-command | Commands **$0.20 / 100K**; storage PAYG **$0.25/GB-mo** (1er GB free); bandwidth free **200 GB/mo** luego **$0.03/GB** | Incluido en modelo Free/PAYG (límites cmd/s) | Máx **10,000** cmd/s (Free/PAYG); Global DB: cada write replicado cuenta por región | activo | [40] |
| CockroachDB Cloud / Basic | SQL distribuido; Basic = sucesor “Serverless” (RUs) | Basic: **$0.20 / 1M RU**; storage **$0.50 / GiB**. Continuum (orgs nuevas ≥2026-09-15): Standard ej. **$0.092/vCPU-hr** (us-east-1); trial **$400** / 30 días | Basic org PAYG: **$15**/mes ≈ **50M RU** + **10 GiB** | Basic ideal hasta ~**30K RU/s**; RU→0 sin actividad | activo (Basic + Continuum según fecha org) | [41][42] |
| MongoDB Atlas Serverless → Flex | **Nota de descarte**: no elegir Serverless instances | N/A como producto vivo a elegir | Migración a Free/Flex/Dedicated | Fin creación Serverless: **Feb 2025**; fin soporte: **2026-01-22** | Serverless instances: **fin de soporte 2026-01-22** | [43] |
| Firestore | Document DB serverless Google (Standard vs Enterprise) | Standard us-central1: reads **$0.03**/100k; writes **$0.09**/100k; deletes **$0.01**/100k; stored **$0.000205479**/GiB | Free: **1 GiB** stored; **50k** reads / **20k** writes / **20k** deletes **por día**; **10 GiB** outbound/mes | Doc máx **1 MiB**; writes/sec/doc: **sin cifra fija** publicada; Enterprise: unidades KiB distintas (p. ej. Read Units **$0.05 / 1M**) | activo | [44][45] |

### Elementos diferenciadores e interesantes

**PlanetScale.** Peer MySQL/Vitess con branching; el modelo actual es **cluster SKU** (Postgres desde **$5/mo** non-HA) tras deprecación Hobby (**2024-04-08**) [37][38]. Útil para discutir “¿sigue siendo serverless pay-per-request?” frente a peers Neon/D1 de ficha.

**Turso.** Unidades **rows read/written** + storage, con Free generoso en rows y opción **self-host libSQL** [39]. Orientación edge/SQLite distinta de Postgres/MySQL managed.

**Upstash Redis.** Único Redis serverless de la pool: **$0.20/100k commands** y trampa de billing en **Global DB** (writes replicados cuentan) [40].

**CockroachDB Cloud / Basic.** Basic mantiene RUs (**$0.20/1M**) y free **$15**/mes de recursos [41]. Continuum (desde **2026-09-15** para orgs nuevas) cambia el relato a **vCPU-hour** [42] — citar qué plan se usa en el cuadro.

**MongoDB Atlas Serverless.** En pool **solo como nota de descarte**: no crear Serverless desde Feb 2025; soporte terminó **2026-01-22**; migrar Flex/Free/Dedicated [43]. No cuenta como candidato “otro” vivo a elegir.

**Firestore.** Document store serverless con free tier diario y precios Standard US publicados [44]; Enterprise cambia unidades. Tope de documento **1 MiB**; sin writes/sec/doc fijo [45].

### Criterios sugeridos para elegir 2

- ¿Motor deseado: **SQL MySQL/Postgres/distribuido**, **SQLite/libSQL**, **Redis**, o **document**?
- ¿Modelo de cobro: **RU/rows/commands** vs **cluster mensual** vs **reads/writes**?
- ¿Se exige **free tier vigente** (Turso/Upstash/Firestore/Cockroach Basic) vs producto sin Hobby (PlanetScale)?
- ¿Evitar candidatos en **deprecación/fin de soporte** (MongoDB Serverless) como “otro” positivo?
- ¿Self-host posible (Turso/libSQL) vs solo managed?
- ¿Alineación con peers de ficha (Aurora/Neon/D1/DynamoDB) sin duplicar el mismo nicho?

### Referencias (Lista 5)

37. https://planetscale.com/pricing  
38. https://planetscale.com/docs/plans/hobby-plan-deprecation-faq  
39. https://turso.tech/pricing · https://docs.turso.tech/help/usage-and-billing  
40. https://upstash.com/docs/redis/overall/billing · https://upstash.com/pricing/redis  
41. https://docs.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic  
42. https://www.cockroachlabs.com/pricing/  
43. https://www.mongodb.com/docs/atlas/flex-migration/  
44. https://cloud.google.com/firestore/pricing  
45. https://firebase.google.com/docs/firestore/quotas · https://cloud.google.com/firestore/enterprise/pricing  

---

## Nota final

Esta guía compara la pool completa para facilitar la deliberación. **No selecciona los 2 finales por lista.** El grupo elige 2 “otros” por lista desde `pool-otros-revisados.md` usando (si lo desea) los criterios neutrales de cada sección.

**Archivos generados:** `guia-eleccion-otros.md` · `citas-pool-otros.csv` · `citas-pool-otros.bib`
