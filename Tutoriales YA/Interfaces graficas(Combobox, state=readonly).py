#Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país. 
# Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        self.label1=ttk.Label(self.ventana1, text="Su nombre:")
        self.label1.grid(column=0, row=0)

        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.nombre)
        self.entry1.grid(column=1, row=0)

        self.label2=ttk.Label(self.ventana1, text="Eliga un pais:")
        self.label2.grid(column=0, row=1)

        self.seleccion=tk.StringVar()
        paises=("Republica Dominicana","España","Mexico","Cuba","Puerto rico")
        self.combobox1=ttk.Combobox(self.ventana1,
                                    width=20,
                                    textvariable=self.seleccion,
                                    value=paises,
                                    state="readonly")
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=1)

        self.boton1=ttk.Button(self.ventana1, text="Ingresar", command=self.login)
        self.boton1.grid(column=0, row=2)
        self.ventana1.mainloop()
        
    def login(self):
        self.ventana1.title("Nombre: "+self.nombre.get()+", Pais: "+self.seleccion.get())


# bloque principal

ventana=Aplicacion()
