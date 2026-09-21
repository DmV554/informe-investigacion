# Fuentes de la sección 4.1 — lista de verificación

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

## 2. Fuentes académicas (ya en `informe/referencias.bib`)

Los DOI abren en el navegador (a `curl` le responden 403). Leer al menos el resumen, la
introducción y la sección donde esté el dato que se cita; anotar página o figura.

### `ustiugov2021` — el de ASPLOS'21

Ustiugov, Petrov, Kogias, Bugnion, Grot. *Benchmarking, Analysis, and Optimization of
Serverless Function Snapshots.* ASPLOS '21, pp. 559–572. https://doi.org/10.1145/3445814.3446714

- Para qué sirve: es el paper que descompone el arranque en frío de una función en **microVM
  (Firecracker)**, mide dónde se va el tiempo y propone snapshots para acortarlo. Sostiene la
  explicación de por qué Lambda paga ~400 ms y de qué es una "mitigación por instantánea" (lo
  que la ficha llama "instantáneas"; en AWS, SnapStart).
- Qué buscar: la descomposición del arranque en frío (creación de la microVM, carga del runtime,
  inicialización de la función) y las latencias que reportan antes y después de sus
  optimizaciones. Cita solo las cifras que leas ahí, con número de figura o tabla.
- Cómo citarlo en 4.1: como marco para interpretar la columna de Lambda ("consistente con la
  descomposición del arranque de microVM reportada por Ustiugov et al."). No para comparar
  proveedores entre sí.

### `golec2024` — revisión sistemática

Golec et al. *Cold Start Latency in Serverless Computing: A Systematic Review, Taxonomy, and
Future Directions.* ACM Computing Surveys 57(3), 2024. https://doi.org/10.1145/3700875

- Para qué sirve: taxonomía de causas y mitigaciones del cold start y órdenes de magnitud
  reportados en la literatura. Es la referencia natural para decir "nuestros valores están en el
  rango publicado".
- Qué buscar: la tabla o sección con latencias de cold start por plataforma/runtime y la
  clasificación de mitigaciones (pre-warming, snapshots, runtimes livianos).

### `aslanpour2021` — edge

Aslanpour et al. *Serverless Edge Computing: Vision and Challenges.* ACSW '21.
https://doi.org/10.1145/3437378.3444367

- Para qué sirve: sostiene la afirmación de que el aislamiento V8 (isolates) tiene arranque
  del orden de milisegundos, que es lo que explica la penalización ≈0 de Workers.
- Qué buscar: la discusión de isolates/V8 frente a contenedores y microVM en el borde.

## 3. Lo que NO se cita como fuente primaria

- Comparativas de un proveedor sobre su categoría (blogs "X es más rápido que Y").
- Benchmarks de terceros sin metodología publicada.
- Esta conversación ni el modelo: los hechos técnicos salen de las páginas de arriba; las cifras,
  de los CSV.

## 4. Cierre

Cuando las 16 filas tengan fecha y ✓, las que se usen en el cuerpo pasan a `referencias.bib`
como `@online` con `url`, `urldate` y `author = {{Proveedor}}` (mismo formato que `gcprun`).
