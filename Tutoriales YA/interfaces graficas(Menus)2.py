# hacer un programa que tenga un menu con nombre ventana, que tenga las opcion cambiar tamaño y una opcion llamada colores
# que tenga un submenu que tenga los colores.

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        # Primer menu de opciones
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.rojo, accelerator="Ctrl+R")
        opciones1.add_command(label="Azul", command=self.azul, accelerator="Ctrl+A")
        opciones1.add_command(label="Verde", command=self.verde, accelerator="Ctrl+V")
        opciones1.add_separator()
        #Submenu
        submenu1=tk.Menu(menubar1)
        submenu1.add_command(label="Rosa", command=self.pink, accelerator="Ctrl+P")
        submenu1.add_command(label="Salmon", command=self.salmon, accelerator="Ctrl+S")
        opciones1.add_cascade(label="Mas colores", menu=submenu1)
        self.ventana1.bind_all("<Control-r>", self.shortcut)
        self.ventana1.bind_all("<Control-a>", self.shortcut)
        self.ventana1.bind_all("<Control-v>", self.shortcut)
        self.ventana1.bind_all("<Control-p>", self.shortcut)
        self.ventana1.bind_all("<Control-s>", self.shortcut)
        menubar1.add_cascade(label="Customizar", menu=opciones1)
        # Segundo menu
        opciones2=tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="redimensionar", command=self.dimension, accelerator="Ctrl+D")
        self.ventana1.bind_all("<Control-d>", self.shortcut)
        menubar1.add_cascade(label="Ventana", menu=opciones2)



        # Ingreso del primer valor
        self.label1=ttk.Label(self.ventana1, text="valor X:")
        self.label1.grid(column=0, row=0)
        self.valor1=tk.StringVar()
        self.entry=ttk.Entry(self.ventana1, textvariable=self.valor1)
        self.entry.grid(column=1, row=0)

        # Ingreso del segundo valor
        self.label2=ttk.Label(self.ventana1, text="Valor Y:")
        self.label2.grid(column=0, row=1)
        self.valor2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, textvariable=self.valor2)
        self.entry2.grid(column=1, row=1)

        self.ventana1.mainloop()

    # teclas rapidas
    def shortcut(self, event):
        if event.keysym=="r":
            self.rojo()
        if event.keysym=="a":
            self.azul()
        if event.keysym=="v":
            self.verde()
        if event.keysym=="d":
            self.dimension()
        if event.keysym=="p":
            self.pink()
        if event.keysym=="s":
            self.salmon()
    # metodos
    def rojo(self):
        self.ventana1["bg"]="red"
    def azul(self):
        self.ventana1["bg"]="blue"
    def verde(self):
        self.ventana1["bg"]="green"
    def pink(self):
        self.ventana1["bg"]="pink"
    def salmon(self):
        self.ventana1["bg"]="salmon"
    def dimension(self):
        self.ventana1.geometry(self.valor1.get()+"x"+self.valor2.get())
    


# Aplicacion
ventana=Aplicacion()