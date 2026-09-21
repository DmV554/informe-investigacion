# Anexo A — Parte B: prompts utilizados (Sección 4.3)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Fabián Solís.
**Secciones cubiertas:** 4.3 Caso TERABYTE.
**Nivel declarado por sección:**
- Sección 4.3: nivel 2. La IA actuó como validador técnico y asistente metodológico, proponiendo el esquema argumentativo para cruzar los datos del caso con la literatura, revisando la coherencia arquitectónica del borrador y resolviendo dudas conceptuales; la persona analizó el caso portuario, definió la arquitectura resultante, seleccionó las fuentes y redactó casi en la totalida el texto final.
**Herramientas:** Claude
**Período:** 20-09-2026 a 21-09-2026.

Los prompts se transcriben literalmente, en orden cronológico, agrupados por sesión. Si alguna parte no se conservó literal, se indica y se presenta como reconstrucción a partir del registro disponible.

---

## Sesión 1 — Claude, 20-09-2026

**Secciones a las que sirvió:** 4.3 Caso TERABYTE.

1. *(Reconstrucción metodológica del prompt)* Actúa como un co-investigador senior en ingeniería de software y arquitectura cloud. Estoy estructurando la Sección '4.3 Caso TERABYTE' para nuestro informe académico (tema TI-05). Considerando nuestro límite estricto de extensión (300-350 palabras), necesito que me propongas un esquema argumentativo denso. 

   Teniendo en cuenta las carpetas Fuentes, Instrucciones, Secciones complementarias y los antecedentes técnicos del 'Informe 1' (Caso La Portuaria), indícame:
   1. ¿Qué datos duros del caso (movimientos de grúa, camiones diarios, latencia, jaulas de Faraday en patio) debo cruzar con la literatura para justificar la viabilidad o los límites de serverless?
   2. ¿Dónde sería lógico insertar referencias cruzadas (ej. 
ef{sec:modelo-costos}, 
ef{sec:poc})?
   
   Dame solo el esqueleto estructural y los puntos de apoyo metodológicos, sin listas con viñetas ni descripciones comerciales, para que yo pueda redactarlo con la rigurosidad técnica necesaria.

2. Ya redacté el borrador de la sección en base a nuestro esquema, las fuentes y las instrucciones de la asignatura (FEP00.3.26). 

   Quiero que revises mi texto y me des feedback crítico sobre la estructura. Evalúa si el nivel de profundidad técnica y el tono (estilo investigador) es el adecuado, y si la progresión lógica entre el modelo de costos y la decisión arquitectónica es fluida. 

   Dame un resumen de lo revisado y su justificación si corresponde. No reescribas el texto.

3. Quiero que me indiques los pasos para cambiar el `referencias.bib` y el `main.tex` con lo siguiente:
   - Sacar la sección de "note" y dejar solo "urldate" bajo norma APA 7.
   - Cambiar cómo se cita en LaTeX, usando `\parencite` en vez de `\cite`.
   
   Explícame cómo realizar estos cambios si corresponde.

4. Revisando mi borrador y las fuentes sugeridas, me surgieron dos dudas para afinar mi redacción:
   1) En el esquema mencionaste la referencia `\parencite{cil2022coldchain}`, ¿de dónde la sacaste y asegura que es la correcta para el monitoreo IoT portuario?
   2) Conceptualmente, ¿cómo explico de forma técnica esta idea sin que suene confusa?: "Un núcleo puramente serverless habría atado la factura al éxito comercial del terminal, a más TEU y más mensajería EDIFACT exigida por la alianza naviera desde 2029, el riesgo de expense explosion que documenta la literatura de FaaS (Liu & Niu, 2024)."

5. *(Reconstrucción metodológica del prompt)* Este es mi borrador final de la sección con los datos integrados:

   "El terminal ya opera 972.000 movimientos de grúa y 1.290.000 de patio al año, más 1.450 camiones diarios con picos de 2.600. Contando registro, confirmación y evidencia por cada evento físico, el tráfico del núcleo transaccional se ubica en el orden de un par de millones de solicitudes mensuales, muy por debajo de los 24,0 millones que fijan el equilibrio de Lambda frente a una flota reservada (
ef{sec:modelo-costos}). En pura aritmética de facturación, serverless gana con holgura hoy y seguirá ganando tras crecer a 920.000 TEU en tres años. El costo no cierra la decisión. La prueba de concepto mide 396 ms de arranque frío en Lambda frente a 2 ms en un borde tipo Workers (
ef{sec:poc}), y el caso impone una cota más dura: la cabina de grúa resuelve el estado en menos de un segundo, sin menús ni confirmaciones, mientras las pilas de contenedores generan jaulas de Faraday que alteran la cobertura del patio cada hora. Sumada a la autonomía exigida de 72 horas sin enlace hacia la nube, esa combinación descarta un núcleo dependiente de invocaciones remotas facturadas por evento. La propuesta técnica del grupo responde fijando el núcleo operacional, el gate y el patio sobre cómputo local siempre encendido y contenedores gestionados, y reserva el borde serverless para el portal público y las notificaciones, donde la continuidad offline no aplica; el patrón replica el monitoreo de cadena de frío ya validado en puertos \parencite{kjorveziroski2021iotedge}. Esa elección fija también el perfil financiero de la propuesta. Terabyte deja de cotizar CAPEX de servidores propios y pasa a OPEX íntegro, capacidad reservada más nodos locales, de consumo acotado y no proporcional a cada movimiento facturable. Un núcleo puramente serverless habría atado la factura al éxito comercial del terminal, a más TEU y más mensajería EDIFACT exigida por la alianza naviera desde 2029: el riesgo de 	extit{expense explosion} que documenta la literatura de precios de FaaS \parencite{liu2024demystifying}. El modelo resultante, coherente con 
ef{sec:limites_lockin} y 
ef{sec:cuadro}, conviene al caso, la porción crítica se paga como flota reservada previsible, y solo el tráfico externo y tolerante a arranque en frío se traslada al proveedor por consumo."

   Para corroborar, ¿la lógica arquitectónica y la justificación matemática frente al modelo de costos son sólidas? Solo confírmame si la base técnica está bien planteada.
