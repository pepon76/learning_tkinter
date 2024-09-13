import tkinter as tk

root = tk.Tk()
root.geometry("500x900")
root.title("Mini app")

def imprimir_texto_caja():
    texto = caja_texto.get("1.0", tk.END)
    etiqueta_2.config(text = f"EL texto a imprimir es el siguiente : {texto}")
    

etiqueta = tk.Label(root, text = "Formulario para el ingreso de datos")
etiqueta_caja = tk.Label(root, text = "Inserte el texto a mostrar")
etiqueta.pack(pady = 20)
etiqueta_caja.pack()
caja_texto = tk.Text(root,height=5,width=20)
caja_texto.pack()



boton = tk.Button(root,text = "Pulsar para imprimir",command=imprimir_texto_caja )
boton.pack(pady = 10)

etiqueta_2 = tk.Label(root)
etiqueta_2.pack()

# Realizo un cambio



root.mainloop()