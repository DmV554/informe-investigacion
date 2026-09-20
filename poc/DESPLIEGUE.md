# PoC TI-05 · Despliegue de las funciones de prueba

Registrar SIEMPRE al desplegar: fecha y hora, región, memoria, runtime/versión. Va en la metodología.

## Cloudflare Workers

### Opción A: con wrangler (recomendada para reproducir)

`wrangler.jsonc` ya define nombre (`poc-ti05-terabyte`) y código (`functions/cloudflare/worker.js`);
no contiene `account_id`: usa la cuenta con la que hagas login.

```bash
npm install
npx wrangler login      # abre el navegador una vez
npx wrangler deploy     # crea el Worker si no existe e imprime la URL
```

Pegar la URL (`https://poc-ti05-terabyte.<tu-subdominio>.workers.dev/`) en `config.json` y anotar
fecha/hora, plan Free, memoria 128 MB, CPU 10 ms/petición.

### Opción B: editor web, sin wrangler

1. Dashboard → Workers & Pages → Create → **Start with Hello World!**
2. Nombre sugerido: `poc-ti05-terabyte`. Deploy (crea el worker con el hello world).
3. Botón **Edit code**. Borrar todo y pegar el contenido de `functions/cloudflare/worker.js`. **Deploy**.
4. Copiar la URL `https://poc-ti05-terabyte.<tu-subdominio>.workers.dev`.
5. Probar en el navegador: debe devolver JSON con `instance_id`, `uptime_ms`, `colo`.
   Recargar varias veces: el `instance_id` debería repetirse (misma instancia) y `uptime_ms` crecer.
6. Anotar: fecha/hora, plan Free, memoria 128 MB (límite del plan), CPU 10 ms/petición (plan Free).

### Forzado de arranque en frío (verificado 19-09-2026)

`wrangler.jsonc` (raíz de la PoC) apunta al mismo Worker creado desde el
panel. `npx wrangler deploy` publica una versión nueva del script (aunque el
código no cambie); la siguiente petición en cada máquina del PoP arranca un
isolate nuevo, y la función lo reporta con `first_request=true`. Requiere
`npx wrangler login` una vez. `medir.py` lo usa en modo forzado
(`metodo_forzado: "wrangler_deploy"` en `config.json`).

## AWS Lambda (consola web)

1. Consola → Lambda → **Create function** → Author from scratch.
   - Nombre: `poc-ti05-terabyte`
   - Runtime: **Node.js 24.x** (verificado con `aws lambda get-function-configuration`
     el 19-09-2026; corregir si la consola ofrece otra versión al momento de crear)
   - Arquitectura: x86_64
   - Región (arriba a la derecha): **us-east-1 (N. Virginia)**
2. Create function. En el editor, reemplazar el contenido de `index.mjs` por el archivo `functions/lambda/index.mjs`. **Deploy**.
3. Configuration → **General configuration** → Edit: Memory **128 MB**, Timeout 10 s. Save.
4. Configuration → **Function URL** → Create function URL → Auth type **NONE** → Save.
   Copiar la URL `https://xxxxx.lambda-url.us-east-1.on.aws/`.
5. Probar en el navegador: JSON con `instance_id`, `uptime_ms`, `request_id`, `region`, `memory_mb`.
6. Configuration → **Environment variables** → Add: `POC_MARKER` = `0`.
   (Es la variable que el script cambia para forzar arranques en frío.)
7. Anotar: fecha/hora, región, memoria, runtime exacto.

### Para el modo forzado y los logs (AWS CLI en tu PC)

- Instalar AWS CLI v2 y ejecutar `aws configure` con una access key (IAM → Users → tu usuario → Security credentials → Create access key). Región por defecto `us-east-1`.
- Verificar: `aws lambda get-function-configuration --function-name poc-ti05-terabyte`
- Forzar frío (lo hace el script): `aws lambda update-function-configuration --function-name poc-ti05-terabyte --environment "Variables={POC_MARKER=<n>}"`
- Logs REPORT (lo hace `logs_lambda.py`): grupo `/aws/lambda/poc-ti05-terabyte`.

## Google Cloud Run

Guía completa para quien despliega (cuenta propia de Google Cloud):
`functions/cloudrun/README.md`. Resumen de los flags de paridad usados en
`gcloud run deploy` (región `us-east4`, memoria mínima real 128 MiB):

| Flag | Qué fija |
|---|---|
| `--execution-environment gen1` | contenedor con gVisor (el modelo que compara el informe) |
| `--memory 128Mi` / `--cpu 1` | memoria mínima real de gen1 / 1 vCPU (default) |
| `--no-cpu-boost` | mide el arranque en frío sin la mitigación de CPU extra al inicio |
| `--cpu-throttling` | CPU limitada fuera de las solicitudes, como el resto de las plataformas |
| `--min-instances 0` | permite escalar a cero (condición para que haya arranque en frío) |
| `--max-instances 1` / `--concurrency 1` | todas las peticiones calientes de un ciclo caen en la misma instancia |

Forzado de arranque en frío: `medir.py` cambia `POC_MARKER` con
`gcloud run services update ... --update-env-vars` (cualquier cambio de
configuración crea una revisión nueva, análogo a `lambda_env` en Lambda).

## Igualdad de condiciones

- Misma lógica de función en las tres (id de instancia al cargar, hora, uptime).
- JavaScript en las tres. Node.js en Lambda y Cloud Run; V8 directo en Workers (diferencia inherente al modelo edge, se declara).
- Memoria por defecto / mínima de cada plataforma, anotada.
- Misma región en AWS y Google; Workers es global (se declara).
- Mismo cliente, misma red, misma ventana horaria para la medición.
