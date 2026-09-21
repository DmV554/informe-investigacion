// PoC TI-05 · TERABYTE · Función de prueba para Google Cloud Run (Node.js 24, ESM)
//
// Mismo cuerpo que index.mjs (Lambda) y worker.js (Workers): identificador de
// instancia generado al cargar el módulo (fuera del handler), hora del
// servidor y uptime. Servidor HTTP mínimo con node:http porque Cloud Run
// exige que el contenedor escuche en 0.0.0.0:$PORT; no hay framework de por
// medio. La función NO mide nada: la latencia se mide desde el cliente
// (medir.py). Metadata de instancia (región, id de VM) se resuelve una vez al
// arrancar, sin bloquear las respuestas: si el servidor de metadata no
// responde en 500 ms (por ejemplo, al probar en local), esos campos quedan
// en null y el servidor sigue funcionando igual.

import { createServer } from "node:http";
import { randomUUID } from "node:crypto";
import { request as httpRequest } from "node:http";

const INSTANCE_ID = randomUUID();
const STARTED_AT = Date.now();
const PORT = Number(process.env.PORT) || 8080;

const METADATA_HOST = "metadata.google.internal";
const METADATA_TIMEOUT_MS = 500;

// Metadata cacheada; se completa (o queda en null) en segundo plano al
// arrancar el proceso y no vuelve a consultarse por petición.
const metadata = { region: null, instanceId: null };

function fetchMetadata(path) {
  return new Promise((resolve) => {
    const req = httpRequest(
      {
        host: METADATA_HOST,
        path,
        headers: { "Metadata-Flavor": "Google" },
        timeout: METADATA_TIMEOUT_MS,
      },
      (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => resolve(res.statusCode === 200 ? data.trim() : null));
      }
    );
    req.on("timeout", () => req.destroy());
    req.on("error", () => resolve(null));
    req.end();
  });
}

async function cargarMetadata() {
  // El servidor de metadata devuelve la región como
  // "projects/<numero>/regions/us-east4"; solo interesa el último segmento.
  const regionCompleta = await fetchMetadata("/computeMetadata/v1/instance/region");
  metadata.region = regionCompleta ? regionCompleta.split("/").pop() : null;
  metadata.instanceId = await fetchMetadata("/computeMetadata/v1/instance/id");
}
cargarMetadata();

function extraerRequestId(headerTrace) {
  // Formato del header X-Cloud-Trace-Context: "TRACE_ID/SPAN_ID;o=1".
  if (!headerTrace) return null;
  const trace = headerTrace.split("/")[0];
  return trace || null;
}

// Instrumentación de la PoC, no comportamiento de producción: GET /salir hace
// que el proceso termine después de responder. Cloud Run ve morir la instancia
// y, con min-instances 0, no arranca otra hasta que llega una petición: la
// siguiente petición medida es la que crea el contenedor y paga el arranque.
// Es la única forma de dejar el servicio en cero instancias a voluntad, porque
// crear una revisión nueva hace que la plataforma arranque un contenedor para
// validarla (health check) antes de enrutar tráfico. Solo activo si el
// despliegue define POC_SALIR_HABILITADO=1.
const SALIR_HABILITADO = process.env.POC_SALIR_HABILITADO === "1";

const server = createServer((req, res) => {
  const now = Date.now();
  if (req.url.split("?")[0] === "/salir") {
    if (!SALIR_HABILITADO) {
      res.writeHead(404, { "content-type": "application/json" });
      res.end(JSON.stringify({ error: "salir deshabilitado" }));
      return;
    }
    res.writeHead(200, { "content-type": "application/json", "cache-control": "no-store" });
    res.end(JSON.stringify({ platform: "google-cloud-run", instance_id: INSTANCE_ID, saliendo: true }), () => {
      server.close();
      setImmediate(() => process.exit(0));
    });
    return;
  }
  const memoriaCfg = Number(process.env.POC_MEMORY_MB);
  const body = {
    platform: "google-cloud-run",
    instance_id: INSTANCE_ID,
    server_time: new Date(now).toISOString(),
    uptime_ms: now - STARTED_AT,
    request_id: extraerRequestId(req.headers["x-cloud-trace-context"]),
    region: metadata.region,
    revision: process.env.K_REVISION ?? null,
    service: process.env.K_SERVICE ?? null,
    // Cloud Run no expone la memoria asignada por variable de entorno; la
    // fija el comando de despliegue (POC_MEMORY_MB) para poder reportarla.
    memory_mb: Number.isFinite(memoriaCfg) ? memoriaCfg : null,
    node_version: process.version,
    cr_instance_id: metadata.instanceId,
  };
  res.writeHead(200, { "content-type": "application/json", "cache-control": "no-store" });
  res.end(JSON.stringify(body));
});

server.listen(PORT, "0.0.0.0");
