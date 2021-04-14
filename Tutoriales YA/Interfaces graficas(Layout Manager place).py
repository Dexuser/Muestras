# usa el layout Manager place

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("400x400")
        self.ventana1.resizable(0,0)
        self.prueba_place()
        self.ventana1.mainloop()
    
    def prueba_place(self):
        self.boton1=ttk.Button(self.ventana1, text="Boton1")
        self.boton1.place(x=300, y=350, width=90, height=30)
        self.boton2=ttk.Button(self.ventana1, text="Boton2")
        self.boton2.place(x=200, y=350, width=90, height=30)
        self.label1=ttk.Label(self.ventana1, text="El buen label", foreground="red")
        self.label1.place(x=20, y=20)

ventana= Aplicacion()