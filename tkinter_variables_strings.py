import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Variables tkinter")

# Creamos la variable de tipo string y le configuramos su valor inicial
texto_var = tk.StringVar()
texto_var.set("Hola este es el texto incial")

# Creamos un label que mostrara el valor del texto_var

etiqueta = tk.Label(root,textvariable=texto_var, font=("Helvetica",14))
etiqueta.pack(pady = 10)

# Creamos la caja de texto para insertar el texto que euremos que se muestre y actualice a tiempo real

entrada = tk.Entry(root,textvariable=texto_var,font=("Helvetica", 14), width=25)
entrada.pack(pady = 10)



root.mainloop()