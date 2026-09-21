# Configuración de compilación para latexmk
$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -shell-escape %O %S';
$biber = 'biber %O %S';
