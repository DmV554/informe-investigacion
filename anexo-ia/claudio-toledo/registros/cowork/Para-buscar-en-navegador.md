# Lo que falta investigar · para pasarle al navegador
### Claudio · 20-09-2026

Sale de cruzar mis listas con `DatosChatsAnteriores/candidatas-C.xlsx`, las 93 fuentes que
levantó Daniel.

> **Aclaración previa:** el Excel de Daniel **no trae plataformas nuevas**. Son las mismas que
> ya tenía, pero con sus URLs oficiales de documentación, admisibilidad y fecha. Eso resulta
> más útil que candidatas nuevas, porque **cierra casi todos mis pendientes**.

---

## PRIORIDAD 1 · Puede invalidar un descarte

### Azure Front Door Edge Actions (Preview)

`https://learn.microsoft.com/en-us/azure/frontdoor/edge-actions`

**El problema:** descarté Azure Front Door por "no califica en la categoría", porque el motor
de reglas no ejecuta código del usuario. Pero Daniel encontró que existe **Edge Actions**,
en vista previa, que **sí ejecuta JavaScript en los PoP de Front Door**.

Datos que trae su nota (a confirmar en la fuente): código 16 KB, ejecución 10 ms, 3 versiones,
100 recursos por suscripción.

**Qué necesito decidir:**
1. ¿Edge Actions está en vista previa o ya es general?
2. Si está en preview, ¿un producto en vista previa califica como alternativa comparable, o
   se descarta por eso mismo?
3. Si califica, **mi descarte de Azure Front Door está mal formulado**: habría que descartar
   el motor de reglas y evaluar Edge Actions por separado.

> Ojo con el límite de **10 ms de ejecución**: es del mismo orden que el nivel básico de
> Akamai. Si los dos entran, hay que poder distinguirlos.

---

## PRIORIDAD 2 · Fuente académica que no está en las 47

### The State of FaaS: An analysis of public Functions-as-a-Service providers

`https://arxiv.org/abs/2408.03021`
Ekwe-Ekwe, Nnamdi; Amos, Lucas · IEEE CLOUD 2024 · DOI 10.1109/CLOUD62652.2024.00055

**Por qué importa:** es un paper **revisado por pares de 2024** que analiza **10 proveedores
FaaS públicos** con sus características, precios e historia. Es posterior a todos los surveys
de la planilla (Wen 2023, Hassan 2021, Li 2022) y **cubre justo el hueco** que mi análisis
detectó: ningún paper del corpus estudia los proveedores actuales.

Según la nota de Daniel, incluye Oracle Functions, Alibaba Function Compute e IBM, que son
tres de mis candidatas.

**Qué necesito:**
1. ¿Qué **10 proveedores** analiza? Lista completa. ¿Hay alguno que no esté en mis cinco listas?
2. ¿Qué **criterios de comparación** usa? Sirven para contrastar con los de Valentina.
3. ¿Qué dice de Oracle, Alibaba e IBM, con página?
4. ¿Cuenta como referencia académica? Es arXiv, pero con DOI de IEEE CLOUD: confirmar que la
   versión publicada existe y citarla por el DOI, no por arXiv.

---

## PRIORIDAD 3 · La dimensión de madurez y confianza

Daniel levantó las páginas oficiales del CNCF para los proyectos de código abierto. Eso
resuelve el campo de "qué tan maduro es" con **fuente preferente**, en vez de impresiones.

| Proyecto | Página CNCF |
|---|---|
| Knative | `cncf.io/projects/knative/` |
| KEDA | `cncf.io/projects/keda/` |
| Spin / SpinKube | `cncf.io/projects/` |
| wasmCloud | `cncf.io/projects/wasmcloud/` |
| WasmEdge | `cncf.io/projects/wasmedge-runtime/` |

**Qué necesito:** el **nivel de madurez de cada uno** (Sandbox / Incubating / Graduated) y la
fecha en que lo alcanzó.

**Y lo que falta, que es lo que más me sirve:** ¿**Fission** y **Nuclio** están en el CNCF
Landscape? ¿En qué categoría y con qué nivel? Son mis dos elegidas de código abierto y no
tengo su estado de madurez, mientras que cuatro de las seis de la ficha sí lo tienen.

Si no están en la CNCF, eso también es dato: sería una diferencia de gobernanza frente a
Knative, KEDA, Spin y wasmCloud.

---

## PRIORIDAD 4 · Firestore, mi única candidata sin verificar

`https://firebase.google.com/docs/firestore`
`https://cloud.google.com/firestore/pricing`
`https://cloud.google.com/firestore/docs/quotas`

Es la única de mis cinco listas que quedó completamente en blanco. Daniel ya tiene las tres
URLs. Cobra por documento leído, escrito y borrado, más almacenamiento y egress, con cuotas
diarias gratuitas.

**Qué necesito:** límites y modelo de cobro, y sobre todo **en qué se diferencia de Cloudflare
D1 y de DynamoDB**, que ya están en la ficha. Si no hay diferencia clara, no entra.

---

## NO NECESITAN INVESTIGACIÓN · solo abrir y copiar

Estas seis cierran mis pendientes y Daniel ya trae los datos. Las abro yo y verifico.

| Pendiente mío | URL de Daniel | Lo que ya anotó |
|---|---|---|
| **Scaleway: precio** | `scaleway.com/en/pricing/serverless/` | EUR 0,000005/GB-s y EUR 0,000015 por 100 solicitudes, tras capa gratuita de 400k GB-s y 1M solicitudes |
| **Supabase: precio** | `supabase.com/pricing` | USD, planes Free/Pro/Team/Enterprise, invocaciones incluidas más excedentes |
| **Railway: límites** | `docs.railway.com/reference/usage-limits` | Límites de uso por plan |
| **Fly.io: límites** | `fly.io/docs/machines/cpu-performance/` | CPU compartida con 6,25 % de base más ráfaga. **Las cuotas de máquinas por organización son dinámicas: no hay tabla pública fija** |
| **Oracle: región del precio** | `oracle.com/cloud/price-list/` | **Tablas globales de OCI, sin variación por región.** Eso cierra mi pendiente |
| **Turso: límites y precio** | `turso.tech/pricing` · `docs.turso.tech/help/usage-and-billing` | USD, planes Free/Developer |

> Dos de esos datos son en sí mismos hallazgos: **Oracle tiene precio global sin variación por
> región**, y **Fly.io no publica una tabla fija de cuotas**. Los dos sirven para el cuadro.

---

## Nota sobre el método de Daniel

En la columna "Cómo la verificaste" anota cosas como *"Abrí la URL (HTTP 200)"*. Eso confirma
que la página **existe**, no que diga lo que la fila afirma. Las cifras que copie de su Excel
las abro igual antes de ponerlas en el cuadro.
