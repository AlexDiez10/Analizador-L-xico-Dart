import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import sys
import os
from datetime import datetime
from random import randint
from analizador_lexico import lexer, errores_lexicos, buscar_columna
from analizador_sintactico import parser, errores_sintacticos

estado_analisis = 0
contenido_archivo = ""

def cargar_archivo():
    global contenido_archivo, estado_analisis
    ruta_archivo = filedialog.askopenfilename(
        title="Analizador de Dart",
        filetypes=[("Archivos de texto", "*.dart"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_archivo = archivo.read()
                texto.config(state="normal")
                texto.delete(1.0, tk.END)
                texto.insert(tk.END, contenido_archivo)
                texto.config(state="disabled")
                estado_analisis = 0  # Reiniciar estado
        except Exception as e:
            texto.config(state="normal")
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, f"Error al leer el archivo: {e}")
            texto.config(state="disabled")

def guardar_log_lexico(tokens, errores):
    random_id = randint(100, 999)
    timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"logs/lexico-{timestamp}-{random_id}.txt"
    os.makedirs("logs", exist_ok=True)

    with open(log_filename, "w", encoding="utf-8") as log_file:
        for tok in tokens:
            if isinstance(tok, str):
                log_file.write(tok)  # Escribir errores léxicos
            else:
                log_entry = f"{tok.type} ('{tok.value}') en la línea {tok.lineno}, columna {buscar_columna(contenido_archivo, tok)}\n"
                log_file.write(log_entry)
        for error in errores:
            log_file.write(f"[ERROR] {error}\n")
    print(f"Log del análisis léxico guardado en '{log_filename}'.")

def guardar_log_sintactico(codigo_dart):
    global errores_sintacticos
    errores_sintacticos.clear()  # Limpiar errores previos

    random_id = randint(100, 999)
    timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"logs/sintactico-{timestamp}-{random_id}.txt"
    os.makedirs("logs", exist_ok=True)

    with open(log_filename, "w", encoding="utf-8") as log_file:
        # Redirigir la salida estándar al archivo de log
        original_stdout = sys.stdout
        sys.stdout = log_file

        print("[INICIO] Análisis sintáctico")
        try:
            parser.parse(codigo_dart, lexer=lexer, debug=True)  # Ejecutar análisis sintáctico
        except Exception as e:
            errores_sintacticos.append(f"[ERROR] {str(e)}")
            print(f"[ERROR] {str(e)}")

        if not errores_sintacticos:
            print("[ÉXITO] El análisis sintáctico se completó sin errores.")
        print("[FIN] Análisis sintáctico")

        # Restaurar la salida estándar
        sys.stdout = original_stdout

    print(f"Log del análisis sintáctico guardado en '{log_filename}'.")
    return len(errores_sintacticos) == 0  # Retorna True si no hubo errores

def analizar():
    global estado_analisis
    if not contenido_archivo:
        messagebox.showwarning("Advertencia", "No se ha cargado ningún archivo para analizar.")
        return

    if estado_analisis == 0:
        # Análisis léxico
        errores_lexicos.clear()
        lexer.input(contenido_archivo)

        # Capturar tokens y errores
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)

        guardar_log_lexico(tokens, errores_lexicos)

        if errores_lexicos:
            cantidad_errores = len(errores_lexicos)
            mensaje_errores = "\n".join(errores_lexicos)
            messagebox.showerror(
                "Errores de Análisis Léxico",
                f"No aprobó el Análisis Léxico\n Se encontraron {cantidad_errores} errores:\n\n{mensaje_errores}"
            )
        else:
            messagebox.showinfo("Análisis Léxico Exitoso", "El archivo pasó el análisis léxico sin errores.")
            estado_analisis = 1  # Cambiar a análisis sintáctico
    elif estado_analisis == 1:
        # Análisis sintáctico
        exito = guardar_log_sintactico(contenido_archivo)
        if exito:
            messagebox.showinfo("Análisis Sintáctico/Semántico Exitoso", "El archivo pasó el análisis sintáctico sin errores.")
        else:
            cantidad_errores = len(errores_sintacticos)
            mensaje_errores = "\n".join(errores_sintacticos)
            messagebox.showerror(
                "Errores de Análisis Sintáctico",
                f"No aprobó el Análisis Sintáctico/Semántico\nSe encontraron {cantidad_errores} errores"
            )

def borrar():
    global estado_analisis, contenido_archivo
    texto.config(state="normal")
    texto.delete("1.0", tk.END)
    texto.config(state="disabled")
    contenido_archivo = ""
    estado_analisis = 0

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Archivos Dart")
ventana.geometry("800x400")

frame_principal = tk.Frame(ventana)
frame_principal.pack(fill=tk.BOTH, expand=True)

texto = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD, width=60, height=20)
texto.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
texto.config(state="disabled")

frame_botones = tk.Frame(frame_principal)
frame_botones.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

btn_cargar = tk.Button(frame_botones, text="Cargar archivo", command=cargar_archivo)
btn_cargar.pack(pady=5, fill=tk.X)

btn_borrar = tk.Button(frame_botones, text="Borrar", command=borrar)
btn_borrar.pack(pady=5, fill=tk.X)

btn_analizar = tk.Button(frame_botones, text="Analizar", command=analizar)
btn_analizar.pack(pady=5, fill=tk.X)

ventana.mainloop()
