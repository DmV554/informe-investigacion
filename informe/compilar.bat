@echo off
rem Script de compilacion para CMD o doble clic
perl "C:\Users\VALENT~1\AppData\Local\Programs\MiKTeX\scripts\latexmk\latexmk.pl" -pdf main.tex %*
