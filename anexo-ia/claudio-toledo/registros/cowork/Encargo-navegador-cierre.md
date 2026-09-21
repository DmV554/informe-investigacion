# Encargo para el navegador · cierre de mis filas
### TERABYTE · TI-05 · 20-09-2026

Documento autocontenido. Es un encargo corto: **tres plataformas, catorce campos en total.**

---

## Contexto

Informe académico sobre computación sin servidor y en el borde. Estoy cerrando un cuadro
comparativo de plataformas. **La mayor parte ya está levantada**; solo faltan los campos que
listo abajo. No necesito análisis ni recomendaciones: solo los datos, con URL y fecha.

---

## REGLAS

**1 · Solo documentación oficial.** El sitio de documentación del proveedor o del proyecto.
No sirven blogs, comparativas, agregadores, foros ni artículos sin autor.

**2 · Toda cifra necesita fecha de consulta.**

**3 · Valor por defecto no es máximo.** Si la página dice "Default", decirlo así y buscar el
máximo aparte.

**4 · Que un proveedor hable bien de sí mismo no es evidencia.** Sí lo es que documente un
mecanismo o un límite.

**5 · Si algo no está publicado, decirlo.** «No publicado», «solo por cotización» o «no
documentado» son respuestas válidas. **Nunca estimar.**

**6 · Notas de versión no son documentación de referencia.** Una nota de 2020 dice cómo era
el producto ese día, no cómo es hoy.

---

# PLATAFORMA 1 · Oracle Cloud Infrastructure Functions

Ya tengo verificado: timeouts (300 s síncrono, 3.600 s detached), memoria en valores fijos
hasta 3.072 MB, precio por tramos, capa gratuita, concurrencia aprovisionada al 25 %, payload
de 6 MB, y que **el precio es global sin variación por región**.

## Faltan cuatro campos

### 1.1 · Modelo de aislamiento

¿Qué tecnología de aislamiento usa OCI Functions? Contenedor, microVM, otra.
**Según la documentación, no por analogía con otros productos.**

Buscar en la documentación de arquitectura o de conceptos de Functions en `docs.oracle.com`.

### 1.2 · Qué opera el equipo

De esta lista cerrada, ¿qué queda del lado del cliente?

> sistema operativo y parcheo · runtime y dependencias · planificación de capacidad ·
> escalado · red (VPC, balanceo, certificados) · despliegue y versionado · observabilidad y
> alertas · recuperación ante fallos

Si Oracle publica un **modelo de responsabilidad compartida**, usarlo y dar la URL. Si no
existe, decirlo: lo marcaré como inferido.

### 1.3 · Estado externo obligatorio

¿La documentación dice que el estado debe externalizarse? ¿A qué servicios remite (Object
Storage, Autonomous Database, otro)?

### 1.4 · Egreso de datos

Precio de salida a internet, con tramos, capa gratuita y fecha. Y si el tráfico entre
servicios de OCI en la misma región tiene o no cargo.

### 1.5 · Extra, si aparece: concurrencia

Tengo una nota de versión de **2020** que menciona «60 GB de memoria total concurrente por
dominio de disponibilidad». **Es de hace seis años y además es memoria, no instancias: no la
voy a usar.**

¿La página vigente de *service limits* publica un límite de concurrencia o de instancias
simultáneas? Si no, responder «no documentado».

---

# PLATAFORMA 2 · Bunny Edge Scripting

Ya tengo: CPU 30 s por solicitud, memoria 128 MB, 50 subsolicitudes, script máximo 10 MB,
128 variables de entorno, y precio de **USD 0,02 por 1.000 s de CPU más USD 0,20 por millón
de solicitudes**.

> **Confirmar de paso esas cifras**, que vienen de una planilla interna sin verificar.

## Faltan seis campos

### 2.1 · Modelo de aislamiento

¿Qué usa? Isolates de V8, WebAssembly, contenedor. Según la documentación.

### 2.2 · Piso mensual

¿Hay **cargo fijo mensual** o mínimo facturable para usar Edge Scripting, o se paga solo por
consumo? Este dato es importante: algunas plataformas de borde cobran un mínimo aunque no
haya tráfico.

### 2.3 · Capa gratuita y región del precio

¿Hay tramo gratuito de CPU o de solicitudes? ¿El precio de cómputo varía por región, o es
único? Si es único, decirlo: esa ausencia también es dato.

### 2.4 · Qué opera el equipo

Misma lista cerrada de la sección 1.2.

### 2.5 · Estado externo obligatorio

¿A qué obliga a externalizar el estado? ¿Qué servicios de Bunny se usan para eso?

### 2.6 · Egreso de datos · **el más importante de esta plataforma**

Tengo anotado que **el ancho de banda CDN se cobra aparte del cómputo**. Necesito:

- El **precio del ancho de banda por GB**, con sus tramos y por región si varía
- Si hay **tramo gratuito**
- Confirmar que efectivamente se factura **separado** del cómputo de Edge Scripting

Es el dato que justifica la inclusión de esta plataforma, así que conviene que quede sólido.

---

# PLATAFORMA 3 · Fission

Ya tengo: versión v1.27.0 del 22-06-2026, siete versiones entre mayo y junio de 2026, y que
el ejecutor por defecto **poolmgr** mantiene pods genéricos ya arrancados (3 por defecto),
mientras que **newdeploy** y **container** sí escalan a cero, y que **el ejecutor se elige por
función**.

## Faltan cuatro campos

### 3.1 · Acreditación

- ¿Está **Fission** en el **CNCF Landscape**? ¿En qué categoría?
- ¿Tiene nivel de madurez: Sandbox, Incubating o Graduated? ¿Desde qué fecha?
- **Si no es proyecto CNCF, decirlo explícitamente** y decir bajo qué gobernanza está

`landscape.cncf.io` · `cncf.io/projects/`

### 3.2 · Modelo de aislamiento

¿Contenedor, pod de Kubernetes, otro? Según su documentación de arquitectura.

### 3.3 · Escala a cero, por defecto

Ya sé que depende del ejecutor. Necesito precisión:

- ¿**Cuál es el ejecutor por defecto** cuando se crea una función sin especificar?
- Confirmar que **poolmgr no escala a cero** y que **newdeploy sí**
- ¿Cuánto tarda en escalar a cero, si está documentado?

### 3.4 · Timeout y concurrencia por defecto

Valores por defecto, indicando que son configurables. Si no están publicados, decirlo.

---

## FORMATO DE RESPUESTA

Un bloque por plataforma:

```markdown
## Oracle Cloud Infrastructure Functions

| Campo | Valor | Dónde lo leí | Confianza |
|---|---|---|---|
| Aislamiento | ... | URL exacta | leído / inferido |
| ... | ... | ... | ... |

### Citas textuales
> "..." — URL, 20-09-2026

### No pude verificar
- ...
```

**La columna «Confianza» es obligatoria:** **leído** (está escrito en la página con esas
palabras) o **inferido** (se dedujo de otra cosa).

**Y al final, tres listas:**
1. Datos que no encontré, por plataforma
2. Contradicciones entre páginas del mismo proveedor
3. **Cifras que vi pero que no son admisibles según las reglas, y por qué**

---

## Lo que NO necesito

- Cifras de arranque en frío: esa columna la cubre otra persona
- Plataformas nuevas: la lista está cerrada
- Análisis o comparaciones entre plataformas
- Los campos que ya tengo, salvo los que pedí confirmar en Bunny
