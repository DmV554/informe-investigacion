# Anexo A — Parte B: prompts utilizados (2.3, 4.2 y Anexo C)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Francisca Abarca.
**Secciones cubiertas:** 2.3 Facturación por consumo; 4.2 Modelo de costos; Anexo C (cálculos y tabla de sensibilidad del modelo de costos); apoyo en Bibliografía (`references.bib`) y revisión de coherencia con 3.2.
**Nivel declarado por sección:**
- Secciones 2.3 y 4.2: nivel 2 en la selección inicial de fuentes, orden temático y corrección de estilo/redacción; nivel 1 en la redacción de análisis propios y decisiones técnicas (todas las afirmaciones, métricas y parámetros se verificaron contra las fuentes primarias del `.bib`).
- Anexo C: nivel 2 en el soporte para la estructuración y depuración del script/tabla de sensibilidad; nivel 1 en la definición de supuestos, rangos de variación y análisis de resultados.
- Bibliografía y Anexo A: nivel 2 en formato de entradas `.bib` y compilación/trazabilidad de prompts para la declaración de uso de IA.
**Herramientas:** Claude (Anthropic), modelo Claude 3.5 Sonnet / Claude 3 Opus (web chat).
**Período:** Septiembre de 2026.

Los prompts se transcriben literalmente, tal como fueron formulados (incluidas erratas y errores de tipeo), en orden cronológico, agrupados por conversación. Los archivos y capturas adjuntos se indican entre corchetes.

---

## Sesión 1 — Claude («Facturación y costos en serverless y edge computing»)

**Enlace o exportación:** Registro literal del chat / Exportación de cuenta.
**Secciones a las que sirvió:** 2.3 Facturación por consumo, 4.2 Modelo de costos, Bibliografía, Anexo C.

1. [2.3 y 4.2] debo realizar las secciones "2.3 Facturación por consumo · 4.2 Modelo de costos", y la investigación es "Serverless y Computación en el Borde (Edge Computing)" analiza el problema y continuamos
2. [2.3 y 4.2] partamos con lo primero, estos son los papers de la investigación completa, quiero que me ayudes a seleccionar cuáles me sirven para mis secciones
3. [2.3 y 4.2] ahora necesito que cada una de estas fuentes las clasifiques en las secciones que te envié y si califican como buena fuentes para la investigación
4. [Bibliografía] tienes razón dejame corregirlo
5. [4.2 y Anexo C] ahora sí
6. [2.3, 4.2 y Bibliografía] que fuentes de información me recomendarías agregar para mis secciones?
7. [2.3, 4.2 y Bibliografía] no, pero me refiero a fuentes que no esten dentro de las que te envíe
8. [Bibliografía] finalmente me quedé con estas referencias, me ayudas a armar un borrador?

---

## Sesión 2 — Claude («Conversación B»)

**Enlace o exportación:** Registro literal del chat / Exportación de cuenta.
**Secciones a las que sirvió:** 2.3 Facturación por consumo, 4.2 Modelo de costos, Anexo C, Bibliografía, Anexo A.

1. [2.3 y 4.2] Prompt inicial (reglas del proyecto):
Eres mi asistente de redacción técnico-académica. Vamos a construir particularmente secciones, un trabajo de investigación universitario que se entregará en formato LaTeX.

DATOS DEL PROYECTO:
- Grupo: Terabyte (9 integrantes)
- Tema: Serverless y Computación en el Borde (Edge Computing)
- Asignatura: Tecnologías de la Información

MATERIALES QUE TE VOY A ENTREGAR (ya disponibles o los subiré a continuación):
- Varios papers/fuentes con la información de contenido a usar
- Un archivo references.bib con TODAS las entradas bibliográficas válidas para citar

REGLAS ESTRICTAS (no negociables):
1. Solo puedes usar \cite{clave} con claves que existan literalmente en el references.bib que te entregue. Antes de citar, verifica que la clave existe en ese archivo exacto.
2. Bajo ningún motivo inventes una cita, una clave de cita, o un autor/fuente que no esté en el .bib. Si una afirmación necesita respaldo y no encuentras una entrada adecuada en el .bib, NO inventes una: en su lugar escribe una marca visible «[FALTA REFERENCIA: descripción breve de qué se necesita citar]» y continúa.
3. Todo el contenido debe basarse en la información real de los papers que te entregue. No agregues datos, cifras o hechos que no estén respaldados por esos documentos o que sean de conocimiento técnico general verificable.
4. El análisis (ventajas, desventajas, comparaciones, opiniones críticas) debe ser una elaboración propia y razonada, no una paráfrasis cercana de una sola fuente. Se revisará similitud/plagio.
5. Toda la redacción debe entregarse en código LaTeX válido, usando comandos de sección apropiados (\section, \subsection, \subsubsection según corresponda), entornos de tabla (table/tabular) para comparativas, y \cite{} para las referencias. No uses \documentclass ni preámbulo salvo que te lo pida explícitamente — solo el contenido de cada sección, salvo que te indique lo contrario.
6. Idioma: español. Tono: formal académico, pero con razonamiento propio y crítico, no genérico.

Cuando te pida una sección específica, redáctala siguiendo estas reglas. Si notas que falta información en los materiales entregados para cubrir algo del temario, dímelo explícitamente en vez de rellenar con contenido inventado.

Confirma que entendiste estas reglas antes de continuar.
2. [2.3] [Adjuntó references.bib y las 17 fuentes, sin texto]
3. [2.3] aquí están subapartados definidos en el temario, ayudame con la seccion 2.3 [adjuntó indicaciones y guía del equipo]
4. [2.3 y 3.2] en la tabla "comparativo" te refieres a la tabla de "Criterios de comparación" o a la tabla de "Cuadro comparativo de plataformas serverless y de borde"
5. [4.2 y 3.2] esta es la tabal de la sección 3.2, hay ciertas secciones que mencionan a "Francisca", ya sea para validar o definir, me ayudas a ver que hacer en esas partes [adjuntó el borrador de 3.2]
6. [4.2] espera, entonces para las tablas 3.2a y 3.2b, ¿qué debo decidir, si uso EC2? y dónde valido si es ECS sobre EC2 o el proveedor que elija?
7. [2.3] me podrías dar al menos un borrador de los párrafos 2 y 3?
8. [2.3] puedes revisarlo? [imagen con tu texto de 2.3]
9. [2.3, 4.2 y Anexo C] mis compañero actualizaron la sección 3.2,  por lo cuál actualicé la sección 2.3 y realicé la sección 4.2 y el anexo C. Puedes revisarlo? [adjuntó 2_3.tex, 3_2.tex y 4_2.tex]
10. [Anexo C] no entendí esto y ayudame a corregir el script [imagen de la tabla de sensibilidad]
11. [Anexo C] pero a lo que voy es que esa tabla dónde debo corregirla??
12. [4.2 y Anexo C] puedes revisarlo? [adjuntó 4_2__ver2_.tex]
13. [4.2 y Bibliografía] dime que poner en esa parte de la tabla, estas son mis referencias [imagen y referencias.bib]
14. [Anexo A] me puedes recopilar todos los prompt que hice parta declararlos en la seccion de declaracion de ia?