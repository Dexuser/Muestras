# Mediante dos controles de tipo LabelFrame implementar la siguiente interfaz visual:

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.Labelframe(self.ventana1, text="articulo")
        self.labelframe1.grid(column=0, row=0)
        self.articulo()
        self.labelframe2=ttk.Labelframe(self.ventana1, text="Operaciones")
        self.labelframe2.grid(column=0, row=1)
        self.operaciones()
        self.ventana1.mainloop()

    def articulo(self):
        self.label1=ttk.Label(self.labelframe1, text="Codigo del articulo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Descripcion:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Precio")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.entry3=ttk.Entry(self.labelframe1)
        self.entry3.grid(column=1, row=2, padx=4, pady=5)
        
    def operaciones(self):
        self.boton1=ttk.Button(self.labelframe2, text="Alta", width=12)
        self.boton1.grid(column=0, row=0, padx=5, pady=5)
        self.boton2=ttk.Button(self.labelframe2, text="Baja", width=12)
        self.boton2.grid(column=1, row=0, padx=5, pady=5)
        self.boton3=ttk.Button(self.labelframe2, text="Modificacion", width=12)
        self.boton3.grid(column=2, row=0, padx=5, pady=5)








# bloque
ventana=Aplicacion()