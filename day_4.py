# Día 4: Variables en Tkinter (StringVar, IntVar, etc.)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Ejemplo de StringVar, IntVar, etc")

# Crear una variable de control StringVar
texto = tk.StringVar()
valor_escala = tk.DoubleVar()

# Comenzamos con StringVar
def actualizar_etiqueta(*args):
    etiqueta.config(text = f"Has escrito: {texto.get()}")

def mostrar_valor_escala(val):
    etiqueta.config(text=f"Valor de la escala: {valor_escala.get()}")
    
# Vincular la función de actualización con la variable
texto.trace_add("write", actualizar_etiqueta)

# Crear un campo de entrada y vincularlo a la variable
entrada = tk.Entry(root, textvariable=texto)
entrada.pack(pady = 10)

# Crear una escala y vincularla a la variable DoubleVar
escala = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=valor_escala, command=mostrar_valor_escala)
escala.pack(pady=10)

# Crear una etiqueta para mostrar el texto
etiqueta = tk.Label(root, text="Texto inicial")
etiqueta.pack(pady=10)

# Crear una etiqueta para mostrar el valor de la escala
etiqueta = tk.Label(root, text="Valor de la escala: 0")
etiqueta.pack(pady=10)


root.mainloop()