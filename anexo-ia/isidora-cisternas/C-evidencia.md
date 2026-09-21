# Anexo A — Parte C: evidencia trazable (2.2 Arranque en frío)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Isidora Cisternas.
**Secciones cubiertas:** 2.2 Arranque en frío: causas, medición y mitigaciones.

## 1. Conversaciones

| # | Herramienta | Fechas | Enlace | Secciones |
|---|---|---|---|---|
| 1 | Claude (chat web claude.ai, en proyecto), Claude Opus 5 (`claude-opus-5`) | 19-09 a 21-09-2026 | https://claude.ai/share/e5d8ed7b-e5fc-414d-9d3d-319346092fbb | 2.2; registro del Anexo A |
| 2 | Claude (chat web claude.ai, en proyecto), Claude Opus 5 (`claude-opus-5`) | 20-09 a 21-09-2026 | https://claude.ai/share/f462e3cd-7dad-4570-b408-93ceccf9802f | 2.5; ampliación del registro del Anexo A |

## 2. Historial de versiones

[COMPLETAR según lo que corresponda:]

- **Documento de trabajo:** historial de versiones de `Apuntes secciones informe` Adjunto en sección trabajo. Contiene los apuntes de lectura de la autora, la versión consolidada inicial de 2.2 y las versiones sucesivas del borrador revisadas en la sesión 1.
- **Repositorio:** commits de la integrante en el repositorio del grupo en ramas "2.2 Arranque en frio" y "2.5 WebAssembly y WASI".


## 3. Qué produjo la IA y qué produjo la persona

**Apuntes y primer borrador.** Los apuntes de lectura de Golec et al. (2025) y Ustiugov et al. (2021) y la primera versión consolidada de 2.2 son de la autora, escritos antes de usar IA.

**Retroalimentación y fuentes.** La IA revisó el borrador contra las Indicaciones (FEP00.3.26) y la guía del equipo. Señaló lo que faltaba respecto de la ficha (medición; mitigaciones de concurrencia aprovisionada, instantáneas y entornos livianos) y marcó imprecisiones conceptuales (definición de arranque en caliente, clasificación de lenguajes, Lambda@Edge como mitigación, cambios de VPC de 2019, nombre actual de Cloud Run functions). También propuso un plan de lectura con fuentes de la planilla del equipo (SeBS, Scheuner & Leitner, Gackstatter et al., Ghorbian) y fuentes oficiales que faltaban (documentación de AWS, Google Cloud y Azure, y los blogs de Cloudflare 2020 y 2025), verificadas mediante búsqueda web durante la sesión. La autora leyó las fuentes, tomó sus propios apuntes y decidió cuáles usar.

**Corrección de citas y referencias.** La IA contrastó las afirmaciones del borrador con los PDF originales (SeBS, Gackstatter et al.) y con la documentación oficial. Detectó una referencia con autores y congreso equivocados (Gackstatter et al.), un dato sin respaldo («latencias sub-milisegundos»), páginas incorrectas (SeBS) y un título equivocado (Cloudflare 2020). Las correcciones en el texto y en el `.bib` las hizo la autora.

**Estructura y redacción de 2.2 (nivel 3).** La IA propuso el esqueleto causas–medición–mitigaciones–cierre, ajustado a lo que pide la ficha, y un borrador con huecos marcados `[COMPLETAR]` que la autora rellenó con sus fuentes. En el párrafo de mitigaciones, la IA propuso la idea que lo organiza (evitar, saltarse o abaratar el arranque en frío, con su costo) y un reordenamiento redactado a partir de las frases de la autora. Por último, la IA redujo la sección completa de unas 640 a 350 palabras sin agregar ideas; los detalles eliminados se informaron a la autora para que decidiera.

**Sección 2.5 (sesión 2).** Los apuntes de lectura (Haas et al. 2017, especificaciones de WASI 0.2 y 0.3, artículo de la Bytecode Alliance y Kjorveziroski et al. 2021) y el primer borrador de 2.5 son de la autora, escritos antes de usar IA en esta sesión.
- *Retroalimentación y fuentes (nivel 2).* La IA revisó el borrador contra las Indicaciones y la guía del equipo, y verificó sus afirmaciones mediante búsqueda web. Detectó una atribución equivocada de la autoría de WASI (desarrollado por el WASI Subgroup del W3C WebAssembly Community Group, no por la Bytecode Alliance junto al W3C), una referencia a la especificación del W3C con versión y fecha que no correspondían, una afirmación sin respaldo (que Wasmtime «certifica» el estándar), un error conceptual (los contenedores no empaquetan un sistema operativo completo) y una cifra de arranque apoyada en una revisión sistemática en lugar de una medición. Sugirió además contenido faltante respecto de la ficha y la guía: evidencia contraria (Jangda et al. 2019), el desarrollo de la portabilidad frente al lock-in, el ecosistema Spin y wasmCloud, y las referencias cruzadas. La autora hizo las correcciones y agregó por su cuenta nuevas referencias (Faasm, Fastly, Cloudflare).
- *Reducción de extensión (nivel 2 o 3).* La IA redujo la segunda versión de la autora de unas 720 a unas 340 palabras. Reescribió y fusionó los párrafos de concepto y de comparación sin agregar ideas nuevas. En el párrafo de cierre solo eliminó cifras repetidas y reordenó frases de la autora. Informó qué eliminó (el desglose de las causas de la ralentización y las cifras duplicadas) para que la autora decidiera.
- *Verificación de sitios oficiales (nivel 2).* La IA confirmó `wasmcloud.com` y la página del proyecto en la CNCF como fuentes válidas para wasmCloud. Indicó que `fermyon.dev` no pudo confirmarse como sitio oficial y que el sitio oficial de Spin es `spinframework.dev`, proyecto de la CNCF creado por Fermyon. 

**Lo que no hizo la IA.** Ninguna cifra, cita o referencia del informe proviene del modelo: todas se tomaron de la fuente original, y la autora las abrió y verificó.


