# Despliegue de Google Cloud Run — PoC TI-05 (TERABYTE)

Guía paso a paso para la persona que despliega esta función con **su propia
cuenta de Google Cloud**. Sigue los comandos tal cual; al final entregas unos
pocos datos a quien ejecuta las mediciones, que las corre desde su propio
computador.

## a) Qué es esto y por qué

Es la tercera plataforma de la comparación (junto a AWS Lambda y Cloudflare
Workers) del PoC de la sección 4.1: contenedor serverless (Google Cloud Run,
gen1/gVisor). Necesitamos que quede desplegada con las mismas condiciones que
las otras dos para que la comparación sea justa. La latencia se mide
desde un único computador cliente contra la URL que tú generes; tú no necesitas
correr nada más que el despliegue.

## b) Requisitos

- Una cuenta de Google (personal o institucional).
- Un proyecto de Google Cloud con **facturación habilitada** (obligatorio
  para usar Cloud Run, aunque toda la prueba cae dentro de la capa gratuita;
  `--max-instances 1` limita el costo a una sola instancia).
- `gcloud` CLI instalada (https://docs.cloud.google.com/sdk/docs/install).
- Autenticar e inicializar: `gcloud init` (elige el proyecto con facturación
  activa).

## c) Habilitar APIs

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
```

## d) Desplegar

Desde esta carpeta (`poc/functions/cloudrun/`):

```bash
gcloud run deploy poc-ti05-terabyte \
  --source . \
  --region us-east4 \
  --allow-unauthenticated \
  --execution-environment gen1 \
  --memory 256Mi \
  --cpu 1 \
  --no-cpu-boost \
  --cpu-throttling \
  --min-instances 0 \
  --max-instances 1 \
  --concurrency 1 \
  --set-env-vars POC_MARKER=0,POC_MEMORY_MB=256,POC_SALIR_HABILITADO=1
```

`--source .` construye la imagen con buildpacks de Google Cloud (no hay
Dockerfile); usa el Node.js indicado en `engines.node` de `package.json`
(24.x.x). La primera vez puede tardar unos minutos.

| Flag | Por qué |
|---|---|
| `--execution-environment gen1` | gen1 usa gVisor: es el modelo de contenedor que describe el informe (Cloud Run también ofrece gen2, basado en microVM, que no corresponde a esta comparación). Es además la generación cuyo mínimo real es 128 MiB. Por defecto Cloud Run elige el entorno según las funciones usadas, así que se fija explícitamente. |
| `--memory 256Mi` | 128 MiB (el mínimo de gen1, igual que Lambda) resultó insuficiente para Node.js 24: los logs del servicio reportaban `Memory limit of 128 MiB exceeded with 128-158 MiB used` y el contenedor moría entre peticiones, contaminando la clasificación de peticiones calientes (verificado 20-09-2026). Se sube a 256 MiB, la siguiente escala disponible; Cloudflare Workers queda en 128 MB porque ese límite es fijo y no configurable (developers.cloudflare.com/workers/platform/limits), y Lambda se deja en 128 MB. La diferencia se declara como limitación y como hallazgo (el modelo de contenedor arrastra más memoria base que el microVM de Lambda). |
| `--cpu 1` | 1 vCPU, el valor por defecto; se deja explícito para que quede documentado. |
| `--no-cpu-boost` | mide el arranque en frío sin mitigación; el CPU boost existe para reducir la latencia percibida del arranque, y esa mitigación es tema de la sección 2.2, no de esta línea base. |
| `--cpu-throttling` | la CPU se limita cuando el contenedor no está sirviendo solicitudes, igual que el modelo de facturación por solicitud de las otras dos plataformas. |
| `--min-instances 0` | si no puede escalar a cero no hay arranque en frío que medir. |
| `--max-instances 1` y `--concurrency 1` | las 5 peticiones calientes de cada ciclo caen todas en la misma instancia, así el clasificador por `instance_id` queda limpio (sin ambigüedad de qué instancia respondió). |
| `POC_MARKER` | variable documentada por compatibilidad con el mecanismo `gcloud_env` (no usado; ver más abajo). |
| `POC_MEMORY_MB` | Cloud Run no expone la memoria asignada por variable de entorno propia; se pasa a mano para que la función pueda reportarla en el JSON. |
| `POC_SALIR_HABILITADO` | habilita el endpoint `GET /salir` (instrumentación de la PoC): si no está en `1`, `/salir` responde 404 y el servicio funciona igual que sin la variable. Es el mecanismo de forzado usado (`metodo_forzado: "cloudrun_salir"`). |

### Si el despliegue falla con 403 (storage.objects.get)

`gcloud run deploy --source .` puede fallar con un HTTP 403 del tipo
`721441032849-compute@developer.gserviceaccount.com does not have
storage.objects.get access` sobre el bucket `run-sources` del proyecto.
Causa: en proyectos de Google Cloud nuevos, la cuenta de servicio de
Compute por defecto ya no recibe el rol Editor automáticamente y puede
quedar sin ningún rol asignado. Cloud Build usa esa cuenta para leer el
código fuente que sube el despliegue, así que sin un rol que incluya
`storage.objects.get` no puede completar el build. Solución (una vez por
proyecto, reemplazando `PROJECT_ID` y `PROJECT_NUMBER`):

```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
  --role=roles/cloudbuild.builds.builder
```

Y volver a correr el `gcloud run deploy` del punto d).

## e) Verificar

Al terminar, `gcloud` imprime la URL del servicio. Pruébala dos veces:

```bash
curl -s <URL>
curl -s <URL>
```

Se espera: el mismo `instance_id` en ambas respuestas, el segundo `uptime_ms`
mayor que el primero, `region` igual a `"us-east4"` y `node_version`
empezando con `"v24"`.

## f) Registrar el despliegue

Completa esta tabla y entrégala junto con los datos del punto h):

| Fecha/hora | Región | Memoria | Generación | node_version | URL | PROJECT_ID |
|---|---|---|---|---|---|---|
| | us-east4 | 256 MiB | gen1 | (del JSON de respuesta) | | |

Para confirmar imagen y revisión activa:

```bash
gcloud run services describe poc-ti05-terabyte --region us-east4 \
  --format 'value(status.url,status.latestReadyRevisionName)'
```

## g) Dar acceso a quien ejecuta las mediciones (solo si otra persona ejecuta las mediciones)

Reemplaza `PROJECT_ID` por el id de tu proyecto y `CUENTA_MEDICIONES` por la
cuenta de Google de quien ejecuta las mediciones (pídesela directamente; no
está en el repositorio):

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/run.admin
```
Por qué: puede actualizar la revisión (método `gcloud_env`, documentado pero no usado) y leer la configuración del servicio. Con `cloudrun_salir` el forzado es un `GET /salir` público y no requiere ningún rol.

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/iam.serviceAccountUser
```
Por qué: para actualizar el servicio necesita poder actuar como la identidad de servicio de Cloud Run.

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/serviceusage.serviceUsageConsumer
```
Por qué: para poder usar las APIs habilitadas del proyecto (Cloud Run, etc.).

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/logging.viewer
```
Por qué: para leer los logs de solicitud (cruce por trace id, `logs_cloudrun.py`).

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/monitoring.viewer
```
Por qué: para poder revisar la métrica integrada "Container startup latency" si hace falta.

## h) Datos a entregar

- URL del servicio.
- `PROJECT_ID`.
- Región: `us-east4`.
- Fecha/hora del despliegue.

## i) Reglas durante las mediciones

- No abrir la URL en el navegador.
- No cambiar la configuración del servicio.
- No volver a desplegar.
- No llamar a `/salir` a mano.

## j) Al terminar el trabajo

```bash
gcloud run services delete poc-ti05-terabyte --region us-east4
```

Y quitar los bindings de IAM otorgados en el punto g) (mismo comando,
cambiando `add-iam-policy-binding` por `remove-iam-policy-binding`, una vez
por rol).

---

## Qué mide y qué no mide el forzado en Cloud Run

Forzar una revisión nueva (`gcloud run services update --update-env-vars
POC_MARKER=n`, mecanismo `gcloud_env`, documentado pero no usado) NO produce
un arranque en frío visible para el cliente en Cloud Run, a diferencia de
Lambda. La causa es el ciclo de vida de Cloud Run: la plataforma no enruta
tráfico a una revisión nueva hasta validarla, y para validarla ya arrancó un
contenedor y le hizo un health check; cuando el comando `gcloud run services
update` retorna, ese contenedor ya tiene entre 1,2 y 2,5 s de vida, así que
la primera petición del cliente llega caliente (verificado el 20-09-2026: 0
de 8 ciclos forzados resultaron fríos desde el cliente, y 1/25 en la corrida
del 21-09, ese único caso por una petición encolada durante el cambio de
revisión). El arranque sí ocurrió; solo que el cliente nunca lo paga.

Por eso la PoC usa como método de forzado `cloudrun_salir` (`GET /salir`, ver
`index.js`): el servicio responde `{"platform":"google-cloud-run",
"instance_id":..., "saliendo":true}` y a continuación cierra el servidor y
termina el proceso (`server.close()` + `process.exit(0)`). Con
`--min-instances 0` Cloud Run no arranca otra instancia hasta que llega una
petición nueva, así que la siguiente petición medida es la que crea el
contenedor y paga el arranque completo. Verificado el 21-09-2026: 3/3 ciclos
forzados con `/salir` dieron frío desde el cliente (1708 / 1797 / 1711 ms,
edad del contenedor al responder entre 78 y 121 ms), contra ~200 ms en
caliente sobre la misma instancia; Cloud Run no reinició el contenedor por su
cuenta durante la ventana medida. Es instrumentación de la PoC, no
comportamiento de producción: el endpoint solo existe para poder dejar el
servicio en cero instancias a voluntad, y solo queda activo si el despliegue
define `POC_SALIR_HABILITADO=1` (ver tabla de flags más arriba).

`medir.py` sigue clasificando el resultado con el criterio
`uptime_menor_que_latencia` (frío solo si la edad del contenedor al responder
es menor que la latencia medida de esa misma petición), que es el criterio
correcto independientemente del método de forzado.

Como cruce del lado del proveedor, `scripts/startup_cloudrun.py` sigue
siendo válido: lee la métrica de Cloud Monitoring
`run.googleapis.com/container/startup_latencies` y escribe
`results/cloudrun_startup.csv` con la media exacta y percentiles
aproximados por bucket para la ventana de la corrida.

## Para quien ejecuta las mediciones

1. Instalar `gcloud` CLI dentro de WSL (repositorio apt de Debian/Ubuntu según
   la guía oficial): https://docs.cloud.google.com/sdk/docs/install
2. `gcloud auth login`
3. `gcloud config set project PROJECT_ID` (el entregado en el punto h).
4. `gcloud config set run/region us-east4`
5. Verificación rápida:
   ```bash
   gcloud run services describe poc-ti05-terabyte --format 'value(status.url)'
   ```
6. Completar en `poc/config.json` la entrada `google-cloud-run`: `url` (la URL
   real) y `gcloud_project` (el `PROJECT_ID`).
7. Prueba de humo (borrar el CSV después):
   ```bash
   python3 scripts/medir.py --forzado 1 --csv data/smoke_cloudrun.csv
   ```
8. Corrida real: `python3 scripts/medir.py --forzado 25`.
