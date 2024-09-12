import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Ejemplo de botón")

# Eventos con argumentos

def boton_accion_con_argumento(mensaje):
    print(f"El mensaje es: {mensaje}")
    
boton = tk.Button(root,text = "Presionar con argumento",
                  command=lambda: boton_accion_con_argumento("Hola !"))
boton.pack(pady = 20)

# Manejo de eventos de teclado

def presionar_tecla(event):
    print(f"Tecla presionada: {event.keysym}")
    
# Enlazamos la tecla enter a el evento

root.bind('<Return>', presionar_tecla)

# Manejo de eventos de raton

def click_raton(event):
    print(f"Click en posicion: ({event.x},{event.y})")

# Enlazar el click del raton a el evento

root.bind('<Button-1>', click_raton)



root.mainloop()