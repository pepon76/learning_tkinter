import tkinter as tk

# Creando la root principal
root = tk.Tk()
root.title("Mini calculadora")
root.geometry("900x600")

def sumar():
    resultado = float(entrada_1.get()) + float(entrada_2.get())
    salida.config(text=f"{resultado}")
    
def restar():
    resultado = float(entrada_1.get()) - float(entrada_2.get())
    salida.config(text=f"{resultado}")

primer_termino = tk.Label(root,text="PRIMER TERMINO")
primer_termino.grid(row=0,column=0)
entrada_1 = tk.Entry(root,width=20)
entrada_1.grid(row=0,column=1)

segundo_termino = tk.Label(root,text="SEGUNDO TERMINO")
segundo_termino.grid(row=1,column=0)
entrada_2 = tk.Entry(root,width=20)
entrada_2.grid(row=1,column=1)

# Creamo ahora los botones

boton_sumar = tk.Button(root,text = "Sumar",width=15, command=sumar)
boton_sumar.grid(row=2,column=0)
boton_restar =tk.Button(root,text = "Restar",width=15, command=restar)
boton_restar.grid(row=2,column=1)

# Creamos un nuevo entry con el resultado
Solucion = tk.Label(root,text="SOLUCION")
Solucion.grid(row=3,column=0)
salida = tk.Label(root,width=20, text="f{resultado}" )
salida.grid(row=3,column=1)













root.mainloop()