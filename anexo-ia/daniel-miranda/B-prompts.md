# Anexo A — Parte B: prompts utilizados (3.1, Anexo D, plantilla y organización)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Daniel Ignacio Miranda Vázquez.
**Secciones cubiertas:** 3.1 Alternativas adicionales; Anexo D (búsqueda documentada de alternativas); plantilla LaTeX (`informe/main.tex`, `referencias.bib`, `.latexmkrc`, `.gitignore`) y organización del repositorio (`trabajo/`); estándar del Anexo A (`anexo-ia/`). Aporte parcial a 3.2 (estructura de tablas y planilla de trabajo, no contenido).
**Nivel declarado por sección:**
- 3.1 Alternativas adicionales: **nivel 2** en la búsqueda inicial y verificación de fuentes (agente de investigación externo guiado con prompts escritos con apoyo de Claude; toda cifra y URL se reabrió en la fuente oficial), en la estructura de la sección y en la revisión de forma; **nivel 1** en la redacción final (borrador propio; corrección de ortografía y estilo con IA). La decisión de qué alternativas entran, los criterios D.1 y las frases de "qué aporta" son de autoría humana: se discutieron con la IA, que señaló inconsistencias, pero cada decisión la tomó el autor (constan en los prompts 40 a 52).
- Anexo D: **nivel 2**. Los criterios (D.1) los redactó el autor; la IA los revisó y transcribió al TeX. Las tablas D.2 a D.6 las llenó la IA a partir de las decisiones y motivos cortos del autor y de los hechos verificados en documentación oficial, sin agregar hechos nuevos; el autor revisó cada fila.
- Plantilla LaTeX, `.bib`, organización del repositorio y estándar de `anexo-ia/`: **nivel 2** (apoyo de formato y diagramación, admitido por el punto 6.1).
- 3.2: **nivel 2** solo en la propuesta de estructura de tablas y en la planilla de recolección; ninguna celda de contenido fue producida por IA en esta sesión.
**Herramientas:** Claude (Anthropic), modo Cowork, modelo `claude-fable-5-1`, sesión única; agente de investigación externo (Grok, xAI), operado por el autor con los prompts de `trabajo/fuentes/guia-agentes-busqueda-fuentes.md` y `trabajo/3.1-alternativas/prompt-verificacion-candidatos.md`, más prompts propios del autor (ver sección "Sesiones con el agente externo").
**Período:** 19-09-2026 a 21-09-2026.

Los prompts se transcriben literalmente, tal como fueron escritos (incluidos errores de tipeo), en orden cronológico. Los archivos que el autor adjuntó se indican entre corchetes.

---

## Sesión 1 — Claude (Cowork), 19-09 a 21-09-2026

**Enlace:** https://claude.ai/code/session_01GKFjHaKv49e4JnUS1XjGv4 (registro literal completo, accesible con la cuenta del usuario; exportación en `registros/` cuando llegue la exportación de datos de la cuenta).
**Secciones a las que sirvió:** 3.1, Anexo D, plantilla LaTeX, organización del repositorio, estructura de 3.2, estándar del Anexo A.

1. Hola, este es un Trabajo de un ramo universitario de administración de proyectos informáticos. Debemos investigar sobre "Serverless y Edge computing" siguiendo unas pautas. Creé un repo con el objetivo de ello, informe-investigación dentro puedes encontrar "indicaciones" con las indicaciones oficiales del profe para el trabajo en md "informe" plantilla overleaf q creamos para empezar a rellenar Y TERABYTE_TI-05_guia-del-equipo .md q es una organización del equipo q creamos para empezar. Yo soy daniel miranda claramente y la empresa/grupo es "TERABYTE" nuestro tema es TI-05 serverless y edge computing. Lee y analiza todo y me cuentas, tenemos fuentes q estamos leyendo y analizando en un drive aparte q aun no tienes acceso, pero para empezar lee lo q tienes a mano
2. /home/daniel/PERSONAL/U_TEMPORAL/fep/investigacion/informe-investigacion
3. No te preocupes por el tiempo, tenemos todo en control, no emitas comentarios o cambies el plan por ello, no sacrificaremos rigurosidad por "poco tiempo". Ya subí la guia de equipo no-truncada y las pautas del curso del trabajo, para q revises. Los detalles menores del repo de la plantilla tex, arreglalos
4. Antes, necesito una breve introducción al tema, antes de leernos las fuentes y papers, necesito comprender a fondo lo q estamos investigando, comentame. Tengo nociones, por supuesto y he utilizado esta tecnologia, pero para estar en sintonia necesito información y definiciones concretas
5. si, hicimos una busqueda preliminar y se está consolidando en un excel. Llevamos 47 fuentes, no leidas todas. Dime que tal de fuentes, si necesitaremos más (probablemente si mientras avanzamos) y si como base está fuerte o no. También necesito empezar a ir viendo lo q me corresponde a mi en la organización, pero no tengo claro q empezar a leer para comenzar a redactar a mano. lo guardé en el repo en "archivos temporal" para q no tengas q buscar en el drive. De todas formas, el drive es "Investigacion_FEP" y es compartido conmigo por si sirve para el futuro
6. Me parece perfecto lo de la estructura del anexo D,armalo, pero en un rama nueva de git, creala q sea representativa y trabajemos ahi. Duda: Entonces 3.1 debe ser prosa explicando o citando al anexo no? analizando
7. Y algo más, pondré a trabajar a un agent a buscar más fuentes, lasq dijiste q tenemos q tener, necesito que me armes la guia para él, para q encuentre todo lo q necesitamos. Tendrá acceso al repo y al drive, asi q tendrá todo el contexto del trabajo. tambien puedo crear o dividir el trabajo en mutiples agents (usaré grok bot, de xAI, investiga si quieres saber lo q es). Q pueda decir igual q fuente corresponda a cada sección ayudaria bastante
8. Lo hizo mi agent, subió al drive "fuentes-candidatas-agentes" revisa a ver q tal.
9. está todo, seguramente hay algun error de permisos, descargaré lo q hizo el agent. Ahi está: /informe-investigacion/archivosTemporal/fuentes_agent/fuentes-candidatas-agentes
10. [Log de compilación de latexmk] No puedo buildear el tex desde vscode
11. como borro los artefactivs viejos
12. [Adjunto: Apuntes secciones informe.md] Esto es lo q llevan mis compas, es un archivo de notas q vamos llenando. Dame ahora mis pautas de que leer, que verificar y como empezar lo mio. Intentando usar lo q llevan ellos de 3.1,3.2
13. ok, pero me pierdo tanta cosa, empieza en simple, como si no supiera nada, que hay q hacer en el trabajo, q tengo q hacer yo en la práctica y como se relaciona con lo de rodolfo, necesitamos algo de algun otro integrante? parte de 0
14. ok, vamos ordenado: 3.1 Miraré el C del otro agent para elegir candidatos por lista, luego q estilo de redacción tieneq ir? tabla o que?
15. ah, ya vi la tabla, pero deberiamos poner solo los candidatos nuevos? no deberiamos comparar con loq el profe ya puso? Se compara todo no?
16. Se permiten pre prints en este trabajo?
17. criterios de inclusion 3.1 para q puedo usar? estoy anotando todo lo q me parece relevante de cada candidato en una primera pasada, luego como elijo? ej ibm lo veo como menos especifico y más condensado todo en su servicio de code cloud, eso seria un indicador q tomaria para no elegirlo
18. si son minimo 6, por q elegimos 14 en la tabla comparativa 3.2?
19. bien, ahora esperamos q otro integrante defina bien los criterios de comparación, luego de ello dijimos q tendremos unas 12 plataformas, cubriendo todo lo q nos piden de modelos (no son 5? dijiste 4) , cuando tengamos los criterios definiremos las columnas finales, cuantas columnas podria ser? el numero. Bien en general?
20. Lo de los 3 criterios tiene sentido? ahora definieron esto: [documento de criterios de comparación 3.2 elaborado por otra integrante] Segun yo esos 3 son de alcance, la complejidad operacional no tiene medición por una razón, no se si es adoc definir algo nosotros
21. entonces, dame el md con la solución para comunicarle a rodolfo para empezar a hacer la 3.2, y debemos tener certeza sobre medir la complejidad operacional
22. lo q me preocupa es q dices con mucha seguridad q encontraremos lo de operacionalidad en las fuentes
23. terminamos 3.1 [pegado de las notas de recolección manual de candidatos por lista] Ayudame con ello
24. dame un prompt para mi otro a gent investigador para q verifique esas dudas
25. en la 3.2 hay q meter lo de los metodos tradicionales cmo parte de las 12 no?
26. como quedaria entonces, no serian 12? dame un esqueleto de la tabla en la practica
27. 3.2 a y 3.2b , considerando todo, lo de rodolfo y lo mio
28. no entiendo q va en anexo y q no, por que lo nuestro si?
29. terminamos 3.1, consolidamos con una redaccion del otro agent: [pegado de "Decisión propuesta — 2 otros por lista"] Faltaria a lo mejor justificar más cada cosa, tu q crees? o la prosa del 3.1 q sea mas general? para no extendernos plataforma a plataforma
30. Lo de las dudas está aca, se me olvido dartelo: [pegado de "Verificación de candidatos 3.1"]
31. Cyual es la parte de nosotros
32. Me armó una guia para poder elegir bien, q piensas?: [pegado de "Guía de elección — Alternativas adicionales"] y si, me añadió mas a la pool pq yo se lo pedí, tienen sus citas respectivas guardadas en un excel. Olvida la reunión con claudio, lo estoy viendo yo solo. Dime que debo leer, como debo elegir, como debo descartar y como empiezo a redactar en el TeX para tener lo final.
33. ah es q aun no decido los criterios d.1 , por eso era la guia, pero supongo q es lo primordial a definir. Con d.1 en mano, la verificación candidatos y la guia elección ya tengo todo no? solo tengo q leer los elementos diferenciadores, las cifras y corroborar alguna q otra cosa en la fuente oficial y listo. lo unico q me faltaria serian esos criterios, son 3 de exclusión y 3 de descarte.
34. Inclusión 2, sobre pertenencia a la lista Q lista?
35. No entiendo bien la dimensión 1 de inclusion
36. terminé de redactarlos ! Dime q te parece o si ajustamos algo: [criterios I1–I3, X1–X3 redactados por el autor]
37. Crees q sea mejor dejar dos criterios de descarte y x1 como una regla abajo?
38. ahi le pedi a otro agent q me ayudara a redactar estas correciones: [tabla D.1 reescrita] Hay cosas q sobran segun yo como lo de etiquetar cada dato en I1
39. Dale, arregla esos detalles y dame el preview de la tabla antes de q redactemos el latex
40. También tenemos q definir "lista" en algun lado o "ficha" pues es de las indicaciones y a no ser q las citemos como fuente es ambiguo para el lector
41. muy bien. Definimos la tabla y fue por mi asi que ahora pasala al main tex, escribela en en el d.1 y luego yo procederé a aplicarlos para elegir los candidatos, luego me ayudarás a llenarlos también
42. [Captura de la tabla D.2] seguimos con estas tablas o la columna de criterio y resultado sobran?
43. /home/daniel/PERSONAL/U_TEMPORAL/fep/investigacion/informe-investigacion/trabajo/3.1-alternativas/citas-pool-otros.bib y csv deberia estar lo q falta. Actualiza el tex, y hacemos commit y push a la rama 3.1
44. [Error de git index.lock]
45. fui eligiendo y dando motivo corto, luego con el otro agent lo estructuramos en una tabla y dio un resumen él final con "par propuesto": [tabla de decisiones por lista] q te parece? Los motivos están ahi, lo q podrias ayudarme es ampliar/precisar en la redacción ahora en el tex
46. Agregamoos lo del paso 5, perfecto. Ampliamos i3 con sexta dimension. Lo de DigitalOcean explicamelo bien antes de tomar una decision
47. podriamos quitar lo de la función central en el x2. Lo de proveedor distinto de aws,google,microsoft creo q sobra, casi todos son distintos. Lo del desampate está bien, pero analiza como cambiará los seleccionados estas decisiones y dime si crees q es lo mejor
48. Sobre la dimensión 3: Acepto tu recomendación, es robusta. Como cambia eso entonces ahora lo de koyeb?
49. ok, comprendo. Actualiza solo los criterios entonces en el TeX, luego contrastaré nuevamente con otra pasada ayudandome de mi agent y te paso nuevamente el md de los D.x rellenos
50. [Adjunto: propuesta-seleccion-anexo-D-2026-09-20.md] A esto llegamos, que tal? Koyeb sigue dentro
51. Dde acuerdo conrtigo, koyeb fuera. Terminemos ese Anexo. Gracias
52. perfecto, dame los comandos para hacer commit y push, antes de redactar el 3.1
53. [Adjunto: borrador-seccion-3.1.md] ahi escribi borrador con redaccion final del otro agent, q me ayudó a mejorar ortografia y demas. revisa q tal, sabes q le gusta añadir cosas innecesarias, asi q revisalo y cuentame q takl
54. [Adjunto: borrador-seccion-3.1-v2.md] AHi si
55. quedó bien robusta la seccin entojnces? la 3.1
56. Bien, esos detalles quedan para el futuro, dame comandos pra hacer el commit
57. Ahora tengo una compañera consolidando todas las branch de todas las secciones. Tenemos duda sobre el anexo de IA, es por persona? Pensaba crear carpeta de prompts , como lo podriamos hacer para q quede todo trazable y adoc con las exigencias del profe?
58. Esperaremos a los merge, luego dictaminamos el estandar para q todos pongan lo relativo a la ia con readme y demás, luego subimos en otro commit y esperamos q los demás suban sus cosas. De moemnto esperamos a esos merge
59. hay una forma de exportar este chat? en archivos?
60. Listo. Mergeado en main, faltan algunas cosas de unos integrantes, pero podemos armar ese estandar de anexo-ia. Haz pull y verifica. Estoy desde mi laptop lejos de mi pc con tu sesión asi q no puedo ejecutar comando, tendrás q hacerlo tu, yo te doy lo q necesites para ello
61. ahi lo tienes, corrige lo de las ref y dale con el estandar anexo ia
62. Grok no puedo acceder a la conversa. Marca para lo q se usó, pero dejando claro q no podemos acceder a esos chats, era una prueba de 3 dias. Haz -> resumen, introducción (definir «ficha»/«lista» y párrafo de aporte) y todo lo de los TODO q sean doables. Ponlos ahi, pero yo las modificaré para q sea con mis palabras, pues asumo q esas partes son las q dice el profe q son aporte propio. sección 5 está up en su rama, falta merge y la rama de 3.2 cloud-fastly-deno tambien tiene un commit nuevo q hay q consolidar (de vaguzzel). Sigue usando el token para hacer commit y push.

*(El prompt 61 iba precedido de un token de acceso a GitHub, omitido aquí y revocado tras su uso.)*

**Nota sobre el prompt 62.** A partir de él la IA generó borradores del resumen ejecutivo, de la introducción (incluido el párrafo de identificación del aporte) y de las conclusiones, marcados en `main.tex` como `[BORRADOR IA]`. El párrafo de aporte y las conclusiones están en la lista del punto 6.1; el compromiso declarado es que el autor y el grupo los reescriben con sus palabras antes de la entrega, y el nivel de esas secciones se fija en el Anexo A según lo que quede en el texto final (0 o 1 si se reescriben; si algún pasaje se conserva, se declara nivel 2 y esta nota es su evidencia).

## Sesiones con el agente de investigación externo (Grok, xAI)

Operadas por el autor. Los prompts de sistema que se le entregaron están versionados en el repositorio:

- `trabajo/fuentes/guia-agentes-busqueda-fuentes.md` — guía de búsqueda de fuentes por sección (bloques A a D). Resultado: `archivosTemporal/fuentes_agent/fuentes-candidatas-agentes/` y `trabajo/fuentes/bib-sin-notas/`. Revisión humana y mecánica en `trabajo/fuentes/revision-fuentes-agentes.md`.
- `trabajo/3.1-alternativas/prompt-verificacion-candidatos.md` — verificación de 19 dudas puntuales en documentación oficial. Resultado: `trabajo/3.1-alternativas/verificacion-candidatos.md`.
- Prompts conversacionales adicionales del autor al agente (ampliación de la pool, guía de elección, estructuración de decisiones en tabla, corrección de estilo del borrador de 3.1). Resultados: `trabajo/3.1-alternativas/guia-eleccion-otros.md`, `propuesta-seleccion-anexo-D-2026-09-20.md`, `citas-pool-otros.csv` y `.bib`.

**Disponibilidad de las conversaciones con el agente externo.** El agente se usó bajo una cuenta de prueba de tres días de xAI que expiró antes de la entrega; las conversaciones no quedaron exportadas ni son accesibles hoy, por lo que **no se adjuntan sus registros**. Se declara igual el uso (nivel 2: búsqueda y verificación de fuentes) y se conserva la evidencia que sí existe: los dos prompts de sistema versionados arriba (texto literal de lo que se le entregó), sus salidas archivadas en el repositorio con fecha, y la revisión humana posterior de cada fuente en su original (`trabajo/fuentes/revision-fuentes-agentes.md`, `trabajo/3.1-alternativas/verificacion-candidatos.md`). Los prompts conversacionales no versionados se dan por perdidos; ninguna cifra, cita o decisión del informe se sostiene solo en ellos.
