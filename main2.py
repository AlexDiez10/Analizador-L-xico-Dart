import os
from datetime import datetime
import ply.yacc as yacc
from analizador_sintactico import *

username = input("Ingrese el nombre de usuario de Git: ")
dart_filename = "algoritmos/" + (input("Ingrese el nombre del archivo de Dart: ")) + ".dart"

timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"logs/sintactico-{username}-{timestamp}.txt"

os.makedirs("logs", exist_ok=True)

parser = yacc.yacc()

try:
    with open(dart_filename, "r", encoding="utf-8") as file:
        codigo_dart = file.read()
        try:
            parser.parse(codigo_dart)
            print("Análisis sintáctico completado sin errores.")
        except Exception as e:
            error_msg = f"Error sintáctico: {str(e)}"
            print(error_msg)
except FileNotFoundError:
    print(f"Error: El archivo '{dart_filename}' no se encontró.")
