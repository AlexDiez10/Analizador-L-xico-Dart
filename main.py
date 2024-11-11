import os
from datetime import datetime
from analizador_lexico import lexer, buscar_columna

username = input("Ingrese el nombre de usuario de Git: ")
dart_filename = "algoritmos/"+(input("Ingrese el nombre del archivo de Dart: "))+".dart"

# Generar el nombre del archivo log
timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"logs/lexico-{username}-{timestamp}.txt"

# Abrir archivo de log
os.makedirs("logs", exist_ok=True)

def find_column(input_data, token):
    line_start = input_data.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

with open(log_filename, "w") as log_file:
    # Leer el código Dart del archivo
    try:
        with open(dart_filename, "r", encoding="utf-8") as file:
            codigo_dart = file.read()
            lexer.input(codigo_dart)
            
            while True:
                tok = lexer.token()
                if not tok:
                    break
                # Verificar si hay un error y escribirlo en el archivo log
                if isinstance(tok, str):  # Si `tok` es un mensaje de error devuelto por t_error
                    log_file.write(tok)  # Escribir mensaje de error
                else:
                    # Registrar token válido en el log
                    log_entry = f"{tok.type} ('{tok.value}') en la línea {tok.lineno}, columna {buscar_columna(codigo_dart, tok)}\n"
                    log_file.write(log_entry)
                    print(log_entry)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{dart_filename}' no se encontró.")
