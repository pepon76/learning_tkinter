import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Variables tkinter")

def mostrar_estado():
    valor = "Activado" if boolean_var.get() else "Desactivado"
    etiqueta.config(text =f"El estado del chesk es: {valor}")
    
def cambiar_color():
    color = entrada.get()
    root.config(bg =f"{color}")
    
# Creamos la variable booleana y la inicializamos en False
    
boolean_var = tk.BooleanVar(root)
boolean_var.set(False)

# Creamos el checkbox

check = tk.Checkbutton(root,text="opcion", variable=boolean_var)
check.pack()

# Etique que muestra el estado del check

etiqueta = tk.Label(root, text = "Estado: Desactivado")
etiqueta.pack(pady = 10)

#Boton para actualizar el texto de la etiuqeta segun el estado del boton

boton = tk.Button(root,text="Actualizar estado",command=mostrar_estado)
boton.pack()
boton2 = tk.Button(root,text="Actualizar color",command=cambiar_color)
boton2.pack()

# Caja de texto para introducir un valor
entrada = tk.Entry(root,width= 50)
entrada.pack(pady = 10)





root.mainloop()