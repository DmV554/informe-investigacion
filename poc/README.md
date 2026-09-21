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
  - *Cloud Run* (`uptime_menor_que_latencia`): frío solo si el contenedor nació dentro de la
    ventana de la petición, es decir, si su edad al responder (`uptime_ms`) es menor que la
    latencia medida de extremo a extremo. El cambio de `instance_id` no basta: la plataforma
    puede tener un contenedor ya despierto (health check de una revisión nueva, o reemplazo
    proactivo tras `/salir`) que responde sin que el cliente pague ningún arranque. Esas
    primeras peticiones no frías se separan en el estado `forzado-sin-frio` del resumen.
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
  Worker) o `cloudrun_salir` (Cloud Run, ver más abajo). Los mecanismos difieren
  porque cada plataforma tiene un ciclo de vida distinto; lo que se busca en las
  tres es el mismo estado de partida: ninguna instancia caliente cuando llega la
  petición medida (escalado a cero).
  **Cloud Run:** cambiar la configuración del servicio (`gcloud_env`, `gcloud run
  services update --update-env-vars`) no sirve para eso, porque la plataforma no
  enruta tráfico a la revisión nueva hasta validarla con un health check, y ese
  health check ya arranca un contenedor; el forzado por revisión no expone un frío
  visible desde el cliente (0/8 ciclos en la verificación del 20-09-2026). Por eso
  se usa `cloudrun_salir` (`GET /salir` a la función): la función responde y termina
  el proceso, y con `min-instances 0` la plataforma queda en cero instancias hasta
  la próxima petición, que es la que paga el arranque (verificado el 21-09-2026:
  3/3 ciclos fríos desde el cliente). `/salir` es instrumentación de la propia PoC,
  no comportamiento de producción, y solo queda activa con la variable de entorno
  `POC_SALIR_HABILITADO=1` del despliegue; se declara como limitación. Se clasifica
  con el criterio `uptime_menor_que_latencia` y, como cruce, el arranque real se
  mide también del lado del proveedor con `scripts/startup_cloudrun.py` (ver
  `functions/cloudrun/README.md`).
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

## Estado y decisiones (21-09-2026)

- Medidas las tres plataformas en la misma ventana: `data/mediciones_20260921-0041_forzado.csv` (25 ciclos
  forzados, 150 peticiones por plataforma, cliente en Chile, 00:41-00:58 hora local, Cloud Run forzado con
  `/salir`). Esa corrida es la fuente del gráfico y de la tabla del informe. Quedan como evidencia
  complementaria: `mediciones_20260921-0005_forzado.csv` (misma noche, Cloud Run forzado por revisión: muestra
  que ese método no expone el frío al cliente) y `mediciones_20260919-2148_forzado.csv` (19-09, solo Lambda y
  Workers: segunda ventana de red).
- En el cuerpo del informe va **solo la corrida forzada** (un gráfico, una tabla), con el frío inducido por el
  evento del ciclo de vida propio de cada modelo (`metodo_forzado`): invalidación del entorno en Lambda,
  publicación de versión en Workers, terminación del proceso en Cloud Run. En las tres, la petición medida
  llega sin ninguna instancia caliente disponible. Se reportan dos métricas: latencia total percibida desde el
  cliente y penalización de arranque (p50 frío − p50 caliente por plataforma), que cancela la red.
- Resultados (`results/resumen.csv`, `results/resumen_latex.txt`):
  - **AWS Lambda** (128 MB): frío p50 838 / p95 890 ms, caliente p50 442 / p95 507 ms (n=25/125), penalización
    **+395 ms**. Los 25 fríos caen en la posición #0 de cada ciclo.
  - **Cloudflare Workers** (128 MB): frío p50 569 / p95 591 ms, caliente p50 567 / p95 574 ms (n=107/43),
    penalización **≈0 ms** (el arranque se detecta con `first_request` pero el cliente no lo percibe). Ventana:
    el 19-09 el caliente fue 231 ms; el 21-09 el RTT hasta el borde de Cloudflare fue ~175 ms (TCP) contra
    ~70 ms dos días antes, **con el mismo colo GIG**. Cambió la ruta del ISP, no el colo: la latencia "al
    borde" depende de la ruta hasta el borde. Dentro de una misma ventana la comparación sí es válida.
  - **Google Cloud Run** (256 MiB, gen1): frío p50 922 / p95 1.656 ms, caliente p50 203 / p95 358 ms
    (n=24/125), penalización **+720 ms**. 24 de 25 ciclos dieron frío visible desde el cliente; en 1 la
    plataforma ya había reemplazado el contenedor (`forzado-sin-frio`). El frío del cliente es disperso
    (306-1.682 ms) mientras el arranque de contenedor que registra la propia plataforma es parejo
    (`scripts/startup_cloudrun.py`, `container/startup_latencies`, ventana de la corrida: n=26, media 1.014 ms,
    p50≈1.018 / p95≈1.119 ms). Lectura: tras la salida del proceso Cloud Run empieza a reemplazar el
    contenedor por su cuenta; la petición paga la parte del arranque que falta cuando llega. Con espera 0 tras
    `/salir` la petición cae en la instancia que muere (HTTP 503); por eso la espera es de 2 s. Forzar por
    revisión nueva (`gcloud_env`, corrida de las 00:05) no expone el frío: 24/25 primeras peticiones llegaron a
    un contenedor que la plataforma ya había arrancado para validar la revisión; el arranque de esas
    revisiones medido por Google fue ~1,6-2,0 s (imagen nueva) frente a ~1,0 s al reponer la misma revisión.
  - Red: Google termina TCP/TLS en un punto de presencia en Chile (TCP 16 ms, TLS 26 ms) y reenvía por su red
    interna a us-east4; Lambda Function URL conecta directo a Virginia (TCP ~140 ms). La comparación de latencia
    total incluye la arquitectura de front-end de cada proveedor, no solo el modelo de ejecución.
  - Memoria: Cloud Run en 128 MiB no sostiene Node.js 24 (OOM, ver nota ¹ del registro de despliegue); Workers
    es fijo en 128 MB; Lambda queda en 128 MB. Diferencia declarada.
  - Limitación: `/salir` es instrumentación de la PoC (activa solo con `POC_SALIR_HABILITADO=1`), no
    comportamiento de producción; los tres mecanismos de forzado son distintos porque los tres ciclos de vida
    lo son.

## Registro de despliegue (completar)

| Plataforma | Fecha/hora despliegue | Región | Memoria | Runtime exacto | Plan |
|---|---|---|---|---|---|
| Cloudflare Workers | 19-09-2026 ~17:20 | global (colo observado desde Chile: GIG, Río de Janeiro) | 128 MB | V8 isolate | Free |
| AWS Lambda | 19-09-2026 ~19:10 | us-east-1 | 128 MB (usa ~82 MB) | Node.js 24.x (verificado 19-09-2026 con `aws lambda get-function-configuration`) | Free tier |
| Google Cloud Run | 20-09-2026 (propia cuenta, ver `functions/cloudrun/README.md`) | us-east4 | 256 MiB¹ | Node.js 24 (gen1/gVisor) | Free tier |

¹ Cloud Run gen1 en 128 MiB (el mínimo, igual que Lambda) no le alcanza a Node.js 24: el
contenedor se quedaba sin memoria y moría entre peticiones (verificado 20-09-2026). Se sube
a 256 MiB; Workers queda en 128 MB porque ese límite es fijo en el plan Free (no configurable)
y Lambda se deja en 128 MB. Diferencia declarada como limitación y como hallazgo.

## Columnas de los CSV de mediciones

`plataforma, modo, ciclo, n_en_ciclo, timestamp_local, latencia_ms, http_status,
instance_id, first_request, uptime_ms, colo, request_id, es_frio, criterio_frio, error`

## Limitaciones conocidas (para la sección de limitaciones del informe)

Un solo cliente y red (Chile); función trivial; un día de medición; free tier; Workers
sin región fija; latencia desde el cliente incluye red; frío forzado por redespliegue
puede diferir del frío natural (por eso se miden ambos).
