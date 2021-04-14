# usa el Layout manager Grid

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.prueba_grid()
        self.ventana1.mainloop()
    
    def prueba_grid(self):
        self.boton1=ttk.Button(self.ventana1, text="Boton1")
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana1, text="Boton2")
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.ventana1, text="Boton3")
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns")
        self.boton4=ttk.Button(self.ventana1, text="boton4")
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.ventana1, text="Boton5")
        self.boton5.grid(column=1, row=1)

ventana=Aplicacion()