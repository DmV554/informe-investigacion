# PoC TI-05 · TERABYTE · Arranque en frío y latencia en serverless

Prueba de concepto de la sección 4.1 del informe (ICI-5444, Trabajo de Investigación 2026).
Mide, desde un cliente en Chile, la latencia de una función trivial idéntica desplegada en
tres modelos de ejecución serverless, distinguiendo arranque en frío y caliente.

## Estructura

```
poc/
├── README.md               este archivo
├── DESPLIEGUE.md           pasos seguidos para desplegar cada función (consola/CLI)
├── config.json             URLs, región, memoria, runtime de cada plataforma
├── functions/
│   ├── cloudflare/worker.js    función desplegada en Cloudflare Workers (V8 isolate)
│   ├── lambda/index.mjs        función desplegada en AWS Lambda (Node.js 24.x, us-east-1)
│   └── cloudrun/               función para Google Cloud Run + README de despliegue
├── scripts/
│   ├── medir.py            medición: invoca, cronometra, clasifica frío/caliente, CSV
│   ├── logs_lambda.py      baja las líneas REPORT de CloudWatch y las cruza por RequestId
│   ├── logs_cloudrun.py    (opcional) baja logs de solicitud de Cloud Run y cruza por trace id
│   └── analizar.py         p50/p95 por plataforma×modo×estado, filas LaTeX, gráfico
├── data/                   datos crudos: un CSV por corrida, mediciones_<fecha-hora>_<modo>.csv — NO editar a mano
└── results/                resumen.csv, resumen_latex.txt, poc-coldstart.png
```

## Qué hace cada función desplegada

Responde un JSON con `instance_id` (fijado una vez por instancia), `server_time`,
`uptime_ms` (tiempo que lleva viva la instancia) y, según plataforma, `first_request`,
`colo` (Workers) o `request_id`, `region`, `memory_mb` (Lambda). La función **no mide
nada**: solo se deja identificar. La latencia se mide desde el cliente.

## Metodología (resumen; el detalle va en el informe)

- **Métrica principal:** latencia total de la petición HTTP medida en el cliente (ms).
- **Clasificación frío/caliente (por plataforma, `criterio_frio` en config.json):**
  - *Lambda* (`instance_id`): frío si la instancia que responde es distinta a la anterior
    de la corrida. Las peticiones secuenciales reutilizan el mismo entorno de ejecución,
    así que un id nuevo implica un arranque. En la primera invocación decide `uptime_ms` bajo.
  - *Workers* (`first_request`): frío solo si la propia instancia declara que esa petición
    la inicializó. Hallazgo de la prueba piloto: Cloudflare reparte peticiones consecutivas
    entre varios isolates vivos del mismo PoP (GIG), por lo que el `instance_id` cambia sin
    que haya arranque; el cambio de id se registra como informativo `(otro_isolate)`.
  - El criterio aplicado queda en la columna `criterio_frio` de cada fila.
- **Cliente:** cada petición abre conexión TCP/TLS nueva (sin keep-alive), como un cliente
  que llega por primera vez; la latencia caliente incluye por tanto el handshake
  (Chile → us-east-1 ≈ 385 ms; Chile → GIG ≈ 205 ms). El DNS se resuelve una vez antes de
  medir para que la primera petición no lo incluya.
- **Protocolo natural:** espera de inactividad → 1 invocación (candidata a fría) →
  5 calientes → repetir. Aplica a todas las plataformas.
- **Protocolo forzado:** provocar un entorno de ejecución nuevo → 1 invocación → 5
  calientes → repetir, sin esperas. Solo plataformas con `forzable: true`; el mecanismo
  exacto queda en `metodo_forzado` (`config.json`): `lambda_env` (cambia `POC_MARKER` de
  la Lambda), `wrangler_deploy` (`npx wrangler deploy` publica una versión nueva del
  Worker) o `gcloud_env` (`gcloud run services update --update-env-vars` cambia
  `POC_MARKER` del servicio de Cloud Run). Los tres son despliegues/actualizaciones
  reales, no un mecanismo artificial. Las plataformas no forzables (ninguna hoy) se
  medirían igual en cada ciclo para tener muestras en la misma ventana.
- **Validación con dato del proveedor:** `Init Duration` de la línea REPORT de CloudWatch
  (Lambda), cruzado por `RequestId`. Workers no expone dato de inicialización.
- **Igualdad de condiciones:** misma lógica de función, JavaScript en ambas, memoria por
  defecto/mínima, mismo cliente, misma red, misma ventana horaria. Workers es global
  (ver `colo`) y corre en V8 sin Node.js: diferencias inherentes al modelo, declaradas.

## Reproducir con cuentas propias

Nada del repositorio está atado a una cuenta concreta: las credenciales viven en las CLI
de cada proveedor (`aws configure`, `npx wrangler login`, `gcloud auth login`) y las URLs
en `config.json`. Para repetir la prueba desde cero:

1. Desplegar las tres funciones con tus cuentas siguiendo `DESPLIEGUE.md` (Lambda y
   Workers) y `functions/cloudrun/README.md` (Cloud Run). Todas caben en el free tier.
2. Pegar en `config.json` la `url` de cada plataforma y, en Cloud Run, el `gcloud_project`.
   Si cambias nombre de función, región o log group, actualízalos ahí mismo.
3. Autenticar las CLI en el computador que va a medir (las tres, si vas a usar el modo
   forzado). Si `aws` o `gcloud` no están en el PATH, apúntalos con `POC_AWS_CLI` o
   `POC_GCLOUD_CLI`.
4. `npm install` (instala wrangler) y correr los comandos de la sección siguiente.

Las mediciones de `data/` y `results/` son las de este equipo; una corrida nueva crea sus
propios archivos y no las sobreescribe.

## Cómo correr

Requisitos: Python 3.8+ (sin dependencias para medir; `pip install matplotlib` para el
gráfico), AWS CLI v2 configurada (`aws configure`, región us-east-1) para forzado y logs
de Lambda, Wrangler autenticado (`npx wrangler login`) para forzar Workers, y gcloud CLI
autenticada (`gcloud auth login`, `gcloud config set project`) para forzado y logs de
Cloud Run.

```bash
# 1. Prueba corta de verificación (~3 min): 1 ciclo natural (1 min) + 2 forzados
python scripts/medir.py --prueba

# 2. Corrida forzada (~10-15 min)
python scripts/medir.py --forzado 20

# 3. Corrida natural (elegir N y espera según tiempo disponible)
python scripts/medir.py --natural 6 --espera 15      # ~1 h 30
python scripts/medir.py --natural 4 --espera 10      # ~40 min

# 4. Bajar REPORT de CloudWatch y cruzar (esperar ~1 min tras terminar de medir).
#    Lee todos los data/mediciones_*.csv por defecto.
python scripts/logs_lambda.py

# 4b. (Opcional, si Cloud Run está desplegado) cruce equivalente con los logs
#     de solicitud de Cloud Run, requiere roles/logging.viewer.
python scripts/logs_cloudrun.py

# 5. Resumen, filas LaTeX y gráfico. Lee todos los data/mediciones_*.csv por defecto;
#    con --csv se eligen archivos concretos (acepta comodines).
python scripts/analizar.py
python scripts/analizar.py --csv data/mediciones_2026*_forzado.csv
```

Durante una corrida **nadie debe abrir las URLs** en el navegador: cualquier petición
externa despierta instancias y contamina la clasificación.

`Ctrl+C` interrumpe sin perder datos: cada fila se escribe al CSV al momento.

Cada corrida crea su propio archivo (`data/mediciones_YYYYMMDD-HHMM_<modo>.csv`), así
nunca se sobreescribe ni se mezcla una corrida con otra. Los archivos de pruebas piloto
que no deban entrar al análisis se nombran sin el prefijo `mediciones_` (p. ej.
`prueba_piloto_*.csv`).

## Estado y decisiones (19-09-2026)

- Medido: AWS Lambda y Cloudflare Workers. Cloud Run pendiente; si se despliega, se repite la corrida forzada
  con las tres plataformas a la vez (`--forzado 25`) y esa pasa a ser la fuente del gráfico. Los datos del
  19-09 quedan como corrida previa.
- En el cuerpo del informe va **solo la corrida forzada** (un gráfico, una tabla), con el frío inducido por un
  despliegue real en cada plataforma (`metodo_forzado`). Los fríos naturales se citan en una frase como validación.
  Se reportan dos métricas: latencia total percibida desde el cliente y penalización de arranque
  (p50 frío − p50 caliente por plataforma), que cancela la red.
- Resultados actuales (`data/mediciones_20260919-2148_forzado.csv`, 25 ciclos, 150 peticiones por plataforma,
  cliente en Chile): Lambda frío p50 754 / p95 826 ms, caliente p50 434 / p95 487 ms (n=25/125), penalización
  +320 ms; Workers frío p50 231 / p95 244 ms, caliente p50 231 / p95 252 ms (n=82/68), penalización ≈0 ms
  (el arranque se detecta con `first_request` pero el cliente no lo percibe). Cruce con CloudWatch 150/150,
  Init Duration mediana 148 ms. La corrida de las 19:29 (Workers sin forzar, n=1 frío) queda como corrida previa.
  Detalle en `results/resumen.csv`.

## Registro de despliegue (completar)

| Plataforma | Fecha/hora despliegue | Región | Memoria | Runtime exacto | Plan |
|---|---|---|---|---|---|
| Cloudflare Workers | 19-09-2026 ~17:20 | global (colo observado desde Chile: GIG, Río de Janeiro) | 128 MB | V8 isolate | Free |
| AWS Lambda | 19-09-2026 ~19:10 | us-east-1 | 128 MB (usa ~82 MB) | Node.js 24.x (verificado 19-09-2026 con `aws lambda get-function-configuration`) | Free tier |
| Google Cloud Run | pendiente (ver `functions/cloudrun/README.md`) | us-east4 | 128 MiB | Node.js 24 (gen1/gVisor) | Free tier |

## Columnas de los CSV de mediciones

`plataforma, modo, ciclo, n_en_ciclo, timestamp_local, latencia_ms, http_status,
instance_id, first_request, uptime_ms, colo, request_id, es_frio, criterio_frio, error`

## Limitaciones conocidas (para la sección de limitaciones del informe)

Un solo cliente y red (Chile); función trivial; un día de medición; free tier; Workers
sin región fija; latencia desde el cliente incluye red; frío forzado por redespliegue
puede diferir del frío natural (por eso se miden ambos).
