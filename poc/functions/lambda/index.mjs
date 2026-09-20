// PoC TI-05 · TERABYTE · Función de prueba para AWS Lambda (Node.js 24, ESM)
//
// Mismo cuerpo que worker.js: identificador de instancia generado al cargar
// el módulo (fuera del handler), hora del servidor y uptime. Expuesta por
// Lambda Function URL (auth NONE) para poder invocarla por HTTP.

import { randomUUID } from "node:crypto";

const INSTANCE_ID = randomUUID();
const STARTED_AT = Date.now();

export const handler = async (event) => {
  const now = Date.now();
  const body = {
    platform: "aws-lambda",
    instance_id: INSTANCE_ID,
    server_time: new Date(now).toISOString(),
    uptime_ms: now - STARTED_AT,
    // Útil para cruzar con la línea REPORT de CloudWatch (Init Duration).
    request_id: event?.requestContext?.requestId ?? null,
    region: process.env.AWS_REGION ?? null,
    memory_mb: process.env.AWS_LAMBDA_FUNCTION_MEMORY_SIZE ?? null,
  };
  return {
    statusCode: 200,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
    body: JSON.stringify(body),
  };
};
