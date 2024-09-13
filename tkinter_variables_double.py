import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Variables tkinter")

# Creamos la variable de tipo Double

double_var = tk.DoubleVar()
double_var.set(1.5)

# Creamos una etiqueta para mostrar el valor
etiqueta = tk.Label(root, text = "Valor decimal: 1.5")
etiqueta.pack(pady = 10)

# Creamos el slider que actualizara el valor
slider = tk.Scale(root,from_=0,to=20,resolution=0.1,orient="horizontal",variable=double_var)
slider.pack(pady = 10)

# Creamo la funcion
def actualizar_etiqueta():
    valor = double_var.get()
    etiqueta.config(text=f"Valor decimal: {valor}")
    
# Creamos el boton para actualizar la eiquete

boton = tk.Button(root,text = "Actualiza la etiqueta",command=actualizar_etiqueta)
boton.pack(pady = 10)



root.mainloop()