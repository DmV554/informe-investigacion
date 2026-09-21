@echo off
rem Modo continuo: vigila cambios y recompila automaticamente al guardar
perl "C:\Users\VALENT~1\AppData\Local\Programs\MiKTeX\scripts\latexmk\latexmk.pl" -pdf -pvc main.tex
