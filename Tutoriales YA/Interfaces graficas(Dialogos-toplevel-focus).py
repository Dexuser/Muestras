# Crea una ventana con un menu, con un dialogo de login, y un dialogo de redimensionar la ventana 
import tkinter as tk
from tkinter import ttk

class dialogos:
    
    def __init__(self, root):
        self.dialogo=tk.Toplevel(root)
        self.label1=ttk.Label(self.dialogo, text="")
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.valor=tk.StringVar()
        self.entry=ttk.Entry(self.dialogo, textvariable=self.valor, width=10)
        self.entry.grid(column=1, row=0, padx=5, pady=5)
        self.entry.focus()
        self.label2=ttk.Label(self.dialogo, text="")
        self.label2.grid(column=0, row=1, padx=5, pady=5)
        self.valor2=tk.StringVar()
        self.entry2=ttk.Entry(self.dialogo, textvariable=self.valor2, width=10)
        self.btn1=ttk.Button(self.dialogo, text="", )
        self.btn1.grid(column=1, row=2, padx=5, pady=5)
        self.entry2.grid(column=1, row=1)
        self.dialogo.grab_set()
        

    def valores(self):
        return (self.valor.get(), self.valor2.get())

    def salir(self):
        self.dialogo.destroy()

# Aplicacion

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("300x300")
        self.menu()
        self.ventana1.mainloop()
    
    def menu(self):
        self.menubar=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar)
        self.opc1=tk.Menu(self.menubar, tearoff=0)
        self.opc1.add_command(label="Login", command=self.login)
        self.opc1.add_command(label="Redimension", command=self.dimension)
        self.menubar.add_cascade(label="Opciones", menu=self.opc1)
    
    def login(self):
        self.dialogo_login=dialogos(self.ventana1)
        self.dialogo_login.label1["text"]="Su nombre"
        self.dialogo_login.label2["text"]="Ingrese su clave"
        self.dialogo_login.entry2.config(show="*")
        self.dialogo_login.btn1.config(text="Ingresar", command=self.entrar)


    def dimension(self):
        self.dialogo_size=dialogos(self.ventana1)
        self.dialogo_size.label1["text"]="Ingrese el ancho:"
        self.dialogo_size.label2["text"]="Ingrese el alto:"
        self.dialogo_size.btn1.config(text="redimensionar", command=self.tamano)

    
    def entrar(self):
        self.ventana1.title(self.dialogo_login.valores()[0])
        self.dialogo_login.salir()
    
    def tamano(self):
        self.ventana1.geometry(self.dialogo_size.valores()[0]+"x"+self.dialogo_size.valores()[1])


ventana1=Aplicacion()


