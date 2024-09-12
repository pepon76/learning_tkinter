import tkinter as tk

root = tk.Tk()
root.geometry("500x600")
root.title("Mini aplicacion con eventos varios")

def cambiar_texto_tecla(event):
    etiqueta.config(text = f"Se ha cambiado el texto pulsando la tecla {event.keysym}" )
    
def cambiar_texto_boton():
    etiqueta.config(text = "Se ha cambiado el texto pulsando el boton" )
    
def cambiar_texto_raton(event):
    etiqueta.config(text=f"Se ha cambiado el texto pulsando el ratón\nPosición X = {event.x}\nPosición Y = {event.y}") 


boton = tk.Button(root,text = "Cambiar texto etiqueta", command=cambiar_texto_boton)
boton.pack(pady = 10)

etiqueta = tk.Label(root)
etiqueta.pack(pady = 10)
root.bind('<Return>', cambiar_texto_tecla)
root.bind('<Button-1>', cambiar_texto_raton)


root.mainloop()