#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera un PDF independiente con el Anexo A.1 (Diccionario de datos de la
base original) a partir de los fuentes de la tesis.

El contenido no se duplica a mano: el preambulo se toma del .tex principal
(y de preambulo.tex) y el anexo de capitulos/anexos.tex en cada ejecucion,
de modo que el anexo suelto siempre refleja la version vigente del informe.
El .tex intermedio se regenera solo; no editarlo.

Uso:  python build_anexo_diccionario.py
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
PRINCIPAL = RAIZ / "TFI - CAMPOS - SCARAZZINI.tex"
PREAMBULO = RAIZ / "preambulo.tex"
ANEXOS = RAIZ / "capitulos" / "anexos.tex"
SALIDA_TEX = RAIZ / "anexo_diccionario_datos.tex"
SALIDA_PDF = RAIZ / "Anexo A1 - Diccionario de datos.pdf"
BUILD = RAIZ / "build"

INICIO_ANEXO = r"\section{Diccionario de datos de la base original}"
FIN_ANEXO = r"\section{Visualizaciones exploratorias complementarias}"


def recortar(texto, inicio, fin, que):
    i = texto.find(inicio)
    if i == -1:
        sys.exit(f"No se encontro el marcador de inicio de {que}: {inicio!r}")
    j = texto.find(fin, i + len(inicio))
    if j == -1:
        sys.exit(f"No se encontro el marcador de fin de {que}: {fin!r}")
    return texto[i:j].rstrip() + "\n"


def main():
    fuente = PRINCIPAL.read_text(encoding="utf-8")
    anexos = ANEXOS.read_text(encoding="utf-8")

    preambulo = recortar(fuente, r"\documentclass", r"\begin{document}", "el preambulo")
    contenido = recortar(anexos, INICIO_ANEXO, FIN_ANEXO, "el anexo del diccionario")

    # El preambulo vive en preambulo.tex: se incrusta para poder quitarle la bibliografia.
    preambulo = preambulo.replace(
        r"\input{preambulo}", PREAMBULO.read_text(encoding="utf-8").rstrip())

    # El anexo suelto no lleva bibliografia: se quita el recurso para no
    # depender de biber ni arrastrar avisos de biblatex.
    preambulo = re.sub(r"^\\addbibresource\{.*\}\s*$", "", preambulo, flags=re.M)

    cabecera = rf"""%% =====================================================================
%% ARCHIVO GENERADO AUTOMATICAMENTE -- NO EDITAR A MANO
%% Fuente:     {PRINCIPAL.name}, {PREAMBULO.name}, capitulos/{ANEXOS.name}
%% Generador:  {Path(__file__).name}
%%
%% Documento suelto con el Anexo A.1 (Diccionario de datos de la base
%% original). Reutiliza el preambulo y el texto del informe completo, de
%% modo que ambos PDF comparten estilo y numeracion (tablas A.1, A.2...).
%% =====================================================================
"""

    cuerpo = r"""
\begin{document}

\begin{titlepage}
\centering

\includegraphics[width=0.95\linewidth]{imagenes/image7.jpeg}\par
\vspace{2.5cm}

{\Large\bfseries ANEXO A.1\\[4pt] DICCIONARIO DE DATOS DE LA BASE ORIGINAL\par}
\vspace{1cm}

{\large Documento complementario del Proyecto Integrador\par}
\vspace{0.4cm}
{\large\itshape Alerta Temprana de Accidentes Viales\\ basada en Inteligencia Artificial\par}

\vfill
{\large Córdoba, Septiembre de 2026 \par}

\end{titlepage}

\setcounter{page}{1}      % la portada no se numera; el anexo arranca en 1

\appendix
\setcounter{chapter}{1}   % el capitulo de anexos es el A, igual que en el informe
\markboth{Anexos}{Anexos}

"""

    cierre = "\n" + r"\end{document}" + "\n"
    doc = cabecera + "\n" + preambulo + cuerpo + contenido + cierre
    SALIDA_TEX.write_text(doc, encoding="utf-8")
    print(f"Escrito: {SALIDA_TEX.name} ({len(contenido.splitlines())} lineas de contenido)")

    BUILD.mkdir(exist_ok=True)
    for _ in range(2):  # dos pasadas: longtable necesita la segunda para los anchos
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-file-line-error",
             f"-output-directory={BUILD}", SALIDA_TEX.name],
            cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    pdf = BUILD / (SALIDA_TEX.stem + ".pdf")
    if not pdf.exists():
        print(r.stdout[-4000:])
        sys.exit("pdflatex no genero el PDF")
    shutil.copyfile(pdf, SALIDA_PDF)
    print(f"Generado: {SALIDA_PDF.name}")


if __name__ == "__main__":
    main()
