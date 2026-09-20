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
  --memory 128Mi \
  --cpu 1 \
  --no-cpu-boost \
  --cpu-throttling \
  --min-instances 0 \
  --max-instances 1 \
  --concurrency 1 \
  --set-env-vars POC_MARKER=0,POC_MEMORY_MB=128
```

`--source .` construye la imagen con buildpacks de Google Cloud (no hay
Dockerfile); usa el Node.js indicado en `engines.node` de `package.json`
(24.x.x). La primera vez puede tardar unos minutos.

| Flag | Por qué |
|---|---|
| `--execution-environment gen1` | gen1 es la única que permite 128 MiB y usa gVisor: es el modelo de contenedor que describe el informe. Por defecto Cloud Run elige el entorno según las funciones usadas, así que se fija explícitamente. |
| `--memory 128Mi` | memoria mínima real de gen1, igual que Lambda (128 MB). |
| `--cpu 1` | 1 vCPU, el valor por defecto; se deja explícito para que quede documentado. |
| `--no-cpu-boost` | mide el arranque en frío sin mitigación; el CPU boost existe para reducir la latencia percibida del arranque, y esa mitigación es tema de la sección 2.2, no de esta línea base. |
| `--cpu-throttling` | la CPU se limita cuando el contenedor no está sirviendo solicitudes, igual que el modelo de facturación por solicitud de las otras dos plataformas. |
| `--min-instances 0` | si no puede escalar a cero no hay arranque en frío que medir. |
| `--max-instances 1` y `--concurrency 1` | las 5 peticiones calientes de cada ciclo caen todas en la misma instancia, así el clasificador por `instance_id` queda limpio (sin ambigüedad de qué instancia respondió). |
| `POC_MARKER` | la variable que el script de medición (`medir.py`) cambia para forzar una revisión (y una instancia) nueva. |
| `POC_MEMORY_MB` | Cloud Run no expone la memoria asignada por variable de entorno propia; se pasa a mano para que la función pueda reportarla en el JSON. |

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
| | us-east4 | 128 MiB | gen1 | (del JSON de respuesta) | | |

Para confirmar imagen y revisión activa:

```bash
gcloud run services describe poc-ti05-terabyte --region us-east4 \
  --format 'value(status.url,status.latestReadyRevisionName)'
```

## g) Dar acceso a quien ejecuta las mediciones

Reemplaza `PROJECT_ID` por el id de tu proyecto y `CUENTA_MEDICIONES` por la
cuenta de Google de quien ejecuta las mediciones (pídesela directamente; no
está en el repositorio):

```bash
gcloud projects add-iam-policy-binding PROJECT_ID --member=user:CUENTA_MEDICIONES --role=roles/run.admin
```
Por qué: puede actualizar la revisión (forzar frío cambiando `POC_MARKER`).

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

## j) Al terminar el trabajo

```bash
gcloud run services delete poc-ti05-terabyte --region us-east4
```

Y quitar los bindings de IAM otorgados en el punto g) (mismo comando,
cambiando `add-iam-policy-binding` por `remove-iam-policy-binding`, una vez
por rol).

---

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
