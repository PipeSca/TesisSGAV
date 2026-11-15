"""Genera los dos diagramas de Gantt del TFI (figura 4.1 y figura 6.1).

Uso:  python scripts/generar_gantt.py   (desde la carpeta TESISV2)
Salida: imagenes/gantt_proyecto.png e imagenes/gantt_implementacion.png
"""
from datetime import date, timedelta
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

FASE = "#2B4A7A"      # barras de fase / etapa
TAREA = "#8E6BB0"     # barras de tarea
HITO = "#C8782A"      # rombos de hito
GRIS = "#9AA5B4"      # fase de descubrimiento
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10.5})


def dibujar(filas, xfmt, salida, xlabel=None, ancho=7.6):
    alto = 0.36 * len(filas) + 1.0
    fig, ax = plt.subplots(figsize=(ancho, alto), dpi=200)
    for i, (tipo, texto, ini, fin) in enumerate(filas):
        y = len(filas) - 1 - i
        if tipo == "hito":
            ax.plot([ini], [y], marker="D", markersize=10, color=HITO, zorder=3)
        else:
            color = {"fase": FASE, "tarea": TAREA, "gris": GRIS}[tipo]
            h = 0.56 if tipo in ("fase", "gris") else 0.46
            ax.barh(y, fin - ini, left=ini, height=h, color=color,
                    alpha=0.95 if tipo != "tarea" else 0.85, edgecolor="white", zorder=2)
    ax.set_yticks(range(len(filas)))
    ax.set_yticklabels([f[1] for f in reversed(filas)])
    for lbl, f in zip(ax.get_yticklabels(), reversed(filas)):
        if f[0] in ("fase", "gris"):
            lbl.set_fontweight("bold")
    ax.tick_params(axis="y", length=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color="#DDDDDD", zorder=0)
    ax.set_ylim(-0.8, len(filas) - 0.2)
    xfmt(ax)
    if xlabel:
        ax.set_xlabel(xlabel)
    fig.tight_layout()
    fig.savefig(salida, dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------- Figura 4.1: cronograma del proyecto ----------------
def d(m, dd):
    return mdates.date2num(date(2026, m, dd))

proyecto = [
    ("gris", "F0 Descubrimiento con el MPF (sprints semanales)", d(2, 10), d(3, 31)),
    ("fase", "F1 Carga, limpieza y transformación", d(4, 1), d(4, 30)),
    ("tarea", "Ingesta y limpieza de datos del MPF", d(4, 1), d(4, 17)),
    ("tarea", "Mapeo de procesos y matriz de riesgos", d(4, 1), d(4, 17)),
    ("tarea", "Flujograma del proceso", d(4, 19), d(4, 23)),
    ("tarea", "Redacción de avances", d(4, 25), d(4, 30)),
    ("fase", "F2 Modelado base y marcos teóricos", d(5, 1), d(6, 29)),
    ("tarea", "Requerimientos, restricciones y partes interesadas", d(5, 1), d(5, 13)),
    ("tarea", "Gestión del riesgo e ISO/IEC 42001", d(5, 15), d(6, 14)),
    ("tarea", "Entrenamiento del modelo base (forecasting preliminar)", d(5, 1), d(6, 14)),
    ("tarea", "Redacción de avances", d(6, 16), d(6, 29)),
    ("hito", "Hito: informe de avance", d(7, 1), None),
    ("fase", "F3 Optimización, MVP e impacto", d(7, 2), d(9, 13)),
    ("tarea", "Mejora del desempeño del modelo", d(7, 2), d(8, 9)),
    ("tarea", "Interfaz dinámica (MVP, TRL 3)", d(7, 2), d(8, 19)),
    ("tarea", "Escalabilidad y gestión del proyecto", d(8, 21), d(9, 4)),
    ("tarea", "Discusión, conclusiones y bibliografía", d(9, 6), d(9, 13)),
    ("hito", "Hito: entrega del informe a la tutora", d(9, 14), None),
    ("fase", "F4 Ajustes finales", d(9, 16), d(9, 29)),
    ("hito", "Hito: entrega del proyecto integrador", d(10, 1), None),
]
MESES = ["ene.", "feb.", "mar.", "abr.", "may.", "jun.", "jul.", "ago.", "sep.", "oct.", "nov.", "dic."]


def fmt_meses(ax):
    ticks = [d(m, 1) for m in range(3, 11)]
    ax.set_xticks(ticks)
    # etiqueta en dos líneas (mes / año) para que no se superpongan
    ax.set_xticklabels([f"{MESES[m - 1]}\n2026" for m in range(3, 11)], fontsize=9.5)
    ax.set_xlim(d(2, 8), d(10, 6))


# ---------------- Figura 6.1: cronograma del plan de implementación ----------------
implementacion = [
    ("fase", "E0 Formalización y lanzamiento con el MPF", 0, 2),
    ("fase", "E1 Condiciones de salida de TRL 3", 1, 7),
    ("tarea", "Medición de la latencia de carga (R2)", 1, 5),
    ("tarea", "Verificación de reidentificación (R4)", 2, 6),
    ("tarea", "Procedimiento de validación humana (R7)", 3, 7),
    ("fase", "E2 Integración en laboratorio (TRL 4)", 6, 15),
    ("tarea", "Ingesta automatizada y API de predicción", 6, 12),
    ("tarea", "Capa de decisión de tres niveles y tablero", 9, 15),
    ("hito", "Hito: TRL 4", 15, None),
    ("fase", "E3 Validación en modo sombra (TRL 5-6)", 15, 27),
    ("tarea", "Operación en paralelo y registro de alertas", 15, 27),
    ("tarea", "Línea base de los indicadores de impacto", 15, 27),
    ("tarea", "Recalibración del umbral con el MPF", 21, 27),
    ("hito", "Hito: TRL 6", 27, None),
    ("fase", "E4 Capacitación y gestión del cambio", 22, 29),
    ("fase", "E5 Piloto operativo en la Unidad Judicial (TRL 7)", 28, 39),
    ("tarea", "Medición de los indicadores de impacto", 28, 39),
    ("hito", "Hito: TRL 7", 39, None),
    ("fase", "E6 Evaluación, transferencia y cierre", 38, 42),
    ("hito", "Hito: cierre del plan", 42, None),
]


def fmt_semanas(ax):
    ax.set_xticks(range(0, 43, 4))
    ax.set_xticks(range(0, 43, 2), minor=True)
    ax.grid(axis="x", which="minor", color="#EEEEEE", zorder=0)
    ax.set_xlim(-0.5, 43)


if __name__ == "__main__":
    dibujar(proyecto, fmt_meses, "imagenes/gantt_proyecto.png")
    dibujar(implementacion, fmt_semanas, "imagenes/gantt_implementacion.png", xlabel="Semana del plan")
    print("OK")
