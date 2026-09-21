// PoC TI-05 · TERABYTE · Función de prueba para Cloudflare Workers
//
// Qué hace: responde un JSON con un identificador de instancia (isolate),
// la hora del servidor y cuántos ms lleva viva la instancia. Workers no
// permite generar aleatorios ni leer el reloj en el ámbito global, así que
// el identificador se fija en la PRIMERA petición que atiende el isolate y
// se reutiliza en las siguientes; cambia solo cuando hay un isolate nuevo.
// La función no mide nada; la medición se hace desde el cliente (medir.py).

let INSTANCE_ID = null;
let STARTED_AT = null;

export default {
  async fetch(request) {
    const now = Date.now();
    const firstRequest = INSTANCE_ID === null;
    if (firstRequest) {
      INSTANCE_ID = crypto.randomUUID();
      STARTED_AT = now;
    }
    const body = {
      platform: "cloudflare-workers",
      instance_id: INSTANCE_ID,
      first_request: firstRequest,          // true => esta petición inicializó la instancia
      server_time: new Date(now).toISOString(),
      uptime_ms: now - STARTED_AT,
      // Centro de datos que atendió la petición: un instance_id nuevo puede
      // deberse a otra ubicación y no a un cold start; colo permite distinguirlo.
      colo: request.cf ? request.cf.colo : null,
    };
    return new Response(JSON.stringify(body), {
      headers: { "content-type": "application/json", "cache-control": "no-store" },
    });
  },
};
