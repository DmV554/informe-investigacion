# Revisión de `fuentes-candidatas-agentes` (bloques A-D)

Fecha de revisión: 2026-09-19. Revisado con apoyo de IA (Claude, Cowork) sobre los 14 archivos entregados por los agentes de búsqueda; esta revisión es apoyo de formato y verificación mecánica, no lectura de las fuentes. **Cada fuente que se use en el informe debe ser abierta y leída por el integrante que la cita.**

## Cifras

| Bloque | Filas CSV | Entradas BIB | Tipos predominantes |
|---|---|---|---|
| A · Académico | 15 | 15 | 11 papers revisados por pares, 2 estándares, 2 informes |
| B · Límites y precios | 54 | 54 | documentación oficial |
| C · Alternativas y datos serverless | 93 | 93 | documentación oficial (73 proveedor, 18 proyecto), 1 paper |
| D · Eventos, Wasm e industria | 21 | 21 | documentación oficial, 2 estándares, 3 encuestas, 1 caso, 1 paper |
| **Total** | **183** | **183** | |

Chequeos mecánicos que pasaron: claves BibTeX idénticas entre CSV y BIB en los cuatro bloques; ninguna clave duplicada entre bloques; ninguna colisión con las 47 claves del Excel; todas las entradas `@online` llevan `urldate`; todas llevan `year`; fecha de consulta 2026-09-19 en las 183 filas.

Muestra verificada de forma independiente (10 fuentes, una por tipo de riesgo): Hellerstein 2019 (PDF abierto CIDR), Yussupov 2019 y López 2018 (DOI vía Crossref), Ekwe-Ekwe & Amos 2024 (DOI IEEE CLOUD 2024 vía Crossref), W3C Wasm core (confirma Release 3.0, CR Draft 2026-08-31), MongoDB Flex migration (confirma retiro de Serverless instances), Fastly pricing (confirma precios públicos de Compute), caso Upside en AWS (confirma Lambda→ECS/Fargate y cifras declaradas), CNCF Annual Survey (confirma edición 2025 publicada 2026-01; N y metodología están en el PDF, no en la página). Las 10 coinciden con lo registrado. No se detectaron referencias inventadas en la muestra.

## Problemas encontrados

1. **Los `.bib` originales no compilan.** El campo `note` de muchas entradas (sobre todo B y C) contiene `%`, `$`, `&` y `≤` sin escapar, que LaTeX interpreta como comandos. Además, con estilo APA el `note` se imprime entre corchetes en la bibliografía, y son notas de trabajo ("scrape", "403", etc.) que no deben aparecer en el informe. **Solución aplicada:** en `bib-sin-notas/` están los cuatro `.bib` con el campo `note` eliminado y `&`/`≤` escapados; compilan limpios con `biber` y la clase `inf-pucv` (183 entradas, 11 páginas de bibliografía de prueba). Las notas siguen disponibles en las columnas del CSV. Al consolidar en `informe/referencias.bib`, usar estos, no los originales.

2. **Cifras de precio dentro de las notas.** Varias notas transcriben tarifas (por ejemplo OCI, GKE, Fastly). Son útiles como pista, pero **no se copian al informe desde la nota**: el integrante abre la página oficial, lee la cifra y la registra con producto, moneda, región, fecha y tipo (punto 5 de las Indicaciones).

3. **Caso público de la sección 5 (bloque D).** El agente no pudo verificar el artículo original de Prime Video (2023) en su fuente y correctamente **no lo citó**. El único caso que registró (Upside, `aws2026upsideserverless`) es un *case study* publicado por AWS, sin autor ni fecha: es material del proveedor, admisible solo declarándolo, y describe una migración Lambda→Fargate dentro de AWS, no un abandono de serverless. Para la sección 5 sigue faltando al menos un caso público verificable en blog de ingeniería con autor y fecha. Tarea pendiente para Fabián.

4. **Encuestas (bloque D).** CNCF Annual Survey 2025 (N=628 según el PDF) y Datadog State of Serverless 2023 / State of Containers and Serverless 2025 están bien clasificadas como `ADMISIBLE-DECLARANDO`. Al citarlas hay que escribir en el texto la muestra y la metodología (y en Datadog, el sesgo de que la población son sus propios clientes).

5. **Tipificación de Jonas et al. 2019.** Registrado como "Informe de industria / ADMISIBLE-DECLARANDO" por ser technical report. Es un reporte técnico de UC Berkeley, no de industria; conviene tipificarlo como reporte académico (`@techreport`, ya está así en el BIB) y tratarlo como fuente académica no revisada por pares, citándolo junto con evidencia revisada.

6. **CNCF Serverless Whitepaper** registrado como PREFERENTE bajo el criterio "estándar de facto del CNCF". Es defendible (el CNCF está en la lista de fuentes preferentes de las Indicaciones), pero es un whitepaper de 2018: usarlo para la definición, no para el estado actual de las plataformas.

7. **Excel: correcciones pendientes que los agentes confirmaron.** Fila 16 (`w3c2026wasmcore`): la URL apunta a core 2.0; la vigente es `https://www.w3.org/TR/wasm-core/` (Release 3.0); el bloque D creó `w3c2026wasmcore3`, así que hay que decidir cuál queda y borrar la otra. Filas 27-30 (reportes de mercado): descartar. Fila 31 y 33: no citar.

## Hallazgos de valor para 3.1 (Claudio y Daniel)

El bloque C documentó con URL y fecha varios cambios de estado que son exactamente el tipo de aporte que las Indicaciones piden registrar en el Anexo D:

- **MongoDB Atlas Serverless**: retirado; migrado a Flex (docs oficiales de migración). Candidato a descartar con fuente.
- **CockroachDB Serverless**: renombrado a **Basic** (la URL antigua devuelve 404).
- **PlanetScale**: planes Hobby y Scaler deprecados; modelo actual distinto.
- **IBM Cloud Functions** (OpenWhisk gestionado): deprecado a fines de 2023; reemplazo Code Engine (fuente: Ekwe-Ekwe & Amos 2024 + docs IBM).
- **Aurora Serverless v1**: línea legacy; comparar con v2.
- **Azure Front Door Rules Engine**: no califica como cómputo en el borde (solo reglas declarativas); **Edge Actions** (preview) sí ejecuta código, con límites muy estrictos.
- **Akamai EdgeWorkers**: sin lista de precios pública; registrar como "solo por cotización".
- **OpenFaaS** no es proyecto CNCF y **Wasmtime** es de la Bytecode Alliance, no del CNCF: no atribuirles acreditación CNCF.

Además, `candidatos-detectados-C.md` lista candidatos nuevos vistos en el CNCF Landscape que no estaban en la guía (Apache OpenServerless, KubeElasti, SlimFaaS, Direktiv, Knix, Camel K) y otros posiblemente discontinuados (Nimbella, Algorithmia, Nuweba). Son entrada para la tabla "candidatos detectados" del registro de búsqueda; ninguno está verificado.

El paper **Ekwe-Ekwe & Amos 2024, "The State of FaaS"** (IEEE CLOUD 2024) es el hallazgo académico más útil del lote para 3.1 y 3.2: comparativa revisada por pares y reciente de proveedores FaaS públicos, incluidos Oracle, Alibaba, IBM y DigitalOcean.

## Cobertura contra los huecos de la guía

| Hueco identificado antes de la búsqueda | Estado |
|---|---|
| Definiciones canónicas (CNCF, NIST, ETSI, edge fundacional) | Cubierto (A) |
| Tres visiones clásicas (Jonas, Hellerstein, Adzic) | Cubierto (A) |
| Precio always-on (EC2, Compute Engine, ECS/GKE) y egress | Cubierto (B); egress AWS está dentro de la página de EC2 On-Demand, no como página aparte |
| Límites y precios de las 14 plataformas del cuadro | Cubierto (B), incluidas regiones y capas gratuitas |
| Mitigaciones de cold start desde docs oficiales | Cubierto (B) |
| 2.4 eventos: colas, pub/sub, idempotencia, orquestación, CloudEvents | Cubierto (D) + 2 papers (A) |
| 2.5 WASI vigente, runtimes, paper fundacional | Cubierto (D, B, A) |
| 2.6 portabilidad y lock-in académico | Cubierto (A) |
| Datos serverless (antes cero) | Cubierto (C), con estados de vigencia |
| Candidatos de 3.1 con producto/precio/límites/estado | Cubierto (C) |
| Encuestas con metodología para sección 5 | Cubierto (D) |
| Casos públicos de salida de serverless | **Parcial**: 1 caso y es material de proveedor |

## Cómo consolidar

1. Cada integrante revisa las filas de su sección en los CSV (columna "Sección del informe") y abre las que va a usar.
2. Lo que se use pasa a la hoja "Fuentes" del Excel (las columnas coinciden) y su entrada del `.bib` correspondiente de `bib-sin-notas/` pasa a `informe/referencias.bib`. No copiar las 183: solo las citadas.
3. Registrar en el Anexo A: búsqueda inicial de fuentes con agente de IA (herramienta y versión), nivel 2, con el prompt usado (`guia-agentes-busqueda-fuentes.md`) y los enlaces a las conversaciones.
