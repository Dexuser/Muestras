# Mediante dos controles de tipo Entry permitir el ingreso de dos números.
# Crear un menú que contenga una opción que cambie el tamaño de la ventana con los valores ingresados por teclado. 
# Finalmente disponer otra opción que finalice el programa

import tkinter as tk
from tkinter import ttk
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        self.label1=ttk.Label(self.ventana1, text="Primer valor: ")
        self.label1.grid(column=0, row= 3)

        self.valor1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, textvariable=self.valor1, width=20)
        self.entry1.grid(column=1, row=3)

        self.label2=ttk.Label(self.ventana1, text="Segundo valor:")
        self.label2.grid(column=0, row=4)

        self.valor2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, textvariable=self.valor2, width=20)
        self.entry2.grid(column=1, row=4)

    

        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="elegir forma", command=self.forma)
        menubar1.add_cascade(label="Tamaño", menu=opciones1)
        opciones2=tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Finalizar", command=self.salir)
        menubar1.add_cascade(label="Salir del programa", menu=opciones2)


        


        self.ventana1.mainloop()
    
    def forma(self):
        self.ventana1.geometry(self.valor1.get()+"x"+self.valor2.get())
        
    def salir(self):
        sys.exit(0)


# aplicacion
ventana=Aplicacion()