import tkinter as tk

root = tk.Tk()
root.geometry("400x600")

# FValidar que sea un numero
def validar_digito():
    if P == "" or P.isdigit():
        True
    else:
        return False
    



# Creamos la validacion
validar_cmd = root.register(validar_digito)

# Crear una entrada de texto con validacion
caja = tk.Text(root, width=20,height=20,validate="key", validatecommand=(validar_cmd, "%P"))
caja.pack(pady=10)


root.mainloop()