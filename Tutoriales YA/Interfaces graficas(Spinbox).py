# usa spinsbox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("330x230")
        self.intro=ttk.Label(
        self.ventana1,
        text="Que tabla de multiplicar quieres generar?",
        foreground="blue")
        self.intro.grid(column=0, row=0, padx=3, pady=3)
        self.number=ttk.Spinbox(self.ventana1, from_=1, to=12, width=10, state="readonly")
        self.number.set(1)
        self.number.grid(column=1, row=0, padx=3, pady=3)
        self.btn=ttk.Button(self.ventana1, text="Generar tablas", command=self.generar)
        self.btn.grid(column=1, row=1, pady=3, sticky="n")
        self.tabla=ttk.Label(self.ventana1, text="")
        self.tabla.grid(column=0, row=1, padx=3, pady=5, sticky="W")
        self.ventana1.mainloop()
    
    def generar(self):
        aux=""
        for i in range(1,13):
            mult= int(self.number.get()) * i
            aux+= self.number.get()+" x "+str(i)+"="+str(mult)+"\n"
        self.tabla["text"]=aux
        # En aux, se toma el numero de la Spinbox Number, y se le concatena el numero con quien se le va a multiplicar 
        # y el resultado, pero antes hay que convertilos a String para concatenarlos

# aplicacion
ventana=Aplicacion()