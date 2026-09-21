# Registro de Desarrollo y Validación · Mitad de Rodolfo (Sección 3.2)
### TERABYTE (TI-05) · Fecha: 20-09-2026 · Responsable: Claudio (asumiendo parte de Rodolfo)

---

## 1. Diagnóstico del material recibido (`Borrador_3.2_Tablas_A_B_v3_resuelto_2026-09-20.md`)

Rodolfo dejó un borrador técnico **v3 de alta calidad** (~50 KB), producto de una revisión formal realizada el 20-09-2026 a las ~04:11 AM (Santiago).

### ¿Contiene lo necesario para validar las filas?
**SÍ, AL 100%.**
- Contiene las 7 plataformas bajo su encargo: AWS Lambda, AWS Fargate, AWS App Runner, AWS Lambda@Edge, AWS CloudFront Functions, Azure Functions y Azure Container Apps.
- Cada celda contiene la cita textual oficial (`[cita]`), extrapolación técnica declarada (`[extrapolación declarada]`) o marca de ausencia (`no documentado`), eliminando cualquier adjetivo subjetivo.
- 13 fuentes oficiales primarias individualizadas ([F1] a [F13]) más las 3 matrices de responsabilidad compartida ([D1-AWS], [D1-Microsoft], [D1-CNCF]).
- Las 11 discrepancias de versiones anteriores fueron formalmente resueltas y cuentan con la marca `[✅ aceptado por Rodolfo, 20-09-2026]`.

### ¿Contiene los dos párrafos de análisis?
**NO redactados como texto corrido de informe**, pero **SÍ contiene todos los hallazgos duros y contrastes no evidentes** para redactarlos de inmediato:
1. **Sobrecosto del borde:** Lambda@Edge cobra exactamente 3,0× el cómputo de Lambda estándar ($0,00005001 vs $0,0000166667 / GB-s) y carece de capa gratuita y concurrencia aprovisionada.
2. **Límite duro de infraestructura:** Techo no configurable de 230 s en Azure Functions HTTP por el *idle timeout* del Azure Load Balancer.
3. **Piso mensual encubierto en mitigaciones:** Provisioned Concurrency (AWS) y Always Ready (Azure Flex) trasladan el costo a facturación continua para evitar el cold start.
4. **Traslado de complejidad operacional:** En Fargate/CaaS se transfiere al equipo la configuración de VPC, ALB y políticas de autoescalado; en Always-On (t3.medium) se asume el 100% de la operación del sistema operativo y parcheo.
5. **Riesgo de vendor lock-in y obsolescencia:** Cierre de AWS App Runner a nuevos clientes (comunicado oficial vigente 2026).

---

## 2. Validación cruzada de filas (Borrador Rodolfo v3 vs `main.tex` / `Tablas-3.2-Definitivas.md`)

| Fila en `main.tex` | Estado en v3 de Rodolfo | Ajuste / Acción de validación requerida |
|---|---|---|
| **Fila 1: AWS Lambda** | Validado. Cifras coinciden ($0.20/M, $0.0000166667/GB-s x86). Identificó tramos por volumen y SnapStart. | **Consolidado OK.** En la tabla se usa el tramo 1 (el aplicable a TERABYTE) y se consigna SnapStart + Provisioned Concurrency. |
| **Fila 2: Azure Functions** | Validado. Documentó Consumption, Flex y Premium. | **Armonización de métrica:** Rodolfo documentó Flex como `$0.40/M + $0.000026/GB-s` (métrica de tiempo/memoria clásica) mientras que la calculadora de Azure cotiza `$0.000018/vCPU-s + $0.0000021/GiB-s`. Ambas son oficiales; se documenta la relación en el texto. Techo HTTP de 230 s incorporado. |
| **Fila 5: AWS Fargate** | Validado. Precio x86 ($0.04048/vCPU-h y $0.004445/GB-h) y ARM ($0.0323798/vCPU-h). | **Consolidado OK.** Se mantiene la nota de que ECS doc admite hasta 32 vCPU / 244 GB frente a los 16 vCPU / 120 GB de la página general de precios. |
| **Fila 6: Azure Container Apps** | Validado. Consumption ($0.000024/vCPU-s, idle $0.000003/s, RAM $0.000003/s). | **Consolidado OK.** Refleja piso condicional a réplicas mínimas > 0. |
| **Fila 9: Lambda@Edge / CF Functions** | Validado. Precios globales CloudFront ($0.60/M y $0.00005001/GB-s para L@E; $0.10/M para CF Functions). | **Consolidado OK.** Fila conjunta validada; se excluye "sub-milisegundo" de la celda de tiempo y se declara como utilización de cómputo. |
| **Fila 10: Instancia Always-On** | Rodolfo la dejó como "PENDIENTE con Francisca". | **Cerrada por Claudio:** Ya configurada como `t3.medium` (2 vCPU, 4 GiB) en `main.tex` ($0.0416/h On-Demand, $0.026/h reservada 1 año = $18.98/mes), alineada con el modelo de costos de 4.2. |
| **AWS App Runner** | Validado como "cerrado a nuevos clientes", con piso por defecto de 1 instancia ($0.007/GB-h). | **Tratamiento:** No entra como fila fija en la tabla principal (para respetar el presupuesto de 12 filas y 1,25 págs), pero **es el eje central del segundo párrafo de análisis** y se detalla en el anexo. |

---

## 4. Estado de Ejecución e Integración (Cerrado)

1. **Armonización de Filas de AWS y Azure:**
   - **Azure Functions (Flex Consumption):** Actualizada a tarifa verificada por Rodolfo de \$0.40/M req. + \$0.000026/GB-s (capa gratuita 250k req. y 100k GB-s/mes) y mitigación Always Ready a \$0.000004/GB-s base + \$0.000016 ejec.
   - **Límites de Azure Functions:** Incorporado explícitamente el techo infranqueable de 230 s para disparadores HTTP impuesto por el Azure Load Balancer.
   - **AWS Fargate:** Rango ampliado hasta 32 vCPU / 244 GB según documentación de Amazon ECS, con nota de que la página de precios solo lista combinaciones hasta 16 vCPU / 120 GB.

2. **Redacción de los Dos Párrafos de Análisis:**
   - Integrados formalmente en `informe/main.tex` (reemplazando el `% TODO (Rodolfo)`) y respaldados en `trabajo/3.2-cuadro/Tablas-3.2-Definitivas.md` (Sección 6).
   - Abordan los contrastes no evidentes exigidos por la rúbrica: el sobrecosto 3,0× de Lambda@Edge, los pisos mensuales encubiertos en Provisioned Concurrency / Always Ready, la redistribución de complejidad operativa hacia VPC/NAT Gateway en CaaS, el techo de 230 s de Azure HTTP y el riesgo empírico de vendor lock-in evidenciado por el cierre de AWS App Runner a nuevos clientes en 2026.

3. **Verificación de Compilación:**
   - Compilación con `pdflatex -interaction=nonstopmode main.tex` exitosa (exit code 0, 23 páginas generadas, 0 errores).

4. **Archivos modificados listos para commit del usuario:**
   - `informe/main.tex`
   - `trabajo/3.2-cuadro/Tablas-3.2-Definitivas.md`

