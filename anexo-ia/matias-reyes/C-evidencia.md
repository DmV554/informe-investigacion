# Anexo A — Parte C: evidencia trazable (1 Marco teórico; 2.1 Modelos de ejecución y aislamiento)

**Trabajo:** Informe TI-05 «Serverless y computación en el borde», grupo TERABYTE, PUCV ICI-5444.
**Integrante:** Matías Reyes
**Secciones cubiertas:** 1 Marco teórico y conceptual; 2.1 Modelos de ejecución y aislamiento; Anexo A, partes B y C.

## 1. Conversaciones

| # | Herramienta | Fechas | Enlace | Exportación en `registros/` | Secciones |
|---|---|---|---|---|---|
| 1 | Claude (Anthropic), modo Cowork, proyecto «Investigacion Valen» | 19-09-2026 | ⟨PEGAR URL⟩ | `registros/sesion1_marco_teorico.md` ⟨exportar⟩ | 1 Marco teórico |
| 2 | Claude (Anthropic), modo Cowork, proyecto «Investigacion Valen» | 19-09-2026 a 20-09-2026 | ⟨PEGAR URL⟩ | `registros/sesion2_seccion_2_1.md` ⟨exportar⟩ | 2.1; candidatos para 3.1 |
| 3 | Claude (Anthropic), modo Cowork, proyecto «Investigacion Valen» | 21-09-2026 | https://claude.ai/code/session_013RAnCWvAidg7cAso1XUs5t | `registros/sesion3_anexo_A.md` ⟨exportar⟩ | Anexo A (B y C) |

Verificar que el profesor pueda abrir cada enlace (compartir la conversación o adjuntar la exportación).

**Archivos producidos con IA y guardados en el proyecto (con fecha de creación, hora de Chile):**

- `claude/marco_teorico.tex` y `claude/marco_teorico_referencias.bib` — 19-09-2026, 02:49.
- `claude/seccion_2_1.tex` y `claude/seccion_2_1_referencias.bib` — 20-09-2026, 00:38.

Cada `.tex` trae al final un bloque «TRAZABILIDAD» con la frase textual (y la página o sección) de cada fuente que respalda cada cita.

## 2. Historial de versiones (commits del integrante)

Salida de `git log --oneline --author="<nombre>"` o de `git log --oneline <rama>` para las ramas propias, con fecha:

- ⟨COMPLETAR desde el repositorio o el historial de Overleaf / Google Doc del equipo: commit o versión en que se integró `marco_teorico.tex` en `main.tex`⟩
- ⟨COMPLETAR: commit o versión en que se integró `seccion_2_1.tex` en `main.tex`⟩
- ⟨COMPLETAR: commit o versión con el párrafo 3 de 2.1 escrito por el integrante⟩

(Las conversaciones con IA no tienen acceso al repositorio del grupo, por eso esta sección la completa el integrante.)

## 3. Qué produjo la IA y qué produjo la persona

**1 Marco teórico y conceptual.** La IA revisó el borrador completo de ~450 palabras, confirmando una frase textual de respaldo por cita. No incluye precios ni cifras. No se asumió hacer a propósito la justificación de cómo se mide cada dimensión (sección 3.2, autoría humana). La persona definió alcance y extensión, revisó y ajustó la redacción, y verifica cada cita en el original antes de entregar (regla 7.5) ⟨indicar qué se reescribió⟩.

**2.1 Modelos de ejecución y aislamiento.** Se hizo una revisión + mejoras de los párrafos 1 y 2 (~320 palabras), la tabla resumen opcional (comentada) y la lista de candidatos para 3.1 salieron de la IA, Las citas se contrastaron con el original el 20-09-2026 (frases textuales en el bloque de trazabilidad). Se descartó a propósito la cifra de Cloudflare que compara Workers con Node por ser comparativa del propio proveedor (regla 7.4), y se advierte que las cifras de Firecracker son de 2020 y medidas por AWS. El **párrafo 3 («cuándo conviene») es de autoría humana íntegra** (punto 6.1)

**Anexo A, partes B y C.** La IA completó el formato a partir de los archivos guardados en el proyecto. Los prompts de las sesiones 1 y 2 aparecen como reconstrucción porque la conversación que llenó el anexo no tenía acceso a las anteriores; el integrante los reemplaza por el texto literal y completa enlaces, commits y niveles finales.
