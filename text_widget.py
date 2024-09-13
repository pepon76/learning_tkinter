import tkinter as tk

root = tk.Tk()
root.geometry("400x600")

# Funcion
def actualizar_etiqueta():
    valor = caja.get("1.0",tk.END)
    etiqueta.config(text =f"{valor}")


# Crear una entrada de texto
caja = tk.Text(root, width=20,height=20)
caja.pack(pady=10)

# Crear una etiqueta para mostrar el texto ingresado
etiqueta = tk.Label(root, text = "Texto incial de la etiqueta")
etiqueta.pack(pady = 10)

# Crear un botón para mostrar el texto ingresado
boton = tk.Button(root,text = "Actualizar etiqueta",command=actualizar_etiqueta)
boton.pack()
root.mainloop()