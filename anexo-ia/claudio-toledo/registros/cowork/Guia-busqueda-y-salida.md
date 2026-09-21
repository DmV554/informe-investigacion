# Guía de búsqueda y formato de salida
### Complemento de `Encargo-navegador-3.2.md` · 20-09-2026

El encargo dice **qué** buscar. Esta guía dice **cómo**, y **cómo entregarlo**.

Todo lo que sigue sale de errores reales cometidos en este mismo trabajo durante los últimos
dos días. No son reglas teóricas.

---

# PARTE 1 · Cómo encontrar la página correcta

## 1.1 · Cada proveedor tiene dos sitios, y solo uno sirve

| Proveedor | Sitio comercial (marketing, a veces precios) | **Documentación** (límites) |
|---|---|---|
| Cloudflare | `cloudflare.com` | **`developers.cloudflare.com`** |
| Google | `cloud.google.com/run` | `cloud.google.com/run/**docs**` y `/quotas` |
| Fastly | `fastly.com` | **`docs.fastly.com`** |
| Deno | `deno.com` | **`docs.deno.com`** |
| Vercel | `vercel.com` | `vercel.com/docs` |
| Netlify | `netlify.com` | `docs.netlify.com` |

**Regla:** el precio suele estar en el sitio comercial, los límites casi siempre en el de
documentación.

**Error real:** se buscaron los límites de un producto en su página de producto y solo
aparecieron casos de uso e integraciones. Los límites estaban en el sitio de documentación,
que es otro dominio.

## 1.2 · Acotar la búsqueda al dominio

```
site:developers.cloudflare.com workers limits
site:docs.fastly.com compute resource limits
site:cloud.google.com run quotas
```

Si el resultado no está en el dominio del proveedor, **no sirve**, aunque acierte.

## 1.3 · Cómo se llaman las páginas

Buscar estas palabras: *Limits* · *Quotas* · *Service quotas* · *Resource limits* ·
*Platform limits* · *Pricing* · *Configuration reference*

## 1.4 · Nota de versión no es documentación

En los sitios de documentación conviven dos cosas:

- **Notas de versión / release notes / what's new:** anuncian un cambio en una fecha. Dicen
  cómo era el producto ese día, no cómo es hoy
- **Documentación de referencia:** el estado actual

**Error real:** se tomó una nota de versión de noviembre de 2020 como fuente de los límites
actuales de un producto en 2026. Seis años de diferencia.

**Para el informe siempre la de referencia.** Si solo existe la nota de versión, decirlo.

---

# PARTE 2 · Cómo leer la página sin equivocarse

## 2.1 · Valor por defecto no es máximo

Si la columna dice **"Default Value"**, ese no es el límite del producto.

**Error real:** una página titulada *"Changing Default Memory and Timeout Settings"* daba
30 segundos y 128 MB. Se tomaron como límites. Los máximos reales eran 300 segundos y
3.072 MB: diez veces y veinticuatro veces más.

**Anotar siempre los dos** cuando existan, y decir cuál es cuál.

## 2.2 · Fijar la región antes de leer el precio

Casi todas las páginas de precios tienen un selector con una región por defecto. Si no se
toca, no se sabe qué se está leyendo.

- Google → **us-east4**, y declararlo
- Cloudflare, Fastly, Deno → si el precio no depende de región, escribir **«global»**. Esa
  ausencia de regiones **es el dato**

## 2.3 · Identificar el plan

Una misma plataforma cobra y limita distinto por plan. **Una fila = un plan**, declarado en
la celda.

**Error real:** una plataforma tenía tres regímenes de precios simultáneos —uso por tramos,
paquetes por cotización, y tarifas heredadas para cuentas antiguas— y la celda no decía cuál
se estaba citando.

## 2.4 · Leer la unidad completa, no solo el número

No es lo mismo:
- GB-s que GiB-s
- por solicitud que por millón de solicitudes
- **tiempo de CPU** que **tiempo de reloj**

**Error real:** una plataforma cobra tiempo de CPU, no duración total de la solicitud. Son
dos números distintos **en la misma página**, y copiar uno por otro cambia el costo por
órdenes de magnitud.

## 2.5 · Buscar el significado real de la unidad

**Error real:** una base de datos cobra por «fila leída». Leyendo la letra chica, una «fila
leída» es en realidad una fila **escaneada**: una consulta mal indexada consume cuota aunque
devuelva tres resultados.

Cuando la unidad tenga nombre propio, buscar su definición en la documentación.

## 2.6 · Buscar el piso, no solo la tarifa

Una tarifa por consumo puede convivir con un **cargo mínimo mensual**. Sin ese dato, la
celda afirma implícitamente que con cero tráfico se paga cero, y a veces es falso.

Buscar: *minimum*, *base fee*, *monthly charge*, *included*, *workspace fee*.

## 2.7 · La capa gratuita es parte del precio

Casi siempre está en la misma página, en otra sección. Sin ella, el precio no describe el
comportamiento en volumen bajo.

---

# PARTE 3 · Qué hacer cuando las fuentes se contradicen

## 3.1 · Página comercial contra documentación

**Citar la documentación**, y anotar la diferencia en Notas.

**Error real:** la página comercial de una plataforma decía "hasta 5 réplicas" y su
documentación decía 6.

## 3.2 · FAQ contra página de precios

**Citar la página de precios.**

**Error real:** el FAQ oficial de un proveedor usaba la tarifa de recursos aprovisionados
para describir el consumo, y al revés. Las cifras estaban cruzadas en su propia página.

## 3.3 · Un error 403 no prueba nada

**Error real:** se concluyó que una plataforma no publicaba precios porque su página de
precios devolvía 403. Un 403 es un bloqueo de acceso, no evidencia de ausencia. El dato real
estaba en la página de límites por nivel, que remitía la tarifa al representante comercial.

---

# PARTE 4 · Qué nunca se puede usar

| No sirve | Por qué |
|---|---|
| **Foros comunitarios** | No son documentación oficial. **Error real:** se afirmó que una plataforma no publicaba sus cuotas basándose en un hilo del foro. Hubo que retirarlo |
| **El proveedor hablando bien de sí mismo** | "50 % más barato que AWS", "independencia real del proveedor". Es autopromoción |
| **Un proyecto comparando a sus competidores** | Su página de comparación sirve de pista, no de fuente sobre los otros |
| **Blogs, agregadores, artículos sin autor** | No verificables |
| **Estimar o inferir** | Si no está publicado, se dice que no está publicado |

---

# PARTE 5 · Autochequeo antes de entregar

Por cada celda:

- [ ] ¿Tiene **URL exacta** y **fecha de consulta**?
- [ ] ¿La URL es del **sitio oficial** del proveedor o del proyecto?
- [ ] ¿Es **documentación de referencia**, no una nota de versión?
- [ ] Si es un límite, ¿es el **máximo** o el valor por defecto? ¿Está dicho cuál?
- [ ] Si es un precio, ¿tiene **moneda, región, tramo, plan y capa gratuita**?
- [ ] ¿La **unidad** está completa, con su base temporal?
- [ ] ¿Lo **leí** en la página, o lo **inferí**?

La última es la más importante.

---

# PARTE 6 · Formato de salida

Dos archivos.

## 6.1 · El CSV

El de `Encargo-navegador-3.2.md`, 19 columnas separadas por punto y coma.

## 6.2 · Un `.md` de respaldo · **este es el que se revisa**

Un bloque por plataforma, con este formato exacto:

```markdown
## Cloudflare Workers (plan Paid)

**Modelo:** cómputo en el borde
**Verificado el:** 20-09-2026

### Campos

| Campo | Valor | Dónde lo leí | Confianza |
|---|---|---|---|
| Aislamiento | ... | URL exacta | leído / inferido |
| Unidad de cobro y piso mensual | ... | URL | leído / inferido |
| Precio de lista | ... | URL | leído / inferido |
| Mitigación (¿se factura?) | ... | URL | leído / inferido |
| Qué opera el equipo | ... | URL | leído / inferido |
| Estado externo / límite que fuerza rediseño | ... | URL | leído / inferido |
| Tiempo máximo | ... | URL | leído / inferido |
| Memoria / vCPU | ... | URL | leído / inferido |
| Payload entrada / salida | ... | URL | leído / inferido |
| Concurrencia / escalado | ... | URL | leído / inferido |
| Egreso de datos | ... | URL | leído / inferido |

### Citas textuales

Para los tres o cuatro datos más importantes, la frase literal de la página:

> "..." — URL, 20-09-2026

### No pude verificar

- ...

### Contradicciones o advertencias

- ...
```

**La columna «Confianza» es obligatoria.** Solo dos valores: **leído** (está escrito en la
página, con esas palabras) o **inferido** (se dedujo de otra cosa). Todo lo inferido se
revisa aparte.

**Las citas textuales son lo que más sirve para revisar.** Una frase literal con su URL se
verifica en diez segundos; un número suelto hay que rastrearlo.

## 6.3 · Y al final, tres listas

1. **Datos que no encontré**, por plataforma
2. **Contradicciones** entre páginas del mismo proveedor
3. **Cifras que vi pero no son admisibles** según la Parte 4, y por qué

La tercera es la más valiosa. En este trabajo ya evitó dos errores: una cifra de foro que se
iba a usar como dato, y un dato técnico que parecía distinguir a una plataforma cuando otra
que ya estaba en la lista tenía exactamente lo mismo.
