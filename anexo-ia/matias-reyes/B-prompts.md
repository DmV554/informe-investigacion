# Anexo A — Parte B: prompts utilizados (1 Marco teórico; 2.1 Modelos de ejecución y aislamiento)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Matías Reyes
**Secciones cubiertas:** 1 Marco teórico y conceptual; 2.1 Modelos de ejecución y aislamiento; Anexo A (partes B y C, solo formato).
**Nivel declarado por sección:**
- 1 Marco teórico y conceptual: nivel 2. La IA buscó fuentes abiertas, y revisó el borrador completo (~450 palabras, LaTeX)
- 2.1 Modelos de ejecución y aislamiento, párrafos 1 y 2: nivel 1
- 2.1, párrafo 3 («cuándo conviene»): nivel 0. Por ser parte comparativa (punto 6.1), la IA no lo redactó: solo dejó la evidencia verificada y preguntas guía; la conclusión es de autoría humana.
- Candidatos «otros» para 3.1 (AWS Lambda MicroVMs, Firecracker, gVisor, Kata Containers, Fastly Compute): nivel 2. La IA los detectó en la búsqueda; la decisión de incluirlos corresponde a los responsables de 3.1.
- Anexo A, partes B y C: nivel 2. La IA completó el formato a partir de los borradores guardados en el proyecto; los datos (nombre, enlaces, commits, niveles finales) los confirma la persona.

**Herramientas:** Claude (Anthropic), modo Cowork en claude.ai, dentro del proyecto «Investigacion Valen» claude-opus-5 que muestre cada conversación;
**Período:** 18-09-2026 a 21-09-2026.

Los prompts se transcriben literalmente, en orden cronológico, agrupados por sesión. Si alguna parte no se conservó literal, se indica y se presenta como reconstrucción a partir del registro disponible.

- Podrias darme tu opinión respecto al marco teórico? cambiarias algo? por que? solo dime los cambios y yo veré si los hago, es mas una revision lo que te pido
- Puedes darme ese main.tex en texto normal? para subirlo a google docs.
- lo siguiente pasamelo a texto normal: \textbf{Computación sin servidor.} Es la ejecución de aplicaciones sin gestionar servidores: una plataforma ejecuta, escala y factura el código según la demanda de cada momento. No implica que desaparezcan los servidores ni la operación, sino que su gestión pasa al proveedor \parencite{cncf2018}. \textcite{schleiersmith2021} la caracterizan por tres cualidades: abstracción de los servidores y de su operación, cobro por uso en vez de por reserva (sin cargo por recursos ociosos) y escalamiento automático desde cero. Tampoco es sinónimo de funciones: incluye los servicios de \textit{backend} gestionados, o BaaS \parencite{golec2024}.

\textbf{Modelos de ejecución.} En las \textit{funciones como servicio} (FaaS) la unidad es una función breve, activada por un evento o una solicitud HTTP, que el proveedor escala horizontalmente \parencite{cncf2018,leitner2019} y libera tras un periodo sin uso, lo que se llama escalamiento a cero \parencite{golec2024}. En los \textit{contenedores sin servidor} la unidad es una imagen de contenedor y el equipo ya no aprovisiona ni escala máquinas virtuales \parencite{awsfargate}, aunque no siempre hay escalamiento a cero: Cloud Run retira la última instancia cuando no hay solicitudes \parencite{gcprun}, mientras que Fargate cobra hasta que la tarea termina \parencite{awsfargatepricing}. El \textit{cómputo en el borde} procesa en recursos ubicados entre la fuente de los datos y el centro de datos de la nube \parencite{shi2016}; este informe estudia su variante sin servidor \parencite{aslanpour2021}.

\textbf{Modelo de referencia.} Las \textit{instancias siempre encendidas} son capacidad aprovisionada en forma continua (máquinas virtuales, o contenedores sobre nodos fijos) que se factura por tiempo encendido, se use o no \parencite{ustiugov2021}. Con cargas en ráfagas, esa capacidad queda subutilizada \parencite{eismann2021}.

\textbf{Dimensiones de comparación.} El \textit{costo} en \textit{serverless} se calcula por consumo (invocaciones, tiempo de ejecución, memoria, CPU y transferencia de datos) \parencite{ghorbian2026}, de modo que el tiempo ocioso no se paga \parencite{adzic2017}; en el modelo siempre encendido es casi fijo para una capacidad dada. Esa diferencia define un volumen de equilibrio (secciones~2.3 y~\ref{sec:costos}). La \textit{latencia} es el tiempo entre el envío de una solicitud y su respuesta, suma de la espera en cola, la asignación de recursos y la ejecución \parencite{golec2024}. Al escalar a cero se agrega el \textit{arranque en frío}, el retardo de preparar un entorno nuevo \parencite{ustiugov2021}, tratado en las secciones~2.2 y~\ref{sec:poc}; el borde, en cambio, reduce la latencia de red al acercar el cómputo a la fuente de los datos \parencite{golec2024}. La \textit{complejidad operacional} es el trabajo del equipo para desplegar, escalar, monitorear y mantener el sistema. El modelo sin servidor traslada parte de ese trabajo al proveedor, un motivo frecuente de adopción \parencite{eismann2021}, pero \textcite{leitner2019} documentan herramientas de prueba y despliegue poco maduras y la necesidad de componer servicios del proveedor, a lo que se suman sus límites y la dep.

-Puedes meterme el 3er parrafo que te dare a continuacion, en el siguiente codigo en LaTeX?
\subsection{Modelos de ejecución y aislamiento}
\label{sec:modelos}

Además de la unidad que ejecuta (sección~\ref{sec:marco}), cada modelo se distingue por cómo aísla a los clientes que comparten una máquina \parencite{shafiei2022}. Compartir servidores permite vender tramos cortos de capacidad que de otro modo quedaría ociosa \parencite{liuniu2024}, pero multiplica el costo de toda sobrecarga de aislamiento \parencite{agache2020}. \textcite{agache2020} agrupan los mecanismos en tres familias: los \textit{contenedores}, que comparten el núcleo del anfitrión y obligan a transar entre seguridad y compatibilidad; la \textit{virtualización}, que da a cada carga su propio núcleo y aísla con fuerza, pero ocupa más memoria y tarda segundos en arrancar \parencite{wen2023}; y el \textit{aislamiento por lenguaje}, como los \textit{isolates} de V8, que comparten un proceso a costa de compatibilidad y de exposición a ataques de canal lateral. En medio se ubican las microVM, máquinas virtuales mínimas, y gVisor, un núcleo en espacio de usuario que atiende las llamadas al sistema del contenedor \parencite{wang2022}.

En FaaS, AWS Lambda crea cada entorno en una microVM de Firecracker que no reutiliza entre funciones ni entre cuentas \parencite{awslambdasec}; según sus creadores, Firecracker agrega menos de 5~MB por microVM, arranca en menos de 125~ms, ejecuta binarios Linux sin modificar y sostiene también a Fargate \parencite{agache2020}. Cloud Run, base de las Cloud Run functions \parencite{gcprunfunctions}, ofrece un entorno basado en gVisor, de arranque rápido pero que no emula todas las llamadas al sistema, y otro basado en microVM, totalmente compatible con Linux y con mejor CPU y red, pero de arranque más lento en algunos servicios \parencite{gcprunenv}; ambos suman una capa de virtualización por hardware \parencite{gcprunsec}. En pruebas independientes, gVisor aisló mejor el rendimiento, pero penalizó más las llamadas al sistema y la red \parencite{wang2022}. En el borde, con nodos de pocos recursos donde VM y contenedores resultan pesados \parencite{xie2021}, Cloudflare Workers ejecuta miles de \textit{isolates} por máquina, solo acepta JavaScript y WebAssembly (sección~2.5) y, contra Spectre, restringe relojes e hilos \parencite{cfworkerssec}. En el modelo siempre encendido, la frontera es la VM arrendada: compatibilidad total \parencite{agache2020} y recursos reservados aunque estén ociosos \parencite{liuniu2024}.

%% ---------------------------------------------------------------------------
%% OPCIONAL: Claude me tiro hacer una tabla resumen (1/4 de página). que nos seria util para la presentación y
%% para el cuestionario, incluirla en el informe solo si cabe en 15 páginas.
%% todas las cifras salen de las fuentes citadas en cada fila.
%% ---------------------------------------------------------------------------
% \tabla{Mecanismos de aislamiento en plataformas sin servidor y de borde}{aislamiento}{|p{2.6cm}|p{3.3cm}|p{4.4cm}|p{3.6cm}|}{%
%     \filaTabla{\textbf{Mecanismo} & \textbf{Frontera entre clientes} & \textbf{Ventaja y costo} & \textbf{Dónde se usa}}
%     \filaTabla{microVM (Firecracker) & Núcleo propio bajo un monitor de VM mínimo & $<$5~MB de sobrecarga, $<$125~ms de arranque, binarios Linux sin cambios \parencite{agache2020} & Lambda, Fargate; Cloud Run 2.\textsuperscript{a} gen. \parencite{gcprunenv}}
%     \filaTabla{Núcleo de aplicación (gVisor) & Llamadas al sistema atendidas en espacio de usuario & Arranque rápido; no emula todas las llamadas; sobrecarga en llamadas al sistema y red \parencite{gcprunenv,wang2022} & Cloud Run 1.\textsuperscript{a} gen.}
%     \filaTabla{Isolate V8 & Memoria separada dentro de un proceso compartido & Miles por máquina; solo JavaScript y WebAssembly \parencite{cfworkerssec} & Cloudflare Workers}
%     \filaTabla{VM completa & Máquina virtual arrendada & Compatibilidad total; recursos reservados aunque estén ociosos \parencite{agache2020,liuniu2024} & Modelo siempre encendido}
% }

DEBES METERLE ESTO: 
Ningún mecanismo gana en todos los frentes a la vez (Seguridad, compatibilidad, densidad y velocidad de arranque se transan entre sí), tal como concluyen tanto Agache et al (2020) y Wang et al (2022), que dicen textualmente que “ningun runtima es ventajoso en todos los aspectos”. Google mismo reconoce quee si entorno de segunda generacion (microVM) “generalmente rinde más bajo carga sostenida”, pero arranca mas lento que el de gVisor en ciertos servicios, lo que da un criterio directo ligado a la condicion de carga. Los Isolatesde v8 solo admiten JavaScript y WebAssembly, sin binarios nativos, mientras que Firecracker sí ejecuta binarios Linux sin modificar, lo que marca la restriccion de compatibilidad de código. Wang et al (2022) también muestran que gVisor penaliza especiualmente las llamadas al sistema. la red y los archivos pequeños. Y aunque Firecracker attanca en menos de 125 ms, Lambda igual mantiene un pool de microVM pre arrancadas porque ese tiempo no alcanza para el escalamiento en ráfaga. La eleccion entre contenedores MicroVM, isolates o VM completa depende del tipo de código que se correra 
(lenguaje/binarios/syscalls), del patron de carga (ráfagas cortas versus sostenidas) y de si el costo de mantener recursos siempre listos compensa evitar la latencia de arranque,

---

## Sesión 1 — Claude (Cowork), 19-09-2026

**Enlace o exportación:** ⟨PEGAR URL de la conversación⟩ / `registros/sesion1_marco_teorico.md` ⟨exportar⟩.
**Secciones a las que sirvió:** 1 Marco teórico y conceptual.
**Producto guardado:** `claude/marco_teorico.tex` y `claude/marco_teorico_referencias.bib` (creados el 19-09-2026, 02:49 hora de Chile).

1. ⟨PEGAR LITERAL⟩ *Reconstrucción:* Con la guía del equipo (Terabyte-Guia-Equipo.md), las Indicaciones y los papers subidos al proyecto, revisar la sección 1 «Marco teórico y conceptual» del informe TI-05 en LaTeX para reemplazar el bloque correspondiente de `main.tex`: máximo una página (~450 palabras); definir computación sin servidor, los tres modelos de ejecución (FaaS, contenedores sin servidor, cómputo en el borde), el modelo de referencia siempre encendido y las tres dimensiones (costo, latencia, complejidad operacional);
2. ⟨PEGAR LITERAL de ajustes posteriores, si los hubo⟩ *Reconstrucción:* No redactar cómo se mide cada dimensión ni por qué son los criterios del cuadro (contenido de 3.2, autoría humana obligatoria);
## Sesión 2 — Claude (Cowork), 19-09-2026 a 20-09-2026

**Enlace o exportación:** ⟨PEGAR URL de la conversación⟩ / `registros/sesion2_seccion_2_1.md` ⟨exportar⟩.
**Secciones a las que sirvió:** 2.1 Modelos de ejecución y aislamiento;
**Producto guardado:** `claude/seccion_2_1.tex` y `claude/seccion_2_1_referencias.bib` (creados el 20-09-2026, 00:38 hora de Chile).

1. ⟨PEGAR LITERAL⟩ *Reconstrucción:* Revisar la subsección 2.1 «Modelos de ejecución y aislamiento» siguiendo la estructura de tres párrafos de la guía (concepto con fuente; comportamiento en FaaS, contenedor sin servidor, borde y siempre encendido; «cuándo conviene»), en 300-350 palabras.
2. ⟨PEGAR LITERAL⟩ *Reconstrucción:* No asumir y redactar el tercer párrafo («cuándo conviene») aunque falte por ser parte comparativa; dejar solo la evidencia verificada y las preguntas que debe responder.
3. ⟨PEGAR LITERAL⟩ *Reconstrucción:* Proponer una tabla resumen opcional, anotar los candidatos a «alternativas adicionales» para 3.1 y agregar la trazabilidad de cada cita.

## Sesión 3 — Claude (Cowork), 21-09-2026

**Enlace o exportación:** https://claude.ai/code/session_013RAnCWvAidg7cAso1XUs5t
**Secciones a las que sirvió:** Anexo A, partes B y C (formato).

1. Puedes llenar y modificar esos 2 archivos con lo que hemos visto en este proyecto? basicamente lo que hay en los otros chats
