# Conversación completa — sesión del 19 y 20-09: 3.1 alternativas y 3.2 cuadro comparativo

- Herramienta: Claude Code 2.1.278
- Identificador de sesión: `cf21efe1-8c94-4839-9cd4-c78d63bcdf68`
- Registro de origen: `cf21efe1-8c94-4839-9cd4-c78d63bcdf68.jsonl`
- Modelos: <synthetic>, claude-opus-5
- Inicio: 19-09-2026 12:28
- Fin: 20-09-2026 21:36

De cada intervención del modelo se transcribe el texto y se listan las
herramientas que ejecutó (lectura y escritura de archivos, comandos y
consultas a documentación). La salida de esas herramientas no se incluye
por extensión; el registro original la conserva íntegra.

---

## Persona — prompt 1 — 19-09-2026 12:28

```text
quiero que analices todas las carpetas, soy claudio quiero que me ayudes a realizar mi parte, no hagas cambios, para el plan de trabajo que debo realizar en base a lo demas escrito, dejemos antotado todo en un .md, tambien deja anotado los prompt en un .md a parte, si quieras creemos una carpeta, llamada sesion actual 19-09
```

### Claude Code — 19-09-2026 12:28

Voy a explorar primero toda la estructura del proyecto.

### Claude Code — 19-09-2026 12:28

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:28

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:29

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:30

Ya revisé todo: las tres carpetas, el repo git, el `main.tex` completo, las indicaciones, la guía del equipo y tus tres documentos de revisión de papers. Voy a crear la carpeta y los dos `.md` sin tocar nada de lo existente.

### Claude Code — 19-09-2026 12:30

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:32

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:33

Voy a usar el editor de archivos directamente, el heredoc se complica con el contenido.

### Claude Code — 19-09-2026 12:34

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 12:35

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 12:35

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:35

Listo, Claudio. No toqué ningún archivo existente (el repo sigue limpio) y creé:

- [Sesion-actual-19-09/Plan-de-trabajo-Claudio.md](Sesion-actual-19-09/Plan-de-trabajo-Claudio.md)
- [Sesion-actual-19-09/Prompts-IA.md](Sesion-actual-19-09/Prompts-IA.md)

**Lo que encontré al revisar todo:**

Tu parte son tres entregables que en realidad son un solo flujo: buscás alternativas → documentás la búsqueda (Anexo D) → justificás las que entran (3.1) → las que califican se vuelven filas del cuadro (3.2). La propia guía dice que vos hacés 3.1 y 3.2, así que no hay traspaso entre medio.

**Tres cosas que vale la pena que sepas ya:**

1. **El repo no tiene una sola sección escrita.** Los 4 commits son puro setup; todos los bloques de [main.tex](informe-investigacion/informe/main.tex) dicen `TODO`. Quedan dos días.
2. **`referencias.bib` está vacío** (solo comentarios). Vos ya tenés el BibTeX de tus 11 papers en `Revision-papers.md`: pegarlo es 15 minutos y destraba la bibliografía de todo el grupo. Es el aporte de mayor impacto que podés hacer fuera de tu sección.
3. **Las columnas del cuadro 3.2 ya están decididas en el `.tex`**, pero Valentina todavía no justifica los criterios. El plan asume que no esperás: usás esas columnas y le avisás.

**Sobre el archivo de prompts:** lo interpreté como las dos cosas a la vez — el registro que exige el Anexo A parte B (con tu declaración por sección en borrador, nivel 2 como máximo), y prompts listos para usar que están redactados para no cruzar el punto 6.1. Cada uno termina pidiendo que el modelo *no* dé cifras. Los prompts del 18-09 los dejé marcados como reconstruidos de memoria: antes de copiarlos al anexo tenés que sacar el texto literal del historial.

Lo que no puse en ningún lado, a propósito: precios, límites técnicos ni URLs como si fueran citas. Las URLs están como punto de partida a confirmar, porque cualquier cifra que salga de mí es exactamente lo que el punto 6.1 prohíbe.

## Persona — prompt 2 — 19-09-2026 12:48

```text
de igual manera esos no son todos los artiuculos, esos papers, son parte de una revision simplemente, de unos 47 papers aproximantamente, entonces la idea es usar los mas relevantes para lo que es nuestra seccion, quiero que hagamos un supuesto de como deberia ir la estructura de lo que es nuestra parte, que nos falta y que es lo que ya tenemos
```

### Claude Code — 19-09-2026 12:48

Buen dato — eso cambia cómo hay que plantear la sección. Déjame verificar qué hay registrado de los otros papers antes de armar la estructura.

### Claude Code — 19-09-2026 12:48

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:48

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:49

Confirmado: localmente solo están tus 11 (el 1 y del 38 al 47). De los otros ~36 no hay registro en estas carpetas — viven en la planilla común. Eso tiene una consecuencia importante para tu sección, y la dejo escrita.

### Claude Code — 19-09-2026 12:50

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 12:51

Creé [Sesion-actual-19-09/Estructura-seccion-3.md](Sesion-actual-19-09/Estructura-seccion-3.md), sin tocar nada más.

**El hallazgo que cambia el planteo:** de tus 11 papers, solo 4 sirven a la sección (39, 43, 44, 45). Pero lo relevante no es ese número — es algo que tu propio análisis ya había anotado y que ahora cobra otro peso: *"el edge de los proveedores: ningún paper lo estudia"* y *"precios vigentes: ninguno sirve"*.

O sea, **nuestra parte es la menos dependiente de papers de todo el informe**. Para 3.1 los papers son cantera de nombres, no evidencia. Para 3.2 directamente no sirven: sus tablas de precios son de 2023 y una tiene un error de factor 10 (tu hallazgo 1). Por eso los papers 46 y 47, que son los mejores del lote, casi no te sirven a vos — le sirven a Francisca.

**Consecuencia: no necesitás leer los otros 36.** De ellos necesitás una sola cosa, y es una tarea que la guía ya les asignó a todos: *¿aparece alguna plataforma que no esté en las cinco listas de la ficha? Mandame el nombre y la página.* Además vale la pena preguntar por tres papers con nombre y apellido: El Ioini et al. (2020) —el hueco grande, el edge de CDN—, Tran y Kim (Knative, va a tu mitad del cuadro) y Tusa et al.

**Qué tenemos:** la estructura de las tres piezas, ~30 candidatos repartidos en las 5 listas, 2 lecturas transversales ya verificadas con página, 5 descartes razonados, el BibTeX listo para pegar y un esqueleto LaTeX que está bastante bien hecho.

**Qué falta:** los datos. Cero límites y cero precios verificados. Son entre 35 y 55 celdas, a 2-3 minutos cada una — entre 6 y 8 horas de trabajo real, de las cuales ~4 son abrir páginas oficiales y anotar con fecha. Es justo lo único que no se puede acelerar, porque el punto 6.1 prohíbe que una cifra salga del modelo.

Hay cuatro decisiones de diez minutos que bloquean todo lo demás: si Vercel y Netlify entran como filas, si Neon es tuyo, si se cierran los criterios con las columnas que ya están en el `.tex`, y qué dice la celda de precio en las filas open source (esa última alimenta el análisis de Rodolfo, así que conviene avisarle).

## Persona — prompt 3 — 19-09-2026 12:53

```text
algo que quiero recalcar, y que lo tengas claro, quiero que trabajes sin modismos al momento de escribirme o redactar cosas, ya que me estas escribiendo con modismos argentinos, para que me escribas neutro de ahora en adelante
```

### Claude Code — 19-09-2026 12:53

Tienes razón, usé voseo. Voy a revisar si se filtró también a los archivos.

### Claude Code — 19-09-2026 12:53

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:53

Los tres archivos están limpios: están escritos en primera persona ("tengo que", "debo", "mi"), que es neutro. El voseo apareció solo en mis respuestas del chat.

Lo guardo como preferencia permanente.

### Claude Code — 19-09-2026 12:53

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 12:53

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 12:53

Anotado y guardado en memoria, así que se mantiene en las próximas sesiones.

De ahora en adelante escribo en español neutro: "tienes", "necesitas", "puedes", sin voseo ni regionalismos de ninguna variante. Aplica tanto a mis respuestas como a los archivos que redacte.

Los tres documentos de `Sesion-actual-19-09/` no necesitan corrección: están escritos en primera persona, que ya es neutro.

## Persona — prompt 4 — 19-09-2026 13:07

```text
me puedes explicar paso a paso, lo que debe contener mi seccion? y que es lo que necesito para realizarla
```

### Claude Code — 19-09-2026 13:08

Te lo explico desde cero, porque tu sección tiene una lógica que no es obvia a primera vista.

---

# Parte 1 · Qué es tu sección, en una frase

La sección 3 completa responde a: **"¿qué plataformas existen, qué límites tienen y cuánto cuestan?"**

Dentro de eso, a ti te tocan dos cosas que son en realidad la misma:

- **3.1** = *qué otras plataformas existen además de las que nombra la ficha*
- **3.2 (tu mitad)** = *cuáles son los límites y precios de un grupo específico de ellas*
- **Anexo D** = *la prueba de que buscaste de verdad*

La clave: **3.1 alimenta a 3.2**. Las alternativas que descubres en 3.1 y que califican se convierten en filas del cuadro de 3.2. Por eso te dieron las dos: no hay traspaso entre personas.

---

# Parte 2 · Qué debe contener cada pieza

## Pieza A · Sección 3.1, Alternativas adicionales

### De dónde sale la exigencia

La ficha del tema TI-05 tiene una fila llamada "Tecnologías, productos y proveedores a comparar" con **cinco listas**. Todas terminan igual: *"y otros que el grupo debe identificar"*.

El punto 4 de las Indicaciones convierte esa frase en una obligación concreta:

> *"Cada vez que la ficha dice «otros», el grupo debe incorporar al menos dos alternativas adicionales relevantes que no figuren en ella, **indicando qué aportan y por qué merecen entrar en la comparación**."*

**Cinco listas × 2 alternativas = 10 mínimo.**

### Qué se evalúa realmente

Esto es lo más importante que puedo explicarte, y es donde se pierde o se gana la nota:

**No se evalúa la lista. Se evalúa la frase de justificación.**

Una alternativa sin justificación no cuenta, aunque esté bien elegida. La diferencia es esta:

| Frase que no sirve | Por qué falla |
|---|---|
| *"Fly.io es una plataforma que permite desplegar contenedores en la nube."* | Describe el producto. Eso está en su página web. No aporta nada. |

| Frase que sí sirve | Por qué funciona |
|---|---|
| *"Fly.io entra porque ejecuta contenedores en múltiples regiones cercanas al usuario, lo que cruza dos categorías que la ficha trata por separado: contenedor sin servidor y cómputo en el borde."* | Dice **qué agrega a la comparación** que las opciones de la ficha no tienen. |

La fórmula mental: **"entra porque aporta ___ , que ninguna de las que ya están cubre"**.

> Esas diez frases las escribes tú, a mano. El punto 6.1 prohíbe que la IA redacte análisis comparativo, y tienes que poder defenderlas oralmente sin el texto delante.

### Contenido concreto de 3.1

Presupuesto: **0,75 página, unas 300 palabras de texto más la tabla.**

1. **Párrafo 1 (~140 palabras).** Dónde buscaste y con qué regla decidiste. Aquí declaras el criterio de inclusión (producto disponible o proyecto activo, con documentación pública de límites, que aporte algo nuevo) y el de descarte (los prototipos de investigación quedan fuera). Cierras remitiendo al Anexo D.

2. **Tabla de 10 filas.** Tres columnas: Lista de la ficha | Alternativa | Qué aporta a la comparación. La tercera es la que se evalúa.

3. **Párrafo 2 (~160 palabras).** Lo que aprendiste del conjunto, que no se deduce leyendo la tabla. Tienes dos hallazgos ya verificados para esto (los del archivo de estructura). Y aquí va la **declaración obligatoria** del punto 4: si las cinco listas dieron al menos dos alternativas, lo dices; si alguna no dio, lo declaras expresamente.

---

## Pieza B · Tu mitad del cuadro 3.2

### Qué exige la ficha

> *"Cuadro comparativo de al menos seis plataformas con sus límites técnicos."*

Es uno de los tres entregables obligatorios del tema. Tú no escribes prosa aquí: **produces celdas**. El párrafo de análisis lo escribe Rodolfo, y el párrafo de criterios lo escribe Valentina.

### Qué plataformas te tocan

Google, Cloudflare, Fastly, Deno/Vercel/Netlify y código abierto. En la práctica son entre 7 y 11 filas.

### Qué va en cada fila

Las columnas ya están decididas en el archivo LaTeX:

**Plataforma · Categoría · Tiempo máximo · Payload máximo · Estado/persistencia · Precio de lista · Otros límites**

### La regla que gobierna esta pieza

El punto 5 de las Indicaciones es estricto con los precios:

1. Toda cifra lleva **producto, moneda, región, fecha de consulta, y si es precio de lista o cotización**.
2. **Una cifra sin fecha no se considera válida.** No es una recomendación: es un criterio de rechazo.
3. Se verifica en la **página o calculadora oficial del proveedor**. No en artículos, no en comparativas.
4. Si el proveedor no publica precio, se escribe **«solo por cotización»**.

Formato de celda:

```
USD 0,0000166667 por GB-s · us-east-1 · lista · consultado 19-09-2026
```

### Dos casos que se resuelven con criterio, no buscando

- **Las filas de código abierto no tienen precio.** Knative, OpenFaaS y Spin se autoalojan. No dejes la celda vacía: escribe que no tiene precio de lista porque el costo es la infraestructura más la operación. Esa celda es el argumento de complejidad operacional que Rodolfo necesita.
- **Lo que no publica precio** va como «solo por cotización», sin excepción.

---

## Pieza C · Anexo D, búsqueda documentada

### Por qué existe

El punto 4 dice que si concluyes que no hay más alternativas, tienes que declararlo y documentar la búsqueda. Y agrega algo que conviene aprovechar:

> Descubrir que un candidato está **descontinuado y descartarlo con fecha y fuente también es aporte**.

Omitir este punto sin declararlo **se evalúa como ficha incompleta**.

### Qué debe contener

1. Un párrafo corto: qué exige el punto 4, qué período cubre la búsqueda, quién la hizo.
2. Los **criterios de inclusión y de descarte**, escritos.
3. Una **tabla de 5 filas**, una por lista: Lista | Fuentes consultadas | Criterios | Descartadas con motivo | Fecha.
4. La declaración final si alguna lista no llegó a dos.

Esta es la pieza que más rinde por hora invertida, y eres el único que la produce.

---

# Parte 3 · Qué necesitas para hacerla

## 1. Material de trabajo

| Necesitas | Estado | Dónde está |
|---|---|---|
| Un navegador y las páginas oficiales de cada proveedor | — | Es tu fuente principal |
| Los candidatos a verificar | **Tienes ~30**, repartidos en las 5 listas | `Plan-de-trabajo-Claudio.md` §6 |
| Una tabla donde anotar cada dato con su fecha | **Tienes la plantilla** | `Plan-de-trabajo-Claudio.md` §7 |
| Capturas de pantalla de cada página de precios | Falta | Respaldo por si el precio cambia antes del lunes |

## 2. Lo que necesitas de otras personas

| Qué | A quién | Si no llega |
|---|---|---|
| Confirmar los criterios (columnas del cuadro) | Valentina | Usas las columnas que ya están en el LaTeX |
| ¿Vercel y Netlify son filas del cuadro? ¿Neon es tuyo? | Rodolfo | Decides tú y le avisas |
| Formato de celda de precio, para que la tabla quede pareja | Rodolfo | Le mandas el tuyo y listo |
| Nombres de plataformas fuera de la ficha que hayan visto en sus papers | Todo el equipo | Te bastan los ~30 que ya tienes |

## 3. Lo que solo puedes poner tú

Esto no se delega, ni a un compañero ni a una IA:

- Las **diez frases de justificación**
- Los **dos párrafos** de 3.1
- El **criterio** con que decides qué entra y qué se descarta
- La **verificación** de cada límite y cada precio en la fuente oficial

## 4. Tiempo

Entre **6 y 8 horas** en total. De esas, unas 4 son mecánicas: abrir páginas y anotar con fecha. El resto es decidir y redactar.

---

# Parte 4 · El orden en que conviene hacerlo

El orden importa, porque cada paso depende del anterior:

1. **Verificar los candidatos** (~1,5 h). Por cada uno: ¿existe hoy?, ¿está archivado?, ¿publica precios y límites? Vas anotando en el Anexo D sobre la marcha, incluidos los que descartas y por qué.
2. **Elegir las diez** (30 min). Dos por lista, con los criterios ya declarados.
3. **Levantar los datos del cuadro** (2–3 h). Fila por fila, celda por celda, con fecha en cada precio.
4. **Escribir las diez justificaciones** (45 min). A mano.
5. **Escribir los dos párrafos de 3.1** (45 min). A mano.
6. **Cerrar el Anexo D** (1 h). Criterios, tabla y descartes.
7. **Entregar tu mitad a Rodolfo** en formato `\filaTabla{}` para que solo tenga que pegarla.

El paso 1 va primero porque hasta que no sepas cuáles sobreviven a la verificación, no sabes cuáles son tus diez ni qué filas extra lleva el cuadro.

---

¿Quieres que partamos por el paso 1? Puedo armarte una lista de verificación de los ~30 candidatos, con qué revisar exactamente en cada uno y dónde anotarlo, para que solo vayas abriendo páginas y completando.

## Persona — prompt 5 — 19-09-2026 13:58

```text
dentro de los chats anteriores, deje la lista de excel de los 47 que estabamos revisando, aun no los terminamos de revisar todos, pero de manera preliminar, esos son los que tenemos, cuales de estos son los mas relevantes para mi parte? asi los puedo analizar y buscar para poder complementer nuestra seccion de buena manera
```

### Claude Code — 19-09-2026 13:58

Déjame buscar ese archivo, porque en la revisión inicial solo encontré los cuatro `.md` y el PDF de indicaciones.

### Claude Code — 19-09-2026 13:58

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:58

Ahí está: `Referencias Investigación.xlsx`. Lo agregaste después de mi primera revisión. Voy a leerlo.

### Claude Code — 19-09-2026 13:58

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:58

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:58

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:58

Encontré la planilla completa. Déjame revisar las otras dos hojas y los comentarios antes de darte el análisis.

### Claude Code — 19-09-2026 13:58

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:59

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 13:59

Encontré la planilla: 47 fuentes, **17 revisadas**. Y hay un hallazgo que cambia tu orden de trabajo.

### Claude Code — 19-09-2026 14:00

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 14:00

El detalle completo está en [Sesion-actual-19-09/Papers-relevantes-para-3.md](Sesion-actual-19-09/Papers-relevantes-para-3.md). Lo importante:

## El hallazgo que cambia tu orden de trabajo

**Las fuentes 18 a 26 no son papers: son documentación oficial de proveedores.** Esa es la materia prima del cuadro 3.2, y **seis de ellas son exactamente de tu mitad, con URL, y ninguna está revisada**:

| N° | Fuente |
|---|---|
| 19 | Cloudflare Workers — Limits |
| 20 | Cloud Run — Request Timeout |
| 21 | Cloud Run — Memory Limits |
| 23 | Fastly — Compute Resource Limits |
| 24 | Deno Deploy — Pricing **and** Limits |
| 26 | Cloud Run — Pricing |

No tienes que salir a buscar las URLs: ya las tienes. Empieza por ahí, no por los papers.

## Los cuatro papers que sí vale la pena que revises

Para 3.1 los papers sirven para **descubrir nombres de plataformas**, no para sacar cifras. Los cuatro más rentables, todos sin revisar:

- **35 · Rise of the Planet of Serverless Computing** — revisión sistemática de 164 artículos, y la hoja de detalles dice que trae una tabla comparativa de límites. Es el inventario más grande del corpus.
- **13 · QuickFaaS** — un paper sobre portabilidad entre plataformas FaaS tiene que nombrar varias para compararlas.
- **11 · Pushing Serverless to the Edge with WebAssembly Runtimes** — alimenta las listas de edge y de código abierto a la vez.
- **10 · WebAssembly as an Enabler** — mismos autores que el paper 39 que ya analizaste.

Y dos que **no necesitas leer**: el 36 y el 37 ya los revisó Isidora. Pídele solo los nombres de plataformas que aparezcan.

## Dos problemas que encontré

**1. Tres fuentes no admisibles están asignadas a "3.2 Criterios y cuadro", tu sección.** La 31 es Cloudflare comparándose con Lambda (el punto 5 usa justamente ese caso como ejemplo de lo no admisible) y la 33 no tiene autoría verificable. La planilla ya las marca como problemáticas, pero siguen asignadas al cuadro.

**2. Alguien puso los papers 46 y 47 como fuente del cuadro 3.2.** Tu propio análisis concluyó lo contrario: el 46 tiene precios de 2023, y el 47 tiene un **error de factor 10 en el precio de Azure** (tu hallazgo 1). Si se citan ahí, entran cifras malas a tu sección.

Ambas cosas hay que avisárselas a Rodolfo, porque las puso él.

¿Quieres que prepare el mensaje para Rodolfo y el de Isidora, o prefieres partir abriendo las seis fuentes oficiales?

## Persona — prompt 6 — 19-09-2026 14:07

```text
esta esta la tabla de rodolfo, ya me la paso: [ Servicio | Categoría | Tiempo Máx. Ejecución | Rango de Memoria / vCPU | Límite Payload (In/Out) | Concurrencia / Escalado | Latencia / Cold Start | Modelo de Cobro y Precio Fechado (Sept 2026, us-east-1) | Complejidad Operacional (Infraestructura / Red) ], y con respecto a los papers los voy a revisar
```

### Claude Code — 19-09-2026 14:08

Rodolfo cambió la estructura: su tabla tiene **9 columnas**, la de `main.tex` tiene 7. Hay que adaptarse, y hay un problema serio en el encabezado.

### Claude Code — 19-09-2026 14:09

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 14:09

Hoja de captura adaptada: [Sesion-actual-19-09/Captura-cuadro-3.2-mi-mitad.md](Sesion-actual-19-09/Captura-cuadro-3.2-mi-mitad.md)

## Lo bueno de su tabla

Las tres últimas columnas —cobro, latencia y complejidad operacional— corresponden **una a una con las tres dimensiones del alcance de la ficha**. Eso está bien pensado: le resuelve el trabajo a Valentina, porque sus criterios ya son las columnas.

## El problema serio: `us-east-1` en el encabezado

`us-east-1` es un nombre de región **de AWS**. No existe fuera de ahí:

- En Google Cloud es `us-east1` o `us-central1` (sin guion antes del número)
- **Cloudflare, Fastly, Deno, Vercel y Netlify no cobran por región** — son redes globales con precio único
- Knative, OpenFaaS y Spin no tienen región: se autoalojan

O sea, ese encabezado deja **toda tu mitad mal etiquetada**. La solución es que la región vaya en la celda, que además es lo que el punto 5 exige: cada cifra declara su región y su fecha.

Lo mismo con "Sept 2026": el punto 5 pide fecha de consulta, no mes. Rodolfo consultó el 18, tú consultas el 19 y el 20.

## De paso, un hallazgo aprovechable

Al resolver eso aparece un contraste que no se ve leyendo la tabla: **los hiperescaladores cobran por región, los proveedores de borde no.** Es una diferencia real entre modelos de ejecución, del tipo que la rúbrica premia. Sirve para tu párrafo 2 de 3.1 y para el análisis de Rodolfo.

## Dos cosas más que revisar con él

**La columna "Latencia / Cold Start" es peligrosa.** Tienes la evidencia para plantearlo: es tu hallazgo 14. El paper 42 da 2–6 s para OpenWhisk, el 47 da 50–500 ms para Docker, Firecracker ~125 ms — pero el primero mide punta a punta y los otros solo la creación del sandbox. No son comparables. Y las cifras de marketing de cada proveedor sobre sí mismo no son admisibles. Propuesta: que cada celda diga **qué mide y de dónde sale**, o que sea cualitativa, y que las cifras duras salgan solo de donde Vicente midió en 4.1.

**Se perdió la columna "Estado / persistencia".** La ficha nombra explícitamente *"Cloudflare Workers (Durable Objects, D1, R2)"* y el subtema 2.6 incluye manejo de estado. Sin esa columna, la lista 5 de la ficha queda sin enganche. Se puede recuperar metiendo D1 como fila.

---

Una cosa práctica: 9 columnas × 12-14 filas no entra en vertical. `pdflscape` ya está cargado en `main.tex`, así que el cuadro va a necesitar `\begin{landscape}`. Y alguien tiene que cambiar la definición `\tabla{}` de 7 a 9 columnas — es de Rodolfo como consolidador, pero conviene que lo sepas antes de mandarle tus celdas.

¿Te preparo el mensaje para Rodolfo con estos cuatro puntos?

## Persona — prompt 7 — 19-09-2026 15:17

```text
hice el analisis y los artiuclos 10,11 y 13, el 10 y 11 no los pude pillar ya que me piden atorizacion para descargarlos y debo pedirlos, pero para el 13, parece ser no muy relevante para lo que es nuestra seccion
```

### Claude Code — 19-09-2026 15:18

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 15:18

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 15:19

Tu análisis del 13 está bien hecho y tu conclusión es correcta. Mi hipótesis era que un paper sobre portabilidad tenía que nombrar varias plataformas para compararlas; resultó que solo usa Azure y GCP. Lo verificaste y corregiste, que es exactamente como debía funcionar.

Además le sacaste dos cosas que no ibas buscando: el dato de OpenFaaS para tu mitad del cuadro, y la primera entrada real del Anexo D como *fuente consultada sin candidatos nuevos*.

## Sobre el 10 y el 11: no te bloquean

Mira cómo quedan tus dos listas afectadas si nunca los consigues:

**Lista 4, código abierto.** La ficha ya nombra seis. Necesitas dos más y tienes cinco candidatos, todos verificables directamente en su documentación o repositorio, sin paper de por medio: Apache OpenWhisk (proyecto de la ASF, que además es fuente preferente), Fission, Nuclio, Fn Project y WasmEdge.

**Lista 3, cómputo en el borde.** La ficha nombra siete. Necesitas dos y tienes seis: Akamai EdgeWorkers, Supabase Edge Functions, Bunny Edge Scripting, más Greengrass, Azure IoT Edge y KubeEdge que ya sacaste de los papers 39 y 44.

No estás corto en ninguna. El 10 y el 11 eran un extra para el ángulo Wasm, y ese ángulo lo puedes sostener con las fuentes 16 y 17 de la planilla: la especificación del W3C y WASI son gratuitas y son **fuente preferente** según el punto 5, mejor posicionadas que un paper para argumentar portabilidad sobre un estándar abierto.

### Si los quieres igual, con límite de tiempo

Intenta primero por el **Sistema de Bibliotecas PUCV**. Las Indicaciones lo listan explícitamente entre las fuentes preferentes, así que si la universidad tiene suscripción a Springer y a IEEE, entras con tu cuenta y los tienes en minutos. Dale diez minutos. Si no resulta, un pedido formal no llega antes del lunes.

Y una regla que no conviene saltarse: la guía dice que toda referencia se abre y se verifica en el original antes de citarla. Si no los lees, **no los cites**. Pero sí anota en el Anexo D que los consultaste y no tuviste acceso al texto completo, con fecha. Eso es búsqueda documentada legítima y suma.

## Una precaución con el dato de OpenFaaS

Lo que encontraste en el 13 (p. 3-4) es bueno para la columna de complejidad operacional, pero es de 2022. Divide el uso:

- **El hecho** que va en la celda sale de la documentación actual de OpenFaaS, con fecha.
- **El argumento** lo respalda el paper, junto con la clasificación del 43 (p. 1531).

Y verifica una cosa antes de escribir "exige Kubernetes": revisa si OpenFaaS ofrece hoy alguna variante de despliegue más liviana. Si la tiene, la afirmación de 2022 quedó desactualizada y ponerla sin matiz en el cuadro sería un error.

## Lo que te toca pasar al grupo

El 13 te dio material que no es tuyo y que la guía te pide reportar:

- **A Fabián (2.6):** es el mejor material de lock-in del corpus, con las dos causas y el costo medido de evitarlo (+3,2 % y +3,8 %). Dile que cite a **Yussupov et al. (2019)** para los efectos del lock-in, no al 13, porque el 13 lo toma de segunda mano y en parte de una página de Cloudflare.
- **A Vicente (4.1):** la metodología de las p. 17-19 y sobre todo los problemas documentados de la p. 24 le sirven para redactar sus limitaciones.

Con esto el 13 te queda además como referencia académica propia, que cubre de sobra tu mínimo de una o dos.

## Persona — prompt 8 — 19-09-2026 15:20

```text
si no es verdad el 13 no nos sirve tanto, ahora quiero que me digas si la tabla de rodolfo esta bien o es pecario en algunas secciones
```

### Claude Code — 19-09-2026 15:21

Hice la auditoría columna por columna, contra los subtemas obligatorios de la ficha y contra el punto 5.

**Veredicto general: la estructura está bien pensada. Tiene tres columnas precarias y una omisión que sí importa.**

Lo que está bien: las tres últimas columnas corresponden con las tres dimensiones del alcance (costo, latencia, complejidad operacional), y las columnas 3 a 6 cubren "límites técnicos", que es lo que la ficha exige como entregable. Eso está correcto.

## Auditoría

| Columna | Veredicto |
|---|---|
| 1 · Servicio | Bien. Mejor que "Plataforma": Cloud Run y Cloud Run functions son servicios distintos |
| 2 · Categoría | Bien |
| 3 · Tiempo Máx. Ejecución | Bien, pero **ambigua** |
| 4 · Rango de Memoria / vCPU | Bien. Buena adición |
| 5 · Límite Payload (In/Out) | **Bien, mejor que lo que había.** Separar entrada y salida es correcto |
| 6 · Concurrencia / Escalado | Bien, pero **ambigua** |
| 7 · Latencia / Cold Start | **Precaria** |
| 8 · Modelo de Cobro y Precio Fechado | **Precaria en el encabezado y sobrecargada** |
| 9 · Complejidad Operacional | **Precaria: sin definir** |

---

## Las tres precarias, por gravedad

### 1. El encabezado de la columna 8 rompe el punto 5

Es lo más grave porque afecta a **toda tu mitad**.

`us-east-1` es región de AWS. En Google es `us-central1` o `us-east1`, y Cloudflare, Fastly, Deno, Vercel y Netlify **no cobran por región**: son redes globales. Las filas de código abierto no tienen región en absoluto. Fijarla en el encabezado deja mal etiquetadas nueve de las catorce filas.

"Sept 2026" tampoco cumple: el punto 5 pide **fecha de consulta**, y él consultó el 18 mientras tú consultas el 19 y el 20.

Y la celda está sobrecargada. Tiene que cargar unidad de cobro, precio, región, fecha y tipo. Pero el subtema obligatorio de facturación nombra además dos cosas que ahí no caben:

- **Salida de datos (egress)**, que es un eje de costo separado
- **Tiempo de CPU frente a tiempo de reloj**, que es decisivo justamente en tu mitad, porque Cloudflare cobra tiempo de CPU y no tiempo de reloj

Ese segundo punto es de las comparaciones no evidentes que la rúbrica premia, y tal como está la tabla se va a perder.

### 2. La columna 7 puede meter un error grave

Ya la marqué en la hoja de captura, pero ahora con el detalle de por qué no hay de dónde llenarla:

- Las cifras de los proveedores sobre sí mismos **no son admisibles** como fuente primaria
- Las de los papers **no son comparables entre sí** — es tu hallazgo 14: el 42 mide punta a punta y el 47 solo la creación del sandbox
- Vicente mide solo dos o tres plataformas en 4.1
- Para las filas de código abierto el dato no significa nada sin decir en qué clúster

Quedan catorce filas y material honesto para tres o cuatro. El resto se llena con marketing o se deja vacío, y ninguna de las dos es buena.

### 3. La columna 9 no está definida

"Complejidad Operacional (Infraestructura / Red)" es el concepto correcto, pero nadie dijo **qué se escribe ahí**. Si cada uno pone texto libre, las filas dejan de ser comparables entre sí, que es justo lo que un cuadro comparativo tiene que lograr.

Esto en rigor es trabajo de Valentina: ella define y justifica los criterios, y sus criterios son las columnas. Nadie lo ha hecho.

---

## La omisión

**Se perdió "Estado / persistencia", y no es un detalle de gusto.** El subtema obligatorio de límites dice textualmente:

> *"Límites y dependencia del proveedor: tiempos máximos, tamaño de carga útil, **manejo de estado** y estrategias de portabilidad."*

La ficha nombra cuatro cosas. La tabla cubre dos: tiempos máximos y carga útil. Manejo de estado y portabilidad no están. Y la ficha además nombra explícitamente *"Cloudflare Workers (Durable Objects, D1, R2)"*, que es tu mitad.

---

## Las dos ambigüedades menores

- **Columna 3:** en el borde hay que decidir si va el tiempo de CPU o la duración total de la solicitud. No son lo mismo y en Cloudflare la diferencia es grande.
- **Columna 6:** "concurrencia" significa dos cosas distintas — solicitudes simultáneas por instancia, o instancias simultáneas máximas. Si cada fila usa una acepción, la columna no compara nada.

Las dos se arreglan con una convención escrita, no cambiando la tabla.

---

## Un problema práctico

Nueve columnas por catorce filas no entra en vertical. Las siete columnas anteriores ya sumaban 14 cm. Va a necesitar `\begin{landscape}` — `pdflscape` ya está cargado en `main.tex` — y aun así va apretado.

Una alternativa que probablemente quede mejor: **partirlo en dos cuadros**, uno de límites técnicos (columnas 1 a 6) y otro de costo y operación (1, 2, 7, 8, 9). Cumple igual el entregable de la ficha, entra sin comprimir y deja espacio para la columna de estado que falta.

---

Resumiendo: la estructura de Rodolfo es mejor que la que había en `main.tex`, pero el encabezado de la columna 8 hay que corregirlo sí o sí porque es un error factual sobre tu mitad, la 7 necesita una regla de llenado antes de que alguien la complete, y la 9 necesita que Valentina la defina.

¿Te armo el mensaje para Rodolfo con esto? Conviene que le llegue antes de que empiece a llenar celdas.

## Persona — prompt 9 — 19-09-2026 15:24

```text
si armame un breve .md con lo que encontraste, que sea claro y conciso
```

### Claude Code — 19-09-2026 15:24

Written for: Rodolfo (integrante 6), enviado por Claudio.

### Claude Code — 19-09-2026 15:24

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 15:24

Listo: [Sesion-actual-19-09/Revision-tabla-3.2-para-Rodolfo.md](Sesion-actual-19-09/Revision-tabla-3.2-para-Rodolfo.md)

Está escrito en tu voz, para enviárselo directamente. Abre reconociendo lo que quedó bien —la estructura suya es mejor que la que había— y después van los cuatro problemas ordenados por urgencia, cada uno con la regla que lo respalda y una propuesta concreta.

Incluí también lo de la planilla (las fuentes 31 y 33 no admisibles, y los papers 46 y 47 mal asignados a 3.2), porque eso todavía no se lo habías pasado y es de su mitad.

Cierra con cinco preguntas concretas. Las tres primeras destraban el llenado de celdas; las dos últimas son las decisiones que tienes pendientes sobre tu propio alcance.

## Persona — prompt 10 — 19-09-2026 15:27

```text
de igual manera no se bien que es lo que hace rodolfo, me podrias explicar brevemente?
```

### Claude Code — 19-09-2026 15:27

Rodolfo es el integrante 6, y es tu contraparte directa: comparten la sección 3.2. Tiene tres trabajos.

## 1. Su mitad del cuadro: AWS y Azure

Levanta límites técnicos y precio de lista fechado de nueve productos:

**AWS:** Lambda, Fargate, App Runner, Lambda@Edge, CloudFront Functions
**Azure:** Azure Functions, Container Apps
**Datos:** Aurora Serverless, DynamoDB

Tú levantas la otra mitad: Google, Cloudflare, Fastly, Deno/Vercel/Netlify y código abierto.

> Nota útil: esa lista confirma que **Neon no es suyo**, porque no es de AWS ni de Azure. Por eso tiene sentido tu pregunta 4.

## 2. Consolida la tabla

Une las dos mitades en un solo cuadro. Por eso te conviene entregarle tus filas ya en formato `\filaTabla{}`, para que solo las pegue, y por eso importa que el formato de celda de precio sea idéntico en ambas mitades: si no, la tabla queda despareja y se nota.

## 3. Escribe los dos párrafos de análisis del cuadro

Esta es la parte que más te afecta. El comentario en `main.tex` dice que las comparaciones no evidentes valen más que leer la tabla en voz alta. **Ese análisis lo construye con tus celdas y con las suyas.**

Por eso las cosas que te señalé no son formalismo: si la columna de cold start se llena con cifras no comparables, o si la celda de código abierto queda vacía en vez de decir por qué no hay precio de lista, él se queda sin material para argumentar.

---

## Por qué la coordinación con él pesa tanto

La guía dice algo que va más allá de ustedes dos:

> *"Los precios se levantan una sola vez en el cuadro 3.2 (integrantes 6 y 7). Las secciones 2.3, 4.2 y 4.3 citan esa tabla."*

O sea, entre los dos son **la única fuente de precios de todo el informe**. Francisca (modelo de costos), Fabián (caso TERABYTE) y quien escriba 2.3 citan la tabla de ustedes en vez de buscar cifras por su cuenta. Si un precio no está, se lo piden a ustedes.

Eso explica por qué el punto 5 es tan estricto y por qué vale la pena arreglar el encabezado antes de llenar: un error ahí se propaga a tres secciones más.

## Lo que ya hizo

En la planilla aparece como revisor parcial de las fuentes 18, 22, 25 y 32 — las páginas oficiales de AWS y Azure. Ya empezó por su mitad.

También es quien asignó los papers 46 y 47 y las fuentes 31 y 33 a "3.2 Criterios y cuadro". Ahí está el desacuerdo que le planteas en el punto 7 del mensaje: tú los revisaste en detalle y concluiste que no corresponden.

## Quién más toca 3.2

**Valentina** (integrante 5) define y justifica los criterios de comparación, que son las columnas del cuadro. Debía acordarlos con ustedes dos **antes** de que llenaran la tabla. No lo ha hecho, y por eso la columna de complejidad operacional quedó sin definir.

## Persona — prompt 11 — 19-09-2026 15:32

```text
comprendo, entonces nos faltan los criterios de valentina, tanto a mi como a rodolfo?, podemos armar mi tabla y lo que debo hacer, con supuestos? ya que de valentina aun no sabemos nada, asi que no se si se pueda avanzar con supuestos a modo de tamplate, para que cuando sea el momento de usar los datos reales, sea mas facil avanzar desde una base, crees que eso este bien? de serlo dejame anotado en un .md lo que seria, y como seria este supuesto
```

### Claude Code — 19-09-2026 15:33

Sí, está bien, y además es lo correcto. La razón es concreta: **los criterios afectan la presentación, no los datos.** El límite de tiempo de Cloudflare Workers es el mismo sea cual sea la columna donde termine. Recolectar datos nunca es trabajo perdido; lo peor que pasa es que sobre un dato.

Y hay algo más fuerte: las tres dimensiones ya están fijadas por la ficha —costo, latencia y complejidad operacional—, así que Valentina no puede inventar otras. El supuesto no es una adivinanza, es una derivación.

### Claude Code — 19-09-2026 15:33

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 15:33

Listo: [Sesion-actual-19-09/Supuesto-columnas-y-captura.md](Sesion-actual-19-09/Supuesto-columnas-y-captura.md)

Tres cosas que vale la pena destacar del enfoque:

**El supuesto no es inventado.** Las tres dimensiones vienen de la ficha, que dice textualmente que hay que determinar en qué condiciones conviene cada modelo "en costo, latencia y complejidad operacional". Valentina no puede reemplazarlas: le toca justificarlas y decir cómo se miden. Por eso las columnas 7, 8 y 9 están fuera de discusión, y las demás salen del subtema 2.6 ("tiempos máximos, tamaño de carga útil, manejo de estado"). Agregué la columna de estado que se había perdido, por esa misma razón.

**Donde hay ambigüedad, capturas las dos versiones.** En tiempo de ejecución anotas tiempo de CPU y duración total; en concurrencia, las dos acepciones. Estando en la misma página cuesta segundos, y te deja inmune a cualquier convención que se decida después.

**La hoja está organizada por página, no por columna.** Eso es lo que baja el costo real: la página de límites de Cloudflare te da tiempo, memoria, payload y concurrencia de una sola visita. Son 13 visitas, no 200 datos sueltos. Y arranca por Deno Deploy, que es la única que trae límites y precio junto.

El mapa de reconciliación de la sección 4 es el que responde tu pregunta de fondo: en ninguna rama pierdes el trabajo de terreno. Lo peor que pasa es que Valentina agregue un criterio nuevo y tengas que volver a las mismas páginas por un dato más.

Una cosa que sí conviene hacer antes de empezar: mandarle a Valentina las diez columnas hoy, avisándole que si no hay contraorden avanzas con esas. Así no queda pasada a llevar —recibe un borrador que corregir en vez de una página en blanco— y tú tienes registro de que se pidió.

Lo único que queda como hueco explícito es el párrafo que justifica los criterios. Ese es suyo, y el punto 6.1 lo nombra entre lo que debe ser de autoría humana del responsable.

## Persona — prompt 12 — 19-09-2026 15:35

```text
pero ya que valentina aun no progresa en su parte nosotros no podemos progresar?, no comprendo bien la parte de valentina
```

### Claude Code — 19-09-2026 15:36

No, no te bloquea. Déjame mostrarte por qué, porque creo que el problema es que su parte suena más grande de lo que es.

## Qué entrega Valentina en 3.2, literalmente

Esto es lo que está en `main.tex`, esperándola:

```
\tabla{Criterios de comparación}{criterios}{...}{%
    \filaTabla{Criterio        & Por qué importa & Cómo se mide en el cuadro}
    \filaTabla{Costo                   &  &  }
    \filaTabla{Latencia                &  &  }
    \filaTabla{Complejidad operacional &  &  }
}
```

**Un párrafo y seis celdas.** Eso es todo lo que le toca en 3.2.

Y fíjate en algo importante: **los tres criterios ya están escritos.** Costo, latencia y complejidad operacional. No los elige ella — vienen de la ficha, que dice que hay que determinar en qué condiciones conviene cada modelo *"en costo, latencia y complejidad operacional"*.

Su trabajo es llenar las otras dos columnas: por qué cada criterio importa, y cómo se mide en el cuadro.

## La sección 3.2 tiene tres partes

| Parte | Quién | Qué es |
|---|---|---|
| Apertura | **Valentina** | "Vamos a comparar estas tres cosas, y por estas razones" |
| El cuadro | **Tú y Rodolfo** | Los datos: límites y precios de cada plataforma |
| Cierre | **Rodolfo** | "Esto es lo que se ve en el cuadro" |

Ella escribe la introducción de la sección. Tú produces el contenido. Rodolfo lo interpreta.

**La introducción no bloquea el contenido.** Se puede escribir al final, igual que el resumen ejecutivo y la introducción del informe completo, que también se escriben cuando todo lo demás ya está.

## Lo único que sí depende de ella

Una sola cosa, y es menor: **cómo se mide cada criterio.**

Por ejemplo, para complejidad operacional ella podría decir que se mide como "cuántos componentes hay que operar" o como "¿requiere Kubernetes, sí o no?". Son dos formas distintas de escribir la misma celda.

Pero fíjate: eso cambia **cómo redactas la celda**, no **qué dato vas a buscar**. En los dos casos tienes que abrir la documentación de Knative y averiguar qué hay que operar para que funcione. El dato es el mismo.

Por eso en la hoja de captura te puse que anotes las dos versiones donde hay ambigüedad: llegas con material para cualquier redacción que ella elija.

## Entonces

Puedes empezar ahora mismo con las trece visitas. Lo que no puedes hacer es **escribir el párrafo de ella**, por dos razones: es su sección, y el punto 6.1 nombra "la justificación de los criterios utilizados" entre lo que tiene que ser de autoría humana del responsable.

Ese párrafo queda como hueco marcado en el `main.tex`. Si el domingo por la noche sigue vacío, ahí el grupo decide qué hacer, pero eso es una conversación de grupo, no tuya.

Lo único que conviene que hagas hoy es mandarle las diez columnas por escrito, avisándole que avanzas con esas si no hay contraorden. No para pedirle permiso, sino para que tenga la oportunidad de corregir y quede registro de que se le consultó.

## Persona — prompt 13 — 19-09-2026 15:38

```text
entonces, de valentina solo tiene que rellenar los 3 criterios, yo debo hacer la tabla y rodolfo interpretar la tabla?
```

### Claude Code — 19-09-2026 15:38

Casi. Dos correcciones.

## Corrección 1: Rodolfo no solo interpreta

Él hace **tres** cosas:

1. Llena **su mitad** del cuadro: AWS y Azure (Lambda, Fargate, App Runner, Lambda@Edge, CloudFront Functions, Azure Functions, Container Apps, Aurora Serverless, DynamoDB)
2. Une las dos mitades en una sola tabla
3. Escribe los dos párrafos de análisis

Tú no haces "la tabla": haces **la mitad** de las filas. La otra mitad es suya.

## Corrección 2: te estás olvidando de tu parte más grande

En tu resumen solo aparece el cuadro, pero el cuadro es la parte **menos** escrita de tu trabajo. Ahí produces celdas.

Tu entregable principal de redacción es **3.1**, que nadie más toca.

## Así queda la sección 3 completa

| Pieza | Quién | Qué produce |
|---|---|---|
| **3.1 Alternativas adicionales** | **Claudio** | Dos párrafos + tabla de 10 filas con las justificaciones |
| 3.2 · párrafo y tabla de criterios | Valentina | Un párrafo + 6 celdas |
| 3.2 · filas del cuadro, mitad Google/Cloudflare/Fastly/Deno/open source | **Claudio** | Celdas con datos |
| 3.2 · filas del cuadro, mitad AWS/Azure | Rodolfo | Celdas con datos |
| 3.2 · consolidación de la tabla | Rodolfo | Junta las dos mitades |
| 3.2 · dos párrafos de análisis | Rodolfo | Interpretación |
| **Anexo D · búsqueda documentada** | **Claudio** | Criterios + tabla de 5 filas + descartes |

Tres de las siete piezas son tuyas, y las dos que llevan redacción propia (3.1 y el Anexo D) no dependen de nadie.

Por eso Valentina no te bloquea: su pieza y las tuyas no se tocan.

## Persona — prompt 14 — 19-09-2026 15:39

```text
entonces puedo comenzar ya lo que es mi seccion?
```

### Claude Code — 19-09-2026 15:39

Sí. Nada te bloquea.

## Antes de empezar, cinco minutos

Manda los dos mensajes primero, porque las respuestas llegan mientras trabajas:

1. **A Rodolfo:** el archivo [Revision-tabla-3.2-para-Rodolfo.md](Sesion-actual-19-09/Revision-tabla-3.2-para-Rodolfo.md) ya está listo para enviar.
2. **A Valentina:** las diez columnas supuestas, avisando que avanzas con esas si no hay contraorden. Así queda registro de que se consultó.

## Después, partir por la visita 1

**Deno Deploy** (fuente 24 de la planilla). Es la única página que trae límites y precio junto, así que es la fila que se completa más rápido y sirve para tomar ritmo y calibrar cuánto demora cada una.

Las trece visitas están en [Supuesto-columnas-y-captura.md](Sesion-actual-19-09/Supuesto-columnas-y-captura.md) §3, en orden. Puedes llenar los bloques directamente en ese archivo.

## La única disciplina que importa hoy

**URL y fecha en el momento, en cada dato.** No "después lo anoto". Un dato sin fecha no es válido según el punto 5, y recuperar la fuente al día siguiente cuesta más que anotarla ahora.

Y donde haya ambigüedad —tiempo de CPU frente a duración total, las dos acepciones de concurrencia— anota las dos. Estando en la página cuesta segundos.

## Cómo sabes que el día está cumplido

- Las trece visitas hechas, con fecha en cada celda
- Los candidatos de 3.1 verificados: cuáles existen, cuáles están archivados
- Las fuentes nuevas agregadas a la planilla

Con eso, mañana solo te queda escribir: las diez justificaciones, los dos párrafos de 3.1 y el Anexo D.

Cuando tengas los datos levantados, avísame y revisamos que ninguna celda haya quedado sin fecha ni sin región antes de que se la pases a Rodolfo.

## Persona — prompt 15 — 19-09-2026 15:40

```text
cuales son mis 10 columnas?
```

### Claude Code — 19-09-2026 15:40

Son las nueve de Rodolfo más la de estado que estás recuperando:

| # | Columna | De dónde sale |
|---|---|---|
| 1 | Servicio | Estructural |
| 2 | Categoría | Estructural |
| 3 | Tiempo máx. de ejecución | Ficha, subtema 2.6: *"tiempos máximos"* |
| 4 | Rango de memoria / vCPU | Necesario para leer el precio (se cobra por GB-s) |
| 5 | Límite de payload (entrada / salida) | Ficha, subtema 2.6: *"tamaño de carga útil"* |
| 6 | Concurrencia / escalado | Costo y complejidad |
| 7 | **Latencia / arranque en frío** | **Dimensión 2 de la ficha** |
| 8 | **Modelo de cobro y precio fechado** | **Dimensión 1 de la ficha** |
| 9 | **Complejidad operacional** | **Dimensión 3 de la ficha** |
| 10 | Estado / persistencia | Ficha, subtema 2.6: *"manejo de estado"* |

Las tres en negrita son **exactamente sus tres criterios**. Ese es el punto que conviene que ella vea: sus criterios no son un texto aparte, son tres columnas del cuadro.

## Mensaje listo para enviarle

> Valentina: estoy por llenar mi mitad del cuadro 3.2 (Google, Cloudflare, Fastly, Deno, código abierto). Como los criterios son la apertura de la sección y todavía no los tenemos, te dejo las columnas con las que pienso avanzar, para que las corrijas si algo no calza.
>
> Son diez: Servicio · Categoría · Tiempo máximo de ejecución · Rango de memoria/vCPU · Límite de payload (entrada/salida) · Concurrencia/escalado · Latencia y arranque en frío · Modelo de cobro y precio fechado · Complejidad operacional · Estado/persistencia.
>
> Las tres últimas de contenido —latencia, cobro y complejidad operacional— son justamente tus tres criterios, que salen del alcance de la ficha. Las otras salen del subtema 2.6 (tiempos máximos, tamaño de carga útil, manejo de estado).
>
> Lo que falta de tu parte es el párrafo que justifica los criterios y la tabla de tres filas que ya está armada en el `main.tex`: por cada criterio, "por qué importa" y "cómo se mide en el cuadro". Eso no lo puedo escribir yo, es tuyo y además el punto 6.1 lo exige de autoría humana del responsable.
>
> Si no hay contraorden, avanzo con estas columnas y levanto los datos. Si después cambias cómo se mide algún criterio, se reescribe la celda sin tener que volver a las fuentes.

Con eso enviado, arranca por Deno Deploy.

## Persona — prompt 16 — 19-09-2026 15:49

```text
igual recordar evitar el sesgo de los papers y no basarnos 100% en los unicos que tenemos ya que son 47 y mas, ya que Daniel estuvo allando mas papers que pueden sernos utiles, solo que aun no comprendo que es lo que se va hacer en mi parte y secciones de valentina y rodolfo, ya que se que hacemos las partes 3.1 y 3.2 pero aun me confunde cual es el trabajo a realizar
```

### Claude Code — 19-09-2026 15:50

Tienes razón en lo de los papers, y te lo respondo abajo. Pero primero el otro punto, porque creo que sé dónde está la confusión.

**La división del cuadro es por filas, no por columnas.** Tú y Rodolfo no se reparten columnas: llenan las mismas diez columnas, pero en filas distintas. Él llena la fila de AWS Lambda completa; tú llenas la fila de Cloudflare Workers completa.

Te dejo el dibujo de cómo queda la sección terminada.

### Claude Code — 19-09-2026 15:50

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 15:50

[Sesion-actual-19-09/Como-se-ve-la-seccion-3.md](Sesion-actual-19-09/Como-se-ve-la-seccion-3.md)

---

# Sobre el sesgo de los papers

Tu punto es correcto y vale la pena precisarlo, porque en tu sección el riesgo es distinto al del resto del informe.

## En tu sección los papers son secundarios

Para 3.2 no sirven en absoluto: los precios y límites salen de documentación oficial, y el punto 5 lo obliga. Ahí no hay sesgo posible porque no se usan.

Para 3.1 sirven como **cantera de nombres**, no como evidencia. Y ahí sí hay un riesgo, pero no es el que uno esperaría.

## El riesgo real: que el corpus defina tu lista

Si sacas tus diez alternativas solo de lo que los papers mencionan, tu sección hereda los sesgos de esa literatura: papers académicos de 2021-2023, con fuerte inclinación a IoT y fog, y que casi no miran el borde comercial de CDN.

Fíjate en la prueba: **Fly.io, Koyeb, Render, Railway, Bunny, Supabase, Turso y Upstash no aparecen en ningún paper del corpus.** Salieron de la tabla de la guía del equipo. Y varios son mejores candidatos que los que sí aparecen, porque están disponibles comercialmente y publican límites, que es tu criterio de inclusión.

Al revés también: los papers te dieron Serverledge, Colony, funcX, tinyFaaS, Faasm, Sledge y DFaaS — siete nombres que **descartaste todos** por ser prototipos de investigación.

O sea: el corpus produjo más descartes que candidatos. Eso confirma que no puede ser tu fuente principal.

## Qué hacer entonces

Buscar por tu cuenta, además de los papers:

- **El landscape de la CNCF**, que es donde están los proyectos de código abierto vivos
- **Las páginas de los propios proveedores**, donde se nombran competidores y productos equivalentes
- **La tabla de la guía del equipo**, que ya trae ~30 candidatos sin origen académico

Y eso queda registrado en el Anexo D como "fuentes consultadas". Una búsqueda que solo mira papers es una búsqueda incompleta, y el punto 4 pide documentar dónde se buscó.

## Sobre los papers nuevos de Daniel

Pídele lo mismo que al resto: **solo los nombres de plataformas que aparezcan y que no estén en la ficha**, con página. No necesitas leerlos.

Pero ojo con el calendario: un paper que llegue mañana por la tarde no alcanza a entrar verificado, y una alternativa sin verificar no la pones. Si llegan hoy, entran; si llegan mañana, se anotan en el Anexo D como encontradas fuera de plazo de verificación. Eso también es búsqueda documentada honesta.

## Persona — prompt 17 — 19-09-2026 16:50

```text
dentro de chats anteriores, deje un .txt, que me mando valentina, pormientras podemos trabajar con eso?
```

### Claude Code — 19-09-2026 16:50

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 16:50

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 16:51

Valentina entregó, y entregó bien. Esto no es un provisorio: es la definición real, y es mejor que el supuesto que armamos.

Déjame actualizarte la hoja de captura, porque cambia lo que tienes que anotar.

### Claude Code — 19-09-2026 16:52

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 16:52

Sí, y mejor que "mientras tanto": esto es la definición final. [Captura-definitiva-mi-mitad.md](Sesion-actual-19-09/Captura-definitiva-mi-mitad.md) reemplaza a las dos hojas anteriores.

## Lo que confirmó

Dio **luz verde a las siete columnas descriptivas, incluida estado**. Tu supuesto estaba bien.

## Lo que resolvió mejor que nosotros

La columna de latencia que yo había marcado como peligrosa: ella la volvió **documental en vez de numérica**. Ya no lleva cifras, lleva el modelo de aislamiento que declara la documentación y el mecanismo de mitigación que ofrece la plataforma, diciendo si se factura. Las cifras medidas se remiten a 4.1, y lo no medido dice «no medido». Así el riesgo de meter marketing o cifras no comparables desaparece.

Y llegó por su cuenta a lo mismo que tú sobre las fuentes 31 y 33: inadmisibles según el punto 5. Que dos personas lo detecten por separado le da mucho más peso frente a Rodolfo.

> Un detalle a aclarar: ella dice que esas dos fuentes "estaban recomendadas en el .md de fuentes que circuló". Tu `Papers-relevantes-para-3.md` dice exactamente lo contrario —las marca como no admisibles—, así que o hay otro documento dando vueltas o leyó mal el tuyo. Conviene aclararlo en una línea.

## Dos correcciones a lo que yo te había dicho

**Fastly: me equivoqué.** Te dije que si no publicaba precios pusieras «solo por cotización». Ella verificó y sí publica precios de uso por tramos; solo los paquetes Advantage y Ultimate son por cotización, y hay tarifas heredadas para cuentas anteriores a noviembre de 2025. La celda tiene que decir qué régimen cita.

**La fecha del `.bib` es del 15 de septiembre.** Si reabres una página, va la fecha de hoy, no se hereda.

## Dos hallazgos suyos que caen justo en tu mitad

**El piso mensual fijo.** Workers tiene cargo mínimo por cuenta al mes y los paquetes de Fastly parten en una cifra mensual alta. Como ella dice, eso rompe el supuesto de que escalar a cero es pagar cero, y rompe justo en el rango de volumen bajo donde está el caso de ustedes. Cloudflare y Fastly son tus dos filas: ese campo no puede quedar vacío.

**El refuerzo de CPU al arranque de Cloud Run se cobra.** Cloud Run también es tuyo.

## Dos cosas que conviene preguntarle hoy

Ella lo pidió: *"díganmelo ahora y lo ajusto antes, no después."*

1. **Complejidad operacional se solapa.** Tres de sus cuatro campos ya están en otras columnas: tiempo máximo repite la columna 3, payload repite la 5, y mínimo facturable repite el tercer campo de costo.

2. **Las filas de código abierto quedan vacías.** En Knative, OpenFaaS y Spin los cuatro campos dan "configurable", justo donde la complejidad operacional es la diferencia real. Propón agregar "qué tiene que operar el equipo". Tienes respaldo verificado: paper 43 p. 1531 y paper 13 p. 3-4.

Son ahora 16 campos por fila y 16 visitas. Empieza igual por Deno Deploy.

## Persona — prompt 18 — 19-09-2026 16:55

```text
entonces con estos cambios en relacion a como estaba antes, que cambia y que se mantiene?
```

### Claude Code — 19-09-2026 16:56

## Cambia

| | Antes | Ahora |
|---|---|---|
| **Estructura de las 3 columnas de criterio** | Celdas de texto libre | **Campos definidos**: costo 3, latencia 2, complejidad 4 |
| **Total a capturar** | 10 columnas | **16 campos** por fila |
| **Columna de latencia** | Numérica, y yo la había marcado como peligrosa | **Documental**: aislamiento declarado + mecanismo de mitigación. Sin cifras. Lo no medido dice «no medido» |
| **Fastly** | «solo por cotización» | **Publica precios por tramos.** La celda dice qué régimen cita: uso por tramos, paquete por cotización, o tarifa heredada anterior a noviembre 2025 |
| **Formato del precio** | producto · moneda · región · fecha · tipo | Lo mismo **+ tramo de volumen + base temporal de la unidad** |
| **Piso mensual** | No existía | **Campo obligatorio (C3).** Cloudflare y Fastly tienen mínimo mensual: escalar a cero no es pagar cero |
| **Mitigación de cold start** | No existía | **Campo obligatorio (L2), indicando si se factura.** El refuerzo de arranque de Cloud Run se cobra |
| **Fechas** | No estaba dicho | La del `.bib` es del 15-sep. **No se hereda**: si reabres la página, va la de hoy |
| **Visitas** | 13 | 16, pero solo **una es realmente nueva**: la configuración de CPU de Cloud Run. Las otras dos ya las tenías marcadas como faltantes, solo que ahora sabes qué buscar en ellas |

## Se mantiene

| | Estado |
|---|---|
| **Las 7 columnas descriptivas** | Aprobadas tal cual, **incluida estado**. Tu supuesto estaba bien |
| **3.1 completo** | **Intacto.** Nada de esto lo toca. Sigue siendo tu entregable escrito principal |
| **Anexo D** | Intacto |
| **Tus ~30 candidatos** | Intactos |
| **El reparto** | Igual: tus filas, las de Rodolfo, él consolida y analiza |
| **Región y fecha en la celda, no en el encabezado** | Confirmado — el campo C2 de ella lo incluye |
| **Fuentes 31 y 33 inadmisibles** | Confirmado, y ella llegó por su cuenta |
| **El orden de visitas** | Igual: partir por Deno Deploy |
| **URL y fecha en el momento** | Igual, y ahora más importante |
| **El rol de los papers** | Igual: cantera para 3.1, no fuente para 3.2 |

## Queda abierto

1. El solapamiento de complejidad operacional — preguntarle a ella hoy
2. Las filas de código abierto sin contenido — preguntarle a ella hoy
3. Vercel, Netlify y Neon — Rodolfo
4. Una tabla o dos, y si va apaisada — Rodolfo
5. Si Rodolfo acepta sacar `us-east-1` del encabezado

---

**Lo que esto significa en tiempo:** los campos subieron de 10 a 16, pero las visitas casi no cambiaron. Y lo que cuesta son las visitas, no los campos: estando en la página de precios de Cloudflare, anotar el piso mensual además del precio toma segundos.

Lo importante es que **3.1 y el Anexo D no se movieron**. Tu trabajo de redacción del domingo sigue idéntico.

## Persona — prompt 19 — 19-09-2026 16:58

```text
armame un .md con las consultas para cada uno, tanto como para valentina como para rodolfo a ver que es lo que me dicen
```

### Claude Code — 19-09-2026 16:58

Written for: Valentina (integrante 5) y Rodolfo (integrante 6), enviados por Claudio.

### Claude Code — 19-09-2026 16:59

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 16:59

[Sesion-actual-19-09/Consultas-pendientes.md](Sesion-actual-19-09/Consultas-pendientes.md)

Los dos mensajes están listos para copiar y pegar, escritos en tu voz.

**A Valentina** van cuatro puntos: los dos problemas que encontramos (el solapamiento de complejidad operacional y las filas de código abierto sin contenido), la aclaración sobre el `.md` que según ella recomendaba las fuentes inadmisibles, y el aviso de que te haces cargo de sus tres hallazgos porque caen en tu mitad.

Para el solapamiento usé su propio argumento: ella dijo que las dos mitades tienen que medir igual, y si Rodolfo y tú interpretan esos campos distinto, no van a medir igual. Eso hace que la pregunta sea difícil de postergar.

**A Rodolfo** le van cuatro preguntas, menos de las que tenía antes: Valentina ya resolvió la regla de la columna de latencia y, de paso, el encabezado, porque su formato de precio exige región por celda. Lo que queda es si el cuadro se parte en dos, Vercel y Netlify, Neon, y el formato de celda.

Agregué al final los dos pedidos cortos a Isidora y a Daniel, con plazo explícito para el de Daniel: lo que llegue después de mañana al mediodía no alcanza a verificarse, y queda en el Anexo D como encontrado fuera de plazo.

Mándalos y arranca por Deno Deploy. Ninguna de esas respuestas te bloquea el levantamiento.

## Persona — prompt 20 — 19-09-2026 17:03

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Sesion-actual-19-09\Consultas-pendientes.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

te dije que me hicieras un .md para valentina y otro para rodolfo
```

### Claude Code — 19-09-2026 17:04

Tienes razón, lo entendí mal. Dos archivos separados.

### Claude Code — 19-09-2026 17:04

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 17:04

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 17:04

Written for: Valentina y Rodolfo respectivamente, enviados por ti.

- [Consulta-Valentina.md](Sesion-actual-19-09/Consulta-Valentina.md) — el solapamiento de complejidad operacional, las filas de código abierto sin contenido, la aclaración del `.md`, y el aviso de que te haces cargo de sus tres hallazgos.
- [Consulta-Rodolfo.md](Sesion-actual-19-09/Consulta-Rodolfo.md) — qué cambió con los criterios, las cuatro preguntas abiertas, y las dos cosas de la planilla que le tocan.

Cada uno es autónomo, así que puedes mandarlos por separado sin que falte contexto.

El combinado [Consulta-pendientes.md](Sesion-actual-19-09/Consultas-pendientes.md) quedó superado; lo puedes borrar cuando quieras. Lo único que tenía y que no pasó a los otros dos son tus dos pedidos cortos, que van por WhatsApp y no necesitan archivo:

**A Isidora:** los nombres de plataformas que aparezcan en los papers 36 y 37, que ella ya revisó, y que no estén en las cinco listas de la ficha. Solo nombre y página.

**A Daniel:** lo mismo con los papers nuevos que está encontrando, con plazo explícito — lo que llegue después de mañana al mediodía no alcanza a verificarse y queda en el Anexo D como encontrado fuera de plazo.

## Persona — prompt 21 — 19-09-2026 17:18

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Sesion-actual-19-09\Consulta-Rodolfo.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey, aun asi teniendo en cuenta eso, rodolfo me mando sus tablas, mas o menos como es que las fue rellenando, las tengo en unos pdfs, llamados borradores_tabla_3.2 y apuntes secciones informe, aqui esta lo que ha hecho rodolfo dime que tal va, analiza de manera exaustiva y detallada, para no dejarnos nada por alto
```

### Claude Code — 19-09-2026 17:18

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 17:18

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 17:18

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 17:19

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 17:19

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 17:20

Analicé los dos PDF a fondo. Hay bastante que rescatar y cuatro problemas serios.

### Claude Code — 19-09-2026 17:21

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 17:22

[Sesion-actual-19-09/Analisis-borrador-Rodolfo.md](Sesion-actual-19-09/Analisis-borrador-Rodolfo.md)

## Va bien, mejor de lo que esperaba

Nueve filas completas, fuentes oficiales identificadas una por una, cifras al nivel de decimales, y varios hallazgos que ningún paper del corpus aporta. Él mismo cierra con *"me falta revisar full a mano esto"*, así que lo entrega como borrador.

Verifiqué dos de sus cálculos y están correctos: Lambda@Edge cuesta exactamente 3,0× el cómputo de Lambda estándar, y ARM es exactamente −20 %. Y su precio de Azure ($0,000016/GB-s) **confirma tu hallazgo 1**: el paper 47 tiene el error de factor 10.

## Cuatro problemas

**1. Las celdas de precio no cumplen el punto 5.** Ninguna de las nueve filas indica región ni fecha *dentro de la celda*. Las fechas existen, pero en la lista de fuentes del final. Como "una cifra sin fecha no se considera válida", formalmente las nueve cifras son inválidas — y este cuadro es la fuente de precios de todo el informe. Se arregla bajando la información a la celda, sin volver a las fuentes.

**2. Armó esto antes de que llegaran los criterios de Valentina.** Le falta la columna de estado, la complejidad operacional está llena de calificaciones subjetivas ("Baja", "Media-alta") que ella prohibió expresamente, y el cold start está lleno de cifras que ella sacó del cuadro. Lo bueno: el texto que sigue a los dos puntos en complejidad sí es evidencia, y las mitigaciones con precio ya están levantadas. Es reordenar, no rehacer.

**3. Se perdió el hallazgo más importante del borrador.** En App Runner escribe "ver hallazgo crítico abajo" y cita como fuente *"AWS App Runner — Availability change (cerrado a nuevos clientes)"*. Pero el hallazgo no está en el PDF.

Eso te importa directamente: **App Runner está nombrado en la ficha.** Si está cerrado a nuevos clientes, tu 3.1 cambia de tono — las alternativas dejan de ser un complemento y pasan a ser un reemplazo. Pídeselo hoy.

**4. Los precios van a romper el LaTeX.** En el PDF varias cifras salieron corruptas (`0 , 12/ 𝐴𝐶𝑈 − ℎ`) porque los `$` se interpretaron como modo matemático. Lo mismo va a pasar en `main.tex`: hay que escapar cada uno como `\$`. Aplica a tu mitad también.

## Dos cosas que conviene mirar con calma

Sigue usando las fuentes 31 y 33, pero **las clasificó correctamente** como secundarias y no las usa para cifras. Mejor de lo que yo suponía. Aun así conviene sacarlas: InventiveHQ cae de plano en "artículos sin autoría verificable", y no aportan nada que la documentación oficial no cubra.

Y en la página 3 dice *"verificadas a fondo en tu revisión con Gemini"*. Eso hay que aclararlo sin acusar: si la IA buscó y él verificó en la fuente, es nivel 1 o 2 y basta declararlo; si las cifras salieron del modelo, el punto 6.1 lo prohíbe. Como 3.2 es compartida, afecta la declaración de ambos.

Ojo con una coincidencia: Valentina dijo que las fuentes 31 y 33 "estaban recomendadas en el `.md` de fuentes que circuló", y Rodolfo habla de "tu revisión con Gemini" cuando tú no hiciste ninguna. Parece haber un tercer documento de revisión dando vueltas que está influyendo en decisiones de tu sección. Vale la pena ubicarlo.

## Persona — prompt 22 — 19-09-2026 17:26

```text
puedes darme un .md con los allazgos para mandarselos a rodolfo? ademas de propuestas en base a las consultas que le mandamos anteriormente, sobre lo que podriamos realizar nosotros sin problema, y sobre las consultas a valentina, nos dijo que nosotros tomaramos ciertas decisiones que nos salgan a conveniencia, ya que ella ahora no tiene mucho tiempo para poder responderlas, que fueramos anotando los cambios que fuimos decidiendo, y las desiciones que fuimos tomando en base a lo primero que nos mando Valentin
```

### Claude Code — 19-09-2026 17:27

Con la delegación de Valentina podemos cerrar casi todo. Te dejo dos archivos: el que le mandas a Rodolfo, y el registro de decisiones que ella pidió que fueran anotando.

### Claude Code — 19-09-2026 17:28

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 17:28

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 17:29

Written for: Rodolfo el primero; el segundo es registro interno del equipo.

- [Hallazgos-y-propuestas-Rodolfo.md](Sesion-actual-19-09/Hallazgos-y-propuestas-Rodolfo.md) — listo para enviar
- [Registro-de-decisiones-3.2.md](Sesion-actual-19-09/Registro-de-decisiones-3.2.md) — la bitácora que pidió Valentina

## Lo que decidimos por ustedes

Con la delegación, cerré las dos consultas de Valentina y las cuatro de Rodolfo. Son **16 decisiones**, todas fundadas en su mensaje original, con quién decidió y por qué.

La más sustantiva: **el solapamiento se resolvió eliminando, no duplicando.** Sus cuatro campos de complejidad operacional se reducen a uno propio:

- Tiempo máximo según disparador → se absorbe en la columna Timeout (el hallazgo de los 230 s de Azure es exactamente eso)
- Carga útil → se elimina, ya está en Payload
- Granularidad y mínimo facturable → se eliminan, ya están en "unidad de cobro" y "piso mensual"
- Qué obliga a externalizar → se fusiona con la columna Estado

Queda **"qué hay que operar"**, que es el campo nuevo que propusimos y el único que rescata las filas de código abierto.

Resultado: **14 campos únicos en vez de 16**, repartidos en dos tablas de 7 y 8 columnas. La reducción viene de sacar duplicados, no de bajar exigencia.

## Sobre el mensaje a Rodolfo

Abre con lo bueno, que es real: verifiqué dos de sus cálculos y están exactos, y su precio de Azure confirma tu hallazgo del error de factor 10 en el paper 47. Eso importa para el tono, porque después vienen cuatro correcciones.

Le pedí el hallazgo de App Runner con prioridad uno y le expliqué por qué te sirve a ti: si una de las cuatro opciones que nombra la ficha está cerrada a nuevos clientes, tu 3.1 deja de ser un complemento y pasa a ser un reemplazo.

La pregunta por Gemini la dejé sin carga, apoyada en que la declaración del Anexo A les toca a los dos y que declarar bien no baja la nota.

El registro queda además como evidencia de autoría para la parte C del Anexo A: decisiones de criterio, humanas, fechadas y fundadas.

## Persona — prompt 23 — 19-09-2026 19:38

```text
deje algunos cammbios que hizo rodolfo a su parte en unos pdfs llamados apuntes secciones, el no comprende bien porque hacer tanto incapie en  AWS AppRunner, analiza eso
```

### Claude Code — 19-09-2026 19:38

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 19:38

Hay dos archivos nuevos, ambos de las 19:35. Los leo.

### Claude Code — 19-09-2026 19:38

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 19:39

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 19:39

Leí los dos. El nuevo es el documento compartido del equipo con todas las secciones; el otro es la misma tabla condensada de antes, y ahí App Runner aparece como fila normal, sin la ⚠ ni la nota de "hallazgo crítico". Esas solo están en el borrador.

Sobre tu pregunta: **Rodolfo tiene parte de razón y yo exageré el énfasis.** Déjame separar lo que se sostiene de lo que no.

## Dónde me pasé

Lo llamé "lo más valioso del borrador" y le puse prioridad uno. Eso fue demasiado, por dos motivos:

**Ninguno de los dos ha visto la página.** Todo lo que tenemos es que él citó una URL y escribió "cerrado a nuevos clientes". El texto del hallazgo se perdió al exportar. Calificar de crítico algo cuya fuente nadie leyó es apresurado.

**Y el orden que le di está mal.** Puse App Runner por encima del problema de región y fecha en las celdas de precio. Eso es al revés: lo de región y fecha afecta a las nueve filas y deja todas las cifras formalmente inválidas según el punto 5. App Runner es una nota al pie en una fila. Su prioridad uno debería ser bajar región y fecha a las celdas.

## Dónde sí se sostiene

**App Runner no es un producto cualquiera: lo nombra la ficha.** En la lista de contenedores sin servidor hay exactamente cuatro productos nombrados —Cloud Run, Fargate, Container Apps y App Runner—, y uno de ellos estaría cerrado.

Eso importa por algo específico: significa que el grupo **verificó la lista de la ficha en vez de darla por buena**. La guía dice que descubrir que algo está descontinuado y descartarlo con fecha y fuente es aporte, pero lo dice de las alternativas que el grupo propone. Que aplique a un producto que la ficha misma nombra es más fuerte, y es raro de conseguir.

Para mi 3.1 cambia el tono del párrafo: si una de las cuatro opciones nombradas ya no admite clientes nuevos, buscar alternativas deja de ser un trámite y Fly.io, Koyeb o Render pasan a ser reemplazos. Y sirve a 2.6 y a 5, porque es el riesgo de dependencia del proveedor convertido en hecho con fecha.

## Lo que hay que hacer, sin discutirlo

El peso depende de qué diga la página, y eso se resuelve abriéndola:

| Si dice | Entonces |
|---|---|
| Cerrado a nuevos clientes, sin fecha de fin de soporte | Nota al pie en la fila y una frase en 3.1. La tabla no cambia |
| Cerrado, con fecha de fin de soporte anunciada | Se mantiene la fila con esa fecha, y entra en 3.1 y en 5 |
| En retiro o descontinuado | La fila se marca y el argumento de 3.1 cambia de tono |

En los tres casos **la fila se queda en el cuadro**: sus límites y precios no dejan de ser ciertos porque no acepte clientes nuevos.

Y el argumento que cierra la discusión sin necesidad de ponerse de acuerdo en la importancia: **cuesta una frase con su cita.** Si resulta significativo y lo omitimos, perdemos un aporte propio verificable que es difícil de conseguir. Si resulta menor y va como nota al pie, no perdimos nada. No hay razón para decidirlo antes de abrir la página.

## Dos cosas más del PDF nuevo

**Era Claude, no Gemini.** Escribe "Recopilé con Claude estos límites técnicos junto con su cifra". En el borrador decía "tu revisión con Gemini", que parece referirse a otra persona. Conviene aclararlo igual para el Anexo A, pero el tono cambia.

**Y ya está haciendo la pasada de verificación.** Dice textual: *"ahora estoy verificando la tabla como tal, cada tecnología con sus elementos correspondientes. No lo tomen como documentación final"*, y que se armó una planilla Excel para verificar las cifras. Ese es exactamente el proceso correcto —IA para recopilar, humano para verificar en la fuente—, así que la consulta sobre la declaración se puede suavizar bastante: es nivel 2 declarable y él ya está haciendo lo que corresponde.

¿Quieres que ajuste el mensaje para Rodolfo con este reordenamiento de prioridades y el tono más suave en lo de la IA?

## Persona — prompt 24 — 19-09-2026 19:40

```text
entonces, que necesito yo, para poder hacer mi parte tanto de valentina como de rodolfo?
```

### Claude Code — 19-09-2026 19:41

Respuesta corta: **de ellos, nada.** Déjame mostrarlo caso por caso, porque llevas varias preguntas girando en torno a esto.

## De Valentina

**Nada.** Ella delegó, y las decisiones ya están tomadas y registradas: los 16 campos quedaron definidos, el solapamiento se resolvió eliminando duplicados, y el campo "qué hay que operar" se agregó con respaldo. Todo está en el registro de decisiones con su fundamento.

Su entregable propio —el párrafo de criterios y la tabla de tres filas— es suyo y no toca tu trabajo. Si el domingo sigue vacío, es conversación de grupo, no tuya.

## De Rodolfo

Cuatro cosas, **ninguna bloqueante**:

| Qué | Para qué sirve | Si no llega |
|---|---|---|
| La fuente y fecha de App Runner | Una frase en 3.1 y una nota al pie | Escribes 3.1 completo y agregas la frase después. No reescribes nada |
| Confirmar las dos tablas | Formato al final | Entregas tus filas con los 14 campos; repartirlas en dos tablas es trabajo de consolidación, suyo |
| Vercel, Netlify, Neon | Cuántas filas levantas | **Ya decidido:** Vercel y Netlify fuera, Neon dentro. Son tus decisiones, están registradas |
| Formato de celda | Que consolidar sea pegar | **Ya definido** por ti en D16 |

## Lo que sí necesitas, y te lo das tú

1. **Un navegador y 16 visitas** — entre 2 y 3 horas. Están mapeadas en orden, con qué buscar en cada una.
2. **Verificar los ~30 candidatos** — 1,5 horas. ¿Existe? ¿Está archivado? ¿Publica límites?
3. **Tu criterio** para las 10 frases de justificación. Eso no te lo puede dar nadie, ni yo.
4. **Tiempo de escritura** — dos párrafos de 3.1, las 10 justificaciones y el Anexo D. Unas 2,5 horas.

## Lo que ya tienes en la mano

- Los 16 campos definidos y las 16 visitas en orden
- ~30 candidatos repartidos en las cinco listas, con su origen
- Dos lecturas transversales verificadas, con página
- Cinco descartes ya razonados para el Anexo D
- El BibTeX de 11 papers listo para pegar
- 16 decisiones tomadas y fundadas
- El formato de Rodolfo como plantilla, y su nivel de detalle como vara

## El reloj

Son las siete y media de la tarde del sábado. Entregan el lunes.

Tu trabajo son entre 6 y 8 horas. Tienes esta noche, todo el domingo y la mañana del lunes. **Alcanza con holgura, pero solo si empiezas ahora.** Cada hora que esperas una confirmación que no necesitas es una hora que le quitas a la verificación, que es lo único que no se puede acelerar ni delegar.

Parte por Deno Deploy: límites y precio en la misma página, y sirve para calibrar cuánto demora cada fila.

## Persona — prompt 25 — 19-09-2026 19:44

```text
okey entonces, crea una carpeta, donde iremos desarrollando lo que es nuestra parte, llamemosla "desarrollo", vayamos punto por punto a corde a lo que debemos abarcar, vayamos paso a paso con lo que nos piden, todo dentro demomento dentro de dos .md, desarrollo 3.1 y desarrollo 3.2
```

### Claude Code — 19-09-2026 19:45

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 19:45

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 19:46

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 19:46

Carpeta creada con los dos archivos de trabajo:

- [Desarrollo/Desarrollo-3.1.md](Desarrollo/Desarrollo-3.1.md)
- [Desarrollo/Desarrollo-3.2.md](Desarrollo/Desarrollo-3.2.md)

Cada uno arranca con **Paso 0: qué me piden**, citando textual la ficha y el punto de las Indicaciones que lo exige, para que no haya que ir a buscarlo a otro archivo. Después van los pasos en orden.

**En 3.1** hay seis pasos. El Paso 1 son los ~30 candidatos repartidos por lista, con su origen y columnas para marcar si existen, si publican límites y si entran. Los Pasos 3, 4 y 5 están marcados **[LO ESCRIBO YO]** y tienen el bloque de texto vacío: son las 10 justificaciones y los dos párrafos, que el punto 6.1 exige de autoría humana. Lo que sí dejé armado es el andamiaje —qué tiene que contener cada párrafo, en qué orden, y las cinco lecturas transversales con su respaldo y su estado de verificación.

**En 3.2** hay cinco pasos. Los 14 campos ya reflejan las decisiones que tomamos, y las 15 visitas están en orden con un bloque para llenar en cada una. En las visitas críticas dejé marcado el dato que hay que cazar: el piso mensual en Cloudflare y Fastly, el refuerzo de CPU facturado en Cloud Run, el régimen de precios en Fastly, y el "qué hay que operar" en las tres de código abierto.

Dos detalles que metí a propósito: separé Knative, OpenFaaS y Spin en filas distintas —agrupadas escondían justo la diferencia que el campo 14 quiere mostrar— y puse el recordatorio de escapar los `$` en los dos archivos, porque el problema que corrompió el PDF de Rodolfo va a pasar igual en LaTeX.

Empieza por la Visita 1. Deno Deploy trae límites y precio en la misma página, así que sirve para calibrar cuánto demora una fila completa.

## Persona — prompt 26 — 19-09-2026 19:57

```text
daniel me mando lo siguiente
```

### Claude Code — 19-09-2026 19:57

Esto encaja con lo que armamos: **los bloques B y C son tuyos**, casi literalmente.

| Bloque de Daniel | Qué es en tu trabajo | Dónde ya lo tienes |
|---|---|---|
| **B · Límites y precios** | Tu mitad del cuadro 3.2 | `Desarrollo-3.2.md`, 15 visitas mapeadas |
| **C · Alternativas y datos serverless** | Tu 3.1 + Anexo D | `Desarrollo-3.1.md`, ~30 candidatos con tabla de verificación |

Los bloques A y D no te tocan: alimentan 1, 2.1-2.6, 2.4, 2.5 y 5.

Y confirma dos cosas que ya teníamos: el CNCF Landscape como fuente de búsqueda, y que el bloque B *"es el que más exige fecha, moneda y región en cada una"*, que es justo la disciplina del punto 5.

## Tres cosas que hay que aclarar con él

**1. A la tabla le falta la columna "quién".**

Dice qué contiene cada bloque y qué secciones alimenta, pero no quién lo levanta. Si B y C son míos porque son mis secciones, perfecto. Si está repartiendo el trabajo de otra forma, hay que saberlo ahora.

**2. El bloque B se estira más allá del cuadro 3.2.**

Incluye *"los precios always-on (EC2, Compute Engine, ECS/GKE) y de egress"*. Eso no son plataformas del cuadro: son la línea base contra la que compara Francisca en 4.2.

Técnicamente la guía dice que los precios se levantan una sola vez, por los integrantes 6 y 7, así que tendría sentido que salgan de nosotros. Pero hay un problema práctico antes: **no se puede levantar un precio de EC2 sin saber qué instancia**. m5.large y c6g.xlarge cuestan distinto, y la cifra depende de la arquitectura que Francisca esté modelando.

Conviene responder que sí, pero pidiéndole a Francisca que especifique las instancias y regiones exactas. Sin eso estaría adivinando, y una cifra adivinada es peor que ninguna.

Lo mismo con egress: es subtema obligatorio de 2.3 y Valentina ya notó que no cabe en la celda de precio del cuadro. Necesita su propio lugar, y hay que definir cuál.

**3. El bloque C dice "toda la lista de datos sin servidor".**

Esa lista incluye Aurora Serverless y DynamoDB, que son de Rodolfo por el reparto AWS/Azure. Si me tocan a mí también, se pisa con lo suyo. Hay que confirmar que ahí sigue valiendo la división que ya acordamos.

## Y una pregunta directa

Menciona un `registro-busqueda.md` que yo no tengo. Si existe un archivo circulando con candidatos, lo necesito antes de cerrar mis diez, porque es exactamente la materia prima del bloque C. Si es el nombre que él le puso a lo que yo estoy construyendo, entonces es `Desarrollo-3.1.md` y basta con decírselo.

Vale la pena preguntarlo ya: es la tercera señal de que hay documentos circulando que no me llegaron. Las otras dos fueron el `.md` de fuentes que mencionó Valentina y la "revisión con Gemini" de Rodolfo.

¿Te armo la respuesta para Daniel con estos cuatro puntos?

## Persona — prompt 27 — 19-09-2026 20:00

```text
ahora que ya tenemos el paso a paso, desarrollalo y yo ire supervisando todo
```

### Claude Code — 19-09-2026 20:01

Puedo desarrollar buena parte, pero dos cosas no, y quiero ser claro sobre cuáles y por qué.

**Las cifras del cuadro no te las puedo dar.** Mi conocimiento llega a mayo de 2026 y los datos tienen que ser de las páginas oficiales de esta semana, con fecha de consulta. Cualquier número que yo escriba sería inventado o viejo, y quedaría en la tabla con un sello de "consultado 19-09-2026" que sería falso. Es justo lo que el punto 6.1 prohíbe y lo que hace que una cifra se evalúe como error grave.

**Las diez justificaciones y los dos párrafos tampoco.** Ahí el problema no es que yo pueda equivocarme: es que el requisito no es que estén bien escritos, es que sean tuyos y los puedas defender de memoria cuando el profesor te interrumpa y te pregunte por qué entró Fly.io.

Sobre la supervisión: funciona para estructura y formato, pero no para esos dos casos. En las cifras no te ahorra nada, porque tendrías que abrir las mismas quince páginas igual para verificar. Y en las justificaciones, supervisar un texto ajeno no es lo mismo que poder sostenerlo sin el papel delante. Rodolfo está ahora mismo rehaciendo a mano una tabla que recopiló con IA, y ese es el costo real de ese atajo.

## Lo que sí desarrollo ahora, y es bastante

1. **El Anexo D completo**, salvo tus hallazgos. La declaración del método, los criterios de inclusión y descarte redactados, la tabla de las cinco listas armada, y los cinco descartes que ya tienes razonados con su fundamento. Es documentación de procedimiento, no análisis.

2. **Todo el andamiaje LaTeX**: las dos tablas del cuadro con sus anchos de columna calculados, el entorno `landscape`, la tabla de 3.1, el Anexo D, y los `$` ya escapados. Formato puro, nivel 1.

3. **El bloque BibTeX para `referencias.bib`**, sacado de tus 11 papers ya verificados. Son 15 minutos y destraba la bibliografía de todo el grupo, que hoy está vacía.

4. **La respuesta a Daniel** con los cuatro puntos.

5. **Una pasada de verificación** sobre lo que vayas llenando: que ninguna celda quede sin región ni fecha, que las divisiones den lo que dices que dan — como hice con el 3,0× y el −20 % de Rodolfo —, y que 3.1 no se pase de las 300 palabras.

## Lo que queda para ti

Las quince visitas y las diez frases. Entre cuatro y cinco horas, y son las únicas horas del trabajo que nadie más puede poner.

Si quieres, parto ahora por el Anexo D y el andamiaje LaTeX mientras tú haces las primeras visitas, y cuando tengas datos los reviso. ¿Te sirve así?

## Persona — prompt 28 — 19-09-2026 20:03

```text
yap, hazlo, pero como busco esos datos para ingresarlos en las tablas?
```

### Claude Code — 19-09-2026 20:03

Te respondo el cómo primero, porque eso lo necesitas para empezar, y dejo los archivos después.

## El método, igual para las quince visitas

**1. Llegar a la página oficial, no a un intermediario.**

La forma más rápida es acotar la búsqueda al dominio del proveedor:

```
site:developers.cloudflare.com workers limits
site:cloud.google.com cloud run pricing
site:docs.fastly.com compute resource limits
```

Si el resultado no está en el dominio del proveedor, no sirve. Un blog que "resume los límites de Lambda" no es fuente válida aunque acierte.

**2. Las páginas de límites se llaman casi siempre igual.** Busca alguna de estas palabras: *Limits*, *Quotas*, *Service quotas*, *Resource limits*, *Platform limits*.

**3. En la página de precios, fija la región antes de leer nada.** Casi todas tienen un selector que viene con una región por defecto, y si no lo tocas no sabes cuál estás leyendo. Para Google elige `us-central1` y déjalo anotado. Para los de borde no hay selector, y esa ausencia **es el dato**: anota "red global, sin región".

**4. Captura de pantalla de cada página de precios.** Es tu respaldo si algo cambia antes del lunes, y es evidencia trazable para el Anexo A.

**5. Anota URL exacta y fecha en el momento.** No al final del bloque.

## Las cuatro trampas de tu mitad

| Plataforma | Qué se pasa por alto |
|---|---|
| **Cloudflare Workers** | La página de límites trae **tiempo de CPU** y **duración total de la solicitud** como cifras distintas. Si copias solo una, la celda queda mal. Anota las dos y di cuál es cuál |
| **Cloud Run** | *Cloud Run* (servicios) y *Cloud Run functions* son **productos distintos** con documentación distinta. Las fuentes 20, 21 y 26 son del primero |
| **Fastly** | La página de precios tiene **varios regímenes**: uso por tramos, paquetes por cotización, y tarifas heredadas. Anota cuál estás citando |
| **Knative, OpenFaaS, Spin** | No tienen "página de límites" en el mismo sentido. Lo que se mira es la **referencia de configuración** y los **valores por defecto**, y se anota que son configurables |

## Cuando el dato no está

No lo infieras ni lo estimes. Escribe lo que corresponda:

- **«No publicado»** si la documentación no lo dice
- **«Solo por cotización»** si el proveedor no publica precio
- **«No aplica»** si la categoría no tiene ese campo, como el payload en una base de datos
- **«Configurable»** más el valor por defecto, en las de código abierto

Una celda honesta que dice "no publicado" vale más que una cifra inventada, y además es material para el análisis de Rodolfo: que un proveedor no publique algo también es una diferencia entre plataformas.

---

Ahora voy con los archivos. Empiezo revisando el BibTeX que ya tienes.

### Claude Code — 19-09-2026 20:03

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:03

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:03

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:04

Encontré un problema en las claves BibTeX antes de armar el archivo, te lo señalo abajo. Ahora los cuatro entregables.

### Claude Code — 19-09-2026 20:04

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 20:05

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 20:05

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 20:06

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 20:06

Written for: Daniel el último; los otros tres son tuyos.

Listos los cuatro:

- [Desarrollo/Desarrollo-AnexoD.md](Desarrollo/Desarrollo-AnexoD.md)
- [Desarrollo/Andamiaje-LaTeX.md](Desarrollo/Andamiaje-LaTeX.md)
- [Desarrollo/referencias-claudio.bib](Desarrollo/referencias-claudio.bib)
- [Sesion-actual-19-09/Consulta-Daniel.md](Sesion-actual-19-09/Consulta-Daniel.md)

## Encontré una colisión de claves BibTeX

Al extraer las entradas apareció esto: la planilla usa `li2022serverless` para el **paper 43** (Li, Yongkang — IEEE TSC 2023), pero en tu `Revision-papers.md` esa clave corresponde al **paper 47** (Li, Zijun — ACM 2022).

Si no se unifica, `\parencite{li2022serverless}` apunta a un paper distinto según quién escriba la cita. Dejé el aviso arriba del `.bib` y la propuesta: `li2023serverless` para el 43, `li2022serverless` para el 47.

También hay una diferencia menor en el paper 41: la planilla dice 2025 y la revista lo numera como 2026. Como lo descartaste, puede quedar fuera del `.bib`.

## Qué tiene cada archivo

**Anexo D** — el párrafo de encabezado y los siete criterios (tres de inclusión, cuatro de descarte) están redactados como borrador para que los ratifiques; es método, no análisis comparativo. Las tablas y la declaración final quedan para ti. Los cinco descartes que ya tenías razonados están cargados, con la fecha en blanco: tres de ellos —Kubeless, Riff/IronFunctions y Azure Front Door— son los que más rinden, porque confirmar que están archivados es exactamente el aporte que reconoce el punto 4.

**Andamiaje LaTeX** — las dos tablas del cuadro con los anchos calculados para página apaisada (21,4 cm y 22,4 cm sobre 22 disponibles), las 21 filas etiquetadas por dueño, la tabla de 3.1, y el Anexo D completo. Las tres filas de código abierto ya traen escrita la celda de "sin precio de lista: se autoaloja". El aviso de escapar los `$` está arriba de todo y repetido en el bloque del cuadro.

Un detalle que conviene avisar al grupo: como el cuadro ahora son dos tablas, Francisca y Fabián tienen que citar **dos etiquetas**, no una. Está anotado en la sección 4 de ese archivo.

**El `.bib`** trae doce entradas, las once tuyas más QuickFaaS. Es pegar y listo.

Ahora te toca la Visita 1. Cuando tengas las primeras filas, mándamelas y hago la pasada de verificación.

## Persona — prompt 29 — 19-09-2026 20:06

```text
te puedo mandar los links de las paginas para que indreses los datos en la tabla?
```

### Claude Code — 19-09-2026 20:07

Puedo abrir las páginas, pero no conviene que yo llene las celdas, y esta vez el motivo es práctico más que reglamentario.

**Las páginas de precios son casi todas JavaScript.** Lo que devuelve una descarga suele ser el armazón sin la tabla, o las cifras de una región por defecto que no puedo elegir ni identificar. Y la región es justamente lo que el punto 5 exige en cada celda.

**El problema de la fecha es peor.** Si yo descargo algo y tú escribes "consultado 19-09-2026", esa fecha afirma que lo consultaste. Si lo que me llegó estaba en caché de hace semanas, la celda queda certificando algo que no pasó — y esa tabla es la fuente de precios de 2.3, 4.2 y 4.3.

Rodolfo hizo exactamente esto y está ahora, sábado en la noche, rehaciendo la tabla a mano.

## Lo que sí te sirve, y es mejor

**Mándame el link junto con lo que anotaste.** Yo abro la página y verifico que coincida.

```
Cloudflare Workers – limits
https://developers.cloudflare.com/workers/platform/limits/
Anoté: tiempo de CPU ___ , duración total ___ , payload ___
```

Así el dato lo tomas tú de la página en vivo, con la región que elegiste, y yo hago una segunda pasada que caza errores de transcripción. Si lo que yo veo no coincide con lo tuyo, lo revisas. El peor caso es que verifiques dos veces; nunca que entre una cifra falsa.

También puedo, sobre la marcha:

- **Revisar aritmética**, como con el 3,0× y el −20 % de Rodolfo
- **Decirte dónde mirar** si una página específica te tiene atascado
- **Chequear cumplimiento**: que ninguna celda quede sin región ni fecha

## La cuenta de tiempo

Son 15 visitas, pero no son 15 páginas distintas:

| Plataforma | Páginas |
|---|---|
| Deno Deploy | 1 (límites y precio juntos) |
| Cloudflare (Workers + D1) | 3 |
| Cloud Run (+ functions + CPU) | 4 |
| Fastly | 2 |
| Knative, OpenFaaS, Spin | 3 |
| Neon | 1 |

A diez minutos cada una son **dos horas y media**. Tienes esta noche y todo el domingo.

Parte por Deno Deploy y mándame la primera fila completa. Con esa calibramos cuánto demora de verdad y si el formato de celda queda como lo necesita Rodolfo.

## Persona — prompt 30 — 19-09-2026 20:11

```text
los que dicen origen Guia a que se refiere?
```

### Claude Code — 19-09-2026 20:11

Se refiere a [Terabyte-Guia-Equipo.md](informe-investigacion/Terabyte-Guia-Equipo.md), sección 5, que tiene una tabla con la columna **"Candidatos a verificar en su documentación oficial"**. De ahí saqué esos nombres.

Por ejemplo, para contenedores sin servidor la guía propone Fly.io, Railway, Render, Scaleway Serverless Containers y Koyeb. Para código abierto propone Apache OpenWhisk, Fission, Nuclio, Fn Project y WasmEdge.

## Lo importante: la guía no es una fuente

Es un documento de trabajo del propio equipo. Esos nombres son **pistas**, no evidencia. No tienen ninguna autoridad detrás: son la idea de alguien sobre qué conviene revisar.

La consecuencia práctica es concreta:

- **No se pueden citar en el informe.** Lo que se cita es la documentación oficial de cada producto, una vez que la abriste.
- **En el Anexo D, "fuentes consultadas" no puede decir "la guía del equipo".** Tiene que nombrar las páginas oficiales que efectivamente abriste.
- **Todos hay que verificarlos.** La propia guía lo advierte: *"algunos candidatos pueden estar descontinuados o haber cambiado de modelo. Descubrirlo y descartarlo con fecha y fuente también es aporte."*

La columna "Origen" del archivo de desarrollo está para que sepas de dónde vino la pista y puedas juzgarla, no para citarla. Por eso los `P-39 p.3` y `P-43 p.1531` son distintos: esos sí son papers verificables, aunque igual sirven solo para nombrar plataformas, no para sacar cifras.

## Un detalle de esa misma tabla

La guía también tiene una columna **"Explorador"**, que dice quién busca candidatos en cada lista:

| Lista | Explorador según la guía |
|---|---|
| Funciones como servicio | Matías (2.1) y Rodolfo (3.2) |
| Contenedores sin servidor | Matías (2.1) y **tú** (3.2) |
| Cómputo en el borde | Isidora (2.5) y **tú** (3.2) |
| Código abierto | Isidora (2.5) y Daniel (2.6) |
| Datos sin servidor | Valentina (2.4) y Francisca (2.3) |

O sea: de las cinco listas, **solo dos son tuyas para explorar**. En las otras tres tú consolidas, pero los candidatos debían venir de otros.

En la práctica no llegó ninguno, así que los estás buscando todos. Vale la pena mencionarlo cuando les pidas los nombres de plataformas: no es un favor, es la tarea que la guía les asigna.

## Persona — prompt 31 — 19-09-2026 20:14

```text
del .md 3.1 con existe se refiere a si existe?, a que se refiere si publica limites? a que se refiere si entra?
```

### Claude Code — 19-09-2026 20:14

Son las tres condiciones de inclusión del Anexo D, una por columna. Te las aterrizo.

## ¿Existe?

**Pregunta:** ¿esto sigue disponible hoy, en septiembre de 2026?

No es filosófico: es si todavía se puede contratar o desplegar.

| Qué mirar | Señal de que no |
|---|---|
| **Producto comercial:** ¿hay página de precios y se puede crear una cuenta? | Avisos tipo "no acepta nuevos clientes", "fin de soporte el DD-MM", o que la página redirija a otro producto |
| **Proyecto de código abierto:** ¿cuándo fue la última versión publicada o el último commit? | Banner de "This repository has been archived" en GitHub, o años sin actividad |

El caso de App Runner es exactamente esto: existe, funciona, pero estaría cerrado a nuevos clientes. Es un "existe con matiz", y el matiz es el dato.

## ¿Publica límites?

**Pregunta:** ¿puedo encontrar en su documentación oficial los números que necesita el cuadro?

Concretamente: timeout, memoria, payload y concurrencia. Y un precio, **o** una declaración expresa de que opera solo por cotización.

Esta columna decide algo puntual: **si puede ser fila del cuadro 3.2 o se queda solo en 3.1.**

| Lo que encuentras | Qué significa |
|---|---|
| Límites y precio públicos | Puede ser fila del cuadro |
| Límites públicos, pero el precio es por cotización | También puede ser fila. La celda dice «solo por cotización» |
| Límites públicos, nada sobre precio | Puede ser fila. La celda dice «No publicado» |
| Nada verificable | **Se descarta.** Es el criterio 3 del Anexo D |

## ¿Entra?

**Pregunta:** ¿pasó las dos anteriores **y** aporta algo que las opciones de la ficha no cubren?

La tercera parte es la que decide, y es criterio tuyo. Una plataforma que existe, publica todo y es equivalente a una que ya está en la ficha **no entra**, porque no agrega nada a una comparación.

### Conviene que esa columna tenga tres valores, no dos

| Valor | Qué significa |
|---|---|
| **3.1** | Entra a la tabla de alternativas, pero no como fila del cuadro (no publica lo suficiente, o no aporta al eje del cuadro) |
| **3.1 + 3.2** | Entra a la tabla **y** como fila del cuadro comparativo |
| **Descarte** | No entra. Anotar cuál de los cuatro criterios de descarte aplica |

Te sirve más que un sí o no, porque de ahí sale directo la decisión del Paso 2: cuáles son tus diez, y cuáles de esas diez se convierten en filas.

## Dónde va lo que descartas

Todo lo que marques "Descarte" pasa al Anexo D con **motivo, criterio aplicado, fuente y fecha**. No se pierde: es la evidencia de que la búsqueda se hizo, y el punto 4 la cuenta como aporte.

Si quieres, te ajusto la columna en `Desarrollo-3.1.md` para que ya venga con los tres valores.

## Persona — prompt 32 — 19-09-2026 20:14

```text
y en establas tablas son de si y de no?
```

### Claude Code — 19-09-2026 20:15

Las dos primeras sí, la tercera no. Te dejo la leyenda y ajusto el archivo para que quede explícito.

### Claude Code — 19-09-2026 20:15

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:15

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:15

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:15

Listo, las cinco tablas quedaron con las columnas claras.

| Columna | ¿Sí o no? |
|---|---|
| **¿Vigente?** | Sí o No, pero admite **"Sí, con matiz"** cuando existe pero con algún problema: cerrado a nuevos clientes, fin de soporte anunciado, sin actividad reciente. El caso de App Runner es justo ese |
| **¿Publica?** | No es sí o no. Es **qué encontraste**: `Límites y precio` · `Límites, precio por cotización` · `Límites, precio no publicado` · `Nada verificable` |
| **Decisión** | Tampoco. Tres valores: `3.1` · `3.1 + 3.2` · `Descarte` |

La de **Decisión** es la que trabaja. De ahí sale el Paso 2 directo:

- Las que digan `3.1` van solo a la tabla de alternativas, con su frase de justificación.
- Las que digan `3.1 + 3.2` además hay que levantarlas en `Desarrollo-3.2.md`, y por eso conviene marcarlas apenas las decidas: cada una suma una visita.
- Las que digan `Descarte` pasan al Anexo D con el criterio que aplicaste y la fecha.

Las columnas de URL y fecha no son de marcar: van con la dirección exacta que abriste y la fecha de hoy.

## Persona — prompt 33 — 19-09-2026 20:19

```text
que quiere decir limites y precio; limites, precio por cotizacion; limites, precio no publicado y nada verificable? te puedo mandar un ejemplo de la pagina de oracle? ahi adjunte imagenes, no se si eso responda lo que es la tabla?
```

### Claude Code — 19-09-2026 20:20

Sí, sirve perfecto, y es buen ejemplo para explicar los cuatro valores.

## Qué significa cada uno

Las dos cosas que se miran son **límites técnicos** (timeout, memoria, payload, concurrencia) y **precio**. La combinación decide el valor:

| Valor | Cuándo |
|---|---|
| `Límites y precio` | La documentación publica ambos. Es el caso normal y el que permite ser fila del cuadro |
| `Límites, precio por cotización` | Publica los límites, pero el precio no: dice "contactar ventas". Los paquetes Advantage y Ultimate de Fastly son así |
| `Límites, precio no publicado` | Publica límites y simplemente no hay nada sobre precio, ni siquiera un aviso de cotización. Es raro |
| `Nada verificable` | No encuentras ni lo uno ni lo otro → **Descarte**, criterio 3 |

## Lo que mandaste

Encontraste la **mitad de precio**, y muy completa:

- Tarifas por **tramos**: gratis hasta 2 millones de invocaciones al mes, y por sobre eso un precio por invocación. Lo mismo en tiempo de ejecución: gratis hasta 400.000 GB-s
- La **unidad de cobro** con su base: invocación por un lado, gigabyte memory-seconds por otro
- La **capa gratuita**, que son esos dos primeros tramos
- Una nota sobre **Provisioned Concurrency**: se cobra cuando no se usa, al 25 % de la tarifa de ejecución
- Y hay **calculadora oficial**, que el punto 5 acepta expresamente como fuente

Tres de esos caen directo en campos del cuadro: el tramo de volumen que pedía Valentina, la capa gratuita, y la mitigación de arranque en frío **indicando que se factura**. Ese último es justo el campo 13.

## Lo que todavía falta

**Los límites técnicos.** Las capturas son de la página de precios; falta la de límites: timeout máximo, memoria máxima, tamaño de payload, concurrencia.

Ojo con una trampa: el estimador muestra campos de memoria y tiempo de ejecución, pero **esos son parámetros de la calculadora, no los límites del producto**. El límite real está en la documentación, buscando *Functions limits* o *service limits* en `docs.oracle.com`.

**La región y la fecha.** Ninguna captura dice a qué región corresponde el precio. Verifica si la página de Oracle tiene selector de región o si el precio es único. Si es único, la celda dice eso; si hay selector, elige uno y anótalo.

## Cómo queda la fila por ahora

```
| Oracle Cloud Functions | Guía | Sí | (falta la página de límites) | (pendiente) | <url de precios> | 19-09-2026 |
```

Con la página de límites pasa a `Límites y precio`, y ahí decides si es `3.1` o `3.1 + 3.2`.

Un aviso sobre la pista de la guía: decía que Oracle Cloud Functions está basado en el proyecto abierto Fn. Si vas a usar eso en tu justificación, verifícalo en la documentación de Oracle, no lo des por bueno porque lo dijo la guía.

## Persona — prompt 34 — 19-09-2026 20:21

```text
eso es lo que aparece ya en toda la pagina
```

### Claude Code — 19-09-2026 20:22

Ahí está el problema, y es útil que aparezca ahora porque te va a pasar en las catorce visitas que quedan.

**Esas son páginas de producto, no de documentación.** Los límites no están ahí y no van a estar: es material de venta.

Cada proveedor tiene dos sitios separados:

| Proveedor | Sitio comercial (precios, marketing) | Documentación (límites, cuotas) |
|---|---|---|
| Oracle | `oracle.com/cloud/...` | **`docs.oracle.com`** |
| Cloudflare | `cloudflare.com` | **`developers.cloudflare.com`** |
| Google | `cloud.google.com/run` | `cloud.google.com/run/**docs**` y `/quotas` |
| Fastly | `fastly.com` | **`docs.fastly.com`** |
| AWS | `aws.amazon.com` | `docs.aws.amazon.com` |

Regla práctica: **el precio suele estar en el sitio comercial, los límites casi siempre en el de documentación.**

## Para Oracle, busca así

```
site:docs.oracle.com functions service limits
```

Oracle además tiene una página general de *Service Limits* que lista las cuotas por servicio. Lo que necesitas de ahí: timeout máximo, memoria máxima, tamaño de payload y concurrencia.

## Dos cosas de lo que mandaste

**Una te sirve y hay que verificarla:** en la pestaña de integraciones dice *"Out-of-the-box support for the CloudEvents standard"*. CloudEvents es un estándar de la CNCF, así que eso es una afirmación concreta y comprobable, y la CNCF es fuente preferente según el punto 5. Si lo confirmas en la documentación, es material sólido.

**La otra no la puedes usar:** *"true vendor independence"* y *"open portability"* son afirmaciones de marketing del propio proveedor sobre su producto. El punto 5 no las admite como evidencia. Sirven como pista para ir a verificar si Functions efectivamente está construido sobre Fn y qué significa eso en concreto, pero no se citan.

Es la misma distinción de siempre: lo que el proveedor **documenta** sirve; lo que el proveedor **afirma sobre sus ventajas** no.

## Persona — prompt 35 — 19-09-2026 20:22

```text
me llevo a eso
```

### Claude Code — 19-09-2026 20:23

Esa página no te sirve, por dos razones.

**Es una nota de versión de 2020.** Anuncia un cambio que ocurrió en noviembre de 2020, no dice cuál es el límite hoy. Entre 2020 y 2026 pudo cambiar otra vez. En los sitios de documentación conviven las notas de versión —anuncios fechados— y la documentación de referencia, que es el estado actual. Para el cuadro necesitas la de referencia.

**Y además no son los límites que buscas.** "Cuántas funciones y aplicaciones puedes crear por región" es una cuota de cuenta. Lo que va al cuadro es otra cosa: timeout máximo, memoria, payload y concurrencia.

## Estás a un clic

En esa misma página hay un enlace que dice **service limits**. Ese es el canónico. Haz clic ahí y busca la sección de Functions.

Si no llegas por ahí:

```
site:docs.oracle.com functions limits timeout memory
```

## Un dato de esa nota que sí es interesante

Dice que los límites **varían según el método de pago**: los clientes de Universal Credit tienen cuotas distintas a los de Pay-as-You-Go. Si eso sigue vigente, es una particularidad que ninguna otra plataforma de la ficha tiene. Pero confírmalo en la página actual, no en la nota de 2020.

## Una cosa sobre el tiempo

Llevas rato en Oracle, que es el candidato 1 de unos 30, y es solo un candidato de 3.1. Tus **doce filas del cuadro son obligatorias pase lo que pase**: Cloud Run, Workers, D1, Fastly, Deno, Knative, OpenFaaS, Spin y Neon.

Dos ajustes que te ahorran harto:

**1. No verifiques los 30 candidatos.** Necesitas **dos por lista**. En cuanto tengas dos que califiquen claramente, cierra esa lista y pasa a la siguiente. Eso baja de 30 verificaciones a unas 12.

**2. Si un candidato se resiste, déjalo.** Tienes de cinco a ocho por lista. Oracle no es imprescindible: si en diez minutos más no aparece la página de límites, anótalo como pendiente y prueba con Alibaba Function Compute o Scaleway, que es la misma lista.

Lo que no puede faltar el lunes son las doce filas del cuadro y las diez justificaciones. Todo lo demás es mejorable.

## Persona — prompt 36 — 19-09-2026 20:24

```text
me aparece eso
```

### Claude Code — 19-09-2026 20:24

Ahora sí es la página correcta. Pero fíjate en el encabezado de la segunda columna: dice **"Default Value"**.

## Lo que tienes y lo que falta

| Dato | Lo que dice | Problema |
|---|---|---|
| Timeout síncrono | 30 segundos | Es el **valor por defecto**, no el máximo |
| Memoria | 128 MB | Igual: por defecto |

El título de la página lo confirma: *"Changing Default Memory and Timeout Settings"*. Es sobre los valores que vienen puestos y cómo cambiarlos, no sobre hasta dónde se pueden subir.

**Eso importa para el cuadro.** Lambda dice 900 s y eso es un máximo. Azure tiene un techo real de 230 s. Si pones 30 s en la fila de Oracle, estarías comparando un valor por defecto contra máximos ajenos, y la columna deja de comparar lo mismo.

Necesitas el **máximo configurable** de timeout y de memoria. Suele estar en la misma sección de referencia o en la página de service limits. Busca la palabra *maximum* en esa área de la documentación.

## Dos cosas valiosas que sí encontraste

**1. Oracle distingue invocación síncrona de "detached".** Son dos timeouts distintos, con parámetros distintos. Eso es exactamente el campo que pedía Valentina: *"tiempo máximo indicando si hay techo distinto según el tipo de disparador"*. Anótalo.

**2. La columna "Fn CLI" confirma la pista de la guía.** La guía decía que OCI Functions está basado en el proyecto abierto Fn, y aquí aparece el CLI de Fn como forma documentada de configurar el servicio, junto con `func.yaml`. Eso ya no es marketing: es la documentación técnica de Oracle mostrando que la herramienta de Fn opera sobre su producto.

Es una fuente válida y verificable para lo que la página comercial solo afirmaba como *"true vendor independence"*. Si Oracle termina entrando en tu 3.1, esa es la evidencia que sostiene la justificación, no la frase de marketing.

## Todavía faltan dos campos

**Payload máximo** y **concurrencia**. Los dos suelen estar en la página de service limits de Functions, la misma que buscabas antes.

Si en diez minutos no aparecen, anota lo que tienes, marca esos dos como pendientes y sigue. Oracle es candidato de 3.1, no una de tus doce filas obligatorias.

## Persona — prompt 37 — 19-09-2026 20:32

```text
entonces vayamos rellenando el .md con esos datos
```

### Claude Code — 19-09-2026 20:32

Voy a registrar lo que verificaste, separando bien los valores por defecto de los máximos.

### Claude Code — 19-09-2026 20:32

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:32

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:32

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:33

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:33

Registrado en [Desarrollo/Desarrollo-3.1.md](Desarrollo/Desarrollo-3.1.md): la fila de la tabla y una sección §7 nueva con el detalle.

## Lo que quedó anotado

**Precio, completo.** Los dos componentes con sus tramos: invocaciones gratis hasta 2 millones y USD 0,0000002 por sobre eso; tiempo de ejecución gratis hasta 400.000 GB-s y USD 0,00001417 por sobre eso. Más la capa gratuita, que son esos mismos dos tramos.

**La mitigación que se factura.** Provisioned Concurrency no usada al 25 % de la tarifa de ejecución, y sin cargo adicional cuando sí se usa. Ese es el campo 13 de Valentina, resuelto.

**Techo distinto según disparador: sí.** Oracle tiene timeouts separados para invocación síncrona y detached, con parámetros distintos. Ese era el campo que ella pedía y ya lo tienes documentado.

**La evidencia de portabilidad.** Dejé anotado que `func.yaml` y el CLI de Fn aparecen en la documentación técnica como formas oficiales de configurar el servicio. Eso sustituye a la frase de marketing de la página comercial, que no es admisible.

## Lo que marqué como pendiente

Puse un aviso destacado en la tabla de límites: **los 30 segundos y los 128 MB son valores por defecto, no máximos.** Si eso entra al cuadro sin corregir, estarías comparando un valor por defecto contra los máximos de Lambda y Azure.

Faltan siete cosas, listadas al final de la sección: los máximos de timeout y memoria, payload, concurrencia, la región del precio, las tres URLs exactas y el modelo de aislamiento.

La nota de versión de 2020 la dejé anotada como pista, marcada explícitamente para no usar.

---

Cuando decidas si Oracle entra, ese bloque se copia tal cual a `Desarrollo-3.2.md` como fila del cuadro. Por eso lo estructuré con los mismos campos.

Ahora, sobre el tiempo: llevas un candidato de 3.1 y ninguna de tus doce filas obligatorias. Si Oracle no suelta los máximos en diez minutos, déjalo pendiente y parte con Deno Deploy, que es fila obligatoria y trae todo en una página.

## Persona — prompt 38 — 19-09-2026 20:42

```text
desde claude web rellene algunas tablas dentro del .md Desarrollo3.1D.md para que lo revises y me digas si esta bien o no
```

### Claude Code — 19-09-2026 20:42

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:42

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:42

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:43

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:44

Hay bastante material bueno acá. Pero lo primero es lo que tiene consecuencias.

## 1. El problema de la fecha

Todas esas filas dicen **19-09-2026**, y tu propia convención dice que eso significa *"la fuente se abrió ese día y respalda lo anotado"*. Pero las abrió un modelo con buscador, no tú.

Eso no invalida el trabajo — es el mismo camino que tomó Rodolfo y está rehaciendo. Lo que hay que hacer es cerrar el ciclo: **abrir cada URL y confirmar el dato.** Verificar algo que ya te apuntaron toma tres o cuatro minutos, no diez. Son unas veinte URLs, hora y media. Mucho menos que descubrirlas desde cero.

Y súbele el nivel a tu declaración del Anexo A para 3.1: pasa a **nivel 2**, con el prompt registrado. Declararlo no baja la nota.

## 2. Lo que salió muy bien

**App Runner confirmado.** Cerrado a nuevos clientes desde el 30-04-2026, anuncio del 31-03-2026, sin nuevas funcionalidades, AWS recomienda migrar a ECS Express Mode. Con la URL oficial. Eso es justo lo que faltaba en el PDF de Rodolfo, y ahora tu párrafo 1 puede decir que una de las cuatro opciones que nombra la ficha ya no es adoptable.

**Cuatro descartes documentados con fecha:** Kubeless archivado el 15-12-2021 (la URL dice `vmware-archive`, se corrobora sola), Riff el 13-03-2021, MongoDB Atlas Serverless retirado en 2025, y OpenWhisk declarado *"Dormant"* por el board de Apache en feb-2026.

Ese último es el más interesante: **los papers 40 y 43 tratan a OpenWhisk como plataforma de referencia del código abierto, y en 2026 Apache anticipa mandarlo al Attic.** Eso es un contraste entre la literatura y el estado actual, y es material de primera para tu párrafo 2.

**Los máximos de Oracle.** 300 s síncrono, 3.600 s detached, 3.072 MB con valores fijos. Y la nota de versión explicando que antes detached también estaba limitado a 300 s. Eso resuelve el campo de Valentina con números.

## 3. Dos problemas de lógica

**Render.** Propones descartarlo por "no califica en la categoría" porque las instancias pagadas no escalan a cero. El problema: **AWS Fargate tampoco escala a cero** —según los propios datos de Rodolfo, cobra hasta que la tarea termina— y Fargate sí está en la ficha.

Si aplicas ese criterio a Render tienes que aplicarlo a Fargate, y ahí el Anexo D se contradice solo. O cambias el motivo del descarte, o lo admites. Es exactamente el tipo de cosa que el profesor puede picar.

**La lectura transversal 4.** Bien que hayas notado que Fly.io cobra distinto por región. Pero se puede salvar acotándola: Fly.io no es borde de CDN, es contenedores cerca del usuario. Si la enuncias sobre Cloudflare, Fastly y Deno, sigue en pie.

## 4. El hueco real: listas 2 y 4

Conté cuántas candidatas limpias tienes por lista:

| Lista | Candidatas firmes | Estado |
|---|---|---|
| 1 · FaaS | Oracle, Alibaba, IBM, Scaleway | ✅ sobra |
| 2 · Contenedores | **solo Fly.io** | ⚠️ falta una |
| 3 · Borde | Akamai, Supabase, Bunny | ✅ |
| 4 · Código abierto | **ninguna firme** | ⚠️ faltan dos |
| 5 · Datos | Turso, Upstash, CockroachDB Basic | ✅ |

En la lista 2, Railway, Render y Koyeb quedaron los tres en "A decidir". **Scaleway Serverless Containers está vacío y es la victoria fácil**: ya abriste Scaleway Functions, el sitio es el mismo.

En la lista 4 todo lo verificado está muerto o dormido. Las vivas posibles son **Nuclio, WasmEdge, Fission y Fn Project**, y las cuatro están vacías o a medias. Ahí hay que meterse.

## 5. Arreglos menores

- **Akamai** debería decir **«solo por cotización»**, que es el valor del punto 5, en vez de "precio no publicado". Tú mismo anotaste que la tarifa se consulta con el representante.
- **La URL de Azure IoT Edge tiene typo**: `en-my/azUre`. No va a resolver.
- **PlanetScale** viene de agregadores. Bien que lo marcaras, pero no se puede usar hasta confirmarlo en la página oficial.
- **CockroachDB** está citado a un blog del proveedor. Para el cambio de nombre sirve; para las cifras necesitas la página de precios.

## 6. Qué haría ahora, en orden

1. **Scaleway Serverless Containers** — cierra la lista 2 en diez minutos
2. **Nuclio y WasmEdge** — cierran la lista 4
3. **Verificar las URLs de tus descartes**, que son lo que más rinde: Kubeless, Riff, MongoDB, OpenWhisk y App Runner
4. **Decidir Render** con criterio consistente
5. Recién después, las doce filas del cuadro

Con eso tienes las diez y el Anexo D queda sólido.

## Persona — prompt 39 — 19-09-2026 20:47

```text
hagamos eso en orden y con respecto a render si, utilicemosla, y veamos bien los descartes, analicemos todos esos detalles para decidir que hacer
```

### Claude Code — 19-09-2026 20:48

Con Render adentro, la cuenta cambia: **la lista 2 queda cerrada con Fly.io y Render.** El único hueco que queda es la lista 4.

Voy a dejar registrado el cambio y el análisis de descartes.

### Claude Code — 19-09-2026 20:48

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:48

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 20:48

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:49

Registrado en [Desarrollo/Desarrollo-3.1D.md](Desarrollo/Desarrollo-3.1D.md), sección §8 nueva.

## Render adentro, y qué obligó a corregir

El motivo del descarte no se sostenía, y la razón está dentro de la propia ficha: **Fargate tampoco escala a cero** —cobra hasta que la tarea termina— y es una de las cuatro opciones que la ficha nombra en esa misma lista. Si el escalado a cero fuera requisito de categoría, Fargate quedaría fuera de su propia lista.

Criterio corregido: un contenedor sin servidor es aquel donde **el equipo no aprovisiona ni administra máquinas ni nodos**. El escalado a cero es una característica, no un requisito de pertenencia.

Queda un subproducto útil: la categoría no es homogénea, unos escalan a cero y otros no, y esa diferencia es la que decide la forma de la curva de costo. Ahí lo dejé por si lo quieres usar en el párrafo 2.

## Los descartes

Cuatro están firmes y solo necesitan que abras la URL: Kubeless, Riff, MongoDB Atlas Serverless y OpenWhisk. Los prototipos del paper 45 también, solo les falta fecha.

Tres están débiles o sin confirmar: OpenLambda, Azure Front Door y sobre todo **IronFunctions**. Ese último tiene un detalle: el repositorio no está archivado y la guía menciona tanto IronFunctions como Fn Project. Vale la pena verificar si uno sucedió al otro, porque entonces el descarte cambia de motivo y la relación entre ambos pasa a ser el dato interesante.

## OpenWhisk merece tratamiento aparte

Es el descarte que más rinde. Los papers 40 y 43 lo tratan como plataforma de referencia del código abierto, y el board de Apache lo declaró *Dormant* en febrero de 2026, anticipando llevarlo al Attic.

Eso es literalmente lo que el punto 4 llama **evidencia contradictoria bien tratada**: la literatura reciente dice una cosa y la fuente primaria del propio proyecto dice otra, con fecha. Va al Anexo D como descarte **y** al párrafo 2 como hallazgo.

## Una corrección estructural del Anexo D

Tienes 30 candidatos y entran 10. La mayoría de los que quedan fuera **no son descartes**: simplemente no fueron los dos elegidos. IBM Code Engine está vigente y documentado; si aparece bajo "descartadas", el anexo afirma algo falso sobre él.

El Anexo D lleva dos tablas separadas: **descartados** (fallaron un criterio, con cuál y con evidencia) y **evaluados, no seleccionados** (calificaban, pero otros dos resultaron más pertinentes).

---

## Lo único que falta

Con Render adentro, **cuatro de las cinco listas están cerradas.** Solo queda la lista 4, donde todo lo verificado está archivado o dormido.

Las vivas por revisar son **Nuclio, WasmEdge, Fission y Fn Project**. Necesitas dos. Ese es el siguiente paso, y es el último bloqueo de 3.1.

## Persona — prompt 40 — 19-09-2026 20:54

```text
cambie el desarrollo-3.1, ahora ese tiene algunos de los cambios que realize revisalo y dime que tal esta
```

### Claude Code — 19-09-2026 20:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:54

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 20:55

Esto avanzó mucho. Las cinco listas quedaron cerradas.

## Lo que está muy bien

**IronFunctions resuelto con elegancia.** No es "abandonado" sino **sucedido por Fn Project** — el mismo equipo de Iron.io lo bifurcó al entrar a Oracle en 2017. Ese descarte ya no depende de arqueología de commits, y además conecta con Fn Project, que está en la misma lista. Es mejor de lo que yo había planteado.

**OpenLambda re-razonado correctamente.** Encontraste que el proyecto sí está activo, pero su README declara propósito de investigación. Entonces el descarte es criterio 1 (prototipo), no criterio 2 (abandono). Esa distinción es fina y es la correcta.

**Azure Front Door ahora tiene evidencia real:** condiciones de coincidencia más hasta cinco acciones predefinidas, sin forma de ejecutar código propio. Con dos URLs oficiales. Pasó de "propuesto" a firme.

**El criterio corregido se aplicó parejo.** Railway con el mismo razonamiento que Render, y PlanetScale reevaluado por el motivo verdadero —si eliges tamaño y cantidad de nodos, estás aprovisionando— en vez de por no escalar a cero.

## Tres cosas que mirar antes del Paso 2

**WasmEdge tiene un problema que ya intuiste.** Anotaste "ojo con que aporte algo distinto de Wasmtime". Es más serio que un ojo: **Wasmtime está en la ficha**, y el criterio 3 exige aportar algo que las opciones de la ficha no cubran. Si WasmEdge es "un runtime de Wasm como Wasmtime", falla ese criterio salvo que puedas nombrar la diferencia concreta.

Con Fission, Nuclio y Fn disponibles, no lo necesitas. Y sería el eslabón más débil si te preguntan en la exposición.

**Fn Project y Oracle son la misma tecnología.** Oracle Cloud Functions está construido sobre Fn. Si eliges los dos, uno en lista 1 y otro en lista 4, alguien puede decir que es una plataforma contada dos veces.

Se puede defender —es el motor abierto frente al servicio gestionado, que es justo un argumento de portabilidad— pero la justificación de cada uno tiene que **hacer explícita la relación**, no esconderla.

**Fn es el más flojo en actividad.** Versión 0.3.768 en feb-2026, mantenimiento. Fission tuvo siete versiones entre mayo y junio; Nuclio varias. Los dos más sólidos de la lista 4 son **Fission y Nuclio**.

## Los tres pendientes no bloquean nada

PlanetScale, Koyeb y Huawei quedaron sin cerrar, pero **ninguna de sus listas los necesita**:

- Lista 5 cerrada con Turso, Upstash y CockroachDB → PlanetScale se puede dejar en D.2 o soltar
- Lista 2 cerrada con Fly.io y Render → Koyeb igual
- Lista 1 cerrada con cuatro → Huawei igual

Sobre Koyeb, además: **ser adquirido no es un criterio de descarte.** Los cuatro criterios son prototipo, descontinuado, sin documentación y no califica. Una adquisición con operación continua no cae en ninguno. Es candidata con nota de continuidad, no descarte.

## Lo que queda por verificar

Todo sigue con fecha 19-09-2026 puesta por el modelo, no por ti. Pero no son 25 URLs: **los que importan de verdad son los 8 descartes**, porque afirmar que algo está archivado y equivocarse sería grave. Esos más las 10 que elijas son 18.

Dos detalles menores: el repositorio de OpenLambda aparece como `open-lambda-23`, que se ve raro para un repo canónico — confírmalo. Y CockroachDB sigue citado a un blog: para el cambio de nombre sirve, para las cifras necesitas la página de precios.

---

Ya puedes hacer el **Paso 2**. Tienes candidatas firmes en las cinco listas y los criterios aplicados de forma consistente. Elegir las dos de cada lista es tuyo: es criterio 3, qué aporta cada una.

## Persona — prompt 41 — 19-09-2026 20:58

```text
pero eso eso no lo habia hecho valentina?, recuerda que mi parte es de claudio, tengo que hacer solo las alternativas adicionales
```

### Claude Code — 19-09-2026 20:59

No, son dos cosas distintas que se llaman igual. Es fácil confundirlas.

| | Criterios de Valentina | Criterios tuyos |
|---|---|---|
| **Dónde van** | Apertura de 3.2 | 3.1 y Anexo D |
| **Qué deciden** | **En qué dimensiones** se comparan las plataformas | **Qué plataformas** entran a la comparación |
| **Cuáles son** | Costo, latencia, complejidad operacional | Inclusión: vigente, documentada, aporta algo nuevo. Descarte: prototipo, archivada, sin documentación, no califica |
| **Resultado** | Las columnas del cuadro | Las 10 filas de tu tabla de 3.1 |

Los suyos son las **columnas**. Los tuyos deciden **quién entra**. Ella no podía hacer los tuyos: son sobre las alternativas que estás buscando tú.

Y el punto 4 te obliga a declararlos: *"documentar la búsqueda realizada: fuentes consultadas, **criterios de descarte** y fecha"*. Eso es tuyo.

## Tu parte son tres cosas, no una

Están nombradas en el propio `main.tex`:

| Línea | Qué dice |
|---|---|
| 317 | `%% 3.1  Responsables: Claudio y Daniel` |
| 349 | `%% 3.2  Responsables: Valentina (criterios), Rodolfo (AWS y Azure), Claudio y Daniel (Google, Cloudflare, Fastly, Deno/Vercel/Netlify, open source)` |
| 683 | `%% ANEXO D. BÚSQUEDA DOCUMENTADA  Responsables: Claudio y Daniel` |

Tu nombre aparece tres veces: **3.1 completo, tu mitad de las filas del cuadro, y el Anexo D.**

Lo que no es tuyo en 3.2: el párrafo de criterios (Valentina), las filas de AWS y Azure (Rodolfo), la consolidación y los dos párrafos de análisis (Rodolfo).

## El Paso 2 es tuyo, y es el corazón de 3.1

Elegir cuáles dos alternativas de cada lista entran a la comparación **es** "alternativas adicionales". No hay nadie más que lo pueda hacer: depende del criterio 3, qué aporta cada una, que es justo lo que se evalúa.

Tienes candidatas firmes en las cinco listas. Lo que falta es que elijas diez y escribas por qué entra cada una.

## Persona — prompt 42 — 19-09-2026 21:00

```text
entonces continuemos con el paso 2
```

### Claude Code — 19-09-2026 21:00

Paso 2 es tuyo, pero puedo dejarte la decisión ordenada. Voy a armar el material en el archivo.

### Claude Code — 19-09-2026 21:00

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 21:01

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:01

Paso 2 quedó armado en [Desarrollo/Desarrollo-3.1.md](Desarrollo/Desarrollo-3.1.md). La elección es tuya, pero ahora tienes el material ordenado para decidir.

## El cambio de enfoque

La pregunta no es "¿es buena esta plataforma?" sino **"¿qué tiene esta que ninguna de las que la ficha ya nombra en esa lista tiene?"**. Por eso cada lista ahora arranca diciendo qué cubre la ficha, y recién después van las candidatas con sus hechos verificados.

Por ejemplo, en la lista 1 la ficha tiene tres hiperescaladores estadounidenses con motores propietarios. Eso deja a la vista qué no está cubierto: otra geografía, otra moneda, un motor abierto, límites de otro orden de magnitud.

## Tres avisos que puse en las tablas

**WasmEdge quedó tachado.** No porque esté mal, sino porque es un runtime de Wasm y Wasmtime ya está en la ficha. Solo entra si puedes nombrar la diferencia concreta, y con Fission y Nuclio disponibles no hace falta arriesgarse.

**Fn Project lleva advertencia.** Es el motor de Oracle Cloud Functions. Puedes elegir los dos, pero entonces la justificación de cada uno tiene que hacer explícita la relación. Escondida, parece que contaste una plataforma dos veces; explícita, es un argumento de portabilidad.

**Huawei quedó entre paréntesis** porque falta resolver si FunctionStage y FunctionGraph son lo mismo. Tiene el dato más llamativo de su lista —72 horas de duración máxima— pero no lo uses hasta resolver el nombre.

## Y una lista de chequeo del conjunto

Al final agregué seis ejes. Diez alternativas que digan todas lo mismo valen menos que diez que cubran cosas distintas: geografía, modelo de cobro, cruce de categorías, portabilidad, límites de otro orden, precio por cotización.

Cuando llenes la tabla de las cinco filas, pásale esa lista por encima. Si cuatro de tus diez son "proveedor europeo más barato", conviene cambiar alguna.

## Persona — prompt 43 — 19-09-2026 21:06

```text
bueno entonces comencemos con el paso 2, a esocger las 10, escoge las que mejor tengan pinta, y luego las vas justificado segun las fuimos seleccionando
```

### Claude Code — 19-09-2026 21:07

No puedo elegirlas yo. Esa elección es el criterio 3 —qué aporta cada una a la comparación— y es lo que el punto 6.1 protege y lo que el profesor te va a preguntar en la exposición. Si las elijo yo, el lunes tienes diez nombres que no puedes defender.

Pero la decisión es mucho más chica de lo que parece. Déjame mostrarte.

## No estás eligiendo diez: estás descartando seis

Con WasmEdge fuera por el riesgo del criterio 3, y Huawei fuera hasta resolver el nombre, te queda esto:

| Lista | Candidatas | Decisión real |
|---|---|---|
| 1 · FaaS | Oracle, Alibaba, IBM, Scaleway | **cuál dejas fuera de cuatro** |
| 2 · Contenedores | Fly.io, Render, Railway | **cuál dejas fuera de tres** |
| 3 · Borde | Akamai, Supabase, Bunny | cuál dejas fuera |
| 4 · Código abierto | Fission, Nuclio, Fn | cuál dejas fuera |
| 5 · Datos | Turso, Upstash, CockroachDB | cuál dejas fuera |

Son **cinco decisiones de "cuál saco"**, no diez de "cuál pongo". Y en cuatro de las cinco listas es elegir entre tres.

## Y nada de lo que saques se pierde

Lo que no elijas va a la **Tabla D.2, "evaluados, no seleccionados"**, con su fuente y su fecha. No es un descarte, no dice que fallara nada. Queda registrado como parte de la búsqueda.

Eso baja mucho lo que está en juego: no hay una elección correcta y cuatro malas. Hay varias defendibles, y la tuya solo tiene que ser consistente.

## La pregunta que resuelve cada lista

Para cada una, mira los hechos ya verificados y responde:

> **De estas tres, ¿cuáles dos me dejan decir algo que no puedo decir con las que la ficha ya nombra?**

Ejemplo del razonamiento, sin que sea tu respuesta: en la lista 3 la ficha ya tiene siete opciones de borde. Akamai es la única con precio por cotización, Supabase es la única que cruza con la capa de datos, y Bunny es la única que separa el ancho de banda CDN del cómputo. Los tres hechos están verificados. **Cuál de esos tres es relevante para una comparación de costo, latencia y complejidad operacional, lo decides tú.**

## Lo que sí puedo hacer, y es donde más te sirvo

Escribe las diez en quince minutos, sin pulir, en la tabla del Paso 2. Después pásamelas y reviso:

- Si alguna "justificación" es en realidad una descripción del producto
- Si el conjunto cubre ejes distintos o se repite
- Si alguna contradice los criterios del Anexo D
- Si alguna no se sostiene con lo que efectivamente verificaste

Esa pasada es rápida y es la que evita los errores que se notan.

Empieza por la lista 3, que es la que tiene los tres hechos más distintos entre sí.

## Persona — prompt 44 — 19-09-2026 21:10

```text
a ver entonces seleecionemos:
FaaS, Oracle y Alibaba
Contenedores: Fly.io, Render
Borde: Akamai y Supabase
Codigo Abierto: Fission y Nuclio
Datos: Turso y Upstash
```

### Claude Code — 19-09-2026 21:10

Registrando la selección.

### Claude Code — 19-09-2026 21:11

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:11

Selección registrada. **El conjunto está bien: los seis ejes quedan cubiertos y ninguna se repite con otra.**

Tres cosas antes de que escribas las justificaciones.

## 1. Render es el eslabón débil

Lo único que tienes verificado es que las instancias pagadas **no** escalan a cero. Eso es una limitación, no un aporte — y encima Fargate, que ya está en la ficha, tampoco escala a cero.

Si te preguntan "¿qué aporta Render a la comparación?", con lo que hay hoy no tienes respuesta.

Dos salidas: buscar qué agrega Render, o cambiarlo por **Railway**, que tiene un modelo de cobro claramente distinto a todo lo de la ficha —RAM a USD 10/GB/mes y CPU a USD 20/vCPU/mes, medidos por minuto y también en reposo—. Ese dato ya está verificado y sostiene una justificación sola.

## 2. De Fission y Nuclio sabes que están vivos, no qué aportan

Verificaste sus fechas de release, que resuelve el criterio 1. Pero el criterio 3 pregunta qué agregan frente a Knative, OpenFaaS, KEDA, Spin, wasmCloud y Wasmtime, que ya están en la ficha. Eso no está verificado.

Las pistas de la guía son concretas y rápidas de confirmar: Fission por su pool de contenedores calientes, que es otra forma de mitigar el arranque en frío; Nuclio por su orientación a alto rendimiento y datos.

## 3. Alibaba quedó con menos datos que la que dejaste fuera

De Alibaba tienes los límites de ráfaga. De Scaleway tenías timeout, payload, concurrencia y escalado a cero, los cuatro. Si Alibaba pasa al cuadro, te espera más trabajo; si cuesta, Scaleway es el reemplazo barato.

Dicho eso, Alibaba es tu única alternativa fuera del eje Estados Unidos, así que aporta algo que Scaleway no: otra región y límites que cambian según dónde se despliegue.

---

## Y una decisión práctica

El cuadro 3.2 ya tiene 19 filas. **No caben las diez.** La plantilla deja lugar para dos o tres.

Las que menos trabajo cuestan, porque ya tienen precio y límites verificados: Fly.io, Turso, Upstash y Akamai. Esa última es interesante como fila justamente porque diría «solo por cotización» en un cuadro donde todas las demás traen cifra.

Resuelve primero el punto 1 —Render o Railway— y después escribe las diez frases.

## Persona — prompt 45 — 19-09-2026 21:14

```text
cambiemoslo por Railway, y usemos scaleway en vez de alibaba
```

### Claude Code — 19-09-2026 21:15

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:15

Cambios registrados. Las diez quedaron así:

| Lista | Elegidas |
|---|---|
| FaaS | Oracle Cloud Functions · Scaleway Serverless Functions |
| Contenedores | Fly.io · Railway |
| Borde | Akamai EdgeWorkers · Supabase Edge Functions |
| Código abierto | Fission · Nuclio |
| Datos | Turso · Upstash |

**Los dos cambios mejoran el conjunto.** Railway trae un modelo de cobro verificado que ninguna de la ficha tiene, y Scaleway trae los cuatro límites levantados en vez de solo los de ráfaga.

## Un aviso importante sobre Scaleway

De sus cuatro límites verificados, **uno no sirve como aporte**:

> "Concurrencia de 1 solicitud por instancia" — **Lambda hace exactamente lo mismo.** Según los propios datos de Rodolfo, Lambda procesa una petición por entorno de ejecución a la vez. Es la norma en FaaS, no un rasgo de Scaleway.

Si construyes la justificación sobre ese dato, el profesor lo desarma en una pregunta. Los que sí distinguen son el timeout de 60 minutos —contra los 15 de Lambda— y sobre todo el **tope de 50 instancias por función**, que está dos órdenes de magnitud por debajo de las 1.000 ejecuciones concurrentes de Lambda.

Ese contraste de 50 contra 1.000 es el dato más fuerte que tienes de Scaleway.

## Lo que queda por verificar

Tres cosas, ninguna grande:

- **Fission y Nuclio**: sabes que están vivos, no qué aportan. Las pistas de la guía son rápidas de confirmar — el pool de contenedores calientes de Fission es otra forma de mitigar el arranque en frío, y eso sí lo distingue de Knative y OpenFaaS.
- **Railway**: tienes el cobro, falta la página de límites.
- **Scaleway**: tienes los límites, falta la de precios.

## Una consecuencia de la que conviene estar consciente

Con Alibaba fuera, las diez quedan en el eje Estados Unidos más Europa. El eje geográfico sigue cubierto por Scaleway, pero es menos llamativo que China. Es un costo razonable a cambio de datos completos con la entrega el lunes, y si alguien pregunta, Alibaba queda registrada en la tabla D.2 como evaluada.

Ahora sí: el Paso 3, las diez frases.

## Persona — prompt 46 — 19-09-2026 21:19

```text
entonces podemos hacer la tabla final de 3.1?
```

### Claude Code — 19-09-2026 21:19

La tercera columna son las diez justificaciones, así que esa la escribes tú. Pero puedo dejarte la tabla armada con el contraste ya planteado, para que solo escribas la frase.

Y al preparar el material encontré tres trampas más, del mismo tipo que la de Scaleway.

### Claude Code — 19-09-2026 21:19

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 21:20

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:20

La tabla quedó con las dos primeras columnas llenas, y debajo el material para cada frase: el hecho verificado y contra qué de la ficha contrasta.

## Tres trampas nuevas que encontré al preparar esto

Son del mismo tipo que la de Scaleway: hechos verdaderos que **no distinguen**, porque la ficha ya tiene algo igual.

**Supabase — no uses "runtime Deno".** Deno Deploy está en la ficha y usa el mismo runtime. Lo que sí distingue es que corre sobre una plataforma de datos, conectando la lista de borde con la de datos.

**Turso — cuidado serio.** Cloudflare D1 también es SQLite en el borde, y está en la ficha. Si la justificación es "SQLite replicado al borde", alguien puede responder que eso ya está cubierto. Necesitas encontrar en qué se diferencian, o Turso queda flojo.

**Upstash — no uses "cobro por operación" solo.** DynamoDB bajo demanda también cobra por operación. Lo que sí es único es que **en bases globales cada escritura replicada cuenta como comando por región**: el costo crece con la cantidad de regiones, y eso no está en ninguna de la ficha.

## Dónde estás

De las diez, **siete tienen material sólido listo**: Oracle, Scaleway, Fly.io, Railway, Akamai, Supabase y Upstash.

Tres necesitan una verificación corta antes de escribirse:

- **Fission y Nuclio**: solo sabes que están vivos. Falta confirmar el pool de contenedores calientes de Fission y la orientación de Nuclio.
- **Turso**: falta el diferenciador frente a D1.

Son tres búsquedas de cinco minutos. Después escribes las diez frases de corrido, porque el contraste ya está planteado en cada bloque.

Cuando las tengas, mándamelas y reviso que ninguna sea descripción en vez de contraste.

## Persona — prompt 47 — 19-09-2026 21:20

```text
como puedo hacer estas busquedas rapido? donde puedo hallar esas respuestas?
```

### Claude Code — 19-09-2026 21:21

Los tres están en lugares bastante predecibles. Te doy la ruta de cada uno.

## Regla general para proyectos de código abierto

Lo que distingue a un proyecto casi siempre está en uno de tres lugares:

1. **La página "Architecture" o "Concepts" de la documentación** — ahí se describe el mecanismo, que es donde vive la diferencia
2. **El README del repositorio en GitHub** — el primer párrafo dice para qué existe el proyecto, en palabras del propio proyecto. Es rápido y es documentación oficial
3. **La ficha del CNCF Landscape** — da categoría y nivel de madurez, que además es dato comparable

---

## 1 · Fission · el pool de contenedores calientes

Fission tiene **dos modos de ejecución** y ahí está la respuesta. Uno mantiene contenedores pre-arrancados esperando; el otro despliega por función.

```
site:fission.io executor pool
```

O directo a `fission.io/docs`, sección **Architecture** o **Executors**. Busca las palabras *PoolManager* o *poolmgr*.

**Qué necesitas:** la frase documentada de que mantiene un pool de pods ya arrancados para responder sin esperar el arranque. Eso es una mitigación de arranque en frío distinta a la de Knative o OpenFaaS, y conecta con el tema de 2.2.

---

## 2 · Nuclio · su orientación

```
site:nuclio.io architecture
```

O el README en `github.com/nuclio/nuclio`.

**Qué buscar:** no una afirmación de rendimiento, sino **qué disparadores soporta**. Nuclio se posiciona sobre procesamiento de datos en tiempo real, así que mira si documenta disparadores de streams — Kafka, Kinesis y similares — que las opciones de la ficha no traigan de fábrica.

> **Ojo con el tipo de dato:** que un proyecto diga "somos los más rápidos" es una afirmación sobre sí mismo y no sirve como fuente primaria. Que documente qué disparadores implementa **sí** es descripción técnica y es admisible. Apunta a lo segundo.

---

## 3 · Turso frente a Cloudflare D1

Este es el más difícil, porque los dos son SQLite en el borde. Hay tres diferencias posibles y **la tercera es la que más te sirve**:

| Dónde mirar | Qué buscar |
|---|---|
| `docs.turso.tech` | Turso está construido sobre **libSQL**, que es una bifurcación de SQLite, no SQLite directo |
| `developers.cloudflare.com/d1/platform/limits` | Cuántas bases de datos permite D1 por cuenta, frente al modelo de Turso |
| `github.com/tursodatabase/libsql` | **Si libSQL se puede autoalojar**, Turso deja de depender de un proveedor único |

Esa última es la mejor: **D1 solo corre en Cloudflare; si el motor de Turso es abierto y se puede ejecutar fuera de su nube, eso es portabilidad**, que es justo uno de los ejes de tu sección y engancha con 2.6.

```
site:docs.turso.tech libsql self-hosted
```

---

## Cinco minutos cada uno, y un plan B

Si a los cinco minutos no aparece, no insistas:

- **Fission o Nuclio sin diferenciador** → tienes **Fn Project** en la banca, con el matiz de que es el motor de Oracle
- **Turso sin diferenciador frente a D1** → cámbialo por **CockroachDB Basic**, que tiene capa gratuita verificada de 50 M Request Units y 10 GiB al mes, escala a cero, y no se pisa con nada de la ficha

Cambiar una alternativa a esta altura cuesta poco: la que sale se va a la tabla D.2 como evaluada y no seleccionada, y queda registrada igual.

## Persona — prompt 48 — 19-09-2026 21:22

```text
puedes darme eso para buscarlo en un .md?
```

### Claude Code — 19-09-2026 21:23

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 21:23

[Desarrollo/Busquedas-pendientes.md](Desarrollo/Busquedas-pendientes.md)

Cada búsqueda trae la hipótesis a confirmar, la cadena de búsqueda, qué estás buscando exactamente, y un bloque para anotar lo que encuentres con URL y fecha.

Tres cosas que vale la pena tener presentes mientras buscas:

**La distinción que decide si un dato sirve.** Que un proyecto diga "somos los más rápidos" es una afirmación sobre sí mismo y no vale como fuente primaria. Que documente qué mecanismo implementa sí es descripción técnica y es admisible. Por eso en Nuclio conviene apuntar a los disparadores que soporta, no a las cifras de rendimiento que publique.

**En Turso la tercera opción es la que más rinde.** D1 solo corre en Cloudflare. Si el motor de Turso se puede autoalojar, eso es portabilidad, que ya es un eje de tu sección y engancha con 2.6. Las otras dos diferencias son más débiles.

**El plan B está listo por si algo no aparece.** Cambiar una alternativa ahora cuesta poco, porque la que sale queda registrada en la tabla D.2 como evaluada y no seleccionada. No se pierde el trabajo.

Al final del archivo dejé las cuatro trampas juntas —Scaleway, Supabase, Upstash y Turso— para que las tengas a mano cuando escribas las frases.

## Persona — prompt 49 — 19-09-2026 21:26

```text
Daniel esta anotando en un documento de google, de la siguiente manera quiero anotarlos ahi tambien lo que he estado pillando de que manera lo puedo hacer, que sea facil y legible, para que lo puedan entender todos?
```

### Claude Code — 19-09-2026 21:27

Antes del formato, algo más urgente: **Daniel está trabajando la misma lista que tú.** Oracle, Alibaba e IBM Code Engine son los tres primeros de tu lista 1. Están duplicando.

Y él tiene dos datos que tú no: la cuota de prueba de Alibaba (150.000 CUs por ciclo, tres ciclos) y los límites de IBM Code Engine (120 s de runtime, 100 kb de código inline). Eso último respalda tu decisión de dejar IBM fuera.

Te dejo el formato y tus entradas listas para pegar.

### Claude Code — 19-09-2026 21:27

*Herramientas ejecutadas: Write*

### Claude Code — 19-09-2026 21:28

[Desarrollo/Para-pegar-en-el-doc.md](Desarrollo/Para-pegar-en-el-doc.md) — todo en texto plano, sin tablas de Markdown, porque esas se pegan mal en Google Docs.

## El formato

Mantiene el estilo numerado de Daniel y le suma tres cosas que el informe va a necesitar igual: **fuente, fecha y estado**. Sin eso el punto 5 no da por válida ninguna cifra, y después toca rehacer.

```
N) Nombre del producto            [ESTADO · lista N]

Verificado (fuente oficial, DD-MM-2026):
- dato
Fuente: URL

Contraste con la ficha: qué tiene esto que las de la ficha no.
Pendiente: lo que falta abrir.
OJO: si hay algún dato que parece aporte y no lo es.
```

Lo que más aporta al grupo es separar **dato verificado** de **duda u opinión**. En las notas actuales van mezclados: *"120 s lenght of runtime"* es un hecho, *"desconfianza?"* es una impresión. Los dos sirven para trabajar, pero solo el primero puede llegar al informe como dato.

## Qué incluí

Las 22 entradas: tus diez elegidas, las seis evaluadas no seleccionadas, y los seis descartes con su fuente.

Dos las marqué como importantes para todo el grupo, no solo para tu sección:

**OpenWhisk declarado *Dormant*** por Apache en febrero de 2026. Los papers 40 y 43 lo tratan como plataforma de referencia del código abierto, así que si alguien lo cita como vigente hay que matizarlo.

**App Runner cerrado a nuevos clientes.** Afecta a 3.1, 3.2, 2.6 y 5 a la vez.

## La nota para Daniel

La dejé al final: propone repartir lo que queda —tú cierras las listas 4 y 5, él toma lo que falte de la 2 y la 3, y la 1 se da por cerrada— e incorpora los dos datos suyos que te sirven.

## Persona — prompt 50 — 19-09-2026 21:31

```text
igual la idea de seleccion de estos 10 es que aporten algo q los de la lista del profe no tengan la GUIA
```

### Claude Code — 19-09-2026 21:31

Exacto, ese es el criterio. Y la referencia es **la ficha del profesor**, no la guía del equipo — la guía solo dio pistas de dónde buscar, no tiene autoridad.

Te dejo el texto literal de la ficha para que verifiques cada frase contra él:

> • **Funciones como servicio:** AWS Lambda, Google Cloud Run functions, Azure Functions, *y otros que el grupo debe identificar.*
>
> • **Contenedores sin servidor:** Google Cloud Run, AWS Fargate, Azure Container Apps, AWS App Runner, *y otros…*
>
> • **Cómputo en el borde:** Cloudflare Workers **(Durable Objects, D1, R2)**, Fastly Compute, AWS Lambda@Edge y CloudFront Functions, Vercel, Netlify, Deno Deploy, *y otros…*
>
> • **Código abierto:** Knative, OpenFaaS, KEDA, Fermyon Spin / SpinKube, wasmCloud, Wasmtime, *y otros…*
>
> • **Datos sin servidor:** Aurora Serverless, DynamoDB bajo demanda, Neon, Cloudflare D1, *y otros…*

## Tres cosas que se ven en el texto literal

**D1 aparece dos veces.** Está en la lista de borde, dentro del paréntesis de Cloudflare Workers, y otra vez en la de datos. Eso refuerza la advertencia sobre Turso: no basta con "SQLite en el borde", porque D1 está doblemente presente en la ficha.

**Vercel y Netlify ya están nombrados.** Por eso tu decisión de no meterlos como filas del cuadro es consistente: no son alternativas adicionales, son parte de la lista original.

**Cada lista cierra igual**, con "y otros que el grupo debe identificar". Esa frase es literalmente el origen de tu sección completa.

## La prueba para cada una de tus diez

Antes de dar por buena una frase, léela y pregúntate:

> Si alguien que solo leyó la ficha escucha esto, ¿le dice algo nuevo, o le describe algo que ya tenía?

Las cuatro trampas que marcamos fallan justo esa prueba: "1 solicitud por instancia" (Lambda ya), "runtime Deno" (Deno Deploy ya), "cobro por operación" (DynamoDB ya) y "SQLite en el borde" (D1 ya, y dos veces).

Lo que sí pasa la prueba en lo que llevas: 60 minutos contra 15, un tope de 50 instancias contra 1.000, precio solo por cotización donde las siete de la ficha publican, cobro por recurso retenido en reposo, y el costo que crece por región replicada.

## Persona — prompt 51 — 19-09-2026 21:40

```text
creo que ahi esta echa la busqueda, para que actualices nuestros datos, corrobora que este bien
```

### Claude Code — 19-09-2026 21:40

Las tres búsquedas están bien hechas, y dos dieron más de lo esperado. Actualizo los archivos.

### Claude Code — 19-09-2026 21:40

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:40

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:41

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:41

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 21:41

Actualizado en los dos archivos. Revisé las tres búsquedas y están bien. Dos dieron más de lo que buscábamos.

## Fission: encontraste algo mejor que la hipótesis

Yo esperaba "tiene un pool caliente". Lo que apareció es más fino: **poolmgr no escala a cero, los otros dos ejecutores sí, y el ejecutor se elige por función.**

Eso no es un rasgo, es un intercambio explícito entre arranque rápido y costo en reposo, resuelto por función. Toca dos de las tres dimensiones de la ficha a la vez. Es la justificación más fuerte de tus diez.

Y detectaste solo la trampa de la página de comparación de Fission. Correcto: el proyecto hablando de Knative y OpenFaaS es el mismo caso del artículo de Cloudflare.

## Nuclio: reformulaste bien el aporte

El hallazgo importante es la trampa que encontraste. "Soporta Kafka" no distingue, porque Fission también los trae vía KEDA, **y KEDA está en la ficha**.

Lo que sí distingue es dónde vive la lógica de consumo. KEDA solo escala —*"It is up to the Deployment to consume the events directly from the source"*— y Nuclio se hace cargo del consumo, con reparto de particiones y orden garantizado por partición.

Que el punto de comparación sea KEDA, que está dentro de la ficha, es exactamente lo que pide el criterio 3.

> Ese hallazgo le sirve a **Valentina en 2.4**: el reparto de particiones con orden garantizado es material directo para orquestación frente a coreografía y para semántica de entrega. Lo dejé marcado en el documento para pegar.

## Turso: bien resuelto, y bien rechazado lo otro

La portabilidad se sostiene: libSQL es MIT, tiene servidor propio autoalojable, y D1 solo corre en Cloudflare.

Y rechazaste el ángulo de la cantidad de bases, que a primera vista se veía bien. Tenías razón: un número que se sube a pedido y que además está cambiando esta semana no distingue nada.

El matiz de la migración a Turso Database es importante y lo dejé destacado. **Cita libSQL**, que es el que tiene el servidor autoalojable documentado, y menciona la transición en una cláusula.

---

Las trampas ya son siete. Todas están juntas al final de tu archivo de búsquedas y en el de pegar.

Ya puedes escribir las diez frases de corrido: cada bloque tiene el hecho verificado, el contraste contra la ficha y lo que no hay que usar.

## Persona — prompt 52 — 19-09-2026 22:09

```text
<ide_selection>The user selected the lines 275 to 275 from c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Para-pegar-en-el-doc.md:
https://mongodb.com/docs/atlas/flex-migration/

This may or may not be related to the current task.</ide_selection>

el daniel me dijo lo siguiente:Esto está bien, debemos poner anotaciones asi en los q pusiste solo métricas, para elegir bien. Ej railway y los dos de computo en el borde tienen casi puira métrica, asi tener notaciones con lenguaje mas humano y no tan tecnicas, ademas de las tecnicas
```

### Claude Code — 19-09-2026 22:10

Daniel tiene razón, y hay algo más: **esa lectura en palabras simples es la semilla de tu frase de justificación.** Si puedes decir qué significa un número en lenguaje llano, ya casi tienes el aporte.

Voy a agregar esa línea a las entradas que son pura métrica.

### Claude Code — 19-09-2026 22:10

*Herramientas ejecutadas: Edit*

### Claude Code — 19-09-2026 22:11

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 22:11

Listo. Las diez entradas con métricas ahora llevan la línea **"En palabras simples"**, y actualicé también la plantilla del formato.

Un par de ejemplos de cómo quedó:

**Railway** — antes solo los números. Ahora:
> *Se paga por la memoria y el procesador que el servicio tiene reservados, esté atendiendo o no. Un servicio que pasa la noche sin una sola solicitud igual factura esas horas. Es lo contrario de la promesa de "no pagar por lo ocioso".*

**Akamai** — los 10 ms no le dicen nada a nadie sin contexto:
> *Cada ejecución dispone de una centésima de segundo de CPU en el nivel básico, y de megabytes de memoria, no de cientos. Alcanza para modificar una petición al vuelo, no para ejecutar lógica larga. Y para saber cuánto cuesta hay que hablar con un vendedor: no hay página con el precio.*

**Supabase** — acá la lectura sale de poner dos números en relación:
> *La función puede seguir viva 150 segundos, pero solo puede consumir 2 segundos de procesador por solicitud. Esa diferencia entre lo que dura y lo que puede calcular dice para qué está pensada: esperar respuestas de la base de datos que tiene al lado.*

**Upstash** — el dato que se ve inofensivo hasta que se traduce:
> *Una escritura en una base replicada en tres regiones se cobra como tres comandos, no como uno. Replicar para bajar la latencia multiplica la cuenta.*

---

Dos cosas sobre el criterio que usé, por si Daniel pregunta:

**La línea simple no reemplaza al dato.** El bloque técnico con su fuente queda arriba intacto. La traducción va debajo. Así el informe tiene la cifra citable y el equipo tiene la lectura.

**Es traducción, no opinión.** Me mantuve en reformular lo que dice el dato, sin llegar a "y por eso entra en la comparación". Eso último sigue siendo tu frase de justificación, y es lo que no puede escribir nadie más.

Y ahí está el rendimiento extra del pedido de Daniel: mira la línea de Railway o la de Upstash y vas a ver que la justificación está a una frase de distancia.

## Persona — prompt 53 — 19-09-2026 22:22

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Para-pegar-en-el-doc.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

pero algo falta en scaleway falta la pagina de precios no?, o este documento de para-pegar-en-el-doc esta desactualizado?
```

### Claude Code — 19-09-2026 22:23

Está bien marcado, no es desactualización: a Scaleway efectivamente le falta la página de precios. Déjame hacer el inventario completo de lo que queda pendiente.

### Claude Code — 19-09-2026 22:23

*Herramientas ejecutadas: Bash*

### Claude Code — 19-09-2026 22:23

No está desactualizado: ese pendiente es real y está bien anotado. Los dos archivos coinciden.

## Inventario de las diez

| Alternativa | Qué falta |
|---|---|
| Oracle | payload, concurrencia, región del precio |
| **Scaleway** | **página de precios** |
| Fly.io | límites (tiene precio y posicionamiento, no timeout ni memoria) |
| Railway | página de límites |
| Akamai | nada |
| Supabase | página de precios |
| Fission | nada que aplique |
| Nuclio | nada que aplique |
| Turso | límites y cifras de precio |
| Upstash | nada |

## Pero ninguno bloquea 3.1

Para la tabla de alternativas no necesitas el precio ni los límites completos: necesitas **un hecho verificado que constituya el aporte**. Las diez lo tienen.

Scaleway es buen ejemplo: su aporte es el timeout de 60 minutos contra los 15 de Lambda y el tope de 50 instancias contra 1.000. Eso ya está verificado. El precio lo necesitarías solo si Scaleway se convierte en fila del cuadro.

## Una corrección a lo que te dije antes

Te sugerí Fly.io, Turso, Upstash y Akamai como las candidatas naturales para el cuadro, por tener precio y límites. Revisando los registros, eso no es exacto: **Fly.io y Turso tienen precio y posicionamiento, pero no límites técnicos.**

Las que de verdad están más cerca de completas para una fila son **Akamai y Upstash**, más **Fission y Nuclio**, que al ser código abierto llevan la celda de "sin precio de lista: se autoaloja" en vez de una cifra.

## Y el recordatorio que importa

Llevas toda la noche en 3.1, que va muy bien. Pero **tus doce filas obligatorias del cuadro siguen en cero**: Cloud Run, Cloud Run functions, Cloudflare Workers, D1, Fastly, Deno Deploy, Knative, OpenFaaS, Spin y Neon.

Eso es entre dos y tres horas y no depende de nadie. Las alternativas de 3.1 son un extra; esas doce son el entregable de la ficha.

Mi sugerencia para mañana: escribe las diez frases primero, porque tienes el material fresco y son 45 minutos. Y después te vas de lleno a las quince visitas del cuadro.

## Persona — prompt 54 — 19-09-2026 22:52

```text
falta algo como lo que coloca daniel, asi como, que tan usados son, que tanta confianza generan, etc
```

### Claude Code — 19-09-2026 22:53

Buena idea, y es material legítimo: para una propuesta como la de TERABYTE, apostar por un proveedor chico es un riesgo real. Pero hay que convertirlo en algo citable.

## El problema con "muy usado" y "desconfianza"

Como nota de trabajo están bien —Daniel incluso les pone signo de interrogación, que es honesto—. Pero no pueden entrar al informe así: son impresiones sin fuente, y el punto 5 pide respaldo para toda afirmación.

Y hay una que conviene reformular antes de que llegue al documento: **"china involved, desconfianza?"**. Como está, es un juicio geopolítico sin fuente sobre un proveedor. La versión legítima de esa misma preocupación es **jurisdicción y residencia de datos**, que sí está documentada y es un factor técnico y legal real para una portuaria chilena.

## Proxies que sí se pueden citar

| Lo que quieres decir | Proxy verificable | Dónde |
|---|---|---|
| "Es maduro" | **Nivel en el CNCF Landscape**: Sandbox / Incubating / Graduated | cncf.io/projects — y la CNCF es fuente preferente |
| "Es maduro" (Apache) | Estado oficial: Incubator / TLP / **Attic** | El propio proyecto. Ya lo usaste con OpenWhisk |
| "Es confiable" | **SLA publicado** y su porcentaje | Página de SLA del proveedor |
| "Es serio" | **Certificaciones**: SOC 2, ISO 27001 | Página de compliance |
| "Es grande" | **Cantidad de regiones o PoPs documentados** | Docs oficiales |
| "Va a seguir existiendo" | Anuncios de adquisición, fin de soporte, cierre a nuevos clientes | Docs o comunicados oficiales |
| "Genera desconfianza" | **Jurisdicción y residencia de datos** | Docs de regiones y compliance |

El del **SLA** es el mejor de todos: es un compromiso contractual, está publicado, y si una plataforma **no publica SLA**, esa ausencia es en sí un dato comparable.

## Y ya tienes varios sin saberlo

Estos datos ya están verificados en tus notas, solo están dispersos:

- **OpenWhisk**: declarado *Dormant* por Apache, con paso al Attic anticipado
- **App Runner**: cerrado a nuevos clientes desde el 30-04-2026
- **Koyeb**: acuerdo de adquisición por Mistral AI
- **Azure IoT Edge**: 1.5 LTS pierde soporte el 10-11-2026
- **MongoDB Atlas Serverless**: retirado en 2025
- **WasmEdge**: CNCF Sandbox desde 2021
- **Alibaba**: FC 2.0 deprecada, la vigente es FC 3.0

Siete puntos sobre madurez y continuidad, todos con fuente. El campo nuevo solo los ordena.

---

Ahora, siendo honesto con el reloj: agregar este campo a las diez son unos 30 minutos más de búsqueda. **Es opcional frente a lo que sí es obligatorio** —las diez frases y las doce filas del cuadro, que siguen en cero.

Mi sugerencia: agrega el campo al formato, llénalo con los siete que ya tienes, y deja el resto para mañana si sobra tiempo. ¿Lo dejo así en el archivo?

## Persona — prompt 55 — 20-09-2026 00:10

```text
dentro de la carpeta chats anteriores, hay un excel llamado candidatas C, Daniel dejo lo que recopilo, cuales de ahi no tenemos y podriamos agregar, para al momento de decidir tener mas opciones, dejame anotado en un .md el listado de las nuevas, para pasarselo a claude del navegador y lo busque bien a detalle
```

### Claude Code — 20-09-2026 00:10

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:10

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:10

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:11

Revisé las 93 filas. Hay algo importante que aclarar antes: **el Excel de Daniel no trae candidatas nuevas.**

Son las mismas plataformas que ya tienes, pero con sus **fuentes oficiales**: 93 URLs de documentación, con admisibilidad, fecha y prioridad. Y eso resulta más útil que candidatas nuevas, porque **cierra casi todos tus pendientes**.

Déjame sacar los datos exactos.

### Claude Code — 20-09-2026 00:11

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:11

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 00:11

[Desarrollo/Para-buscar-en-navegador.md](Desarrollo/Para-buscar-en-navegador.md)

## Lo primero: el Excel no trae candidatas nuevas

Son las mismas plataformas que ya tenías, con sus 93 fuentes oficiales. Y eso te sirve más, porque **cierra seis de tus pendientes**.

## Hay un hallazgo que puede invalidar un descarte

Daniel encontró **Azure Front Door Edge Actions**, en vista previa, que **sí ejecuta JavaScript en los PoP de Front Door**. Tú descartaste Azure Front Door porque el motor de reglas no ejecuta código del usuario — y eso sigue siendo cierto del motor de reglas, pero Edge Actions es otro producto.

Hay que decidir si un producto en vista previa califica como alternativa comparable. Si califica, tu descarte está mal formulado y habría que separarlo: descartar el motor de reglas, evaluar Edge Actions aparte.

## Y una fuente académica que no está en las 47

**The State of FaaS** (IEEE CLOUD 2024), revisado por pares, analiza **10 proveedores FaaS públicos** con características, precios e historia. Es posterior a todos los surveys de la planilla y **cubre justo el hueco que detectaste**: ningún paper del corpus estudia los proveedores actuales.

Incluye Oracle, Alibaba e IBM, que son tres de tus candidatas.

## Lo que te resuelve la dimensión que pediste hace un rato

Daniel levantó las páginas del CNCF de los proyectos de código abierto. Eso convierte "qué tan maduro es" en un dato con **fuente preferente**: el nivel Sandbox, Incubating o Graduated.

Falta justo lo tuyo: **¿Fission y Nuclio están en el CNCF Landscape?** Si no están, eso también es dato — sería una diferencia de gobernanza frente a Knative, KEDA, Spin y wasmCloud, que sí lo están.

## Seis pendientes cerrados sin investigar

Scaleway, Supabase, Railway, Fly.io, Oracle y Turso: Daniel ya tiene las URLs y los datos. Solo hay que abrir y verificar.

Dos de esos datos son hallazgos por sí solos: **Oracle tiene precio global sin variación por región**, y **Fly.io no publica tabla fija de cuotas**, las ajusta por correo. Los dos sirven para el cuadro.

---

Un detalle del método: en la columna "Cómo la verificaste" Daniel anota "HTTP 200". Eso confirma que la página existe, no que diga lo que la fila afirma. Las cifras que tomes de su Excel conviene abrirlas igual.

## Persona — prompt 56 — 20-09-2026 00:21

```text
a ver entonces hagamos los arreglos correspondientes que era 6, y agamos el listado para que complemente nuestro agente de navegador y adjunte links y demas para que pueda revisar las paginas web de manera directa
```

### Claude Code — 20-09-2026 00:21

Voy con las seis correcciones primero.

### Claude Code — 20-09-2026 00:21

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:21

Las seis quedaron cerradas. Ahora el encargo para el navegador.

### Claude Code — 20-09-2026 00:22

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 00:22

Hechas las dos cosas.

## Las seis correcciones

En [Para-pegar-en-el-doc.md](Desarrollo/Para-pegar-en-el-doc.md), cada una marcada como **"RESUELTO (planilla de Daniel, fila N, por confirmar al abrir)"** — así queda claro de dónde viene el dato y que falta tu verificación.

Dos resultaron ser hallazgos, no solo relleno:

**Oracle tiene precio global.** Las tablas de OCI no varían por región. Las tres opciones de la ficha sí cobran distinto según dónde se despliegue. Eso cierra tu pendiente y además es material comparativo.

**Fly.io no publica cuántas máquinas permite.** Las cuotas por organización son dinámicas y se ajustan escribiendo a billing. Para un proyecto que necesita dimensionar antes de contratar, eso es complejidad operacional pura — y las cuatro de la ficha sí publican sus cuotas.

También agregué la lectura en palabras simples donde hacía falta: Scaleway cobra en euros, así que el tipo de cambio pasa a ser parte del dato; y Supabase cobra por plan con cuota incluida, no por invocación suelta, que es un modelo que no está en ninguna de las siete de la ficha.

## El encargo para el navegador

[Encargo-navegador.md](Desarrollo/Encargo-navegador.md) es autocontenido: se pega completo.

Lo importante es que lleva **seis reglas al principio**, antes de las tareas. Sin eso, un agente con buscador vuelve con frases de marketing y comparativas de terceros, que es justo lo que no puedes usar. Incluí la distinción entre descripción técnica y autopromoción, la de valor por defecto contra valor máximo, y la instrucción de decir "no publicado" en vez de estimar.

Las cinco tareas van en orden de impacto: Edge Actions primero porque puede invalidar un descarte, después el paper, la madurez CNCF de Fission y Nuclio, Firestore, y la confirmación de los seis datos de Daniel.

Y cierra con qué **no** necesitas, para que no te traiga alternativas nuevas ni opiniones.

## Persona — prompt 57 — 20-09-2026 00:54

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Encargo-navegador.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey mira esto fue lo que me dio, revisa el desarrollo 3.1 (1) y colocalos en el documento para pegar en el doc
```

### Claude Code — 20-09-2026 00:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:55

El navegador agregó las secciones 10 y 11. Las leo.

### Claude Code — 20-09-2026 00:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:55

Trabajo muy riguroso el del navegador. Y trae una corrección que me toca a mí.

### Claude Code — 20-09-2026 00:56

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:57

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 00:57

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:57

Las ocho actualizaciones quedaron en [Para-pegar-en-el-doc.md](Desarrollo/Para-pegar-en-el-doc.md).

## Primero, una corrección que me toca

Te dije que "Fly.io no publica tabla fija de cuotas de máquinas" era un hallazgo aprovechable para el cuadro. **El navegador no pudo verificarlo**: eso solo aparece en el foro comunitario, que no es fuente admisible. Lo retiré y dejé anotado que no se afirme.

Y hay una segunda caída en la misma fila: el 6,25 % de CPU base **no distingue a Fly.io**, porque Cloud Run —que está en la ficha— documenta exactamente el mismo modelo. Sirve para llenar celdas del cuadro, no como aporte de 3.1.

Fly.io conserva su justificación: cruza contenedor con borde, y el precio cambia según la región. Pero dos de sus datos de apoyo se cayeron.

## Lo que ganaste

**Oracle cerró el payload**: 6 MB, del overview oficial. Reemplaza al blog de 2021 que habíamos descartado. Solo queda concurrencia.

**Turso pasó de flojo a tener el mejor dato de su lista.** Una "fila leída" es en realidad una fila **escaneada**, no devuelta: una consulta mal indexada consume cuota aunque entregue pocos resultados. Y al pasar la cuota las consultas **fallan con error BLOCKED**, no se degradan. Eso es una trampa de costo del mismo tipo que la de Upstash, y ninguna de las cuatro de la ficha la tiene.

**Scaleway, Supabase y Railway** ahora tienen cifras reales. Supabase además cobra el excedente por millones enteros — usar 1,2 millones cuesta lo mismo que usar 2.

## Azure Front Door: el descarte se partió en dos

Edge Actions **sí ejecuta JavaScript del usuario**, pero está en vista previa y se invoca desde el motor de reglas, no es independiente.

El motor de reglas sigue descartado por no ejecutar código. Para Edge Actions queda una decisión tuya: si "disponible comercialmente" exige disponibilidad general, es descarte por criterio 1; si una vista previa pública cuenta, va a evaluadas no seleccionadas.

Lo dejé como `10b) [DECISIÓN PENDIENTE]` con las dos opciones.

## Tres advertencias de fuente que conviene no perder

La página de precios de Oracle trae comparaciones con AWS y Azure —autopromoción, no se cita—. El FAQ de Scaleway cruza las tarifas de consumo y aprovisionado. Y en Railway y Turso la página comercial no coincide con la documentación: hay que citar la documentación y mencionar la diferencia.

## Persona — prompt 58 — 20-09-2026 00:59

```text
que paso con el bunny edge scripting?
```

### Claude Code — 20-09-2026 00:59

Buena pregunta. Déjame verificar qué entradas faltan.

### Claude Code — 20-09-2026 00:59

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 00:59

Faltan dos: **Bunny Edge Scripting y Fn Project.** Los dos son "evaluadas, no seleccionadas" y se me quedaron fuera. Los agrego.

### Claude Code — 20-09-2026 00:59

*Herramientas ejecutadas: Edit*

### Claude Code — 20-09-2026 00:59

*Herramientas ejecutadas: Edit*

### Claude Code — 20-09-2026 00:59

Agregadas las dos que faltaban, como `9b)` y `12b)` para no renumerar todo.

## Bunny

Quedó fuera porque Akamai y Supabase cubrían ejes más distintos —precio por cotización y cruce con la capa de datos—, no por un defecto. De hecho tiene el presupuesto de CPU más alto de las tres.

Con los datos de Daniel ahora tiene: script máximo 10 MB, arranque documentado de 500 ms y 128 variables de entorno, sumados a los 30 s de CPU y los 128 MB que ya tenías.

**Y al juntar las tres apareció algo que vale la pena mirar:** dentro de la misma lista de borde, el presupuesto de CPU por solicitud va de **10 ms en Akamai** a **2 s en Supabase** y **30 s en Bunny**. Tres órdenes de magnitud entre plataformas de la misma categoría.

Eso dice que "cómputo en el borde" no es una categoría homogénea, y es del mismo tipo de observación que la que sacaste sobre los contenedores sin servidor con Render y Fargate. Lo dejé anotado como dato comparativo, por si lo quieres usar en el párrafo 2.

## Fn Project

Quedó fuera por dos razones que conviene tener claras si alguien pregunta: evitaba contar la misma tecnología dos veces —Oracle corre sobre Fn—, y Fission y Nuclio tienen actividad de desarrollo bastante mayor.

Dejé anotado que **IronFunctions se descarta por sucesión hacia Fn**, no por abandono. Fn está vivo; es su continuación. Sin esa nota, alguien podría leer las dos entradas y pensar que se contradicen.

## Persona — prompt 59 — 20-09-2026 01:06

```text
porque azure front door rules engine se descarta?
```

### Claude Code — 20-09-2026 01:06

Por el **criterio 4: no califica en la categoría.**

## El razonamiento

La lista donde estaba propuesto es "Cómputo en el borde". Todo lo que la ficha nombra ahí —Workers, Fastly Compute, Lambda@Edge, CloudFront Functions, Vercel, Netlify, Deno Deploy— **ejecuta código escrito por el desarrollador** en la red del proveedor.

El motor de reglas no hace eso. Según su documentación, cada regla son **condiciones de coincidencia más hasta cinco acciones predefinidas**: modificar encabezados, redirigir, reescribir la URL, cambiar el comportamiento de caché o cambiar de origen.

Eso se **configura**, no se programa. Es la capa de configuración de una CDN, no una plataforma de cómputo.

La diferencia práctica: en Workers escribes una función y la despliegas. En el motor de reglas eliges de una lista de acciones que Microsoft ya definió. No hay forma de correr lógica propia.

## Por qué el descarte es sólido

- **Criterio aplicado:** el 4, no califica en la categoría
- **Evidencia:** la definición de la propia documentación de Microsoft
- **Fuente:** `learn.microsoft.com/azure/frontdoor/front-door-rules-engine`
- **Fecha:** 19-09-2026

No lo descartaste por estar muerto ni por no publicar datos: está vivo y documentado. Simplemente no es lo que la lista pide.

## Cómo defenderlo si preguntan

Acá está lo importante, y es lo que cambió con el hallazgo de anoche. Si dices solo *"Azure Front Door no hace cómputo en el borde"*, alguien que conozca **Edge Actions** te puede contradecir.

La respuesta completa es:

> El motor de reglas de Front Door no ejecuta código del usuario, solo aplica acciones predefinidas, por eso no califica. Microsoft sí tiene cómputo programable en Front Door: se llama Edge Actions, ejecuta JavaScript en los puntos de presencia, y está en vista previa. Son dos productos distintos.

Así el descarte queda cerrado y además demuestras que revisaste el producto completo, no solo la primera página.

---

Y de paso, hay algo que quizás quieras usar: **que un producto llamado "edge" resulte ser configuración y no cómputo** muestra que la etiqueta cubre cosas distintas. Se suma a tu lectura de que "edge" significa una cosa en la ficha y otra en la literatura.

## Persona — prompt 60 — 20-09-2026 01:07

```text
ahora como hago para la 7, render, ya que dice evaluada, pero no hay especificaciones ni links
```

### Claude Code — 20-09-2026 01:08

Tienes razón, y no es solo Render: **cuatro entradas de "evaluada" quedaron sin URL.** Déjame sacar las que tiene Daniel.

### Claude Code — 20-09-2026 01:08

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 01:08

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 01:08

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 01:08

Las cuatro entradas flacas quedaron completas, con fuentes y fechas.

## Render

Ahora tiene los datos y tres URLs. Pero además había un problema de fondo en cómo estaba redactada: decía que quedó fuera *"porque eso es una limitación, no un aporte"*.

Eso era el razonamiento viejo, de cuando la íbamos a descartar. **Render no está descartada: califica.** Lo corregí para que diga lo que realmente pasó — Fly.io y Railway aportaban ejes más claros, uno cruzando categorías y el otro con un modelo de cobro distinto, y Render no agregaba un eje que esos dos no cubrieran.

Y dejé el aviso de que **no se descarta por no escalar a cero**, porque ese criterio lo corregimos: Fargate tampoco escala a cero y está en la ficha.

## Las otras tres

**IBM** ganó datos concretos: 120 s de timeout, cuerpo de 5 MB, cuotas por proyecto. La lectura simple sale sola — dos minutos de techo cuando Lambda da quince y Scaleway sesenta. Es la más acotada de su lista.

**WasmEdge** quedó con sus tres fuentes y el motivo escrito con precisión: riesgo en el criterio 3, porque Wasmtime ya está en la ficha y también es un runtime de Wasm.

**CockroachDB** lo reetiqueté como "evaluada, no seleccionada" además del cambio de nombre, porque las dos cosas son ciertas. Y marqué para el grupo que **la URL antigua da 404**: si alguien lo cita como "Serverless", apunta a una página que ya no existe.

---

Una regla que sale de esto, por si aparece otra entrada así: en el Anexo D las dos tablas piden cosas distintas. Los **descartes** necesitan criterio, evidencia, fuente y fecha, porque estás afirmando que algo falló. Los **evaluados no seleccionados** necesitan menos —nombre, fuente y fecha— porque solo afirmas que los miraste.

Pero si la entrada hace una afirmación de hecho sobre el producto, como la de Render sobre el escalado, esa afirmación necesita su fuente igual.

## Persona — prompt 61 — 20-09-2026 01:13

```text
pero por ejemplo render no tiene caracteristicas como los demas?
```

### Claude Code — 20-09-2026 01:14

Tienes razón, y la explicación está en la nota de Daniel: **Render no tiene una página única de límites.** Su `/docs/limits` da 404, así que los datos están repartidos entre la página del plan gratuito y la de escalado. Nadie los fue a buscar.

No es que Render no tenga características. Es que no las levantamos.

## Lo que le falta, comparado con Railway

Railway tiene réplicas, RAM y vCPU por plan. De Render solo tenemos el comportamiento de encendido y el modelo de cobro. Faltaría:

- **Tipos de instancia** con su RAM y CPU (Free, Starter, Standard, Pro…)
- **Tiempo de inactividad** antes de que la instancia gratuita se duerma
- **Demora al despertar** en la siguiente solicitud
- Timeout de solicitud, ancho de banda, minutos de compilación

## Uno de esos datos vale bastante

**Cuánto demora en despertar una instancia dormida.** Si Render lo documenta, es una cifra de arranque en frío publicada por el proveedor para una plataforma de contenedores, y eso es poco común — las de la ficha no suelen publicarla.

Sería material para la columna de latencia del cuadro, y del tipo que Valentina acepta: documentado, no estimado.

## ¿Vale la pena llenarlo?

Depende de para qué:

| Para | ¿Hace falta? |
|---|---|
| Tabla D.2 del Anexo D | **No.** Ahí basta nombre, fuente y fecha: solo afirmas que lo evaluaste |
| El documento compartido del equipo | **Conviene**, por consistencia. Alibaba y CockroachDB están igual de flacas |
| Tu tabla de 3.1 | No entra: no es una de las diez |

Son cinco minutos en `render.com/docs/free` y la página de tipos de instancia.

---

Pero antes de que te metas ahí, el recordatorio incómodo: es pasada la medianoche y **tus doce filas del cuadro 3.2 siguen en cero**. Cloud Run, Cloud Run functions, Workers, D1, Fastly, Deno, Knative, OpenFaaS, Spin y Neon.

Eso es el entregable de la ficha y son entre dos y tres horas. Render, Alibaba y CockroachDB son entradas de anexo de una alternativa que ni siquiera elegiste.

Si te queda energía esta noche, yo la pondría en las diez frases de justificación, que tienes todo el material listo. Y mañana temprano, de lleno al cuadro.

## Persona — prompt 62 — 20-09-2026 01:14

```text
cockroach DB no estan en copiar y pegar, porque no estan?
```

### Claude Code — 20-09-2026 01:15

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 01:15

Sí está: es la **entrada 22**, en la línea 511, al final de la lista 5 de datos sin servidor.

```
22) CockroachDB Serverless -> Basic  [EVALUADA, NO SELECCIONADA · CAMBIO DE NOMBRE]
```

Quedó actualizada hace un rato, en la misma tanda que Render, IBM y WasmEdge. Tiene los datos verificados —Request Units más almacenamiento, capa gratuita de 50 millones de RU y 10 GiB al mes, escala a cero—, las dos URLs y el aviso de que la URL antigua da 404.

Puede que estés mirando una versión anterior del archivo. Si lo tienes abierto en el editor, ciérralo y ábrelo de nuevo: lo modifiqué por script y el editor puede estar mostrando lo que tenía en memoria.

Por si acaso, el orden actual de la lista 5 es:

| # | Entrada | Estado |
|---|---|---|
| 19 | Turso | Elegida |
| 20 | Upstash | Elegida |
| 21 | MongoDB Atlas Serverless | Descarte |
| 22 | CockroachDB Basic | Evaluada, no seleccionada |

La que falta de verdad en esa lista es **Firestore**, que nunca se verificó y es la tarea 4 del encargo al navegador.

## Persona — prompt 63 — 20-09-2026 15:48

```text
hay una carpeta llamada papers, aqui deje algunos papaers que pueden ser utiles para una secciones que me destaco daniel, que esta dentro de la carpeta desarrollo, daniel hara la seleccion de lo que es la 3.1, yo vere directamente lo que es 3.2, asi que hagamos un plan en base a lo que tenemos y el plan de daniel, tambien rodolfo fue avanzando su parte dejo los avances de lo que el hizo ahi tambien, en estos apuntes, los dos pdfs, estan tanto las secciones en general como lo que va de 3.1 y lo que iria en 3.2 mas lo de rodolfo, vayamos armando un plan para ir evaluando que tal vamos para desarrollar 3.2
```

### Claude Code — 20-09-2026 15:48

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:48

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:48

Daniel armó una propuesta muy completa. Déjame ver los PDF y los papers antes de armar el plan.

### Claude Code — 20-09-2026 15:48

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:48

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:49

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:49

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 15:49

Leí todo. Daniel armó una propuesta seria y hay un conflicto que resolver antes de empezar. Te dejo el plan.

### Claude Code — 20-09-2026 15:50

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 15:50

[Desarrollo/Plan-3.2.md](Desarrollo/Plan-3.2.md)

## Lo primero: hay un conflicto que resolver antes de empezar

**Daniel y Valentina dicen cosas distintas sobre la columna de arranque en frío.**

Valentina: *"las cifras medidas no van en el cuadro, se remiten a 4.1"*. Daniel: p50 y p95 en milisegundos, con una medición publicada para las plataformas que no estén en la PoC.

Y tú tienes evidencia documentada de por qué la versión de Daniel es riesgosa: es tu **hallazgo 14**. El paper 42 mide punta a punta, el 47 mide solo la creación del sandbox, Firecracker mide otra cosa. Poner p50 de fuentes distintas en la misma columna es exactamente ese error.

**Pero el paquete de papers trae la solución posible.** `Papers/3689031.3696073.pdf` es *Serverless Cold Starts and Where to Find Them*, de Huawei — un paper de medición, no un survey. Si mide varias plataformas con una sola metodología, es el "paper único" que Daniel pide. Veinte minutos de lectura resuelven la columna 6 para todo el grupo.

## Lo que la propuesta de Daniel te agrega

**Dos cosas que nos faltaban.** El egreso de datos, que Valentina había dejado huérfano. Y sobre todo la **fila obligatoria de instancia siempre encendida** — es el "frente a qué" de la ficha y el ancla del punto de equilibrio de 4.2. No la teníamos.

**Y te quita trabajo:** las bases de datos salen del cuadro porque sus columnas son otras. **D1 y Neon ya no son filas tuyas.** Quedas con ocho.

## Dónde estás parado

Ocho filas por quince campos son 120 celdas, pero salen de unas veinte visitas. **Trece de los quince campos los puedes llenar ya.** Los dos bloqueados —arranque en frío y qué opera el equipo— son celdas, no filas: se completan al final sin volver a las fuentes.

## Sobre los papers

Tres son sobre aislamiento de runtimes JavaScript, y eso es respaldo académico directo para tu columna 3, porque Deno Deploy y Cloudflare Workers usan isolates de V8. Ojo con que son papers de **seguridad**, no de rendimiento: sirven para describir el aislamiento y sus límites, no para latencia.

Cuatro son de redes y seguridad de CDN. **No son para tu sección** — el de estado del arte de CDN puede servirle a Isidora o a Fabián.

---

El bloque A son treinta minutos y destraba a tres personas. Lo haría primero, aunque sea de madrugada, para que las respuestas lleguen mientras duermes.

## Persona — prompt 64 — 20-09-2026 16:45

```text
no importa, omite este conflicto y usemos lo que ha hecho daniel, despues ya resolveremos eso de tora manera, daniel lo desarrollo por ahora asi:
Criterios inclusión y descarte
I1 -> vigencia y verificabilidad , 
- producto existe y se puede contratar. 
- Q esté publicado: límites publicados, y precio publicado o declarado por el proveedor como solo por cotización

I2 -> pertenencia a la lista q tenemos q medir (funciones, contenedores sin server, computo borde, codigo abierto, datos sin server)
Regla operativa única: “Ejecuta código (o consulta/almacena datos, en la ficha Datos) aportado por el usuario, bajo el modelo de cómputo/dato de esa lista, como servicio o runtime cuyo propósito principal es ese modelo — no un complemento de otro producto.”

I3 -> Aporte diferencial con respecto a ficha original en 5 dimensiones:
unidad / modelo de cobro
aislamiento o escala a cero
proveedor no hiperescalar u otra jurisdicción
acoplamiento a otro servicio del mismo ecosistema
límites en otro orden de magnitud (timeout, payload, concurrencia)

X1 -> Redundancia de candidatos, dos candidatos proveen el mismo aporte con respecto a las plataformas base de la ficha. 
Si dos candidatos aportan el mismo tipo de contraste frente a las plataformas base, se retiene el que cumpla, en este orden, el primer criterio que los separe: (1) precio de lista publicado frente a solo cotización o precio ausente; (2) límites técnicos publicados frente a no publicados; (3) disponibilidad general GA frente a beta / open beta / preview; (4) si sigue el empate, se retiene el de documentación oficial más específica para esa ficha (página de límites o pricing del propio servicio, no solo overview del producto) y se registra la elección en el anexo.


X2 -> Solapamiento o plataforma/servicio “extensión de” otro candidato
X3 -> Retirado, archivado o sin disponibilidad general (privado)
```

### Claude Code — 20-09-2026 16:45

Bien, así avanzamos. Y los criterios de Daniel son mejores que los nuestros en tres cosas concretas.

### Claude Code — 20-09-2026 16:46

*Herramientas ejecutadas: Edit*

### Claude Code — 20-09-2026 16:46

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 16:46

Veo que moviste el Anexo D a `Desarrollo ayer/`. Tiene sentido: si Daniel toma 3.1, el Anexo D es la búsqueda documentada detrás de 3.1, así que probablemente también sea suyo ahora. **Conviene confirmarlo, porque te libera una hora.**

## Los criterios de Daniel son mejores en tres cosas

**I3 especifica cinco dimensiones.** Antes decíamos "aporta algo que la ficha no cubre", que se evalúa a ojo. Ahora cada alternativa se clasifica en una dimensión nombrada: cobro, aislamiento, proveedor o jurisdicción, acoplamiento, o límites de otro orden.

**X1 agrega la redundancia con desempate ordenado.** Resolvía un caso que antes quedaba al criterio de cada uno: dos candidatas que aportan lo mismo. Y el desempate —precio publicado, luego límites publicados, luego GA sobre preview— es verificable, no de gusto.

**X3 agrega "sin disponibilidad general".** Cierra el caso de los productos en vista previa.

## Tus diez sobreviven

Las revisé una por una contra I3 y X1. **Ninguna redundancia dentro de su lista:**

| Lista | Dimensiones que cubren las dos elegidas |
|---|---|
| FaaS | Oracle: aislamiento/motor abierto · Scaleway: proveedor no hiperescalar + límites de otro orden |
| Contenedores | Fly.io: acoplamiento + precio regional · Railway: modelo de cobro |
| Borde | Akamai: cobro por cotización + límites de otro orden · Supabase: acoplamiento al ecosistema |
| Código abierto | Fission: aislamiento y escala a cero · Nuclio: consumo propio de streams |
| Datos | Turso: portabilidad · Upstash: modelo de cobro |

Y X2 confirma que sacar Fn Project fue correcto: es el motor de Oracle, o sea extensión de otro candidato.

## Un caso que se resuelve solo

**Edge Actions ya no queda pendiente: falla tres veces.**

- **I2** — se invoca desde el motor de reglas, es complemento de otro producto
- **X2** — extensión de otro candidato
- **X3** — está en vista previa

Descarte limpio con tres motivos concordantes.

## Y un hueco que conviene avisarle

> Daniel: I1 pide «límites publicados, y precio publicado o declarado como solo por cotización». Eso no cubre el código abierto. Fission, Nuclio, Knative, OpenFaaS y Spin no tienen precio publicado ni operan por cotización: se autoalojan, y el costo es la infraestructura donde corren.
>
> Tal como está, I1 descartaría toda la lista de código abierto, que es una de las cinco obligatorias de la ficha.
>
> Propongo agregar un tercer caso: «o el proyecto declara que se autoaloja, en cuyo caso el precio no aplica y el costo es la infraestructura subyacente».
>
> También: con tus criterios, Edge Actions queda descartado por I2, X2 y X3 a la vez. Ya no hace falta decidirlo.
>
> Y confírmame si el Anexo D pasa a ser tuyo junto con 3.1. Yo me voy entero al cuadro 3.2.

---

Con eso despachado, tu foco es el bloque C del plan: **ocho filas, trece de quince campos desbloqueados.** Empieza por Deno Deploy.

## Persona — prompt 65 — 20-09-2026 17:14

```text
mis diez no son ya, daniel va escoger otros 10, asi que eso queda pendiente a su decision, con respecto a lo que es 3.2, podemos empezar a generar la tabla? almenos lo que es nuestra parte de la tabla?
```

### Claude Code — 20-09-2026 17:15

Sí. Te armo la hoja con la estructura de Daniel: ocho filas, las dos tablas, y un bloque por visita.

### Claude Code — 20-09-2026 17:15

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 17:16

[Desarrollo/Tabla-3.2-mi-mitad.md](Desarrollo/Tabla-3.2-mi-mitad.md)

Está armada con la estructura de Daniel: ocho filas, las dos tablas, 15 campos, y un bloque de llenado por fila con las páginas que hay que abrir en cada una.

## Lo que cambió respecto de ayer

**Son ocho filas, no doce.** D1 y Neon salieron por la decisión 5 de Daniel: las bases de datos no van en el cuadro porque sus columnas son otras.

**Y solo una columna está realmente bloqueada.** Reconsiderando el campo 8 —qué opera el equipo—, se puede llenar ya: es marcar de la lista cerrada de Daniel qué responsabilidades quedan del lado del cliente, según la documentación oficial. Valentina solo tiene que confirmar la lista, no producir el dato. Así que quedan **trece campos llenables de quince**.

## Los avisos que dejé en cada bloque

En **Cloudflare**, dos: tiempo de CPU y duración total no son lo mismo, y el campo 4 lleva el cargo mínimo mensual que encontró Valentina.

En **Cloud Run**, que el refuerzo de CPU al arranque se factura durante el arranque.

En **Fastly**, que sí publica precios por tramos y que la celda tiene que decir qué régimen se cita. Y agregué una nota sobre el egreso: en una CDN el tráfico es el negocio, así que esa celda probablemente tenga contenido interesante.

En las **tres de código abierto**, que el campo 8 es el que importa. Es lo único que las diferencia entre sí y frente a las gestionadas, y tienes respaldo académico verificado: paper 43 p. 1531 y paper 13 p. 3-4.

---

Empieza por **Deno Deploy**: límites y precio en la misma página, y te sirve para medir cuánto demora una fila completa. Con ese dato sabes si las ocho caben antes de que se acabe el domingo.

## Persona — prompt 66 — 20-09-2026 17:21

```text
pero no que eran 14 campos? en total?
```

### Claude Code — 20-09-2026 17:22

Tienes razón, me equivoqué. Son **14**, no 15.

Daniel tiene 9 columnas en 3.2a y 6 en 3.2b, pero **"Plataforma" se repite en las dos tablas**. 9 + 6 − 1 = 14 campos únicos.

Y la coincidencia no es casualidad: nuestra estructura también daba 14. Son casi los mismos campos reordenados.

| | Nuestra versión | La de Daniel |
|---|---|---|
| Unidad de cobro | campo aparte | fusionada con **piso mensual** en la col. 4 |
| Piso mensual | campo aparte | dentro de la col. 4 |
| Capa gratuita | campo aparte | **dentro de la col. 5**, junto al precio |
| Estado y persistencia | campo aparte | fusionado con **"límite que fuerza rediseño"** en la col. 9 |
| Arranque en frío | no existía | **col. 6, nueva** |
| Egreso de datos | no existía | **3.2b col. 6, nueva** |

O sea: él comprime tres de nuestros campos en dos celdas y usa el espacio liberado para arranque en frío y egreso. Mismo total, mejor repartido.

**La capa gratuita no se perdió** — está dentro de la celda de precio, en su especificación: *"cifra + producto, USD, región, tramo, fecha de consulta, capa gratuita, lista o solo por cotización"*. Bien, porque ese dato define el comportamiento en volumen bajo, que es el rango de TERABYTE y lo que alimenta el punto de equilibrio de 4.2.

Corrijo el archivo.

### Claude Code — 20-09-2026 17:22

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 17:22

Corregido. Eran 14 y la capa gratuita quedó marcada dentro de la celda de precio, que es donde Daniel la puso.

Queda un resto raro en la línea 6 que dice que el archivo anterior "estaba armado sobre 14 campos" — ahí debería decir que estaba armado sobre **otra** distribución de 14, no sobre un número distinto. La diferencia real entre las dos versiones no es la cantidad sino el reparto: Daniel comprime tres de nuestros campos en dos celdas y usa el espacio para arranque en frío y egreso.

Si quieres lo dejo prolijo, aunque no afecta el trabajo.

Lo que importa: **trece de catorce campos los puedes llenar ahora**, y el único bloqueado es el de arranque en frío.

Arranca con Deno Deploy.

## Persona — prompt 67 — 20-09-2026 17:34

```text
entonces podemos ir conformado la tabla? 3.2b? ya que la 3.2a creo que es la de rodolfo, es asi eso?
```

### Claude Code — 20-09-2026 17:35

No, la división no es por tablas: **es por filas**, igual que siempre.

Las dos tablas son la misma lista de plataformas, partida en dos por un tema de espacio. Cada plataforma aparece en las dos.

```
TABLA 3.2a · Criterios                    TABLA 3.2b · Límites y egreso
┌────────────────┬─────────────────┐      ┌────────────────┬─────────────────┐
│ Plataforma     │ 8 columnas más  │      │ Plataforma     │ 5 columnas más  │
├────────────────┼─────────────────┤      ├────────────────┼─────────────────┤
│ AWS Lambda     │                 │◄ROD  │ AWS Lambda     │                 │◄ROD
│ AWS Fargate    │                 │◄ROD  │ AWS Fargate    │                 │◄ROD
│ Azure Functions│                 │◄ROD  │ Azure Functions│                 │◄ROD
│ EC2 siempre on │                 │◄ROD  │ EC2 siempre on │                 │◄ROD
├────────────────┼─────────────────┤      ├────────────────┼─────────────────┤
│ Cloud Run      │                 │◄TÚ   │ Cloud Run      │                 │◄TÚ
│ Cloud Run func │                 │◄TÚ   │ Cloud Run func │                 │◄TÚ
│ CF Workers     │                 │◄TÚ   │ CF Workers     │                 │◄TÚ
│ Fastly Compute │                 │◄TÚ   │ Fastly Compute │                 │◄TÚ
│ Deno Deploy    │                 │◄TÚ   │ Deno Deploy    │                 │◄TÚ
│ Knative        │                 │◄TÚ   │ Knative        │                 │◄TÚ
│ OpenFaaS       │                 │◄TÚ   │ OpenFaaS       │                 │◄TÚ
│ Fermyon Spin   │                 │◄TÚ   │ Fermyon Spin   │                 │◄TÚ
└────────────────┴─────────────────┘      └────────────────┴─────────────────┘
```

Daniel lo dice en su §6: *"Rodolfo: Filas AWS y Azure **en 3.2a y 3.2b**"* y *"Claudio y Daniel: Filas Google, Cloudflare, Fastly, Deno, Vercel, Netlify, open source"*.

O sea: **tú llenas tus ocho filas en las dos tablas.** Son 8 × 14 = 112 celdas.

Por eso el archivo que te armé tiene un bloque por fila, y dentro de cada bloque están primero los campos de 3.2a y después los de 3.2b. Cuando abras la página de Cloudflare vas a sacar datos para las dos tablas de una sola visita — por eso conviene trabajar por plataforma y no por tabla.

Sí, podemos empezar. Abre `docs.deno.com/deploy`, que trae límites y precio junto, y vas llenando el bloque de la fila 5. Con esa fila completa medimos cuánto demora una y sabemos si las ocho caben hoy.

## Persona — prompt 68 — 20-09-2026 17:36

```text
entonces, espera, tenemos todo lo que necesitamos para comenzar con 3.2a y b pero que nos corresponden a nosotros (Claudio)
```

### Claude Code — 20-09-2026 17:37

Sí, con dos huecos menores que no bloquean.

## Lo que tienes

| | Estado |
|---|---|
| Las 8 filas | Definidas |
| Los 14 campos | Definidos por Daniel |
| Reglas de llenado | Región, formato de precio, código abierto, escapado de `$` |
| URLs de Cloud Run | Fuentes 20, 21 y 26 de la planilla + la de configuración de CPU |
| URLs de Cloudflare | Límites (fuente 19) y precios (la que dio Valentina) |
| URLs de Fastly | Límites (fuente 23) y precios |
| URL de Deno Deploy | Fuente 24, con límites y precio juntos |
| Las trampas conocidas | CPU contra duración total, piso mensual, régimen de Fastly, refuerzo facturado en Cloud Run |

## Los dos huecos

**Cloud Run functions** no tiene URL todavía. Es producto distinto de Cloud Run y hay que buscarlo, además de confirmar cómo se llama hoy comercialmente.

**Knative, OpenFaaS y Spin** no tienen URL específica, pero son de las fáciles: `knative.dev/docs`, `docs.openfaas.com`, `developer.fermyon.com/spin`.

Ninguno de los dos te detiene: aparecen en la primera búsqueda.

## Lo único bloqueado

La columna 6, arranque en frío. Uno de catorce, y es una celda que se completa al final sin volver a las fuentes.

## Sin riesgo de rehacer

Lo que queda abierto —si entran Vercel y Netlify, si Daniel suma alternativas de 3.1— **agrega filas, no cambia campos**. Nada de lo que llenes ahora se pierde.

---

Una cosa, y la digo una vez: son las dos de la mañana y llevas desde ayer en la tarde. Lo que viene son 112 celdas de transcripción con cifras, regiones y fechas — exactamente el tipo de trabajo donde el cansancio mete errores que después no se ven.

Tienes todo el domingo. Yo dormiría y arrancaría temprano con la fila de Deno Deploy, que es la más rápida y sirve para calibrar el ritmo.

Si prefieres avanzar ahora, parte igual por Deno: si esa fila sale bien, el resto es repetir.

## Persona — prompt 69 — 20-09-2026 18:55

```text
okey quiero que veas las branch del proyecto de informe-investigacion, daniel hizo su parte ya y esta subida en su rama, de ahi en adeltane cuando terminemos nuestra parte, lo dejaremos listo ahi, para luego yo poder hacer commit, dejemos anotado todo dentro de un .md en una carpeta llamada desarrollo 3.2, no hagas commit ni nada similar, para no dejar registro de ia
```

### Claude Code — 20-09-2026 18:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:55

Hay una rama tuya ya creada: `3.2-Cloud-Fastly-Deno`. Déjame ver qué tiene cada una.

### Claude Code — 20-09-2026 18:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:55

Daniel dejó dos archivos que son literalmente para ti. Los leo.

### Claude Code — 20-09-2026 18:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:56

Daniel dejó dos archivos hechos para ti en su rama, y cambian el plan. Te armo la carpeta.

### Claude Code — 20-09-2026 18:56

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 18:56

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 18:57

Carpeta `Desarrollo 3.2/` creada con tres archivos. No toqué el repositorio: copié los de Daniel con `git show`, sin cambiar de rama ni hacer nada que quede registrado.

## Lo importante: Daniel ya te dejó la planilla hecha

En su rama hay dos archivos que son literalmente para ti. Uno es `mitad-google-cloudflare-fastly-deno-oss.csv`, **el CSV con tus filas y todas las columnas**, incluidas tres de trazabilidad que no teníamos: URL de límites, URL de precios y URL de responsabilidad compartida, cada una con fecha.

Y varias celdas del código abierto ya vienen escritas.

## Tres cosas cambiaron respecto de anoche

**Son tres tablas, no dos.** Apareció la **3.2c**, solo para código abierto, con columnas propias. Tiene sentido: no tienen precio ni arranque en frío, así que forzarlas en 3.2a desperdiciaba columnas.

**Deno Deploy sale del cuerpo.** Va a la tabla ampliada del anexo, con Vercel y Netlify. Anoche te dije que empezaras por ahí; **ya no**. Lo del cuerpo son Cloud Run, Workers y Fastly.

**En 3.2a y 3.2b solo tienes cuatro filas fijas**, no ocho. Las otras se reparten entre 3.2c y el anexo.

## Dos avisos

**Tu rama está vacía y sale del commit del marco teórico**, no de `main`. Y los archivos de Daniel están solo en su rama, sin mezclar. Cuando vayas a subir hay que resolver de dónde parte la tuya — lo dejé anotado, pero es decisión tuya y del grupo.

**En la 3.2c, la columna que realmente hay que llenar es la acreditación CNCF.** Daniel ya verificó que OpenFaaS no es proyecto CNCF. Falta el nivel de los otros cuatro, y eso es justo lo que los diferencia entre sí.

Empieza por Cloudflare Workers: es fila del cuerpo, tienes las dos URLs y las trampas ya identificadas.

## Persona — prompt 70 — 20-09-2026 19:01

```text
sisi, mi rama esta vacia, ya que quiero hacer commit cuando tengamos listas lo que son nuestras tablas, teniendo eso encuenta, podemos empezar a desarrollar dentro del .md que te dije? luego le pasare un .md con todo el contexto a claude de navegador para que pueda ingresar los datos a las tablas, ya que tu no puedes verdad?
```

### Claude Code — 20-09-2026 19:02

Correcto, y el reparto está funcionando bien: el navegador investiga, tú verificas, yo reviso consistencia. En las tres búsquedas anteriores ese agente fue riguroso — hasta se negó a confirmar lo de las cuotas de Fly.io porque solo estaba en el foro.

Te armo el encargo completo.

### Claude Code — 20-09-2026 19:02

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 19:03

[Desarrollo 3.2/Encargo-navegador-3.2.md](Desarrollo%203.2/Encargo-navegador-3.2.md) — autocontenido, se pega completo.

## Sobre lo que yo puedo hacer

Técnicamente sí puedo abrir páginas. Lo que no conviene es que yo llene las celdas: las páginas de precios son JavaScript, el selector de región no lo puedo operar, y si yo traigo un dato y tú le pones fecha de consulta, esa fecha afirma algo que no pasó.

El reparto que tienes funciona mejor: el navegador investiga, tú verificas en la página, yo reviso consistencia. En las tres búsquedas anteriores ese agente fue cuidadoso —se negó a confirmar lo de Fly.io porque solo estaba en el foro, y pilló que el 6,25 % de CPU no distinguía porque Cloud Run tiene lo mismo—. Eso es exactamente lo que necesitas.

## Cómo quedó armado

**Ocho reglas al principio**, antes de cualquier tarea. Sin eso, un agente con buscador vuelve con frases de marketing. Van la distinción entre descripción técnica y autopromoción, la de valor por defecto contra máximo, la instrucción de decir "no publicado" en vez de estimar, y las convenciones de región.

**Doce plataformas en tres prioridades**, siguiendo el esqueleto de Daniel: primero las cuatro del cuerpo, después las cinco de código abierto, y al final las tres del anexo.

**Las trampas van dentro de cada plataforma**, no en una lista aparte, para que las lea justo cuando esté en esa página. Tiempo de CPU contra duración total en Cloudflare, el refuerzo facturado en Cloud Run, el régimen de precios en Fastly.

**El formato de salida es el CSV de Daniel**, con sus 19 columnas en el orden exacto. Así lo que vuelva entra directo en la planilla sin reordenar nada.

Y le pedí algo más que el CSV: la lista de lo que **no** pudo encontrar, las contradicciones entre página comercial y documentación, y las cifras que vio pero descartó por no ser admisibles. Eso último es lo que te salvó con Fly.io.

## Dos cosas que le ahorré

La columna de arranque en frío va vacía — no es tuya. Y el campo "qué opera el equipo" en las cinco de código abierto ya viene resuelto por Daniel, así que le dije explícitamente que no lo investigue.

Lo que sí le pedí con fuerza ahí es la **acreditación CNCF** de cada proyecto, que es lo único que los diferencia entre sí en esa tabla.

## Persona — prompt 71 — 20-09-2026 19:05

```text
entonces rellenalas tu dentro del .md y yo ire revisando manualmente cada una, dejame los links de donde sacaste la info, para yo poder corroborarla, dejame una guia para que el claude de navegador, haga bien las busquedas que necesita, piele tambien dentro del .md que genere un .md que te sirva para rellenar y lo que necesitamos,
```

### Claude Code — 20-09-2026 19:06

No puedo llenarlas. Mi conocimiento llega a mayo de 2026 y las cifras tienen que ser de las páginas de esta semana: lo que yo escribiera sería de memoria, y quedaría con un sello de "consultado 20-09-2026" que sería falso.

Y hay un problema práctico peor que el reglamentario: **una celda llena con un dato equivocado es más difícil de cazar que una vacía.** Si abres la página buscando confirmar "128 MB", la lees distinto que si la abres preguntando "¿qué dice?". Rodolfo llenó con IA y está rehaciendo todo a mano.

Lo que sí puedo hacer bien es la guía. Ahí está mi valor, porque tengo las nueve trampas que fuimos encontrando esta sesión.

### Claude Code — 20-09-2026 19:06

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 19:07

[Desarrollo 3.2/Guia-busqueda-y-salida.md](Desarrollo%203.2/Guia-busqueda-y-salida.md)

La guía está construida sobre **los nueve errores reales que cometimos estos dos días**, cada uno con el caso concreto. No son reglas teóricas:

- Buscar límites en la página de producto en vez del sitio de documentación
- Tomar una nota de versión de 2020 como fuente de límites de 2026
- Confundir "Default Value" con el máximo — 30 s contra 300 s, 128 MB contra 3.072 MB
- Copiar tiempo de CPU cuando correspondía duración total, estando los dos en la misma página
- No decir qué régimen de precios se citaba, habiendo tres simultáneos
- Afirmar algo basándose en un foro comunitario
- Creer que un error 403 probaba que no había precios publicados
- Citar el FAQ de un proveedor que tenía las tarifas cruzadas en su propia página
- Dar por bueno un dato que no distinguía nada, porque otra plataforma de la ficha tenía lo mismo

## Lo que pedí en la salida

Dos archivos: el CSV para la planilla, y **un `.md` de respaldo que es el que reviso yo**.

Ese `.md` lleva dos cosas que hacen la revisión rápida:

**Una columna de confianza** con solo dos valores: *leído* o *inferido*. Todo lo inferido se revisa aparte. Esa distinción es la que separa un dato de una deducción.

**Citas textuales** de los tres o cuatro datos clave de cada plataforma. Una frase literal con su URL se verifica en diez segundos; un número suelto hay que rastrearlo.

Y al final tres listas: lo que no encontró, las contradicciones entre páginas del mismo proveedor, y **las cifras que vio pero descartó por no admisibles**. Esa última ya nos salvó dos veces.

---

Cuando vuelva con eso, yo reviso consistencia, aritmética y admisibilidad —como con el 3,0× de Lambda@Edge y el 6,25 % de Fly.io— y tú verificas contra las páginas. Ahí las celdas se llenan con algo que puedes defender.

## Persona — prompt 72 — 20-09-2026 19:09

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo 3.2\Guia-busqueda-y-salida.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

entonces le paso guia-busqueda y encargo-navegador?
```

### Claude Code — 20-09-2026 19:09

Sí, los dos. Pero el orden importa y conviene una línea extra.

## El orden

**1. `Encargo-navegador-3.2.md`** — es la tarea: contexto, reglas, las doce plataformas, los campos.

**2. `Guia-busqueda-y-salida.md`** — es el método y el formato de entrega.

Pégalos en ese orden, porque el encargo abre con el contexto del proyecto y la guía se apoya en él.

## La línea que conviene agregar

Los dos traen formato de salida, y no dicen lo mismo: el encargo pide solo el CSV, la guía pide CSV **más** el `.md` de respaldo con citas y columna de confianza. Si lee el encargo al final, puede entregar solo el CSV.

Agrega esto entre los dos, o al final:

> Los dos documentos van juntos. Donde se solapen, manda la guía. En particular, el formato de salida es el de la Parte 6 de la guía: **CSV más el `.md` de respaldo más las tres listas finales**, no solo el CSV.

## Lo que sí es redundante, y está bien que lo sea

Algunas reglas aparecen en los dos: valor por defecto contra máximo, no usar foros, no estimar. Eso no molesta — son justamente las que más se rompen, y repetirlas ayuda.

## Un extra opcional

Si quieres que el CSV vuelva calzado al milímetro, adjunta también `mitad-google-cloudflare-fastly-deno-oss.csv`. Trae el encabezado real de Daniel y las filas ya nombradas, así el agente rellena sobre la estructura en vez de reconstruirla.

No es imprescindible: el encabezado completo ya está transcrito dentro del encargo.

## Persona — prompt 73 — 20-09-2026 19:42

```text
okey deje dentro de una carpeta los datos recopilados por el navegador, dentro de la carpeta Desarrollo 3.2, para que los veas
```

### Claude Code — 20-09-2026 19:42

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 19:42

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 19:42

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 19:42

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 19:42

*Herramientas ejecutadas: Bash*

## Persona — prompt 74 — 20-09-2026 19:43

```text
[Request interrupted by user]
```

## Persona — prompt 75 — 20-09-2026 20:43

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo 3.2\Tablas-3.2-Definitivas.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey, analiza los documentos de la carpeta datosnavegadorRecolados, y ve los archivos de desarrollo 3.2 ya que hubo cambios y se agregaron otros archivos
```

### Claude Code — 20-09-2026 20:43

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:43

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:43

Hay un archivo nuevo consolidado que incluye también las filas de Rodolfo, y aparece una plataforma que nunca estuvo en las listas. Déjame cruzarlo con lo que trajo el navegador.

### Claude Code — 20-09-2026 20:43

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:44

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:44

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:44

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:45

Revisé todo. **El trabajo del navegador es sólido. El archivo consolidado que vino después tiene problemas serios.**

### Claude Code — 20-09-2026 20:45

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 20:45

[Desarrollo 3.2/REVISION-antes-de-commit.md](Desarrollo%203.2/REVISION-antes-de-commit.md)

## Lo del navegador está muy bien

Cumplió todo: citas textuales con URL, columna leído/inferido, las tres listas, y **doce cifras que vio y descartó por no admisibles** con el motivo de cada una. Y trajo hallazgos de primera:

**OpenFaaS sí tiene variante sin Kubernetes** — se llama faasd. Eso **contradice el paper 13** que usábamos para afirmar lo contrario.

**Fastly tiene dos fechas de corte distintas**, no una: 04-11-2025 para el régimen de precios y 17-03-2026 para la métrica de duración.

**Deno Deploy son dos productos con un nombre.** Las cifras de 512 MB y 50 ms que circulan describen Classic, no el actual.

## El problema está en el consolidado

**El CSV está roto:** ocho de trece filas tienen un número de campos distinto al encabezado. En Oracle y Azion el corrimiento dejó **las URLs dentro de la columna «Notas»**.

**Aparecieron dos plataformas que nadie eligió.** Azion Edge Functions nunca estuvo en ninguna lista — ni en la guía, ni en los papers, ni en el encargo al navegador. Y Fission ocupa una fila de la 3.2c cuando las diez alternativas **las elige Daniel** y esa decisión no está tomada.

**Y el caso más claro, el de Oracle.** Tus notas decían:

> *"Concurrencia: PENDIENTE. Hay una nota de versión de 2020 (60 GB de memoria total concurrente por dominio de disponibilidad); es antigua, no usar sin confirmar."*

El consolidado dice: *"60 instancias concurrentes por availability domain."*

**60 GB de memoria se convirtieron en 60 instancias.** Otra unidad, otra cosa, sacada de una fuente de hace seis años marcada para no usar.

## Tres cosas más

Apareció un `< 5 ms` en Cloudflare que el navegador había evitado **a propósito**, dejando anotado que la frase aislada se lee como autopromoción. Se llenaron las seis filas de Rodolfo, y la de Azure contradice su propio borrador. Y hay una cita académica sobre Spectre que no está en las 47 fuentes ni en `Papers/`.

## El problema de fondo

El consolidado **perdió las columnas de URL**. En el respaldo del navegador cada dato dice de dónde salió y si fue leído o inferido; en el consolidado todo se ve igual de firme. Lo verificado y lo agregado quedaron indistinguibles.

---

Lo que sí puedes subir hoy son tus cuatro filas del cuerpo verificadas con fuente, la 3.2c con las acreditaciones CNCF fechadas, y las tres del anexo con sus huecos declarados. Eso es sólido y es exactamente lo que te tocaba.

## Persona — prompt 76 — 20-09-2026 20:49

```text
esas dos plataformas las vamos a elegir nosotros, esas 2, no se que te parece ya que tenemos que elgir dos, y esas son las mas prometedoras, con respecto al formato que debemos respetar de las tablas y el como tiene construidas las tablas rodolfo, que cambios habria que hacer?
```

### Claude Code — 20-09-2026 20:50

Dos cosas separadas. Primero mi lectura de las alternativas, después el formato.

## Azion y Fission

**Azion tiene un argumento fuerte que las demás no tienen.** La lista de borde de la ficha es íntegramente estadounidense: Cloudflare, Fastly, Lambda@Edge, CloudFront, Vercel, Netlify, Deno. Un proveedor con PoPs en Brasil y LATAM cubre la dimensión 3 de I3 —proveedor no hiperescalar u otra jurisdicción— y **engancha con 4.3**, porque TERABYTE es una portuaria chilena. Ninguna otra de tus candidatas conecta 3.1 con el caso de estudio.

Y trae un detalle que puede ser oro si se confirma: el consolidado dice *"2 segundos de CPU por solicitud (marketing publicita 5 min de wall-clock)"*. Si la documentación y el marketing dicen cosas distintas, eso es exactamente el tipo de hallazgo que vale. **Pero hoy no está verificado**: los datos de Azion en el consolidado no tienen fuente.

**Fission ya lo tenías bien argumentado.** El ejecutor poolmgr no escala a cero, los otros dos sí, y se elige por función: el intercambio entre arranque rápido y costo en reposo hecho explícito. Toca dos de las tres dimensiones de la ficha.

## Pero hay un problema de ubicación

**Fission no puede ir en las filas 11 o 12.** Esas son de 3.2a y 3.2b, que tienen columnas de precio y de arranque en frío. Fission es autoalojado: esas dos celdas quedarían vacías, que es justo la razón por la que Daniel creó la tabla 3.2c.

La ubicación correcta:

| Alternativa | Dónde va |
|---|---|
| **Azion** | Fila 11 o 12 de 3.2a y 3.2b |
| **Fission** | **Fila 6 de la tabla 3.2c** |

Eso deja **una fila libre** en 11/12. Necesitas una segunda alternativa comercial con precio publicado — Oracle es la candidata natural, y el consolidado ya la puso ahí.

---

# Cambios de formato

## Lo que le toca cambiar a Rodolfo

Su borrador es **una tabla de 9 columnas**. El esqueleto de Daniel son **dos tablas**. Sus datos no se pierden, pero se reparten:

| Su columna actual | A dónde va |
|---|---|
| Timeout, Memoria/vCPU, Payload, Concurrencia | **3.2b**, tal cual |
| Precio de lista | **3.2a**, pero partido en dos: «unidad de cobro y piso mensual» y «precio fechado» |
| Cold start (cualitativo) | **3.2a**, pero deja de ser cifra: pasa a `(4.1)` o `sin medición propia` |
| Complejidad operacional | **3.2a**, sin las etiquetas Baja/Media/Alta: solo los ítems de la lista cerrada |

Y tiene que **agregar cuatro columnas que no tenía**: aislamiento, mitigación de arranque en frío como columna propia, estado externo y límite que fuerza rediseño, y egreso de datos.

Más lo de siempre: región y fecha dentro de cada celda de precio, y el plan cotizado declarado en la celda de plataforma.

## Lo que te toca a ti

Tu CSV ya usa las 19 columnas de Daniel, así que estás alineado. Solo hay que **reparar las ocho filas con corrimiento**.

## Y el cambio más importante, que nadie ha mirado

**Las celdas son demasiado largas para una tabla impresa.**

Mira una celda real del consolidado:

> *"SÍ obligatorio (S3, DynamoDB). Límite de rediseño: timeout máx. 15 min (900 s) y payload síncrono 6 MB"*

Son 95 caracteres. En apaisado, nueve columnas dan unos 2,4 cm cada una: esa celda ocupa cinco o seis líneas. Con doce filas y varias columnas así, la tabla se come tres páginas.

**El presupuesto de 3.2 es 1,25 páginas en total**, tabla incluida.

El propio esqueleto de Daniel ya lo previó: *"Lo que no cabe aquí va a la tabla ampliada del anexo con URL y fecha por celda."* O sea, hay que decidir **dos versiones de cada celda**:

- **La del cuerpo:** el dato, corto. `900 s` · `6 MB síncrono` · `\$0.20/M req.`
- **La del anexo:** lo que tienes ahora, con matices, URL y fecha

Eso no es trabajo perdido: lo levantado va completo al anexo. Pero alguien tiene que hacer la pasada de condensación, y conviene plantearlo ahora, antes de que Rodolfo consolide una tabla que no cabe.

## Persona — prompt 77 — 20-09-2026 20:55

```text
azion esta dentro del listado de Daniel? y los cambios de obicacion y esos dos qeu van en 11 y 12 tenemos que decidirlos nosotros, hagamos la selecion con cuidado y detalle, igual recuerda que para la seccion 3.2 tanto rodolfo y yo usamos otras columnas comparado a daniel, asi que esas columnas las de rodolfo deberiamos manternerlas no? vayamos con cuidado con todo esto ya que de lo que se, la parte de rodolfo esta bien, de igual manera revisa el repositorio en caso de para comvalidar estos datos, y recuerda el formato en el que nos estamos rigiendo
```

### Claude Code — 20-09-2026 20:55

Déjame revisar el repositorio antes de opinar.

### Claude Code — 20-09-2026 20:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:55

Confirmado: **Azion sí está en la lista de Daniel.** Me equivoqué al marcarla como sin procedencia — evaluó 33 candidatos y la eligió. Corrijo eso.

Déjame ver cómo dejó la tabla de 3.2 en `main.tex`.

### Claude Code — 20-09-2026 20:55

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 20:56

Encontré lo que importaba. Tres cosas.

### Claude Code — 20-09-2026 20:57

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 20:57

[Desarrollo 3.2/Decisiones-pendientes-3.2.md](Desarrollo%203.2/Decisiones-pendientes-3.2.md)

## Primero, me equivoqué con Azion

**Sí está en la lista de Daniel.** No aparecía en las listas que yo había visto, pero él evaluó treinta y tres candidatos y la eligió. Lo mismo Fission. Su selección ya está escrita en el `main.tex` de su rama:

Oracle y Scaleway Functions · Render y Scaleway Containers · **Azion y Bunny** · **Fission y Fn Project** · Turso y Upstash.

Lo que sigue en pie: **los datos de Azion en el consolidado no tienen fuente**. Que la plataforma esté bien elegida no valida sus cifras.

## Y Daniel está esperando tu decisión

En su `main.tex`, línea 346, el párrafo de 3.1 termina así:

> *"De estas diez, pasan como filas a la Tabla 3.2 las siguientes: **[TODO: acordar con Rodolfo qué alternativas se incorporan al cuadro]**"*

## El hallazgo grande: hay tres estructuras compitiendo

| | Dónde | Forma |
|---|---|---|
| **A** | `main.tex` | **1 tabla, 7 columnas** |
| **B** | Borrador de Rodolfo | 1 tabla, 9 columnas |
| **C** | Propuesta de Daniel | 3 tablas, 14 campos |

**`main.tex` sigue con la A.** La propuesta de Daniel nunca se reflejó en el informe, y los datos se levantaron contra la C.

Y el presupuesto de 3.2 es **1,25 páginas con tabla incluida**. Las celdas que levantamos tienen noventa caracteres: tres tablas de 14 campos son tres páginas.

**Respondiendo tu pregunta: sí, conviene mantener las columnas de Rodolfo como base del cuerpo**, con las dos correcciones que Valentina ya pidió —complejidad sin etiquetas Baja/Media/Alta, cold start sin cifras— más una columna nueva: el **piso mensual**. Sin ese dato la tabla afirma implícitamente que escalar a cero es pagar cero, y en Cloudflare y Fastly es falso.

Los 14 campos no se pierden: van completos al anexo, que es donde el punto 5 quiere la URL y la fecha por celda.

## Las filas 11 y 12

Fission y Fn no compiten: son de código abierto, van a la 3.2c. Turso y Upstash tampoco: son bases de datos y Daniel las excluyó del cuadro.

De las seis que quedan, **Oracle y Azion** son las que más cambian el cuadro:

- **Oracle** tiene precio único global, sin variación por región. Las diez filas fijas cobran distinto según la región — es el único contraste de ese tipo. Y sus datos ya están casi todos verificados por ti.
- **Azion** es la única con jurisdicción latinoamericana, y **conecta 3.1 con 4.3** porque TERABYTE es una portuaria chilena.

Las otras salen por X1: Scaleway se pisa con Azion en el eje de jurisdicción, Render se pisa con la fila 10 en el eje de escalado, Bunny se solapa parcialmente con Fastly.

**El riesgo:** Azion no tiene fuente. Si no alcanzas a levantarla hoy, **Bunny es el reemplazo con datos ya verificados** por el navegador.

## Y algo para Rodolfo

Su trabajo está bien — el consolidado le cambió una cifra. En Azure Flex Consumption su borrador dice `$0.40/millón + $0.000026/GB-s` y el consolidado dice `$0.000018/vCPU-s`. **La suya es la que vale**, o él confirma.

## Persona — prompt 78 — 20-09-2026 21:08

```text
ahi daniel me mando el esqueleto en el que se baso rodolfo para sus tablas, estan en esqueleto-3.2a-3.2b.md revisa ese documento
```

### Claude Code — 20-09-2026 21:08

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:08

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:09

Es **byte a byte el mismo archivo** que copié de la rama de Daniel a las 18:56. No trae información nueva.

Pero lo que me dices sí cambia algo importante.

## Si Rodolfo se basó en ese esqueleto, mi recomendación anterior está mal

Yo te propuse mantener las columnas de Rodolfo —las 9 de su borrador— como base del cuerpo. Eso tenía sentido si él seguía en su estructura vieja.

Pero si ya adoptó el esqueleto, entonces **el equipo completo está en la estructura de Daniel**: tres tablas, 14 campos. Y de hecho sus filas en el consolidado están en formato 3.2a/3.2b con los 14 campos, no en sus 9 originales.

Eso resuelve dos de las seis decisiones pendientes: **la estructura ya está acordada y es la C.** No hay que elegir.

Una nota de cronología, por si acaso: el borrador de Rodolfo es del 19-09 a las 17:16 y el esqueleto de Daniel está fechado 20-09. Así que el borrador es anterior. Si Rodolfo rehízo sus tablas contra el esqueleto, perfecto. Si alguien reformateó sus datos viejos, hay que confirmarlo con él — y ahí la discrepancia de Azure cobra otro sentido.

## Entonces el problema real es uno solo: no cabe

Hice la cuenta.

En página apaisada, carta, el ancho útil son unos **22,9 cm**. La tabla 3.2a tiene 9 columnas de contenido, o sea **2,5 cm cada una**.

Una celda como esta, que es real:

> *"SÍ obligatorio (S3, DynamoDB). Límite de rediseño: timeout máx. 15 min (900 s) y payload síncrono 6 MB"*

Son 95 caracteres. A 2,5 cm de ancho en letra chica caben unos 16 por línea: **seis líneas de alto**. Con doce filas, la tabla mide unos **29 cm de alto**.

**El alto disponible en apaisado son 16 cm.** La 3.2a sola ocupa casi el doble de una página, y todavía faltan la 3.2b y la 3.2c.

## La salida

No es cambiar la estructura: es **escribir dos versiones de cada celda**.

| | Cuerpo | Anexo |
|---|---|---|
| Tiempo máx. | `900 s` | `900 s (15 min) por ejecución` + URL + fecha |
| Estado / límite | `S3 o DynamoDB · 900 s` | La frase completa con el motivo del rediseño |
| Precio | `\$0.20/M + \$0.0000167/GB-s` | Con región, tramo, capa gratuita, tipo y fecha |

El dato pelado en el cuerpo, la frase completa en el anexo. Eso baja las celdas a una o dos líneas y la tabla entra.

Es exactamente lo que el esqueleto de Daniel ya previó: *"Lo que no cabe aquí va a la tabla ampliada del anexo con URL y fecha por celda."* Solo que nadie ha hecho esa pasada de condensación.

Y queda pendiente algo que nadie ha tocado: **`main.tex` sigue con la tabla de 7 columnas**. Alguien tiene que reemplazarla por las tres nuevas, y eso es de Rodolfo como consolidador.

¿Quieres que arme la versión condensada de tus filas, para tener un ejemplo concreto de cuánto se achica?

## Persona — prompt 79 — 20-09-2026 21:11

```text
que esto fue lo que me dijo daniel: "el rodo dejó 9, la idea es q se queden unas 5 por ahi
y nosotros complementamos pa las 11
porque la +1 de las 11 tieneq ser una de estrategia tradicional
12 totales"
entonces por ultimo despues achicamos las tablas en latex
```

### Claude Code — 20-09-2026 21:11

Hice la cuenta y cuadra:

| | Filas |
|---|---|
| Rodolfo, recortado de 9 a 5 | Lambda · Fargate · Lambda@Edge+CloudFront (fila conjunta) · Azure Functions · Container Apps |
| Tuyas | Cloud Run functions · Cloud Run · Cloudflare Workers · Fastly Compute · **+2 alternativas** |
| La tradicional | Contenedor sobre EC2 reservada |
| **Total** | **12** |

Los 9 de Rodolfo bajan a 5 solos: **Aurora y DynamoDB salen por ser bases de datos** —decisión 5 de Daniel—, Lambda@Edge y CloudFront se fusionan en una fila, y App Runner sale porque está cerrado a nuevos clientes. 9 − 2 − 1 − 1 = 5.

## Y acá está la buena noticia

**Tus cuatro filas fijas ya están levantadas.** El navegador trajo Cloud Run functions, Cloud Run, Cloudflare Workers y Fastly Compute con los 19 campos y sus URLs. Más las tres del anexo y las cinco de código abierto.

**Te faltan solo las dos alternativas.** Eso es todo.

## Qué cuesta cada opción

| Alternativa | Qué tienes | Qué falta |
|---|---|---|
| **Oracle** | Timeout sync y detached, memoria, precio por tramos, capa gratuita, mitigación al 25 %, payload 6 MB, precio global sin región | Concurrencia (la de «60 GB» de 2020 no sirve), aislamiento, egreso, estado externo |
| **Azion** | Nada con fuente | Los 14 campos completos |
| **Bunny** | CPU 30 s, 128 MB, 50 subsolicitudes, precio de CPU y solicitudes, ancho de banda aparte, script 10 MB | Aislamiento, estado externo, egreso con precio, concurrencia |

**Oracle está a cuatro campos.** Azion está a catorce. Bunny a cuatro también, y con la ventaja de que el navegador ya verificó lo suyo.

Si el tiempo aprieta, Oracle y Bunny son las dos que menos trabajo cuestan y las dos están en la lista de Daniel. Si Azion vale el esfuerzo por el ángulo latinoamericano —que para 4.3 es real—, hay que levantarla entera.

## Sobre achicar en LaTeX al final

De acuerdo con dejarlo para el final. Un aviso para que no sorprenda: la 3.2a mide unos 29 cm de alto contra 16 disponibles, así que hay que recortar cerca del 45 %. Bajar de `\small` a `\tiny` da quizás un 30 %. **Va a hacer falta acortar texto además de achicar letra**, así que conviene que quien haga esa pasada sepa que no alcanza solo con el tamaño de fuente.

Nada que resolver ahora. ¿Avanzamos con las dos alternativas?

## Persona — prompt 80 — 20-09-2026 21:13

```text
entonces usemos oracle y bunny, no hay problema, vayamos completando las tablas y lo necesario a lo que corresponde a mi, claudio
```

### Claude Code — 20-09-2026 21:13

Decidido entonces. Voy a consolidar lo que ya está verificado y dejar marcado exactamente qué falta.

### Claude Code — 20-09-2026 21:14

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:15

[Desarrollo 3.2/MIS-FILAS-3.2.md](Desarrollo%203.2/MIS-FILAS-3.2.md)

Consolidé todo lo tuyo en las tres tablas. Cada dato lleva marca de procedencia: `[NAV]` verificado por el navegador con URL, `[YO]` levantado por ti el 19, `[DANIEL]` sin confirmar, `[FALTA]` sin levantar.

## Estás mucho más cerca de lo que parecía

**Cuatro de tus seis filas del cuerpo están completas**, con fuente y fecha: Cloud Run functions, Cloud Run, Cloudflare Workers y Fastly Compute. La tabla 3.2c está entera, con las acreditaciones CNCF fechadas. Y las tres del anexo también.

**Te faltan nueve campos, todos en las dos alternativas:**

| Fila | Falta |
|---|---|
| **Oracle** | Aislamiento · Qué opera el equipo · Estado externo · Egreso |
| **Bunny** | Aislamiento · Piso mensual · Capa gratuita y región · Qué opera el equipo · Estado externo · Egreso |

En Bunny el egreso es el que más importa: el ancho de banda CDN es un producto aparte, y ese es justo su aporte a la comparación.

## Tres cosas que corregí al consolidar

**Saqué el `< 5 ms` de Cloudflare.** El navegador describió el mecanismo sin número y dejó dicho por qué: lo citó como descripción, no como evidencia de rendimiento.

**Dejé marcado que la concurrencia de Oracle no se puede tomar** de la nota de 2020 — son 60 GB de memoria, no 60 instancias.

**En Bunny, el arranque de 500 ms lo dejé fuera de la columna de mitigación**, porque esa columna es de mecanismo y eso es una cifra.

## Y una decisión que aparece

Daniel eligió **Fission y Fn Project** como las dos alternativas de código abierto, pero la tabla 3.2c del esqueleto tiene una sola fila para alternativa. ¿Entran las dos o solo una? Conviene preguntárselo, porque cambia el tamaño de esa tabla.

---

Nueve campos son unas cuatro o cinco visitas: la documentación de arquitectura de Oracle, su página de service limits, y las dos de Bunny que ya tienes ubicadas. ¿Preparo el encargo corto para el navegador con solo eso?

## Persona — prompt 81 — 20-09-2026 21:17

```text
dejemos solo una a modo de desicion propia para lo que este campo, y si prepara el encargo para el navegador
```

### Claude Code — 20-09-2026 21:18

Fission es la que conviene dejar, y hay un motivo concreto.

Las columnas de la 3.2c son aislamiento, **escala a cero**, timeout y concurrencia por defecto, qué opera el equipo y acreditación. El aporte de Fission cae justo en la segunda: es la única donde la respuesta no es sí ni no, sino *"depende del ejecutor, y se elige por función"*. En esa columna destaca sola.

Y Fn quedaría redundante: **Oracle ya está en la fila 11 de 3.2a**, así que el contraste motor abierto contra nube gestionada ya es visible sin darle una fila propia. El propio Daniel lo describe como *"un solo contraste de portabilidad, contado en dos listas"*.

Además Fission tiene siete versiones entre mayo y junio de 2026; Fn solo mantenimiento.

Ahora el encargo.

### Claude Code — 20-09-2026 21:18

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:18

[Desarrollo 3.2/Encargo-navegador-cierre.md](Desarrollo%203.2/Encargo-navegador-cierre.md)

Es corto: **tres plataformas, catorce campos**. Mucho más acotado que el anterior.

## Cómo quedó repartido

**Oracle** — cuatro campos: aislamiento, qué opera el equipo, estado externo y egreso. Más una pregunta extra sobre concurrencia, explicando por qué no sirve la nota de 2020: son 60 GB de memoria, no instancias, y tiene seis años.

**Bunny** — seis campos, y marqué el egreso como **el más importante de esa plataforma**. Que el ancho de banda CDN se cobre aparte del cómputo es justo lo que justifica su inclusión, así que conviene que ese dato quede sólido. También le pedí confirmar las cifras que vienen de la planilla de Daniel sin verificar.

**Fission** — cuatro campos, con la acreditación CNCF primero. Y en la escala a cero pedí precisión: cuál es el ejecutor por defecto cuando se crea una función sin especificar. Eso es lo que hace que la celda diga algo comparable en vez de "depende".

## Lo que mantuve del formato que funcionó

Las seis reglas al principio, la columna leído/inferido, las citas textuales y las tres listas finales. Agregué una regla nueva que no estaba: **las notas de versión no son documentación de referencia**, porque ese error ya nos costó tiempo con Oracle.

Y cerré diciendo qué no necesita: nada de arranque en frío, ninguna plataforma nueva, y ninguno de los campos que ya tienes salvo los de Bunny que pedí confirmar.

Cuando vuelva, esas nueve celdas cierran tus seis filas del cuerpo, y con la 3.2c y el anexo ya listos tendrías tu parte completa.

## Persona — prompt 82 — 20-09-2026 21:26

```text
dentro de la carpeta desarrollo 3.2 deje el .md de cierre que me pediste encargar
```

### Claude Code — 20-09-2026 21:26

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:26

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:26

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:26

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:27

Muy buen trabajo otra vez. Voy a integrarlo, y hay **una corrección importante a algo que yo tenía mal**.

### Claude Code — 20-09-2026 21:27

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:27

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:28

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:28

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:28

[Desarrollo 3.2/MIS-FILAS-3.2.md](Desarrollo%203.2/MIS-FILAS-3.2.md) — **tu parte quedó completa.** Seis filas del cuerpo, la 3.2c con Fission incluida, y el anexo.

## Una corrección a algo que yo tenía mal

Yo había anotado que Oracle tiene **"precio único global, sin variación por región"**. Eso vale **solo para el cómputo**. El navegador encontró que **el egreso sí se segmenta en tres grupos de región de origen**. Si esa celda dijera "global", estaría mal.

## Y la nota de 2020 era peor de lo que pensábamos

No solo estaba vieja: **cambió el ámbito**. Decía 60 GB por dominio de disponibilidad; la página vigente dice 60 GB **por región** (180 GB con tres dominios). Haberla descartado fue lo correcto.

Y hay un hallazgo ahí: **Oracle no publica un número de ejecuciones simultáneas.** Su límite está expresado en memoria, no en instancias. Es la única de las doce filas con esa unidad.

## Tres hallazgos que valen

**Bunny corre sobre Deno.** Su runtime es un isolate de V8 construido con Deno en Rust. Y Deno Deploy está en tu anexo — hay una conexión ahí si Rodolfo la quiere usar.

**El mismo patrón en Oracle y Bunny:** el cómputo tiene precio global, el tráfico es regional. Dos proveedores distintos con la misma estructura.

**Y uno que sirve directo a 4.3:** el ancho de banda de Bunny en **Sudamérica cuesta \$0,045/GB, cuatro veces y media más que Europa o Norteamérica**. Para una portuaria chilena, la región donde se sirve el tráfico cambia la factura de forma sustantiva.

## Fission: no es proyecto CNCF

Confirmado por ausencia en los listados de cncf.io y porque su propio README no lo reclama. Apache 2.0, patrocinado por InfraCloud y Srcmesh, nacido en Platform9.

El navegador hizo una distinción fina que conviene conservar: **estar en el Landscape y ser proyecto CNCF son cosas distintas**, y la ficha del Landscape no la pudo verificar porque es una aplicación JavaScript. No afirma ni una cosa ni la otra.

## Quedan tres huecos, y los tres se declaran

La tarifa de egreso de Oracle sobre los 10 TB —la celda se carga por script y llegó vacía—, el valor por defecto de `--concurrency` en Fission donde dos páginas dicen 5 y 500, y el aislamiento de Deno, Vercel y Netlify, que ninguna documenta.

Ninguno se rellena. Se declaran, que es lo que corresponde.

## Persona — prompt 83 — 20-09-2026 21:30

```text
entonces empieza a rellenar en latex, al igual que daniel, el informe de investigacion, para yo poder hacerle commit a nuestra parte
```

### Claude Code — 20-09-2026 21:30

Antes de escribir: **el `main.tex` de tu carpeta de trabajo es el viejo**, el de `main`. El de Daniel, con 3.1 escrito y el `.bib` ampliado, está solo en su rama.

Si edito el de tu carpeta, escribes sobre una versión que no tiene el trabajo de Daniel. Así que te dejo los bloques listos para pegar, y tú los pones una vez que estés en la rama correcta.

### Claude Code — 20-09-2026 21:31

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:31

[Desarrollo 3.2/LATEX-para-main.md](Desarrollo%203.2/LATEX-para-main.md)

Están las tres tablas completas con tus seis filas llenas y las de Rodolfo vacías, marcadas con comentario para que él las complete.

## Por qué no lo escribí directo en `main.tex`

El archivo de tu carpeta de trabajo es el de `main`: **no tiene el 3.1 de Daniel ni su `.bib` ampliado**. Si lo edito ahí, después chocas con su trabajo al mezclar. Los bloques van sobre la versión de su rama.

## Decisiones de formato que tomé

**Tres tablas, las dos grandes en apaisado.** Calculé los anchos para que sumen 22,8 cm sobre los 22,9 disponibles: 3.2a con nueve columnas y 3.2b con seis.

**La 3.2c cabe en vertical**, porque le saqué una columna: *"qué opera el equipo"* dice lo mismo en las seis filas —todo salvo lo que provea el clúster—, así que va en la nota al pie en vez de repetirse seis veces.

**Condensé las celdas** para el cuerpo. La versión larga con matices y URLs queda en `MIS-FILAS-3.2.md` para el anexo, que es lo que el esqueleto de Daniel ya preveía.

**Todo en `\scriptsize`** y con los `$` escapados.

## Las cuatro notas al pie

Cubren lo que el punto 5 exige declarar: la fecha y las regiones de referencia, que la lista de responsabilidades es construcción del grupo y no un estándar, por qué la columna de arranque en frío dice "sin medición propia", y **los tres datos que no se publicaron** — la tarifa de egreso de Oracle, los paquetes por cotización de Fastly y la contradicción de Fission.

Esa última nota es la que convierte los huecos en método declarado en vez de trabajo incompleto.

## Dos cosas para avisar al grupo

El cuadro ahora son **dos etiquetas**, `cuadro-criterios` y `cuadro-limites`. Quien lo cite desde 2.3, 4.2 o 4.3 tiene que usar las dos.

Y hay que **borrar la tabla vieja de 7 columnas** antes de pegar estas, o quedan duplicadas.

## Persona — prompt 84 — 20-09-2026 21:33

```text
pero yo estoy trabajando en la rama 3.2-cloud-fastly-demo asi que no deberia haber problema
```

### Claude Code — 20-09-2026 21:33

Déjame verificar, porque puede haber un problema real.

### Claude Code — 20-09-2026 21:33

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:33

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:33

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:33

Tienes razón, verifiqué y **el bloque de la tabla 3.2 es idéntico en las dos ramas.** Las diferencias de Daniel están en 3.1 y en el Anexo D, que son regiones distintas del archivo. Git mezcla eso sin conflicto.

Así que sí: puedes trabajar en tu rama sin problema. Retiro la advertencia.

Pero encontré dos cosas concretas que sí hay que resolver.

### Claude Code — 20-09-2026 21:33

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:34

Verificado. Puedes trabajar en tu rama.

## Pero hay dos referencias que se rompen

**`tab:cuadro-comparativo` se usa en dos lugares que no son tuyos.** Mis bloques renombran esa etiqueta a `cuadro-criterios` y `cuadro-limites`, y eso deja colgadas:

- **Línea 346 de Daniel**, en el párrafo de 3.1: *"pasan como filas a la Tabla~\ref{tab:cuadro-comparativo}"*
- **Línea 480**, en la tabla de declaración de IA

Cuando se mezclen las ramas, las dos saldrían como `??` en el PDF.

**La solución más simple:** que la tabla 3.2a conserve la etiqueta `cuadro-comparativo` en vez de `cuadro-criterios`. Así las referencias existentes siguen funcionando y solo hay que agregar la segunda etiqueta para 3.2b.

Voy a cambiarlo.

### Claude Code — 20-09-2026 21:34

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:34

Listo. [Desarrollo 3.2/LATEX-para-main.md](Desarrollo%203.2/LATEX-para-main.md) está listo para pegar en tu rama.

## Lo que verifiqué

**El bloque de la tabla 3.2 es idéntico en tu rama y en la de Daniel.** Sus cambios están en 3.1 y en el Anexo D, que son regiones distintas del archivo. Git las mezcla sin conflicto, así que tenías razón.

Y de las tres etiquetas que uso, `sec:poc` y `sec:costos` ya existen en tu rama.

## El arreglo que hice

Encontré que `tab:cuadro-comparativo` se usa en dos lugares que no son tuyos: el párrafo de 3.1 de Daniel y la tabla de declaración de IA. Si renombraba esa etiqueta, las dos salían como `??` en el PDF.

Así que la tabla 3.2a **conserva la etiqueta `cuadro-comparativo`**. Las referencias existentes siguen funcionando y solo se agrega `cuadro-limites` para la 3.2b.

## Lo que queda por hacer al pegar

**Borrar la tabla vieja de 7 columnas** antes de insertar las tres nuevas, o quedan duplicadas y la etiqueta se repite.

Y avisar al grupo que ahora son dos etiquetas: quien cite el cuadro desde 2.3, 4.2 o 4.3 tiene que usar `cuadro-comparativo` para los criterios y `cuadro-limites` para los límites.

## Una cosa que aparecerá al compilar

La nota (c) referencia `\ref{anexo:busqueda}`... en realidad no, esa la usa Daniel. Pero sí conviene que compiles **dos veces** para que resuelvan las referencias cruzadas, y que revises si la 3.2a entra de alto. Si se pasa, el primer recurso es bajar de `\scriptsize` a `\tiny`; el segundo, acortar las celdas de precio, que son las más largas.

## Persona — prompt 85 — 20-09-2026 21:35

```text
yap entonces traspasa los datos al informe de investigacion para hacerle commit yo despues
```

### Claude Code — 20-09-2026 21:35

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:35

*Herramientas ejecutadas: Bash*

### Claude Code — 20-09-2026 21:36

*Herramientas ejecutadas: Write*

### Claude Code — 20-09-2026 21:36

You've hit your session limit · resets 1:40am (America/Santiago)

