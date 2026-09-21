# Script de compilación para PowerShell
# Usa la ruta corta (8.3) para evitar problemas con la tilde 'á' en Perl
$scriptPath = "C:\Users\VALENT~1\AppData\Local\Programs\MiKTeX\scripts\latexmk\latexmk.pl"
if (Test-Path $scriptPath) {
    perl $scriptPath -pdf main.tex $args
} else {
    Write-Host "Compilando con pdflatex y biber directamente..." -ForegroundColor Cyan
    pdflatex -synctex=1 -interaction=nonstopmode -shell-escape main.tex
    biber main
    pdflatex -synctex=1 -interaction=nonstopmode -shell-escape main.tex
    pdflatex -synctex=1 -interaction=nonstopmode -shell-escape main.tex
}
