# Fuentes de la sección 4.1 — lista de verificación

> **Estado 21-09-2026:** las 16 páginas fueron leídas y contrastadas con su afirmación.
> El resultado está en la sección 5 y las citables ya están en `informe/referencias.bib`
> (claves `cf*`, `gcr*`, `gcp*`, `aws*`, `urldate = 2026-09-21`).

Regla del enunciado (§5 y §6.1): toda afirmación se verifica en la fuente original, toda cita
lleva fecha de consulta, y las cifras se obtienen de la fuente, no del modelo. Marca cada fila
cuando la hayas leído tú y anota la fecha. Si la página no dice lo que la fila afirma, no se
cita: se reformula la afirmación o se elimina.

Cifras propias: `poc/data/mediciones_20260921-0041_forzado.csv`, `poc/results/resumen.csv`,
`poc/results/cloudrun_startup.csv` (rama `PoC`, commit `950d22c`). No requieren fuente externa;
requieren el anexo B.

## 1. Documentación oficial (fuentes preferentes)

| # | Afirmación que sostiene en 4.1 | Página | Qué confirmar exactamente | Fecha | ✓ |
|---|---|---|---|---|---|
| 1 | Workers: 128 MB por isolate, no configurable | https://developers.cloudflare.com/workers/platform/limits/ | Frase "Each isolate can consume up to 128 MB"; que no hay opción para cambiarlo ni diferencia Free/Paid | | |
| 2 | Workers: cada Worker corre en un isolate V8; un despliegue publica una versión nueva (isolates nuevos) | https://developers.cloudflare.com/workers/reference/how-workers-works/ | Descripción de isolates y de cómo se despliega/actualiza el código en el edge | | |
| 3 | Cloud Run gen1 usa gVisor; gen1 es la única generación que permite 128 MiB | https://docs.cloud.google.com/run/docs/about-execution-environments | Tabla gen1 vs gen2: sandbox y memoria mínima | | |
| 4 | Cloud Run: límite de memoria configurable; el contenedor muere si lo excede | https://docs.cloud.google.com/run/docs/configuring/services/memory-limits | Comportamiento al exceder el límite (nuestro log: "Memory limit of 128 MiB exceeded") | | |
| 5 | Cloud Run: el contenedor debe escuchar en `$PORT`; la instancia se considera lista cuando responde (startup) | https://docs.cloud.google.com/run/docs/container-contract | Contrato de arranque; qué pasa cuando el proceso termina | | |
| 6 | Cloud Run valida una revisión nueva con un health check de arranque antes de enrutar tráfico | https://docs.cloud.google.com/run/docs/configuring/healthchecks | Startup probe por defecto (TCP) y su rol en marcar la instancia como lista | | |
| 7 | Cloud Run: revisiones, tráfico y escalado a cero (`min-instances 0`) | https://docs.cloud.google.com/run/docs/resource-model | Definición de servicio/revisión/instancia; cuándo se enruta tráfico a una revisión | | |
| 8 | Cloud Run: CPU asignada solo durante solicitudes (`--cpu-throttling`) y startup CPU boost | https://docs.cloud.google.com/run/docs/configuring/cpu-allocation | Qué hace cada opción; por qué desactivamos el boost (mide sin mitigación) | | |
| 9 | Cloud Run: vCPU configurable independiente de la memoria (`--cpu 1`) | https://docs.cloud.google.com/run/docs/configuring/services/cpu | Rango permitido y relación mínima CPU/memoria | | |
| 10 | Métrica `run.googleapis.com/container/startup_latencies` (arranque del contenedor visto por la plataforma) | https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z | Buscar `container/startup_latencies` en la sección Cloud Run: definición y unidad (ms) | | |
| 11 | Cloud Run: métricas disponibles, incluida latencia de arranque | https://docs.cloud.google.com/run/docs/monitoring | Lista de métricas del servicio | | |
| 12 | Lambda: ciclo de vida del entorno de ejecución (Init → Invoke → Shutdown); cambiar la configuración invalida los entornos | https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html | Fase Init; que la actualización de la función/configuración crea entornos nuevos | | |
| 13 | Lambda: la CPU es proporcional a la memoria asignada | https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html | Frase sobre CPU proporcional; rango 128 MB–10 GB | | |
| 14 | Lambda: `Init Duration` en la línea REPORT de CloudWatch | https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html | Campos de la línea REPORT (Duration, Billed Duration, Init Duration) | | |
| 15 | Lambda Function URL: endpoint HTTPS directo a la función (sin CDN delante) | https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html | Qué es una Function URL; que es regional | | |
| 16 | GCP: la cuenta de servicio por defecto ya no recibe rol Editor en proyectos nuevos (nuestro 403 al desplegar) | https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts | Política `iam.automaticIamGrantsForDefaultServiceAccounts` y su valor por defecto | | |

Notas para citar:
- Formato: Proveedor, "Título de la página", URL, consultado el DD-MM-2026.
- Las filas 5–7 sostienen la afirmación central de 4.1 ("crear una revisión no expone el frío al
  cliente"). Si los documentos no lo dicen textualmente, la afirmación se presenta como
  **observación propia** respaldada por los datos (24/25 primeras peticiones con contenedor ya
  despierto, `mediciones_20260921-0005_forzado.csv`), no como cita.
- La fila 16 va al anexo B (guía de despliegue), no al cuerpo.

## 2. Fuentes académicas (en `informe/referencias.bib`) — leídas completas el 21-09-2026

**Decisión: 4.1 no cita papers.** Ninguno de los tres mide Lambda, Cloud Run ni Workers reales, ni
analiza cuantitativamente los isolates V8; usarlos para "nuestros valores están en el rango
publicado" no se sostiene. La comparación entre los tres aislamientos en nubes públicas es aporte
propio (mediciones del equipo, Anexo B); los mecanismos de plataforma se citan con la documentación
oficial de la sección 1; causas y mitigaciones con literatura las desarrolla 2.2.

Qué dice cada uno, por si 2.2 o Conclusiones los necesitan:

- `ustiugov2021` (ASPLOS'21): testbed propio (vHive + Firecracker, un servidor). Descompone el
  arranque en microVM (p. 563, Fig. 2); aun con snapshots el frío es 1-2 órdenes de magnitud mayor
  que caliente (p. 564); su técnica REAP acelera 3,7× en promedio (no "un orden de magnitud").
  Única frase académica sobre Workers/V8: §8.3, p. 570 — los *language sandboxes* (Cloudflare
  Workers, V8 isolates) evitan el costo de la virtualización de hardware a cambio de aislamiento
  más débil que las VM. Cualitativa. Cloud Run no aparece.
- `golec2024` (ACM CSUR): taxonomía de causas (p. 12) y mitigaciones (pp. 18-25, Fig. 13). Sin
  tabla de latencias por plataforma. Útil: p. 17, "la CPU escala linealmente con la RAM en la
  mayoría de las plataformas" y "el cold start disminuye al aumentar la RAM". Se contradice sobre
  lenguajes interpretados vs compilados (p. 16 vs p. 17): no citar nada de Node.js desde ahí.
  No nombra SnapStart, provisioned concurrency, Cloud Run ni V8.
- `aslanpour2021` (ACSW'21): *vision paper*, sin mediciones. Solo sirve para "el arranque en frío
  es el desafío principal del serverless en el borde" (p. 6, §5.1). No menciona V8 ni Cloudflare.

## 3. Lo que NO se cita como fuente primaria

- Comparativas de un proveedor sobre su categoría (blogs "X es más rápido que Y").
- Benchmarks de terceros sin metodología publicada.
- Esta conversación ni el modelo: los hechos técnicos salen de las páginas de arriba; las cifras,
  de los CSV.

## 4. Cierre

Cuando las 16 filas tengan fecha y ✓, las que se usen en el cuerpo pasan a `referencias.bib`
como `@online` con `url`, `urldate` y `author = {{Proveedor}}` (mismo formato que `gcprun`).

## 5. Resultado de la verificación (21-09-2026)

| # | Veredicto | Clave `.bib` | Nota |
|---|---|---|---|
| 1 | Confirma | `cfWorkersLimits` | "Each isolate can consume up to 128 MB of memory". Sin opción de cambiarlo. |
| 2 | Parcial | `cfHowWorkersWorks` | Confirma que cada Worker corre en un isolate V8. **No** trata el despliegue: "un despliegue crea isolates nuevos" queda como observación propia (evidencia: `first_request` tras `wrangler deploy`). |
| 3 | Parcial | `gcrExecEnv` | Confirma gen1 = gVisor y que gen2 exige ≥512 MiB. No dice "128 MiB" textual: redactar como "gen1 admite menos de 512 MiB". |
| 4 | Confirma | `gcrMemoryLimits` | "Instances that exceed their allowed memory limit are terminated." |
| 5 | Confirma | `gcrContainerContract` | Escuchar en `$PORT`; startup probe para determinar que el contenedor arrancó. |
| 6 | Parcial | `gcrHealthchecks` | Confirma el startup probe TCP por defecto y que al pasarlo el contenedor se considera listo. La página **no** afirma que el tráfico siempre espere al probe: "no expone el frío al cliente" se presenta como observación propia (24/25). |
| 7 | Confirma | `gcrResourceModel` | Cada despliegue crea una revisión; el tráfico va a la última revisión sana; escalado a cero. |
| 8 | Parcial | `gcrCpuAllocation` + `gcrCpu` | La primera confirma CPU solo durante solicitudes. El startup CPU boost está en la segunda ("additional CPU during instance startup time and for 10 seconds after"), no en la primera. |
| 9 | Confirma | `gcrCpu` | Rango de vCPU y mínimos de memoria por vCPU. |
| 10 | Confirma | `gcpMetricsRun` | `container/startup_latencies`, "Container startup latency", DELTA DISTRIBUTION, ms (sección Cloud Run del índice P–Z, verificado en el HTML). |
| 11 | Confirma | `gcrMonitoring` | Tabla de métricas con "Container startup latency". |
| 12 | Parcial | `awsLambdaLifecycle` | Confirma Init → Invoke → Shutdown y la línea `REPORT ... Init Duration`. **No** dice que cambiar la configuración invalide los entornos: eso queda como observación propia (25/25 fríos tras cambiar `POC_MARKER`). |
| 13 | Confirma | `awsLambdaMemory` | "Lambda allocates CPU power in proportion to the amount of memory configured." 128 MB–10 240 MB. |
| 14 | Sustituida | `awsLambdaLifecycle` | La URL original (envío de logs a CloudWatch) no describe la línea REPORT; el campo `Init Duration` aparece en la página de la fila 12. Se cita esa. |
| 15 | Confirma | `awsLambdaUrls` | "A function URL is a dedicated HTTP(S) endpoint for your Lambda function." Formato regional. |
| 16 | Confirma | `gcpOrgPolicySA` | `iam.automaticIamGrantsForDefaultServiceAccounts`, aplicada por defecto en organizaciones creadas desde el 3-05-2024. |

Regla aplicada: lo que la página dice se cita; lo que solo nuestros datos muestran se escribe como
observación propia con su evidencia. No mezclar.
