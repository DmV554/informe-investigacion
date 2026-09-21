# Anexo A — Parte B: prompts utilizados (2.2 Arranque en frío)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Isidora Cisternas.
**Secciones cubiertas:** 2.2 Arranque en frío: causas, medición y mitigaciones. La sección 2.5 (WebAssembly y WASI) no fue trabajada con IA en esta sesión: la IA leyó los apuntes de 2.5 que estaban en el mismo documento, pero no produjo texto ni análisis para ella.
**Nivel declarado por sección:**
- 2.2, párrafos de causas, medición y mitigaciones: **nivel 3**. La autora redactó los borradores a partir de sus propios apuntes y lecturas. La IA dio retroalimentación, sugirió y verificó fuentes, detectó citas que no respaldaban lo afirmado, propuso la idea que organiza el párrafo de mitigaciones (cada familia actúa sobre una parte distinta del proceso: evitar, saltarse o abaratar el arranque, con su costo) y redactó un párrafo de mitigaciones reordenado a partir de las frases de la autora. Finalmente, la IA redujo la sección completa de unas 640 a 350 palabras sin agregar ideas.
- Cifras, citas y referencias de 2.2: nivel 2 en la búsqueda (la IA localizó en fuentes oficiales y papers algunos datos, entre ellos el 94 % de Gackstatter et al., la reducción de 10 veces de Cloudflare 2025 y el costo de caché de SnapStart en Python y .NET, y confirmó datos que la autora ya tenía en sus apuntes, como los 380 s de SeBS y el 60 % de AWS). Ninguna cifra ni referencia proviene del modelo: todas se tomaron de la fuente, y la autora las abrió y verificó en el original. [CONFIRMAR]
**Herramientas:** Claude (Anthropic), chat web claude.ai dentro de un proyecto, modelo Claude Opus 5 (`claude-opus-5`) [CONFIRMAR modelo indicado por la interfaz]. Durante la conversación la IA usó búsqueda web, lectura de páginas web y ejecución de código (solo para contar palabras).
**Período:** 19-09-2026 a 21-09-2026 [CONFIRMAR fechas].

**Ampliación por la sesión 2 (sección 2.5).** La sesión 2 es posterior a la sesión 1 y en ella sí se trabajó la sección 2.5 con IA. La frase de «Secciones cubiertas» sobre 2.5 describe solo la sesión 1. Nivel declarado para 2.5:
- 2.5, párrafos de concepto (Wasm y WASI) y de comparación (contenedores, rendimiento y portabilidad en el borde): **nivel 3**. La autora redactó el borrador inicial a partir de sus propios apuntes y fuentes. La IA revisó ese borrador contra la ficha y la guía del equipo. Señaló errores factuales y de referencias: la autoría de WASI, la fecha y versión de la especificación del W3C citada, el verbo «certifica» aplicado a Wasmtime, la descripción de los contenedores como un sistema operativo completo y una cifra de arranque atribuida a una revisión sistemática. También sugirió contenido que faltaba: la evidencia contraria de Jangda et al. (2019), la distinción entre portabilidad del runtime y portabilidad de la aplicación, el contraste entre Fastly Compute y Cloudflare Workers y el ecosistema Spin y wasmCloud. Después, la IA redujo la sección de unas 720 a unas 340 palabras: reescribió y fusionó estos dos párrafos a partir de la versión de la autora, sin agregar ideas nuevas. 
- 2.5, párrafo de cierre (cuándo conviene y cuándo no): corresponde a la discusión crítica de la evidencia (punto 6.1), por lo que solo admite nivel 0 o 1. La autora redactó el párrafo. Al reducir la extensión, la IA solo eliminó cifras repetidas y trasladó a ese párrafo una frase de la autora (la superioridad en throughput de los contenedores siempre encendidos), sin redactar texto nuevo. 
- Cifras, citas y referencias de 2.5: **nivel 2** en la búsqueda. Mediante búsqueda web, la IA localizó y verificó en fuentes oficiales y papers los siguientes datos: la fecha de publicación de WASI 0.3.0 (11-06-2026) y su implementación en Wasmtime 46; el estado de la especificación core (Wasm 2.0 como Candidate Recommendation Draft del 16-06-2025 y release 3.0 del 11-09-2026); las cifras de Jangda et al. (ralentización media de 1,45× a 1,55×, con picos de 2,08× y 2,5×); el estado de wasmCloud en la CNCF; y el sitio oficial de Spin (`spinframework.dev`). Indicó además que `fermyon.dev` no pudo confirmarse como sitio oficial. Las referencias de Faasm, Fastly y Cloudflare las agregó la autora. Ninguna cifra ni referencia proviene del modelo: todas se tomaron de la fuente, y la autora las abrió y verificó en el original.

Los prompts se transcriben literalmente, tal como fueron escritos (incluidos errores de tipeo), en orden cronológico. Los archivos que la autora adjuntó o tenía cargados en el proyecto se indican entre corchetes.

---

## Sesión 1 — Claude (chat web, claude.ai), 19-09 a 21-09-2026

**Enlace:** (https://claude.ai/share/f462e3cd-7dad-4570-b408-93ceccf9802f).
**Secciones a las que sirvió:** 2.2 y este registro del Anexo A.

1. [Archivos del proyecto: `instrucciones_inv.md`, `TERABYTE-TI05-Guia-del-equipo.md`, `Apuntes secciones informe.md` (borrador de 2.2 y apuntes), `Referencias Investigación - Fuentes.csv`, y los dos papers en .md: Golec et al., *Cold Start Latency in Serverless Computing*; Ustiugov et al., *Benchmarking, analysis, and optimization of serverless function snapshots*]
Hola, necesito que revises los documentos de tu contexto. Encontraras las intrucciones de un trabajo que estoy realizando con mi equipo "Terabyte" en el archivo "instrucciones_inv.md" encontrarás las instrucciones de mi profesor y en "TERABYTE-TI05-Guia-del-equipo_md.md" encontrarás como nos estamos distribuyendo como equipo. Yo soy Isidora, por lo que me tocó la sección 2.2 y 2.5. Actualmente comencé a realizar la 2.2 y en el archivo "Apuntes secciones informe.md" podrás encontrar una  versión consolidada de redacción que realicé, y más abajo encontraras los apuntes sueltos como tal que hice en base a dos papers que tambien tienes en tu contexto. También encontrarás todas las referencias actuales que tenemos como equipo en "Referencias Investigación-Fuentes.csv". Revisa todo eso y necesito que me des retroalimentación sobre cómo podria mejorar mis parrafos considerando lo que me pidió mi profesor y mi equipo y las limitaciones que tengo.

2. Ok, tengo algunas consultas de los puntos que me dijiste: 

1. Si bien en las instrucciones de mis compañeros pusieron que en cada seccion de los 2.X debe ir "concepto, comparación entre modelos y cuándo conviene" le doy más prioridad a lo que puso mi mismo profesor que pide para mi sección de arranque en frio " causas, medición y mitigaciones (concurrencia aprovisionada, instantáneas, entornos livianos)." ya que es lo que pide textual. Quizas igual haría tu sugerencia de esqueleto pero para que lo tengas en cuenta. Aparte, cómo haré mitigaciones comparadas por modelo con su costo con solo 140 palabras? Y en la tabla comparativa del 3.2 creo que ahi van los costos como tal.  


Con lo demás si estoy igual de acuerdo. Solo que con tantos papers no se por donde sacar la información y qué otras fuentes agregar ya que es materia que yo nunca habia visto. Revisé esas dos fuentes que te adjunté pero no se cuál más revisar.
Podrías crearme algún plan para poder mejorar mi sección 2.1 con las cosas que le faltan? Podrias decirme qué papers/documentos revisar que estan en mi .csv y qué otras me faltan.
También podrias quizás modificar un poco mi parrafo de redacción actual dejando lo que creas que si sirve y dejando espacios donde debería rellenar cosas indicando qué. 
Tenemos hasta el lunes a las 18hrs para entregar esto pero quiero dejar la 2.1 cerrada hoy antes de las 4pm

*(Nota: en este prompt "2.1" se refiere a la sección 2.2; la IA lo interpretó así y lo indicó en su respuesta.)*

3. [Adjunto: `Apuntes secciones informe.md` actualizado, con apuntes de las referencias leídas y nueva versión del borrador de 2.2]
Mira tu contexto, te adjunté la nueva versión de mi borrador para la sección 2.2, al principio del documento, están todos mis apuntes de las referencias que leí. Al final aparece el borrador como tal. Por favor revisalo y ayudame con sugerencias sobre cómo estructurarlo mejor. Siento que ciertas cosas como esta parte "Ustiugov et al. midieron que esto desplaza el retraso a la ejecución, que tarda en promedio un 95 % más que en caliente por los fallos de página, y que precargar las páginas que la función usa siempre reduce el arranque 3,7 veces [ustiugov2021snapshots]." están de más o quizas las cambiaría un poco. En sí necesito ayuda sobre todo en la parte de la mitigación siento que no logré conectar bien las ideas como tal.
Recuerda revisar las instrucciones de mi profesor y la división de mis compañeros. No cambies mi tipo de redacción.

4. [Adjunto: `Apuntes secciones informe.md` actualizado]
Ya mira, ya corregí los detalles que me dijiste al igual que las referencias que me equivoqué. Por mientras las dejé algunas en .bib ya que así lo debo meter en mi informe. No te fijes en el formato de las citas por ahora. Revisa nuevamente mi borrador y dime si está bien o le cambiarias algo mas. Si sé que es extenso pero quiero dejarlo bien hecho y luego resumirlo. Revisa en el contexto y verás la actualización de mi documento

5. [Adjunto: `Apuntes secciones informe.md` actualizado]
Ya actualicé de nuevo el borrador, con las mejoras que me dijiste, tenias razon en algunas que me fijaba más en costo o frecuencias que en latencia como tal y corregí algunas citas. confirmame si está bien

6. [Adjunto: `Apuntes secciones informe.md` actualizado]
Ya. Ahi ya termine de corregir todo. Ahora necesito que me ayudes a reducir mi sección a las 300–350 c/u que me piden mis compañeros. No cambies ideas ni agregues nuevas cosas. Solo limitate a resumir las ideas para que cumplan con lo solicitado. Manten el formato y listado de las citas.

7. De los niveles de IA que categoriza mi profesor, en que nivel encasillarias la ayuda que me diste?

8. [Adjuntos: `README.md` de `anexo-ia/`; `B-prompts.md` y `C-evidencia.md` de Daniel Miranda como modelo de formato]
Metete a mi carpeta de informe-investigacion>anexo-ia y revisa el readme. Necesito que generes los dos .md del registro de ia en base a lo que me ayudaste. Necesito que esos dos .md me los pases por acá. No lo agregues a la carpeta

*(La IA no tenía acceso a la carpeta local; trabajó con las copias del `README.md` y de los archivos de Daniel Miranda cargadas en el proyecto. Este prompt produjo este archivo y `C-evidencia.md`: nivel 2, apoyo de formato del Anexo A.)*

---

## Sesión 2 — Claude (chat web, claude.ai, en proyecto), 20-09 a 21-09-2026 [CONFIRMAR fechas]

**Herramienta:** Claude (Anthropic), chat web claude.ai dentro de un proyecto, modelo Claude Opus 5 (`claude-opus-5`). 
Durante la conversación la IA usó búsqueda web y lectura de páginas web.
**Enlace:**(https://claude.ai/share/e5d8ed7b-e5fc-414d-9d3d-319346092fbb)
**Secciones a las que sirvió:** 2.5 y este registro del Anexo A.

9. [Archivos del proyecto: `instrucciones_inv.md`, `TERABYTE-TI05-Guia-del-equipo (1).md`, `Apuntes secciones informe (1).md` (apuntes de 2.5), `README.md` de `anexo-ia/`, y `B-prompts.md` y `C-evidencia.md` de Daniel Miranda]
Hola, necesito que leas los documentos de tu contexto en donde encontrarás las instrucciones de mi investigación "intrucciones_inv.md" redactadas por mi profesor y la division de trabajo de mi equipo "terabyte" en donde me toca redactar la sección 2.2 y 2.5. Actualmente estoy viendo la 2.5 ya que la 2.2 ya está lista. Analiza las intrucciones y lo que se me pide. En el documento "Apuntes secciones informe (1).md" aparecen los apuntes que hice en base a las referencias que utilicé. Revisa mi sección y sugiereme mejoras o si crees que así está bien:
[Pegado: borrador de la autora de la sección 2.5, tres párrafos, con 6 referencias]

10. Ya mira, realicé las correcciones que me sugeriste y también agregué nuevas citas para cubrir lo que me faltaba. Agregué lo que conviene y no conviene al final del texto también. Podrias ayudarme a reducir las palabras si? Que creo que me pasé del limite:
[Pegado: segunda versión de la autora de la sección 2.5, cuatro párrafos (unas 720 palabras), con 13 referencias]

11. al final cambié las referencias para wasmCloud y Fermyon Spin a las paginas oficiales, serían estas o no?:
 WASMCloud https://wasmcloud.com/
fermyon https://www.fermyon.dev/

12. De los niveles de IA que categoriza mi profesor, en que nivel encasillarias la ayuda que me diste?

13. [Adjuntos: `B-prompts.md` y `C-evidencia.md` de la autora, generados en la sesión 1]
Metete a mi carpeta de informe-investigacion>anexo-ia y revisa el readme. Necesito que actualices estos .md (agrega lo que falta de este chat, no cambies lo que ya está) del registro de ia en base a lo que me ayudaste. Necesito que esos dos .md me los pases por acá. No lo agregues a la carpeta

*(La IA no tenía acceso a la carpeta local; trabajó con la copia del `README.md` cargada en el proyecto y con los dos archivos adjuntos. Este prompt produjo la ampliación de este archivo y de `C-evidencia.md` sin modificar el texto existente: nivel 2, apoyo de formato del Anexo A.)*
