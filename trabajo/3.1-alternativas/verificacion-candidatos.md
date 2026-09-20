# Verificación de candidatos 3.1 — TERABYTE TI-05

Verificación puntual de cifras anotadas por el grupo frente a documentación **oficial de proveedores**, sin blogs ni comparativas de terceros como fuente de números. Consulta: **2026-09-20** (America/Santiago). Este documento no elige candidatos; solo confronta lo anotado con lo publicado.

> **Addendum 2026-09-20 (clarificación de proceso):** El grupo elige **2 “otros” por lista** desde una **pool** de candidatos ya revisados. El agente **no** elige ni rankea el par final. Puede **añadir** candidatos diferenciadores a la pool solo si están verificados como el resto. Ver companion: [`pool-otros-revisados.md`](./pool-otros-revisados.md). La sección histórica “Propuestas de 2 candidatos por lista” más abajo queda **superada** por esa pool (no usar como selección final).

## 1. OCI Functions pricing + AWS Lambda pricing (mismo día)

### Bloque A — OCI Functions pricing

- **Anotado por el grupo:** free invocations up to 2M/month then USD 0.0000002 each; free execution up to 400,000 GB-s/month then USD 0.00001417 per GB-s; provisioned concurrency billed at 25% when unused.
- **Encontrado:** Invocation: First 2 million per month Free; Over 2 million per month US$0.0000002 per Function invocation. Execution Time: First 400,000 per month Free; Over 400,000 per month US$0.00001417 per Gigabyte memory-seconds. "Unused Provisioned Concurrency is priced at 25% of the rates for Execution Time… There is no additional charge for Provisioned Concurrency that is used to execute Functions."
- **URL:** https://www.oracle.com/cloud/cloud-native/functions/
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

### Bloque B — AWS Lambda pricing (mismo día)

- **Anotado por el grupo:** request price, GB-s price, free tier (sin comparar con OCI).
- **Encontrado:** "The free tier includes one million requests and 400,000 GB-seconds per month." En ejemplos oficiales (US East N. Virginia): monthly request price $0.20 per one million requests; monthly compute price $0.0000166667 per GB-s (x86 on-demand, primer tramo ilustrado).
- **URL:** https://aws.amazon.com/lambda/pricing/
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide (cifras de request, GB-s y free tier publicadas; no se interpreta comparación con OCI)

## 2. OCI Functions limits

- **Anotado por el grupo:** timeout 300s sync / 3600s detached; memory fixed 128/256/512/1024/2048/3072 MB; + payload y concurrency si publicados.
- **Encontrado:** Sync invocation timeout maximum value: 300 seconds (default 30). Detached invocation timeout minimum 5, maximum 3600 seconds. Memory one of: 128, 256, 512, 1024, 2048, 3072 MB. Request payload max 6MB; response payload max 6MB. Service limits: total-concurrency-mb default 60 GB (180 GB in three-AD regions); provisioned-concurrency-mb 40 GB. When total-concurrency-mb is reached, HTTP-429 errors are returned.
- **URL:** https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscustomizing.htm ; https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm ; https://docs.oracle.com/en-us/iaas/Content/General/service-limits/default.htm ; https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage_topic-Monitoring-concurrent-function-execution.htm
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 3. Alibaba FC 3.0 — CU, rates USD (región fuera de China continental), free tier, subscription

- **Anotado por el grupo:** qué es un CU y cómo se calcula; rates pay-as-you-go USD en región fuera de mainland China; free tier; modelo subscription si existe.
- **Encontrado:** CU es el ítem unificado de facturación: "CU usage = Σ(resource usage × CU conversion factor)" (p. ej. active vCPU 1.0 CU/(vCPU·s), memory 0.15 CU/(GB·s), invocations 75 CU/10,000 invocations). Precios tier mensuales **calculados de forma independiente por región** (mismas tablas USD aplicables también fuera de mainland; ejemplo de límites regionales: Singapore, US Virginia, Germany Frankfurt): Tier 1 (0, 100 million] USD 0.000020/CU (descuento oficial Aug 27, 2024–Aug 27, 2026: USD 0.0000160/CU); Tier 2 (100 million, 500 million] USD 0.000017/CU (desc. USD 0.0000136/CU); Tier 3 >500 million USD 0.000014/CU (desc. USD 0.0000112/CU). Trial: 150,000 CU por ciclo, tres ciclos, para primeros usuarios. Modelos: pay-as-you-go, CU resource plans, resident resource pools (subscription GPU).
- **URL:** https://www.alibabacloud.com/help/en/functioncompute/fc-3-0/product-overview/billing-overview-of-fc ; https://www.alibabacloud.com/help/en/functioncompute/fc/product-overview/pay-as-you-go-billing-methods ; https://www.alibabacloud.com/help/en/functioncompute/trial-quota-1
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide (región fuera de mainland: tarifas CU publicadas por región; p. ej. Singapore / US (Virginia) / Germany (Frankfurt) en límites oficiales)

## 4. Alibaba FC limits

- **Anotado por el grupo:** burst instances 300 China main / 100 elsewhere; excess HTTP 429; max timeout y max memory FC 3.0.
- **Encontrado:** Quota Center default "Maximum number of instances" Per region: **300**. Instance delivery speed: 300 instances per minute. Maximum memory per function: 32 GB. Maximum function runtime: 86,400 s. Compute node limits varían por región (p. ej. China Hangzhou 600 vCPU / 1,200 GB; Singapore / US Virginia 300 vCPU / 600 GB; Japan Tokyo / Germany Frankfurt 100 vCPU / 200 GB). Al exceder cuota el documento habla de "throttling error"; no se encontró en la página de quotas la frase literal "HTTP 429" ni el par "300 China / 100 elsewhere" como conteo de instancias burst.
- **URL:** https://www.alibabacloud.com/help/en/functioncompute/fc-3-0/product-overview/limits-of-usage
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (timeout 86400 s y memory 32 GB coinciden; default 300 instancias/región; no publicado el split exacto 300 China / 100 elsewhere ni HTTP 429 literal en esa página)

## 5. IBM Code Engine functions — límites y precios

- **Anotado por el grupo:** "120 s runtime" y "100 KB inline code" son de **functions** no apps/jobs; límites completos; precios vCPU-s, GB-s, invocations USD + free tier.
- **Encontrado (límites functions):** Length of runtime 120 seconds; Memory 48000 MB; Size of request/response body 5 MB; Code size (inline) 100 KB including base64 overhead; Code size (local source) 200 MB compressed; Code size (API) 100 KB including base64 overhead. (Apps: timeout default/max distintos; Jobs: timeout hasta 86400 s — confirmado que 120 s / 100 KB son de la tabla Function limits.)
- **Encontrado (precios):** Docs de pricing remiten al catálogo; el escenario oficial de estimación publica free tier: 100,000 vCPU seconds/month; 200,000 GB seconds/month; 100,000 HTTP requests/month; y rates de ejemplo $0.00003431 per vCPU second; $0.00000356 per GB second; $0.538 per million requests — con disclaimer: "The prices that are used in this example… do not reflect current prices". Página de producto pricing no devolvió tarifas extractables.
- **URL:** https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits ; https://cloud.ibm.com/docs/codeengine?topic=codeengine-pricing ; https://cloud.ibm.com/docs/account?topic=account-sample ; https://www.ibm.com/cloud/code-engine/pricing
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (límites 120 s / 100 KB de functions: coincide; free tier y unidades publicados en docs oficiales; unit prices "current" no publicados de forma definitiva en página de producto — solo en escenario con disclaimer)

## 6. Scaleway Serverless Functions — billing EUR / USD / free tier

- **Anotado por el grupo:** unidad y precio en EUR + free tier; si hay precios USD publicados.
- **Encontrado:** Resource consumption €0.000005 / GB-s (€0.50 per 100k GB-s) after 400 000 GB-s Free Tier per account and per month; Request consumption €0.000015 / 100 requests (€0.15 per 1M requests) after 1 000 000 requests Free Tier; Provisioned resources €0.000017 / GB-s. "Prices before tax." No se publicaron precios en USD en esa página.
- **URL:** https://www.scaleway.com/en/pricing/serverless/
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide (EUR + free tier); USD: no publicado (https://www.scaleway.com/en/pricing/serverless/)

## 7. Fly.io Machines

- **Anotado por el grupo:** billing per second on (CPU/RAM), smallest configs USD, stopped machine charge?, egress, límites documentados, región si varían precios.
- **Encontrado:** Started Machines billed per second (tablas Price/second, Price/hour, Price/month por región). Ejemplo Ashburn-style table: shared-cpu-1x / 256MB $0.00000075/s ($0.0027/h, $1.94/mo). Additional RAM ~$5 per 30 days per GB (con markup regional). Stopped Machines: rootfs $0.15 per 1GB per 30 days stopped. Egress to public internet: North America/Europe $0.02/GB; Asia Pacific/Oceania/South America $0.04/GB; Africa/India $0.12/GB. Precios de Machines varían por región (múltiples matrices). Límites duros de tamaño máximo / conteo / timeout de Machine: no publicados como cifras fijas en la página de pricing (organizaciones pueden tener automated scaling limits).
- **URL:** https://fly.io/docs/about/pricing/
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (billing, smallest shared-cpu-1x 256MB, stopped rootfs, egress y variación regional: coinciden; max machine size/count/timeout: no publicado en esa página)

## 8. Railway pricing

- **Anotado por el grupo:** RAM $10/GB/mo, CPU $20/vCPU/mo, per-minute also at idle, egress $0.05/GB; fixed plan fee besides usage?
- **Encontrado:** RAM $10 / GB / month; CPU $20 / vCPU / month; Network Egress $0.05 / GB; Volume Storage $0.15 / GB / month. "You're billed by the minute for compute resources." Subscription + Resource Usage: Free $0/mo; Hobby $5/mo; Pro $20/mo; Enterprise Custom. "Your subscription fee goes toward your resource usage."
- **URL:** https://docs.railway.com/pricing
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (RAM/CPU/egress y plan fee: coinciden; "also at idle" no aparece como frase — se factura por minuto de compute provisionado/consumido según docs; no afirmar idle gratuito)

## 9. Render

- **Anotado por el grupo:** Free instances spin down after inactivity (exact time); paid do not scale to zero; monthly price smallest paid; workspace quota per plan.
- **Encontrado:** "Render spins down a Free web service that goes **15 minutes** without receiving any inbound traffic." FAQ: "Paid compute plans do not spin down." Smallest paid web service instance: Starter **$7/month**, 512 MB RAM, 0.5 CPU. Workspace: Hobby $0/month + compute (max 25 services, 5 GB bandwidth…); Pro $25/month + compute; Scale $499/month + compute; Enterprise custom.
- **URL:** https://render.com/docs/free ; https://render.com/docs/faq ; https://render.com/pricing
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 10. Bunny Edge Scripting

- **Anotado por el grupo:** 30s CPU vs wall clock?; separate total time limit?; 128 MB, 50 subrequests, 10 MB script, 500 ms cold start, $0.20/million requests, CDN bandwidth separate with rate.
- **Encontrado:** Limits: CPU Time per request **30s**; Active memory **128 MB**; Subrequests **50**; Script size **10 MB**; Startup time **500ms**. Pricing: $0.20 / million requests; $0.02 / 1000s CPU time. "CDN bandwidth is charged at the normal rate and billed separately. It is not included in the CPU Time or Requests charges." No se publica un "total wall-clock time limit" separado del CPU time en la página de limits.
- **URL:** https://bunny.net/docs/scripting/limits ; https://bunny.net/docs/scripting/pricing
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (CPU 30s, 128 MB, 50, 10 MB, 500 ms, $0.20/M, CDN aparte: coinciden; wall-clock / total time limit separado: no publicado)

## 11. Supabase Edge Functions

- **Anotado por el grupo:** 256 MB, 2s CPU/request, worker lifetime 150s free / 400s paid; how invocations billed; URL oficial Postgres + RLS.
- **Encontrado:** Maximum Memory 256MB; Maximum CPU Time 2s per request; Wall clock worker lifetime Free 150s / Paid 400s; Request idle timeout 150s. Invocations: "$2 per 1 million invocations" over plan quota; Free quota 500,000; Pro/Team 2 million. OPTIONS not billed. Postgres RLS: guía oficial Row Level Security.
- **URL:** https://supabase.com/docs/guides/functions/limits ; https://supabase.com/docs/guides/platform/manage-your-usage/edge-function-invocations ; https://supabase.com/docs/guides/database/postgres/row-level-security
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 12. Akamai EdgeWorkers tiers

- **Anotado por el grupo:** Basic/Dynamic/Enterprise Compute memory 1.5/2.5/4 MB, total time 4/5.5/10 s, CPU 10/20/70 ms; no public price list (URL proving contact sales).
- **Encontrado:** Per event handlers (onClientRequest etc.): Maximum memory 1.5 MB / 2.5 MB / 4 MB; Maximum CPU time 10 / 20 / 70 ms; Maximum wall time 4 / 5.5 / 10 seconds (Basic / Dynamic / Enterprise). Billing: charged by events invoked per month; Marketplace activation of Basic/Dynamic/Enterprise packages; resource tiers have "corresponding billing rates" without listing USD amounts on techdocs. Página de producto marketing devolvió Access Denied.
- **URL:** https://techdocs.akamai.com/edgeworkers/docs/resource-tier-limitations ; https://techdocs.akamai.com/edgeworkers/docs/reporting-and-billing ; https://techdocs.akamai.com/edgeworkers/docs/edgeworkers-free-trial
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide (límites); precios públicos USD: no publicado (solo Marketplace/trial/account — https://techdocs.akamai.com/edgeworkers/docs/edgeworkers-free-trial)

## 13. Fission executors

- **Anotado por el grupo:** poolmgr default 3 warm generic pods; poolmgr no scale-to-zero; newdeploy y container yes; executor chosen per function; current stable version + release date.
- **Encontrado:** CLI `--poolsize int` "(default 3)". Docs: poolmgr keeps warm pool; idle specialized pods reaped back to pool via idletimeout — "for newdeploy and container, scaling down to zero is configured with `minScale: 0`; for poolmgr, releasing idle pods is governed by the function’s `idletimeout`." ExecutorType per function: poolmgr | newdeploy | container. Latest GitHub release **v1.27.0**, assets fechados **2026-06-22**.
- **URL:** https://fission.io/docs/concepts/executors/ ; https://fission.io/docs/reference/fission-cli/fission_environment_create/ ; https://github.com/fission/fission/releases
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide (con matiz: poolmgr no usa minScale:0; reap por idle timeout, no "scale-to-zero" estilo Deployment)

## 14. Nuclio

- **Anotado por el grupo:** published trigger list; Kafka partition served by single replica; "dealer" component exists; stable version + date.
- **Encontrado:** Triggers documentados: Cron, Azure Event Hub, HTTP, Kafka, Kinesis, MQTT, NATS, NATS JetStream, RabbitMQ, v3ioStream. Kafka: "a given partition is handled only by one replica" and messages processed sequentially. Architecture: "Nuclio includes a “dealer” entity that can dynamically distribute N resources (shards, partitions, tasks, etc.) to M processors". Latest release listado **1.17.8** (GitHub, ~2026-09-10); stable badge histórico menciona v1.16.x en notes.
- **URL:** https://docs.nuclio.io/en/stable/reference/triggers/ ; https://docs.nuclio.io/en/stable/reference/triggers/kafka.html ; https://docs.nuclio.io/en/latest/concepts/architecture.html ; https://github.com/nuclio/nuclio/releases
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 15. Descartas OSS — Kubeless, riff, IronFunctions

- **Anotado por el grupo:** Kubeless (VMware archived), riff (archived), IronFunctions (forked to Fn Project under Oracle) — URL + fecha exacta.
- **Encontrado:**
  - **Kubeless:** README oficial en https://github.com/vmware-archive/kubeless — "WARNING: Kubeless is no longer actively maintained by VMware." Repo bajo org `vmware-archive`. **Fecha exacta de archivado:** no publicada en el README (sin día calendario en el aviso).
  - **riff:** https://projectriff.io/ — "March 13, 2021 — Project riff is complete. So Long, and Thanks for All the Fish".
  - **IronFunctions → Fn:** https://blogs.oracle.com/cloud-infrastructure/oracle-simplifies-cloud-native-development (January 25, 2019): "Oracle last year started the Fn Project… It was developed by the serverless group from Iron.io that was hired into Oracle". OCI Functions docs: "powered by the Fn Project open source engine" / "based on Fn Project" — https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm. Repo histórico: https://github.com/iron-io/functions.
- **URL:** (arriba)
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (riff fecha exacta 2021-03-13; Iron/Fn relación Oracle documentada 2019-01-25; Kubeless archived/unmaintained confirmado, **fecha exacta de archive no publicada**)

## 16. Turso

- **Anotado por el grupo:** billing units (rows read/written, storage, DBs, replicas), USD rates, free tier; libSQL server self-hostable con URL exacta.
- **Encontrado:** Plan Free $0/month: 100 databases, 5GB storage, 500 Million monthly rows read, 10 Million monthly rows written (y syncs/otros en tabla de pricing). Developer from $4.99/month (annual display) con overages p. ej. storage $0.75/GB, rows read $1/Billion, rows written $1/Million. Docs usage: rows read/written + storage; quotas bloquean con BLOCKED. Self-host / local: libSQL server vía Turso CLI `turso dev`; código abierto https://github.com/tursodatabase/libsql ; docs https://docs.turso.tech/local-development.
- **URL:** https://turso.tech/pricing ; https://docs.turso.tech/help/usage-and-billing ; https://docs.turso.tech/local-development ; https://github.com/tursodatabase/libsql
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 17. Upstash Redis

- **Anotado por el grupo:** $0.20 per 100k commands, max 10k cmd/s, global DB replicated writes count per region; storage y egress costs?
- **Encontrado:** Commands $0.20 per 100K commands; Max commands/sec 10,000 (Free/PAYG); "Global databases… each write is replicated to every read region, and each replicated write counts as a command for billing." Storage PAYG: $0.25 / GB per month (first 1 GB free). Bandwidth: free up to 200 GB/month, then $0.03 / GB.
- **URL:** https://upstash.com/docs/redis/overall/billing ; https://upstash.com/pricing/redis
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

## 18. Firestore

- **Anotado por el grupo:** billing units (reads/writes/deletes per 100k; storage GiB; egress), USD US region, free tier, Standard vs Enterprise, quotas (doc size, writes/sec/doc).
- **Encontrado (Standard, Iowa us-central1):** Document Reads $0.03 per 100,000; Writes $0.09 per 100,000; Deletes $0.01 per 100,000; Stored Data $0.000205479 / GiB (unit price table); Free tier: 1 GiB stored, 50,000 reads/day, 20,000 writes/day, 20,000 deletes/day, 10 GiB outbound/month. Internet egress (Americas etc.): first 10 GiB free then $0.12/GiB (tiered). Max document size 1 MiB. Writes/sec per document: "The exact maximum rate that an app can update a single document depends highly on the workload" (no cifra fija publicada). Collection sequential indexed field ~500 writes/s best-practice note. **Enterprise:** unidades distintas (Read/Write Units en KiB), precios distintos (p. ej. Read Units $0.05 / 1,000,000 count).
- **URL:** https://cloud.google.com/firestore/pricing ; https://cloud.google.com/firestore/enterprise/pricing ; https://firebase.google.com/docs/firestore/quotas ; https://firebase.google.com/docs/firestore/best-practices
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide parcialmente (billing Standard US + free tier + doc 1 MiB + diferencia Enterprise: coinciden; writes/sec/doc cifra fija: no publicado)

## 19. MongoDB Atlas Serverless discard

- **Anotado por el grupo:** exact end-of-creation y end-of-support dates from official Flex migration page.
- **Encontrado:** "As of **February 2025**, you can create Flex clusters, and can no longer create M2 and M5 clusters or **Serverless instances**… As of **January 22, 2026**, Atlas no longer supports M2 and M5 clusters and Serverless instances." Migración automática a Free/Flex/Dedicated según uso.
- **URL:** https://www.mongodb.com/docs/atlas/flex-migration/
- **Fecha de consulta:** 2026-09-20
- **Veredicto:** coincide

---

## URLs fallidas

| URL | Problema | Usado en su lugar |
| --- | --- | --- |
| https://www.ibm.com/cloud/code-engine/pricing | Contenido de tarifas no extractable / página casi vacía | https://cloud.ibm.com/docs/codeengine?topic=codeengine-pricing + escenario https://cloud.ibm.com/docs/account?topic=account-sample |
| https://www.akamai.com/products/serverless-computing-edgeworkers | Access Denied (403/edge block) | https://techdocs.akamai.com/edgeworkers/docs/resource-tier-limitations y free-trial/billing docs |
| https://docs.nuclio.io/en/stable/reference/triggers/triggers.html | 404 | https://docs.nuclio.io/en/stable/reference/triggers/ |
| https://api.github.com/repos/vmware-archive/kubeless (y otros) | 403 rate limit | Páginas HTML/README de GitHub vía WebFetch |
| Precios "live" IBM Code Engine catalog | No cifras actuales en página producto | Escenario oficial con disclaimer de no-current |

---

## Propuestas de 2 candidatos por lista (3.1) — SUPERADA

> **SUPERADA 2026-09-20.** No usar como elección final. La pool completa (sin ranking) está en [`pool-otros-revisados.md`](./pool-otros-revisados.md). El grupo elige 2 por lista desde esa pool. Lo siguiente se conserva solo como histórico de una ronda previa de propuestas.

*histórico — el grupo decide; preferencia entonces: CNCF Landscape / peers; sin inventar productos*

### 1. Funciones como servicio

1. **Huawei Cloud FunctionGraph** — FaaS gestionado peer en Landscape/encuestas Asia-Pacífico, fuera del set Lambda/Cloud Run/Azure/Oracle/Alibaba/IBM/Scaleway. Producto: https://www.huaweicloud.com/intl/en-us/product/functiongraph.html — Pricing: consultar pricing oficial Huawei de la región.
2. **Tencent Cloud Serverless Cloud Function (SCF)** — FaaS público documentado en revisiones FaaS; distinto de los ya verificados. Producto: https://www.tencentcloud.com/products/scf — Pricing: página oficial SCF pricing de Tencent Cloud.

### 2. Contenedores sin servidor

1. **Koyeb** — Serverless containers con scale-to-zero; aparece en exploraciones tipo Landscape/peers (nota: está en el conjunto “Fly/Railway/Render/Scaleway/Koyeb” del brief; se propone explícitamente desde ese set). Producto: https://www.koyeb.com/ — Pricing: https://www.koyeb.com/pricing
2. **DigitalOcean App Platform** — Contenedores/apps gestionados con escala; alternativa managed fuera de los hiperescalares ya listados. Producto: https://www.digitalocean.com/products/app-platform — Pricing: https://www.digitalocean.com/pricing/app-platform

### 3. Cómputo en el borde

1. **Azion Edge Functions** — Edge compute/FaaS en red de borde (LATAM-relevante), fuera de CF/Fastly/Lambda@Edge/CloudFront Functions/Vercel/Netlify/Deno. Producto: https://www.azion.com/en/products/edge-functions/ — Pricing: documentación/pricing Azion oficial.
2. **Fermyon Cloud (Spin)** — Hosting managed de Spin (CNCF), Wasm en borde/cloud; complementa Spin OSS ya en Landscape. Producto: https://www.fermyon.com/cloud — Docs: https://developer.fermyon.com/

### 4. Código abierto

1. **Apache OpenWhisk** — Plataforma FaaS OSS histórica en Landscape/encuestas, fuera de Knative/OpenFaaS/KEDA/Spin/wasmCloud/Wasmtime. Repo/docs: https://openwhisk.apache.org/
2. **Direktiv** — Workflow/serverless event-driven OSS listado en ecosistema CNCF Landscape (serverless tools). Sitio: https://direktiv.io/ — Repo: https://github.com/direktiv/direktiv

### 5. Datos sin servidor

1. **PlanetScale** — MySQL serverless/branching managed; peer frecuente frente a Aurora/Neon/D1. Producto: https://planetscale.com/ — Pricing: https://planetscale.com/pricing
2. **CockroachDB Serverless** (CockroachDB Cloud) — SQL distribuido serverless managed. Producto: https://www.cockroachlabs.com/product/cockroachdb/ — Pricing Cloud: https://www.cockroachlabs.com/pricing/

---

## Resumen de veredictos (19 ítems)

| Veredicto | Cantidad | Ítems (sección) |
| --- | --- | --- |
| coincide | 12 | 1, 2, 3, 6, 9, 11, 12, 13, 14, 16, 17, 19 |
| coincide parcialmente | 7 | 4, 5, 7, 8, 10, 15, 18 |
| no coincide | 0 | — |

Aspectos puntuales **no publicados** (dentro de secciones coincide/parcial): precios USD Scaleway; wall-clock Bunny separado; writes/sec/doc Firestore cifra fija; fecha exacta archive Kubeless; hard limits Fly size/count/timeout; unit prices “current” IBM Code Engine en página de producto.

**Conteo por sección (1–19):** coincide **12** · coincide parcialmente **7** · no coincide **0**.

**Archivo:** `/workspace/fuentes-terabyte/trabajo/3.1-alternativas/verificacion-candidatos.md`
