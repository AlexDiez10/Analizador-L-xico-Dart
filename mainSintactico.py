import os
from datetime import datetime
from analizador_sintactico import parser
from analizador_lexico import lexer  # Para que el parser pueda usarlo
import sys

# Pedir datos al usuario
username = input("Ingrese el nombre de usuario de Git: ")
dart_filename = "algoritmos/" + input("Ingrese el nombre del archivo de Dart (sin extensión): ") + ".dart"

# Generar el nombre del archivo log
timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"logs/sintactico-{username}-{timestamp}.txt"

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Procesar el archivo Dart
try:
    with open(dart_filename, "r", encoding="utf-8") as file:
        codigo_dart = file.read()
except FileNotFoundError:
    print(f"Error: El archivo '{dart_filename}' no se encontró.")
    sys.exit(1)

# Abrir el archivo de log para escritura y redirigir salida estándar
with open(log_filename, "w", encoding="utf-8") as log_file:
    # Redirigir la salida estándar al archivo de log
    sys.stdout = log_file

    print("\n[INICIO] Análisis sintáctico")
    try:
        # Realizar el análisis sintáctico
        parser.parse(codigo_dart, lexer=lexer, debug=True)
    except Exception as e:
        # Guardar cualquier error ocurrido durante el análisis
        print(f"[ERROR] {str(e)}")

    print("\n[FIN] Análisis sintáctico")

# Restaurar la salida estándar
sys.stdout = sys.__stdout__

print(f"Análisis completado. Resultados guardados en '{log_filename}'.")
