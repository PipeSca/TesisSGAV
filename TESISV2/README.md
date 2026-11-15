# TFI — Alerta Temprana de Accidentes Viales (versión corregida)

Proyecto LaTeX del trabajo final, con las correcciones del `.docx` revisado ya aplicadas
sobre la estructura original del repositorio `TesisSGAV`.

## Cómo compilar en VS Code

1. Instalar la extensión **LaTeX Workshop** (James Yu).
2. Tener una distribución completa: **TeX Live** (Linux/macOS) o **MiKTeX** (Windows).
   Paquetes usados: `lmodern`, `babel-spanish`, `biblatex` + `biber`, `siunitx`,
   `cleveref`, `enumitem`, `tabularx`, `longtable`, `booktabs`, `fancyhdr`, `xurl`.
3. Abrir **la carpeta** en VS Code (no el archivo suelto) y abrir
   `TFI - CAMPOS - SCARAZZINI.tex`.
4. `Ctrl+Alt+B` o *LaTeX Workshop: Build LaTeX project*.
   La receta configurada en `.vscode/settings.json` ya corre
   `pdflatex → biber → pdflatex → pdflatex`, necesario para la bibliografía y para que
   las referencias cruzadas queden bien numeradas.

## Estructura

- `TFI - CAMPOS - SCARAZZINI.tex` — documento principal.
- `preambulo.tex` — paquetes, estilos y macros (`\notaflot`, `\eng`, `\var`, `\xgboost`, …).
- `portada.tex`, `frontmatter/` — portada, resumen y agradecimientos.
- `capitulos/` — introducción, marco teórico, desarrollo del producto, resultados,
  conclusiones, anexos y listado de símbolos.
- `imagenes/` — figuras.
- `bibliografia.bib` — fuentes en formato BibLaTeX (estilo APA).

Ver `CAMBIOS.md` para el detalle de lo que se modificó y lo que conviene revisar.
