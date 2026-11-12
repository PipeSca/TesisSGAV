# Cambios aplicados respecto del repositorio original

## Redacción
- Se aplicaron las correcciones resaltadas en naranja en el `.docx`: cambios de tiempo
  verbal (futuro/pretérito → presente), despersonalización ("podemos" → "se puede"),
  y ajustes menores de vocabulario a lo largo de todos los capítulos.

## Capítulo 2 — Marco teórico
- Nueva subsección **2.5.7 Métricas de Evaluación de Modelos**, con las diez fórmulas
  nuevas escritas en LaTeX (ecuaciones MAE, MSE, RMSE, MASE, devianza de Poisson,
  Brier, exactitud, precisión, sensibilidad y F1) y sus tablas de apoyo.

## Capítulo 3 — Desarrollo del producto
- Introducción nueva del apartado 3.5 (aclaración sobre la no comparabilidad de los
  experimentos).
- Tabla 3.2: se eliminó la fila MASE y se reescribió la interpretación del MAE.
- Tabla de métricas del XGBoost con capa Z-Score: encabezado, valores de MSE y RMSE
  actualizados, fila MAE agregada y nota reescrita.
- Párrafos nuevos sobre la distribución de Z-Score, con su tabla de niveles de riesgo.
- Tabla nueva de síntesis comparativa de los experimentos, al cierre del apartado 3.6.2.
- Apertura reescrita del apartado 3.7, con la lista de razones de la elección del
  modelo de línea de base, y párrafo nuevo sobre la exploración de datos.
- Apartado 3.5.5: párrafo de las cuadrículas y cierre del apartado reescritos.
- Nota de la tabla del umbral ampliada.

## Capítulos 4 y 5
- `capitulos/resultados.tex` es ahora el **Capítulo 4 — Resultados** (versión breve con
  cuatro tablas, `\label{cap:resultados}`). Reemplaza al texto anterior de conclusiones.
- Nuevo `capitulos/conclusiones.tex`: **Capítulo 5 — Conclusiones**
  (`\label{cap:conclusiones}`).
- Ambos se adaptaron al estilo del resto del documento: `booktabs`, `\notaflot`,
  `\qty{…}{\percent}` y referencias con `\cref`/`\ref` en lugar de números fijos
  (figura 3.14, tabla 3.13, tablas 3.20–3.21, sección 1.6).

## Numeración e índices
- Las referencias escritas a mano ("sección 1.5", "sección 3.7.1", "sección 3.8.1",
  "sección 2.4.1", "sección 3.8.3", "Apéndice B", "apartado 2.4") pasaron a `\ref`.
- Tabla A.1 fijada con `[H]`: antes flotaba detrás del `longtable` A.2 y el índice de
  tablas las listaba en orden A.2, A.1.

## Apéndice B — Listado de símbolos
- Siglas agregadas: AUC-ROC, CABA, FCE, FPA, ID, NASA, OMS, RISC-V, SECYT, SNIICT,
  UI, UNESCO, UNVM, UX. La columna de significado ahora ajusta línea (`p{12cm}`).
- Símbolos agregados: $z_{t,k}$, $(\cdot)^{\top}$, $i$, $w$, $D$, $\mathrm{BS}$,
  $VP$, $VN$, $FP$, $FN$, $F_1$.
- Convenciones nuevas: semana de 28 bloques, clases del sistema de alerta
  (crítica/normal, alerta permanente) e identificación y nivel de riesgos (R1–R11, P, I,
  inherente/residual).

## Para revisar
1. **`% REVISAR` en `capitulos/desarrollo_producto.tex`**: el texto anuncia "cinco
   razones" y la lista tiene cuatro ítems (a–d). En el `.docx` tampoco estaba el
   quinto.
2. **Tablas reconstruidas**: en el `.docx` llegaron con epígrafe y nota pero sin
   contenido. Se armaron con los datos del propio texto y conviene verificarlas:
   - `tab:simbolos-formulas` — símbolos empleados en las fórmulas.
   - `tab:matriz-confusion-estructura` — estructura de la matriz de confusión.
   - `tab:sintesis-metricas` — síntesis de métricas por grupo.
   - `tab:niveles-riesgo-zscore` — distribución de niveles de riesgo (47,6 / 50,6 / 1,8 %).
   - `tab:sintesis-experimentos` — síntesis comparativa de experimentos; la columna
     "Métrica principal" se completó eligiendo el valor más representativo de cada
     experimento.
3. En el apartado 3.7 se quitó la oración final del párrafo "Usualmente se trabaja…"
   (la que explicaba la elección del árbol XGBoost), porque la reemplaza la lista de
   razones nueva.
4. **Siglas sin agregar o supuestas**: `PPIDTA-IA` (introducción) no se incluyó en el
   listado porque su desarrollo no figura en el texto. `SECYT` se desarrolló como
   "Secretaría de Ciencia y Tecnología (UNC)"; confirmar.
5. **Brier / MSE**: el Capítulo 4 informa "Brier 0,1931", mientras que la tabla de
   métricas de error del modelo de línea base (Capítulo 3) presenta el mismo valor
   como MSE. Son equivalentes con objetivo binario, pero conviene unificar el nombre.
