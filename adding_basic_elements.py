# Importando el modulo
import tkinter as tk

# Creando la root principal

root = tk.Tk()
root.title("Mi root principal")
root.geometry("900x600")

# Añadimos un widget de tipo label

etiqueta = tk.Label(root,text = "Hola esta es mi primera ventana")
etiqueta.pack(pady = 20)

etiqueta1 = tk.Label(root, text = "Segunda etiqueta")
etiqueta1.pack(pady = 20)

etiqueta2 = tk.Label(root, text = "Tercera etiqueta")
etiqueta2.pack(pady = 20)

etiqueta3 = tk.Label(root, text = "Cuarta etiqueta")
etiqueta3.pack(pady = 20)

def cambiar_texto_etiqueta():
    etiqueta1.config(text = "Nuevo texto")

# Añadimos un boton que cierra la root principal

boton = tk.Button(root,text = "Cerrar", command=cambiar_texto_etiqueta)
boton.pack(pady = 10)

# Añadimos un caja de texto
caja_texto = tk.Text(root,height=5, width=40)
caja_texto.pack()

# Añadimos un campo input
entrada = tk.Entry(root)
entrada.pack(pady = 10)

root.mainloop()


# Con estas lineas podemos saber los metodos que tiene cada widget
#print(boton.configure().keys())
#print(dir(boton))