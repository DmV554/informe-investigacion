# Propuesta de selección — Anexo D (D.2–D.6)

**Informe:** TERABYTE · TI-05 · rama `daniel/3.1-alternativas-anexo-d`  
**Fecha de esta propuesta:** 2026-09-20 (America/Santiago)  
**Criterios aplicados:** Tabla D.1 + regla de desempate según redacción actualizada de D.1 (I3 con seis dimensiones; X2 solo retiro/archivo; desempate en cinco pasos).  
**Evidencia de cifras/límites:** `guia-eleccion-otros.md` y `verificacion-candidatos.md` (consulta 2026-09-20).  
**Alcance:** rellenar Resultado/Motivo en D.2–D.6. **D.7 no se trata aquí.**  
**Estado:** propuesta para aprobación humana (Daniel / grupo). No es decisión cerrada hasta que el grupo la ratifique.

---

## Orden de aplicación (igual en las cinco listas)

1. **X1, X2** a toda la pool de la lista.  
2. **I1, I2, I3** a los que no cayeron en X.  
3. Si quedan **más de dos** que cumplen I1–I3: **regla de desempate** (pasos 1→5).  
4. Si quedan exactamente dos: entran ambos, sin desempate.  
5. Si queda uno o ninguno: declarar en D.7 (fuera de este documento).

### Dimensiones I3 (referencia)

1. Unidad o modelo de cobro  
2. Mecanismo de aislamiento o de escala a cero  
3. Otra jurisdicción o región de operación documentada (moneda, ubicación de datos o PoP)  
4. Acoplamiento a otro servicio del mismo ecosistema  
5. Límites en otro orden de magnitud (tiempo, payload, concurrencia)  
6. Portabilidad entre despliegue gestionado y autoalojado  

**No cuentan:** popularidad, madurez percibida, herramientas de desarrollo, ni el mero hecho de ser un proveedor distinto.

### Desempate (pasos)

1. Precio de lista vigente publicado frente a solo cotización o precio ausente  
2. Límites técnicos publicados frente a no publicados  
3. Disponibilidad general (GA) frente a beta / beta abierta / vista previa (pública o privada)  
4. Documentación oficial más específica (límites o pricing del propio servicio)  
5. Si siguen >2 con **contrastes distintos**: retener los dos cuya dimensión I3 sea más útil al resto del informe (cobro → 2.3 y 4.2; escala a cero / frío → 2.2; portabilidad → 2.6; jurisdicción/región → 4.3)

Registro de un descartado por sobrar: `desempate, paso n` (no un código X).

---

## Resultado consolidado (par que entra por lista)

| Lista | Alternativa 1 | Alternativa 2 | Ancla principal en el informe |
|---|---|---|---|
| D.2 Funciones | Oracle OCI Functions | Scaleway Serverless Functions | 2.6 + 4.3 |
| D.3 Contenedores | Koyeb | Scaleway Serverless Containers | 2.2 / 4.2 + 4.3 |
| D.4 Borde | Azion Edge Functions | Bunny Edge Scripting | 4.3 + 2.3 / 4.2 |
| D.5 Código abierto | Fission | Fn Project | 2.2 + 2.6 |
| D.6 Datos | Turso (libSQL) | Upstash Redis | 2.3 / 4.2 + 2.6 |

---

## D.2 Funciones como servicio

**Plataformas de la ficha:** AWS Lambda, Google Cloud Run functions, Azure Functions.

### Puertas X

Ningún candidato de la pool activa **X1** (no son extensión/modo de otro de la misma lista ni de la ficha) ni **X2** (ninguno retirado/archivado).

### Inclusión candidata a candidata

#### Oracle Cloud Infrastructure Functions — **Entra (I1–I3)**

- **I1:** Cumple. Límites oficiales (p. ej. timeout sync máx. 300 s, detached hasta 3600 s, memoria fija 128–3072 MB, payload 6 MB). Precio de lista USD vigente en página de producto (invocaciones y GB-s tras free tier; provisioned idle al 25 % del execution time).  
- **I2:** Cumple. FaaS gestionado; ejecuta código del usuario.  
- **I3:** Cumple. Dimensión **(6)** portabilidad managed↔self-host: OCI Functions está documentado como basado en / powered by Fn Project. Dimensión auxiliar **(5):** modo detached con timeout hasta 3600 s frente al techo sync típico de la ficha.  
- **Útil para:** §2.6 (portabilidad / dependencia del proveedor con puente OSS); límites en el cuadro comparativo.

#### Scaleway Serverless Functions — **Entra (I1–I3)**

- **I1:** Cumple. Límites publicados (timeout 10 s–60 min, escala máx. 50, concurrency 1/instancia, payload 6 MiB). Precio de lista en **EUR** en pricing serverless (resource, requests, provisioned) + free tier mensual. USD no publicado; no se exige USD si hay lista vigente.  
- **I2:** Cumple. FaaS.  
- **I3:** Cumple. Dimensión **(3):** moneda de facturación EUR y operación documentada en UE.  
- **Útil para:** §4.3 (jurisdicción / moneda frente al caso TERABYTE).

#### IBM Cloud Code Engine (functions) — **Descartado (I1)**

- **I1:** No cumple. Límites de *functions* sí publicados (p. ej. runtime 120 s, inline 100 KB). El precio unitario “actual” no está como lista vigente en producto: el escenario oficial de estimación lleva advertencia de que **no refleja precios actuales**. Eso no cuenta como precio publicado bajo I1.  
- No se evalúa I2/I3.

#### Alibaba Cloud Function Compute 3.0 — **Descartado (desempate, paso 5)**

- **I1:** Cumple (límites FC 3.0; pay-as-you-go por CU en USD por región, también fuera de mainland).  
- **I2:** Cumple.  
- **I3:** Cumple. Dimensión **(1)** modelo de cobro por **CU** (conversión unificada vCPU/memoria/invocaciones), distinto del request+GB-s de Lambda/Azure. Auxiliar **(5):** runtime hasta 86 400 s y memoria hasta 32 GB.  
- **Por qué no entra al par:** tras I, quedaban >2 vivos con contrastes distintos (Oracle portabilidad, Scaleway jurisdicción, Alibaba cobro CU, más Huawei/Tencent). Paso 5: se retienen Oracle (2.6) y Scaleway (4.3). El cobro CU aportaría a 2.3/4.2, pero el informe ya desarrolla cobro FaaS hiperescala en 3.2; portabilidad OSS↔managed y jurisdicción UE aportan huecos que la ficha no cubre.

#### Huawei Cloud FunctionGraph — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen (pricing USD en docs intl.; límites p. ej. duración máx. 259 200 s, memoria 10 GB).  
- **I3:** Cumple de forma más débil: **(5)** duración máxima en otro orden; cobro request+GB-s cercano al de la ficha (poca novedad en **(1)**).  
- **Desempate:** frente a Alibaba (mismo “bloque” Asia/intl. con techos altos), Alibaba gana por especificidad del cobro CU (pasos 4–5). Luego fuera del par final por paso 5 frente a Oracle+Scaleway.

#### Tencent Cloud SCF — **Descartado (desempate)**

- **I1 / I2:** Cumplen (USD intl.; free tier temporal + basic package; límites memoria/timeout documentados).  
- **I3:** **(1)** basic package post free-tier; **(3)** regiones intl. documentadas — contraste del mismo tipo que Huawei/Alibaba.  
- **Desempate:** redundante en tipo de contraste con Huawei/Alibaba; se retiene Alibaba en ese grupo y luego el par final es Oracle+Scaleway.

---

## D.3 Contenedores sin servidor

**Plataformas de la ficha:** Google Cloud Run, AWS Fargate, Azure Container Apps, AWS App Runner.

### Puertas X

Ningún **X1** entre candidatos de la pool.  
Ningún **X2:** DigitalOcean App Platform **no** se descarta por X2 aunque Scale to Zero esté en private preview (X2 actual = solo retiro/archivo).

### Inclusión y desempate

#### Koyeb — **Entra (I1–I3)**

- **I1:** Cumple (pricing $/s Standard/Eco, planes; instancias documentadas).  
- **I2:** Cumple (contenedores serverless gestionados).  
- **I3:** **(2)** scale-to-zero GA documentado; **(1)** cobro por segundo con línea Eco.  
- **Útil para:** §2.2 (escala a cero / frío) y §2.3 / 4.2 (unidad de cobro).

#### Scaleway Serverless Containers — **Entra (I1–I3)**

- **I1:** Cumple (límites timeout/scale/concurrency/memoria; precio EUR GB-s y vCPU-s + free tier).  
- **I2:** Cumple.  
- **I3:** **(3)** EUR / UE; **(1)** free tier de memoria y vCPU.  
- **Nota X1:** Scaleway Functions (D.2) y Containers (D.3) son listas distintas → X1 no aplica entre ellas.  
- **Útil para:** §4.3.

#### Fly.io (Machines) — **Descartado (I1)**

- Precio por segundo y cargos (p. ej. rootfs en stopped, egress) **sí** publicados.  
- **I1 falla** porque los límites técnicos duros de Machine (tamaño/conteo/timeout como cifras fijas) **no** están publicados en la documentación de pricing/límites usada en la verificación (2026-09-20). Sin límites publicados no hay I1.

#### Railway — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen (RAM/CPU/egress + fee de plan; docs de usage).  
- **I3:** **(1)** modelo subscription + usage por minuto.  
- No aporta STZ GA comparable a Koyeb ni jurisdicción/moneda como Scaleway. Fuera del par por paso 5.

#### Render — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen.  
- **I3:** spin-down a los 15 min **solo en Free**; paid **no** scale-to-zero (documentado). El contraste de escala a cero queda acotado al plan gratuito → menos útil para 2.2 que Koyeb (STZ GA).

#### DigitalOcean App Platform — **Descartado (desempate, paso 3 / 5)**

- **X2:** no aplica (producto contratable; no retirado).  
- **I1 / I2:** Cumplen como PaaS de contenedores (precio desde ~$5/mo, límites de app publicados).  
- Scale to Zero está en **private preview** → no se usa como dimensión **(2)** sólida; en desempate, la preview pierde en **paso 3** frente a alternativas GA cuando se discute disponibilidad del mecanismo. El aporte restante (precio de entrada) es débil frente a Koyeb+Scaleway → **paso 5**.

---

## D.4 Cómputo en el borde

**Plataformas de la ficha:** Cloudflare Workers (DO/D1/R2), Fastly Compute, Lambda@Edge, CloudFront Functions, Vercel, Netlify, Deno Deploy.

### Puertas X

Ningún X1 relevante en la pool viva.  
Ningún X2 (Fermyon en open beta **no** es X2 bajo la definición actual).

### Inclusión y desempate

#### Azion Edge Functions — **Entra (I1–I3)**

- **I1:** Cumple (límites de functions; pricing compute + invocations en USD).  
- **I2:** Cumple (ejecuta código del usuario en edge).  
- **I3:** **(3)** región / PoP con relevancia LATAM documentada en el producto; **(1)** cobro por compute e invocations.  
- **Útil para:** §4.3.

#### Bunny Edge Scripting — **Entra (I1–I3)**

- **I1:** Cumple (límites CPU 30 s, memoria 128 MB, script 10 MB, etc.; pricing $/M requests + CPU time). Wall-clock total separado: no publicado — no impide I1 si el resto de límites está.  
- **I2:** Cumple.  
- **I3:** **(1)** modelo $/M + CPU; **(5)** CPU 30 s frente a límites de milisegundos de otros edges de ficha (p. ej. CloudFront Functions / perfiles muy cortos).  
- **Útil para:** §2.3 / 4.2.

#### Azure Front Door (Rules Engine / Edge Actions) — **Descartado (I2)** *(ya en main.tex)*

- Rules Engine: condiciones + acciones predefinidas, **no** ejecuta código arbitrario del usuario → falla I2.  
- Edge Actions: ejecuta código pero en vista previa; el descarte registrado en el anexo prioriza I2 sobre el producto “Front Door” como candidato de borde tipo Workers.

#### Akamai EdgeWorkers — **Descartado (I1)**

- Límites por tier (memoria/CPU ms/wall) **sí** publicados.  
- Precio USD de lista **no** aparece en techdocs (Marketplace / trial / account). Tampoco hay declaración explícita de “solo por cotización” que satisfaga el segundo brazo de I1. → **I1 no cumple**.

#### Fermyon Cloud (Spin gestionado) — **Descartado (desempate, paso 3)**

- **I1 / I2:** Cumplen (planes Starter/Growth; ejecuta apps Spin).  
- **I3:** **(6)** portabilidad con Spin/SpinKube de la ficha (managed↔OSS).  
- Estado **open beta** (sin SLA en docs consultadas) → en desempate frente a candidatos GA del mismo proceso de selección, pierde en **paso 3**.

#### Supabase Edge Functions — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen.  
- **I3:** **(4)** acoplamiento a Postgres + RLS del mismo ecosistema.  
- Contraste válido y distinto de Azion/Bunny, pero el paso 5 prioriza el par **jurisdicción LATAM (4.3) + cobro/límites edge de red (2.3/4.2)** sobre el acoplamiento BaaS.

---

## D.5 Código abierto

**Plataformas de la ficha:** Knative, OpenFaaS, KEDA, Fermyon Spin / SpinKube, wasmCloud, Wasmtime.

### Puertas X *(varias ya cerradas en main.tex)*

| Candidato | Resultado | Detalle |
|---|---|---|
| Kubeless | Descartado (X2) | Repo bajo `vmware-archive`; README: ya no mantenido por VMware. |
| riff | Descartado (X2) | Proyecto declarado terminado (13-03-2021). |
| IronFunctions | Descartado (X1) | Linaje sucedido por Fn Project (mismo equipo → Oracle); se evalúa Fn. |

### Resto de la pool

#### Fission — **Entra (I1–I3)**

- **I1:** Para OSS self-hosted, “contratable” = usable/mantenido; límites/comportamiento de executors documentados (poolmgr / newdeploy / container; `minScale: 0`). Sin precio managed (N/A).  
- **I2:** Cumple (plataforma FaaS sobre Kubernetes; encaja en “plataforma” de I2 OSS).  
- **I3:** **(2)** mecanismos distintos de escala (pool caliente vs scale-to-zero por executor).  
- **Útil para:** §2.2.

#### Fn Project — **Entra (I1–I3)**

- **I1 / I2:** Cumplen (proyecto activo; motor FaaS OSS).  
- **I3:** **(6)** documentación de que OCI Functions está powered by Fn → portabilidad managed↔self-host.  
- **X1 vs OCI Functions:** no aplica (listas distintas).  
- **Útil para:** §2.6 (y coherencia con Oracle en D.2).

#### WasmEdge — **Descartado (I3)**

- **I1 / I2:** Runtime OSS; I2 OSS admite runtime.  
- **I3:** No cumple. La ficha ya incluye **Wasmtime**. Ser “otro runtime Wasm” no es dimensión de la lista I3 (el mero hecho de ser otro proyecto no cuenta). No aporta cobro, jurisdicción, acoplamiento nuevo, ni portabilidad managed distinta documentada como hueco frente a Wasmtime.

#### Direktiv — **Descartado (I2)**

- Motor de **flujos** event-driven sobre K8s/Knative.  
- I2 OSS pide componente cuyo propósito principal sea plataforma, **runtime** o **autoescalado**, en línea con lo que la ficha ya incluye. Direktiv es orquestación de flows → **no cumple I2**. (Caso límite registrado así, no como I3.)

#### Apache OpenWhisk — **Descartado (I3)**

- **I1 / I2:** Cumplen (FaaS OSS Apache; defaults de timeout/memoria/code size publicados).  
- **I3:** No aporta dimensión nueva frente a **OpenFaaS / Knative** ya en ficha (otro FaaS OSS self-hosted sin cobro/jurisdicción/portabilidad managed distinta documentada como hueco).

#### Nuclio — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen.  
- **I3:** **(4)** triggers (Kafka, etc.) y contrato partición→réplica — acoplamiento streaming.  
- Contraste válido, pero paso 5 prioriza Fission (2.2) + Fn (2.6) por anclaje directo a secciones del informe frente a streaming, menos central en el índice actual.

---

## D.6 Datos sin servidor

**Plataformas de la ficha:** Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1.

### Puertas X

| Candidato | Resultado | Detalle |
|---|---|---|
| MongoDB Atlas Serverless | Descartado (X2) | Sin creación de instancias Serverless desde feb 2025; fin de soporte 22-01-2026; migración a Free/Flex/Dedicated (doc Flex migration). |

### Resto

#### Turso (libSQL) — **Entra (I1–I3)**

- **I1:** Cumple (pricing Free/Developer, units rows/storage; quotas documentadas).  
- **I2:** Cumple (consulta/almacena datos del usuario).  
- **I3:** **(1)** cobro por rows read/written (+ storage); **(6)** self-host de libSQL documentado. Distinto de Neon (Postgres) / Aurora / D1 (SQLite en CF sin el mismo puente self-host/cobro).  
- **Útil para:** §2.3 / 4.2 y §2.6.

#### Upstash Redis — **Entra (I1–I3)**

- **I1:** Cumple ($/comando, storage, bandwidth, límites cmd/s).  
- **I2:** Cumple (almacén serverless de datos).  
- **I3:** **(1)** modelo pay-per-command sobre API Redis — hueco no cubierto por Aurora/Neon/D1/DynamoDB.  
- **Útil para:** §2.3 / 4.2.

#### PlanetScale — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen (pricing cluster actual post-Hobby).  
- **I3:** posible **(1)** cobro por SKU mensual frente a ACU/RU — pero el motor MySQL/Vitess **solapa el eje SQL managed** ya cubierto por Aurora (y el contraste “¿sigue siendo serverless pay-per-request?” es analítico, no una dimensión I3 limpia).  
- Fuera del par por paso 5 frente a Turso+Upstash (más hueco de modelo de datos/cobro).

#### CockroachDB Cloud (Basic) — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen (RUs, storage, free de organización en Basic).  
- **I3:** **(1)** RUs — cercano al relato serverless SQL; solapa fuerte con Aurora como SQL distribuido/managed.  
- Paso 5: menos útil que Turso (libSQL + portabilidad) y Upstash (Redis).

#### Firestore — **Descartado (desempate, paso 5)**

- **I1 / I2:** Cumplen.  
- **I3:** **(1)** reads/writes/deletes; **(4)** ecosistema Google.  
- DynamoDB ya cubre NoSQL managed en la ficha; el aporte diferencial es menor que Redis API + libSQL edge para el cuadro. Paso 5.

---

## Frases candidatas para columna “Motivo / qué aporta” (las que Entran)

Listas para pegar (ajustables al tono del anexo):

| Lista | Candidato | Motivo (entra) |
|---|---|---|
| D.2 | Oracle OCI Functions | Portabilidad managed↔Fn Project (I3-6); timeouts detached documentados (I3-5). |
| D.2 | Scaleway Serverless Functions | Facturación EUR y operación UE (I3-3); free tier y concurrency 1 documentados. |
| D.3 | Koyeb | Scale-to-zero GA y cobro por segundo Standard/Eco (I3-2, I3-1). |
| D.3 | Scaleway Serverless Containers | Precio EUR/UE y free tier GB-s/vCPU-s (I3-3, I3-1). |
| D.4 | Azion Edge Functions | PoP/región LATAM y pricing compute+invocations (I3-3, I3-1). |
| D.4 | Bunny Edge Scripting | Cobro $/M+CPU y CPU 30 s frente a edges de ms (I3-1, I3-5). |
| D.5 | Fission | Executors con scale-to-zero configurable (`minScale:0`) (I3-2). |
| D.5 | Fn Project | Motor OSS de OCI Functions; portabilidad managed↔self-host (I3-6). |
| D.6 | Turso | Cobro por rows y self-host libSQL (I3-1, I3-6). |
| D.6 | Upstash Redis | Redis serverless pay-per-command (I3-1); hueco frente a la ficha. |

---

## Notas para el registro en `main.tex`

1. En Resultado usar exactamente el criterio: `Entra (I1--I3)`, `Descartado (I1)`, `Descartado (I2)`, `Descartado (I3)`, `Descartado (X1)`, `Descartado (X2)`, `Descartado (desempate, paso n)`.  
2. Anotar el **número de dimensión I3** en el motivo de los que entran (lo pide D.1).  
3. Fecha de consulta ya precargada: **2026-09-20**.  
4. No inventar precios ni límites: citar solo lo ya verificado en guía/verificación o reabrir la URL oficial el día que se cierre el anexo.  
5. **D.7** queda pendiente si alguna lista no llega a dos (con esta propuesta, las cinco listas llegan a dos).

---

*Fin de la propuesta. Autoría de la decisión final: grupo TERABYTE (punto 6.1 de las Indicaciones).*
