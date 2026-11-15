# TESISV2: versión V3 del TFI

Esta carpeta es la versión LaTeX completa del TFI con todas las correcciones trabajadas hasta el 15/11/2026. Se armó así:

1. **Base:** la V5 (`TFI - CAMPOS - SCARAZZINI V5 (TESISV2).pdf`, 12/11), reconstruida en LaTeX a partir del repo (V4.1) y del texto de ese PDF.
2. **Encima de la V5:** los cambios de `lista_cambios_V3.md` que ya estaban decididos.

Para compilar: `pdflatex → biber → pdflatex → pdflatex` sobre `TFI - CAMPOS - SCARAZZINI.tex`. Compila sin errores ni referencias indefinidas.

## Estructura (igual a la V5)

| Archivo | Contenido |
|---|---|
| `frontmatter/resumen.tex`, `abstract.tex`, `agradecimientos.tex` | Resumen, Abstract (nuevo en V5) y agradecimientos en tercera persona |
| `capitulos/introduccion.tex` | Cap. 1 (la 1.6 pasa a ser "Estructura del documento") |
| `capitulos/objetivos.tex` | Cap. 2: necesidad, objetivos y alcance (nuevo en V5) |
| `capitulos/marco_teorico.tex` | Cap. 3 (con 3.2 Metodologías ágiles y 3.4.1 tabla de normas) |
| `capitulos/desarrollo_producto.tex` | Cap. 4: metodología aplicada, problema, requerimientos, datos, experimentación (síntesis), línea base y gestión de riesgos |
| `capitulos/resultados.tex` | Cap. 5 |
| `capitulos/implementacion.tex` | Cap. 6, **versión nueva sin costo-beneficio** |
| `capitulos/conclusiones.tex` | Cap. 7 |
| `capitulos/anexo_experimentos.tex` | Apéndice A: experimentos |
| `capitulos/anexos.tex` | Apéndice B: diccionario de datos y visualizaciones |
| `capitulos/simbolos.tex` | Apéndice C |
| `scripts/generar_gantt.py` | Genera `imagenes/gantt_proyecto.png` y `imagenes/gantt_implementacion.png` |

## Cambios aplicados sobre la V5

- **C6.1–C6.12, capítulo 6 y su eco en el resto del documento:** nuevo capítulo 6 sin costo-beneficio, con el costo de los siniestros solo como contexto, el impacto económico declarado no cuantificable, la integración operativa e indicadores de impacto. Se ajustaron en consecuencia el Resumen, el Abstract, la 1.6, el OE6, la tabla 2.1, el cap. 5 (párrafo 2 y tabla 5.4), la tabla 7.1 y la 7.4. Se quitaron de la bibliografía Sysarmy/Coderhouse y Rava.
- **AR1–AR11, redacción de resultados:** todo se reporta contra la tasa base del 71,1 % y la alerta permanente; sin "buen resultado" ni "notablemente"; "en línea con" ISO/IEC 42001; MSE en lugar de "Brier" en la tabla 5.4.
- **M4.4, escala de tres niveles (verde, amarillo, rojo):** se eliminó la fila del cambio "de tres a cuatro niveles" en la tabla 4.2. Cambiaron RF4, el Z-Score de la 4.3, el cap. 5, la tabla 5.4, la tabla 7.1, la justificación de los criterios de riesgo, el apéndice C y el Gantt de implementación. Se agregó también una nota en el marco teórico. La matriz de riesgos (con naranja) no se tocó.
- **P1–P8:**
  - P1: Gantt del proyecto regenerado, sin etiquetas superpuestas.
  - P2: "(una semana)" en la tabla 5.2.
  - P3: cita a Novello en el párrafo de CABA.
  - P4: definición de modo sombra (cap. 6).
  - P5: "un modelo" en la 3.5.1.
  - P6: oración de la 3.1 reformulada.
  - P7: oración de la 4.2 reformulada.
  - P8: se eliminó la oración de la 7.3.
- **M5.8, errores de redacción:** latinismos, "primer tarea", "accidentólogos", "Ciudad Autónoma", coma doble, paréntesis suelto, "lag_1", "cláusula 6.1", "Crítica"/"Clasificación", RAG → "codificación tipo semáforo" (y se quitó la sigla RAG). No se unificó "accidentes" → "siniestros" en todo el documento.

## Diferencias con la V5 que se resolvieron a favor de la V4.1

Al reconstruir aparecieron lugares donde la V5 había perdido retoques de la V4.1. En esos casos se mantuvo el texto de la V4.1:
- las definiciones de variables debajo de las ecuaciones 3.1 y 3.2;
- la notación VP/VN/FP/FN;
- el listado completo de siglas y símbolos del apéndice C.

## Pendiente de decisión o verificación

- **C6.8:** la frase "Los requerimientos que quedan pendientes forman parte del plan de implementación del capítulo 6" (4.3.3) se dejó como estaba. Está marcada con un comentario.
- **Cortes del Z-Score de tres niveles** (4.3): roja > 2σ, amarilla entre 1σ y 2σ, verde ≤ 1σ. Marcado `% VERIFICAR`.
- **Cronología de la tabla 4.1:** es una reconstrucción por temas. Marcada `% VERIFICAR`.
- **Números de apartados ISO de la tabla 3.1:** chequearlos contra la norma.
- **Columnas del Kanban** (pendiente, en curso, en revisión, terminado): confirmar.
- **Bibliografía nueva:** `brooke1996` y `sauro2011` (SUS, cap. 6).
- **"Aprendizajes y aportes de la formación de grado":** el apartado propuesto (cap. 8 provisorio) no está incluido, igual que en la V5.
- **Quedan para después:** M1.x, M2.x, M3.x, M4.1–M4.3 y M5.1–M5.7.
