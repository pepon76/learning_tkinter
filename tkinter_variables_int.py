import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Variables tkinter")

def actualizar_label():
    valor = numero_var.get()
    etiqueta.config(text=f"Valor actual: {valor}")
    
# Creamos la variable Intvar

numero_var = tk.IntVar()
numero_var.set(0)

#Creamos una etiqueta que se actuializara con el valor de IntVar

etiqueta = tk.Label(root,text="Valor actual : 0")
etiqueta.pack(pady=10)

# Creamos un spinbox cuadro de seleccion

spin = tk.Spinbox(root, from_=0, to=100, textvariable = numero_var)
spin.pack(pady = 10)

# Creamos un boton que al hacer click actualizara el label

boton = tk.Button(root,text= "Actualizar label", command=actualizar_label)
boton.pack(pady = 10)


root.mainloop()