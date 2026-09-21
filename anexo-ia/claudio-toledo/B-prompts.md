# Anexo A — Parte B: prompts utilizados (3.1, 3.2 y bibliografía)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Claudio Patricio Toledo Mac-lean.
**Secciones cubiertas:** 3.1 Alternativas adicionales (búsqueda y verificación de candidatos, aporte al Anexo D); 3.2 Cuadro comparativo, mitad Google / Cloudflare / Fastly / Deno-Vercel-Netlify / código abierto y consolidación de la mitad de AWS y Azure; bibliografía (revisión de las fuentes a su cargo); organización del trabajo propio.
**Nivel declarado por sección:**

- **3.1 Alternativas adicionales: nivel 2.** La IA ordenó el esquema de la sección, armó los listados de candidatos a revisar y estructuró los criterios de descarte; la verificación de cada candidato en la documentación oficial y la decisión de cuáles entraban son propias. La selección final de las diez alternativas y la redacción del texto publicado en el informe son de Daniel Miranda, que declara su propia fila.
- **3.2 Cuadro comparativo — llenado de las filas a mi cargo: nivel 2.** La IA (Claude Code y Cowork) buscó y transcribió a las tablas de trabajo los límites, precios y condiciones publicados en la documentación oficial de cada plataforma, siempre con la URL y la fecha de consulta a la vista; la revisión celda por celda contra esa fuente y la decisión sobre qué plataformas entran son propias. Ninguna cifra se tomó de lo que el modelo supiera: todas provienen de la página oficial citada en `registros/cowork/salidas/`.
- **3.2 Cuadro comparativo — dos párrafos de análisis: nivel 0.** Texto de autoría humana. Se deja constancia de que esos párrafos no aparecen en ninguna de las transcripciones de las sesiones de esta carpeta.
- **3.2 — volcado a LaTeX y verificación de compilación: nivel 1.** Apoyo de formato y diagramación: paso de las tablas de markdown a los entornos `longtable` de la plantilla y revisión de que el documento compilara. No cambió el contenido de las celdas ni el texto.
- **Bibliografía (las fuentes a mi cargo): nivel 2.** La IA resumió y tradujo al español los *abstracts*, dio el formato de fila de la planilla del grupo y apoyó la comparación de fortalezas y debilidades entre artículos. Los DOI y las entradas BibTeX se obtuvieron de Crossref y de los propios PDF, no del modelo; la selección de qué artículo entra en qué sección es propia.

- **Organización del trabajo (plan personal, consultas a compañeros, registro de decisiones): nivel 2.** No es contenido del informe y se declara igual, porque el esquema de trabajo que produjo influyó en cómo se organizó 3.1 y 3.2.
- **Este Anexo A (mi declaración): nivel 2.** La IA revisó las transcripciones, exportó los registros y redactó el borrador de esta declaración; los niveles declarados y la firma son decisión propia.

**Herramientas:**
- Claude Code 2.1.271, 2.1.275 y 2.1.278 (Anthropic), modelo `claude-opus-5`.
- Claude (Anthropic), aplicación de escritorio / Cowork, usada como agente de navegador para levantar datos de la documentación oficial. *(Modelo y versión: pendientes de confirmar por el integrante.)*

**Período:** 18-09-2026 a 20-09-2026.

Los prompts se transcriben literalmente, en orden cronológico, agrupados por sesión. Los de las sesiones de Claude Code se exportaron del registro interno de cada sesión con `anexo-ia/_herramientas/exportar_conversacion.py`, sin editarlos ni resumirlos: se conservan tal como fueron escritos, con sus erratas. Algunos prompts incluyen una línea `<ide_opened_file>` o `<ide_selection>` que no escribió la persona: la agrega el editor para indicar qué archivo estaba abierto; se deja porque forma parte de lo que recibió el modelo. La sesión de Cowork (sesión 3) no conserva el texto literal del chat; en su lugar se entregan los encargos que se le pegaron completos, que son los prompts efectivamente empleados.

---

## Sesión 1 — Claude Code 2.1.271, 18-09-2026 02:46 a 19-09-2026 14:58

**Exportación:** `registros/claude-code-sesion-d4406eea-prompts.md` (prompts) y `registros/claude-code-sesion-d4406eea-conversacion.md` (conversación completa).
**Identificador de sesión:** `d4406eea-e25d-4bef-a2fe-4e0b7442cca2`. **Modelo:** `claude-opus-5`.
**Secciones a las que sirvió:** bibliografía (revisión de los artículos a mi cargo, DOI y BibTeX, traducción de *abstracts*); apoyo a la selección de fuentes de 3.1 y 3.2.
**Nivel:** 2.

### Prompt 1 — 18-09-2026 02:46

```text
okey quiero que analices los archivos, Soy claudio y tengo que empezar con el trabajo de investigacion, no se bien por donde comenzar, se que tengo que recabar articulos, pero no se muy como buscarlos, se que puedo buscarlos manualmente en web of cience, pero no se bien si me sirven ono para lo que es mi seccion
```

### Prompt 2 — 18-09-2026 03:10

```text
voy a estar revisando antes, estos articulos e ir revisando si aportan o no a cada seccion, ve dandome el formato de cada fila para cada paper que vayamos analizando
```

### Prompt 3 — 18-09-2026 03:22

```text
okey ahora, quiero que en base a los articulos que tenemos como pdf, vayamos 1 por 1 analizandolo, quiero que en un .md me dejes anotado el doi, y el .bib de cada articulo, quiero analizarlos por numero, asi que vayamaos de manera ascendente partiendo del 47
```

### Prompt 4 — 18-09-2026 04:08

```text
ahora analiza a detalle cada paper, de la misma manera que el 47, guarda detalle y ten sumo cuidado con cada uno, y guarda en un .md lo que debo colocar en el excel
```

### Prompt 5 — 18-09-2026 04:17

```text
me interesa que lo hagas como ese formato tal cual, a eso me referia, eso quiero mantenerlo para todos los articulos que revisemos
```

### Prompt 6 — 18-09-2026 04:19

```text
ahora al momento de colocar lo que es la seccion, quiero que me justifiques porque es esa seccion y no otra
```

### Prompt 7 — 18-09-2026 14:29

```text
okey ahora agregue del 42 al 39, quiero que los revises y ademas, de las secciones, ahora pueden ser varias secciones, asi como se ve en la imagen, ayudame y llendo a detalle paper por paper, sin dejar detalles por alto, tambien quiero que me traduzcas el abstract de cada paper para poder comprender a lo que se trata
```

### Prompt 8 — 18-09-2026 15:36

```text
quiero que en un .md, hagamos un analisis a detalle de cada paper, tomando en cuenta los pros y contras de cada uno
```

### Prompt 9 — 18-09-2026 15:42

```text
teniendo en cuenta este analisis, ahora hubo cambios en las secciones a las que aporta cada articulo que hemos analizado?
```

### Prompt 10 — 18-09-2026 15:49

```text
de igual manera como analizaste el 38 si no tengo acceso a el? tu puedes tener acceso a ese artiuculo? o estabas inventando?
```

### Prompt 11 — 18-09-2026 15:54

```text
creo que ahi lo restaure, es ese? puedes revisar si lo es? si lo es analizalo para ver que seciones cubre este articulo
```

### Prompt 12 — 18-09-2026 17:13

```text
tengo una duda en el plan de trabajo que tenemos lo desmas integrantes y demsa, hay una cantidad mas o menos a revisar por cada integrante?
```

### Prompt 13 — 19-09-2026 14:54

```text
dentro de los papers consegui el 13, que tan util es para mi seccion?
```

---

## Sesión 2 — Claude Code 2.1.278, 19-09-2026 12:28 a 20-09-2026 21:36

**Exportación:** `registros/claude-code-sesion-cf21efe1-prompts.md` (prompts) y `registros/claude-code-sesion-cf21efe1-conversacion.md` (conversación completa).
**Identificador de sesión:** `cf21efe1-8c94-4839-9cd4-c78d63bcdf68`. **Modelo:** `claude-opus-5`.
**Secciones a las que sirvió:** 3.1 Alternativas adicionales (esquema, listados de candidatos, criterios de descarte); 3.2 Cuadro comparativo (estructura de las tablas 3.2a/3.2b/3.2c, llenado de las filas a mi cargo, consolidación de la mitad de AWS y Azure, volcado a LaTeX); organización del trabajo y consultas a Valentina, Rodolfo y Daniel.
**Nivel:** 2 en 3.1 y en el llenado de 3.2; 1 en el volcado a LaTeX.

> **Nota sobre el prompt 69.** Dice «no hagas commit ni nada similar, para no dejar registro de ia». Se transcribe tal cual, como todos los demás. El criterio en ese momento era hacer los commits a mano y no dejar coautoría automática en el mensaje; esta declaración registra el uso que aquella decisión no dejó anotado en el historial. El punto 6.4 de las indicaciones es explícito en que declarar correctamente no baja la nota.

### Prompt 1 — 19-09-2026 12:28

```text
quiero que analices todas las carpetas, soy claudio quiero que me ayudes a realizar mi parte, no hagas cambios, para el plan de trabajo que debo realizar en base a lo demas escrito, dejemos antotado todo en un .md, tambien deja anotado los prompt en un .md a parte, si quieras creemos una carpeta, llamada sesion actual 19-09
```

### Prompt 2 — 19-09-2026 12:48

```text
de igual manera esos no son todos los artiuculos, esos papers, son parte de una revision simplemente, de unos 47 papers aproximantamente, entonces la idea es usar los mas relevantes para lo que es nuestra seccion, quiero que hagamos un supuesto de como deberia ir la estructura de lo que es nuestra parte, que nos falta y que es lo que ya tenemos
```

### Prompt 3 — 19-09-2026 12:53

```text
algo que quiero recalcar, y que lo tengas claro, quiero que trabajes sin modismos al momento de escribirme o redactar cosas, ya que me estas escribiendo con modismos argentinos, para que me escribas neutro de ahora en adelante
```

### Prompt 4 — 19-09-2026 13:07

```text
me puedes explicar paso a paso, lo que debe contener mi seccion? y que es lo que necesito para realizarla
```

### Prompt 5 — 19-09-2026 13:58

```text
dentro de los chats anteriores, deje la lista de excel de los 47 que estabamos revisando, aun no los terminamos de revisar todos, pero de manera preliminar, esos son los que tenemos, cuales de estos son los mas relevantes para mi parte? asi los puedo analizar y buscar para poder complementer nuestra seccion de buena manera
```

### Prompt 6 — 19-09-2026 14:07

```text
esta esta la tabla de rodolfo, ya me la paso: [ Servicio | Categoría | Tiempo Máx. Ejecución | Rango de Memoria / vCPU | Límite Payload (In/Out) | Concurrencia / Escalado | Latencia / Cold Start | Modelo de Cobro y Precio Fechado (Sept 2026, us-east-1) | Complejidad Operacional (Infraestructura / Red) ], y con respecto a los papers los voy a revisar
```

### Prompt 7 — 19-09-2026 15:17

```text
hice el analisis y los artiuclos 10,11 y 13, el 10 y 11 no los pude pillar ya que me piden atorizacion para descargarlos y debo pedirlos, pero para el 13, parece ser no muy relevante para lo que es nuestra seccion
```

### Prompt 8 — 19-09-2026 15:20

```text
si no es verdad el 13 no nos sirve tanto, ahora quiero que me digas si la tabla de rodolfo esta bien o es pecario en algunas secciones
```

### Prompt 9 — 19-09-2026 15:24

```text
si armame un breve .md con lo que encontraste, que sea claro y conciso
```

### Prompt 10 — 19-09-2026 15:27

```text
de igual manera no se bien que es lo que hace rodolfo, me podrias explicar brevemente?
```

### Prompt 11 — 19-09-2026 15:32

```text
comprendo, entonces nos faltan los criterios de valentina, tanto a mi como a rodolfo?, podemos armar mi tabla y lo que debo hacer, con supuestos? ya que de valentina aun no sabemos nada, asi que no se si se pueda avanzar con supuestos a modo de tamplate, para que cuando sea el momento de usar los datos reales, sea mas facil avanzar desde una base, crees que eso este bien? de serlo dejame anotado en un .md lo que seria, y como seria este supuesto
```

### Prompt 12 — 19-09-2026 15:35

```text
pero ya que valentina aun no progresa en su parte nosotros no podemos progresar?, no comprendo bien la parte de valentina
```

### Prompt 13 — 19-09-2026 15:38

```text
entonces, de valentina solo tiene que rellenar los 3 criterios, yo debo hacer la tabla y rodolfo interpretar la tabla?
```

### Prompt 14 — 19-09-2026 15:39

```text
entonces puedo comenzar ya lo que es mi seccion?
```

### Prompt 15 — 19-09-2026 15:40

```text
cuales son mis 10 columnas?
```

### Prompt 16 — 19-09-2026 15:49

```text
igual recordar evitar el sesgo de los papers y no basarnos 100% en los unicos que tenemos ya que son 47 y mas, ya que Daniel estuvo allando mas papers que pueden sernos utiles, solo que aun no comprendo que es lo que se va hacer en mi parte y secciones de valentina y rodolfo, ya que se que hacemos las partes 3.1 y 3.2 pero aun me confunde cual es el trabajo a realizar
```

### Prompt 17 — 19-09-2026 16:50

```text
dentro de chats anteriores, deje un .txt, que me mando valentina, pormientras podemos trabajar con eso?
```

### Prompt 18 — 19-09-2026 16:55

```text
entonces con estos cambios en relacion a como estaba antes, que cambia y que se mantiene?
```

### Prompt 19 — 19-09-2026 16:58

```text
armame un .md con las consultas para cada uno, tanto como para valentina como para rodolfo a ver que es lo que me dicen
```

### Prompt 20 — 19-09-2026 17:03

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Sesion-actual-19-09\Consultas-pendientes.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

te dije que me hicieras un .md para valentina y otro para rodolfo
```

### Prompt 21 — 19-09-2026 17:18

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Sesion-actual-19-09\Consulta-Rodolfo.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey, aun asi teniendo en cuenta eso, rodolfo me mando sus tablas, mas o menos como es que las fue rellenando, las tengo en unos pdfs, llamados borradores_tabla_3.2 y apuntes secciones informe, aqui esta lo que ha hecho rodolfo dime que tal va, analiza de manera exaustiva y detallada, para no dejarnos nada por alto
```

### Prompt 22 — 19-09-2026 17:26

```text
puedes darme un .md con los allazgos para mandarselos a rodolfo? ademas de propuestas en base a las consultas que le mandamos anteriormente, sobre lo que podriamos realizar nosotros sin problema, y sobre las consultas a valentina, nos dijo que nosotros tomaramos ciertas decisiones que nos salgan a conveniencia, ya que ella ahora no tiene mucho tiempo para poder responderlas, que fueramos anotando los cambios que fuimos decidiendo, y las desiciones que fuimos tomando en base a lo primero que nos mando Valentin
```

### Prompt 23 — 19-09-2026 19:38

```text
deje algunos cammbios que hizo rodolfo a su parte en unos pdfs llamados apuntes secciones, el no comprende bien porque hacer tanto incapie en  AWS AppRunner, analiza eso
```

### Prompt 24 — 19-09-2026 19:40

```text
entonces, que necesito yo, para poder hacer mi parte tanto de valentina como de rodolfo?
```

### Prompt 25 — 19-09-2026 19:44

```text
okey entonces, crea una carpeta, donde iremos desarrollando lo que es nuestra parte, llamemosla "desarrollo", vayamos punto por punto a corde a lo que debemos abarcar, vayamos paso a paso con lo que nos piden, todo dentro demomento dentro de dos .md, desarrollo 3.1 y desarrollo 3.2
```

### Prompt 26 — 19-09-2026 19:57

```text
daniel me mando lo siguiente
```

### Prompt 27 — 19-09-2026 20:00

```text
ahora que ya tenemos el paso a paso, desarrollalo y yo ire supervisando todo
```

### Prompt 28 — 19-09-2026 20:03

```text
yap, hazlo, pero como busco esos datos para ingresarlos en las tablas?
```

### Prompt 29 — 19-09-2026 20:06

```text
te puedo mandar los links de las paginas para que indreses los datos en la tabla?
```

### Prompt 30 — 19-09-2026 20:11

```text
los que dicen origen Guia a que se refiere?
```

### Prompt 31 — 19-09-2026 20:14

```text
del .md 3.1 con existe se refiere a si existe?, a que se refiere si publica limites? a que se refiere si entra?
```

### Prompt 32 — 19-09-2026 20:14

```text
y en establas tablas son de si y de no?
```

### Prompt 33 — 19-09-2026 20:19

```text
que quiere decir limites y precio; limites, precio por cotizacion; limites, precio no publicado y nada verificable? te puedo mandar un ejemplo de la pagina de oracle? ahi adjunte imagenes, no se si eso responda lo que es la tabla?
```

### Prompt 34 — 19-09-2026 20:21

```text
eso es lo que aparece ya en toda la pagina
```

### Prompt 35 — 19-09-2026 20:22

```text
me llevo a eso
```

### Prompt 36 — 19-09-2026 20:24

```text
me aparece eso
```

### Prompt 37 — 19-09-2026 20:32

```text
entonces vayamos rellenando el .md con esos datos
```

### Prompt 38 — 19-09-2026 20:42

```text
desde claude web rellene algunas tablas dentro del .md Desarrollo3.1D.md para que lo revises y me digas si esta bien o no
```

### Prompt 39 — 19-09-2026 20:47

```text
hagamos eso en orden y con respecto a render si, utilicemosla, y veamos bien los descartes, analicemos todos esos detalles para decidir que hacer
```

### Prompt 40 — 19-09-2026 20:54

```text
cambie el desarrollo-3.1, ahora ese tiene algunos de los cambios que realize revisalo y dime que tal esta
```

### Prompt 41 — 19-09-2026 20:58

```text
pero eso eso no lo habia hecho valentina?, recuerda que mi parte es de claudio, tengo que hacer solo las alternativas adicionales
```

### Prompt 42 — 19-09-2026 21:00

```text
entonces continuemos con el paso 2
```

### Prompt 43 — 19-09-2026 21:06

```text
bueno entonces comencemos con el paso 2, a esocger las 10, escoge las que mejor tengan pinta, y luego las vas justificado segun las fuimos seleccionando
```

### Prompt 44 — 19-09-2026 21:10

```text
a ver entonces seleecionemos:
FaaS, Oracle y Alibaba
Contenedores: Fly.io, Render
Borde: Akamai y Supabase
Codigo Abierto: Fission y Nuclio
Datos: Turso y Upstash
```

### Prompt 45 — 19-09-2026 21:14

```text
cambiemoslo por Railway, y usemos scaleway en vez de alibaba
```

### Prompt 46 — 19-09-2026 21:19

```text
entonces podemos hacer la tabla final de 3.1?
```

### Prompt 47 — 19-09-2026 21:20

```text
como puedo hacer estas busquedas rapido? donde puedo hallar esas respuestas?
```

### Prompt 48 — 19-09-2026 21:22

```text
puedes darme eso para buscarlo en un .md?
```

### Prompt 49 — 19-09-2026 21:26

```text
Daniel esta anotando en un documento de google, de la siguiente manera quiero anotarlos ahi tambien lo que he estado pillando de que manera lo puedo hacer, que sea facil y legible, para que lo puedan entender todos?
```

### Prompt 50 — 19-09-2026 21:31

```text
igual la idea de seleccion de estos 10 es que aporten algo q los de la lista del profe no tengan la GUIA
```

### Prompt 51 — 19-09-2026 21:40

```text
creo que ahi esta echa la busqueda, para que actualices nuestros datos, corrobora que este bien
```

### Prompt 52 — 19-09-2026 22:09

```text
<ide_selection>The user selected the lines 275 to 275 from c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Para-pegar-en-el-doc.md:
https://mongodb.com/docs/atlas/flex-migration/

This may or may not be related to the current task.</ide_selection>

el daniel me dijo lo siguiente:Esto está bien, debemos poner anotaciones asi en los q pusiste solo métricas, para elegir bien. Ej railway y los dos de computo en el borde tienen casi puira métrica, asi tener notaciones con lenguaje mas humano y no tan tecnicas, ademas de las tecnicas
```

### Prompt 53 — 19-09-2026 22:22

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Para-pegar-en-el-doc.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

pero algo falta en scaleway falta la pagina de precios no?, o este documento de para-pegar-en-el-doc esta desactualizado?
```

### Prompt 54 — 19-09-2026 22:52

```text
falta algo como lo que coloca daniel, asi como, que tan usados son, que tanta confianza generan, etc
```

### Prompt 55 — 20-09-2026 00:10

```text
dentro de la carpeta chats anteriores, hay un excel llamado candidatas C, Daniel dejo lo que recopilo, cuales de ahi no tenemos y podriamos agregar, para al momento de decidir tener mas opciones, dejame anotado en un .md el listado de las nuevas, para pasarselo a claude del navegador y lo busque bien a detalle
```

### Prompt 56 — 20-09-2026 00:21

```text
a ver entonces hagamos los arreglos correspondientes que era 6, y agamos el listado para que complemente nuestro agente de navegador y adjunte links y demas para que pueda revisar las paginas web de manera directa
```

### Prompt 57 — 20-09-2026 00:54

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo\Encargo-navegador.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey mira esto fue lo que me dio, revisa el desarrollo 3.1 (1) y colocalos en el documento para pegar en el doc
```

### Prompt 58 — 20-09-2026 00:59

```text
que paso con el bunny edge scripting?
```

### Prompt 59 — 20-09-2026 01:06

```text
porque azure front door rules engine se descarta?
```

### Prompt 60 — 20-09-2026 01:07

```text
ahora como hago para la 7, render, ya que dice evaluada, pero no hay especificaciones ni links
```

### Prompt 61 — 20-09-2026 01:13

```text
pero por ejemplo render no tiene caracteristicas como los demas?
```

### Prompt 62 — 20-09-2026 01:14

```text
cockroach DB no estan en copiar y pegar, porque no estan?
```

### Prompt 63 — 20-09-2026 15:48

```text
hay una carpeta llamada papers, aqui deje algunos papaers que pueden ser utiles para una secciones que me destaco daniel, que esta dentro de la carpeta desarrollo, daniel hara la seleccion de lo que es la 3.1, yo vere directamente lo que es 3.2, asi que hagamos un plan en base a lo que tenemos y el plan de daniel, tambien rodolfo fue avanzando su parte dejo los avances de lo que el hizo ahi tambien, en estos apuntes, los dos pdfs, estan tanto las secciones en general como lo que va de 3.1 y lo que iria en 3.2 mas lo de rodolfo, vayamos armando un plan para ir evaluando que tal vamos para desarrollar 3.2
```

### Prompt 64 — 20-09-2026 16:45

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

### Prompt 65 — 20-09-2026 17:14

```text
mis diez no son ya, daniel va escoger otros 10, asi que eso queda pendiente a su decision, con respecto a lo que es 3.2, podemos empezar a generar la tabla? almenos lo que es nuestra parte de la tabla?
```

### Prompt 66 — 20-09-2026 17:21

```text
pero no que eran 14 campos? en total?
```

### Prompt 67 — 20-09-2026 17:34

```text
entonces podemos ir conformado la tabla? 3.2b? ya que la 3.2a creo que es la de rodolfo, es asi eso?
```

### Prompt 68 — 20-09-2026 17:36

```text
entonces, espera, tenemos todo lo que necesitamos para comenzar con 3.2a y b pero que nos corresponden a nosotros (Claudio)
```

### Prompt 69 — 20-09-2026 18:55

```text
okey quiero que veas las branch del proyecto de informe-investigacion, daniel hizo su parte ya y esta subida en su rama, de ahi en adeltane cuando terminemos nuestra parte, lo dejaremos listo ahi, para luego yo poder hacer commit, dejemos anotado todo dentro de un .md en una carpeta llamada desarrollo 3.2, no hagas commit ni nada similar, para no dejar registro de ia
```

### Prompt 70 — 20-09-2026 19:01

```text
sisi, mi rama esta vacia, ya que quiero hacer commit cuando tengamos listas lo que son nuestras tablas, teniendo eso encuenta, podemos empezar a desarrollar dentro del .md que te dije? luego le pasare un .md con todo el contexto a claude de navegador para que pueda ingresar los datos a las tablas, ya que tu no puedes verdad?
```

### Prompt 71 — 20-09-2026 19:05

```text
entonces rellenalas tu dentro del .md y yo ire revisando manualmente cada una, dejame los links de donde sacaste la info, para yo poder corroborarla, dejame una guia para que el claude de navegador, haga bien las busquedas que necesita, piele tambien dentro del .md que genere un .md que te sirva para rellenar y lo que necesitamos,
```

### Prompt 72 — 20-09-2026 19:09

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo 3.2\Guia-busqueda-y-salida.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

entonces le paso guia-busqueda y encargo-navegador?
```

### Prompt 73 — 20-09-2026 19:42

```text
okey deje dentro de una carpeta los datos recopilados por el navegador, dentro de la carpeta Desarrollo 3.2, para que los veas
```

### Prompt 74 — 20-09-2026 19:43

```text
[Request interrupted by user]
```

### Prompt 75 — 20-09-2026 20:43

```text
<ide_opened_file>The user opened the file c:\Users\La Gema\Desktop\Visual Proyectos\Investigacion\Desarrollo 3.2\Tablas-3.2-Definitivas.md in the IDE. This may or may not be related to the current task.</ide_opened_file>

okey, analiza los documentos de la carpeta datosnavegadorRecolados, y ve los archivos de desarrollo 3.2 ya que hubo cambios y se agregaron otros archivos
```

### Prompt 76 — 20-09-2026 20:49

```text
esas dos plataformas las vamos a elegir nosotros, esas 2, no se que te parece ya que tenemos que elgir dos, y esas son las mas prometedoras, con respecto al formato que debemos respetar de las tablas y el como tiene construidas las tablas rodolfo, que cambios habria que hacer?
```

### Prompt 77 — 20-09-2026 20:55

```text
azion esta dentro del listado de Daniel? y los cambios de obicacion y esos dos qeu van en 11 y 12 tenemos que decidirlos nosotros, hagamos la selecion con cuidado y detalle, igual recuerda que para la seccion 3.2 tanto rodolfo y yo usamos otras columnas comparado a daniel, asi que esas columnas las de rodolfo deberiamos manternerlas no? vayamos con cuidado con todo esto ya que de lo que se, la parte de rodolfo esta bien, de igual manera revisa el repositorio en caso de para comvalidar estos datos, y recuerda el formato en el que nos estamos rigiendo
```

### Prompt 78 — 20-09-2026 21:08

```text
ahi daniel me mando el esqueleto en el que se baso rodolfo para sus tablas, estan en esqueleto-3.2a-3.2b.md revisa ese documento
```

### Prompt 79 — 20-09-2026 21:11

```text
que esto fue lo que me dijo daniel: "el rodo dejó 9, la idea es q se queden unas 5 por ahi
y nosotros complementamos pa las 11
porque la +1 de las 11 tieneq ser una de estrategia tradicional
12 totales"
entonces por ultimo despues achicamos las tablas en latex
```

### Prompt 80 — 20-09-2026 21:13

```text
entonces usemos oracle y bunny, no hay problema, vayamos completando las tablas y lo necesario a lo que corresponde a mi, claudio
```

### Prompt 81 — 20-09-2026 21:17

```text
dejemos solo una a modo de desicion propia para lo que este campo, y si prepara el encargo para el navegador
```

### Prompt 82 — 20-09-2026 21:26

```text
dentro de la carpeta desarrollo 3.2 deje el .md de cierre que me pediste encargar
```

### Prompt 83 — 20-09-2026 21:30

```text
entonces empieza a rellenar en latex, al igual que daniel, el informe de investigacion, para yo poder hacerle commit a nuestra parte
```

### Prompt 84 — 20-09-2026 21:33

```text
pero yo estoy trabajando en la rama 3.2-cloud-fastly-demo asi que no deberia haber problema
```

### Prompt 85 — 20-09-2026 21:35

```text
yap entonces traspasa los datos al informe de investigacion para hacerle commit yo despues
```

---

## Sesión 3 — Claude (Cowork / aplicación de escritorio) como agente de navegador, 20-09-2026

**Exportación:** el chat no conserva un registro literal exportable. Lo que se entrega son los **encargos que se le pegaron completos**, que son los prompts efectivamente empleados, y las salidas que devolvió. Están en `registros/cowork/`.
**Secciones a las que sirvió:** 3.1 (verificación de candidatos en documentación oficial) y 3.2 (levantamiento de límites, precios y condiciones de las plataformas a mi cargo).
**Nivel:** 2.

Los encargos se escribieron en Claude Code (sesión 2) y se pegaron en la otra herramienta. Cada uno es autocontenido y todos imponen la misma regla: solo documentación oficial del proveedor, con URL y fecha de consulta, y sin análisis ni recomendaciones.

| # | Prompt (documento pegado completo) | Fecha | Archivo |
|---|---|---|---|
| 1 | Listado de plataformas candidatas nuevas a buscar, con lo que hay que verificar de cada una | 20-09-2026 00:11 | `registros/cowork/Para-buscar-en-navegador.md` |
| 2 | Encargo de verificación de candidatas de 3.1: qué comprobar, qué fuentes se aceptan y en qué formato devolverlo | 20-09-2026 00:22 | `registros/cowork/Encargo-navegador.md` |
| 3 | Encargo de las tablas 3.2: qué campos levantar para Google, Cloudflare, Fastly, Deno/Vercel/Netlify y código abierto, con las reglas de fuente, moneda, región y fecha | 20-09-2026 19:02 | `registros/cowork/Encargo-navegador-3.2.md` |
| 4 | Guía de búsqueda y formato de salida que acompaña al encargo anterior | 20-09-2026 19:06 | `registros/cowork/Guia-busqueda-y-salida.md` |
| 5 | Encargo de cierre: campos que quedaron incompletos tras la primera vuelta | 20-09-2026 21:18 | `registros/cowork/Encargo-navegador-cierre.md` |

**Salidas que devolvió**, en `registros/cowork/salidas/`: `3.2-respaldo.md`, `tabla-3.2.csv` y `tabla-3.2-open-source.csv` (datos por plataforma con su URL y fecha de consulta), y `registro-desarrollo-rodolfo-3.2.md` (registro de la validación cruzada entre el borrador v3 de Rodolfo Fernández y las tablas, del 20-09-2026 23:09). Cada celda de las tablas del informe se revisó después contra la URL que acompaña al dato.

