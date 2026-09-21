# Configuración de latexmk para el informe TI-05.
# La usa VS Code (LaTeX Workshop) y la línea de comandos: `latexmk main.tex`.
# Equivale a lo que hace Overleaf: pdflatex con -shell-escape (minted) y biber.

$pdf_mode = 1;                       # pdflatex -> PDF directo
$pdflatex = 'pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$bibtex_use = 2;                     # ejecutar el gestor de bibliografía y limpiar .bbl con -C
$biber = 'biber %O %S';              # la clase inf-pucv usa biblatex con backend biber
$clean_ext = 'bbl bcf run.xml synctex.gz xmpi fls fdb_latexmk _minted-%R';
$out_dir = '.';
