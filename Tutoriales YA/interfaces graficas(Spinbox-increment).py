import tkinter as tk
from tkinter import ttk
from random import randint

class Aplicacion:

    def __init__(self):
        #Inicializamos 2 variables
        self.victoria=0
        self.perder=0
        #Configuramos la ventana
        self.root=tk.Tk()
        self.root.geometry("300x300")
        self.root.resizable(1,1)
        self.labelframe=ttk.LabelFrame(self.root)
        self.labelframe.grid(column=0, row=0, padx=4, pady=5)
        self.lf_componentes()
        self.labelframe2=ttk.Labelframe(self.root)
        self.labelframe2.grid(column=0,row=1, padx=4, pady=5)
        self.lf2_componentes()

        self.root.mainloop()

    def lf_componentes(self):
        self.label1=ttk.Label(self.labelframe,
        text="De que numero es multiplo el numero:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        #generador de numeros
        self.valor=tk.StringVar()
        self.valor.set(randint(1,120))
        self.entry1=ttk.Entry(self.labelframe, textvariable=self.valor, width=10)
        self.entry1.grid(column=0, row=1, padx=4, pady=5)
    
    def lf2_componentes(self):
        self.label_num=ttk.Label(self.labelframe2, text="El numero es multiplo de:")
        self.label_num.grid(column=0, row=1, padx=4, pady=4, sticky="w")
        self.numbers=ttk.Spinbox(self.labelframe2, from_=2, to=12, width=5)
        self.numbers.grid(column=1, row=1, padx=4, pady=4)
        self.boton=ttk.Button(self.labelframe2, text="Comprobar", command=self.comprobar)
        self.boton.grid(column=0, row=2, padx=4, pady=4, columnspan=2)
        self.aciertos=ttk.Label(self.labelframe2, text="Victorias:")
        self.aciertos.grid(column=0, row=3, padx=2, pady=3, sticky="w")
        self.fallos=ttk.Label(self.labelframe2, text="Fallos:")
        self.fallos.grid(column=0, row=4, padx=2, pady=3, sticky="w")

    def comprobar(self):
        if int(self.valor.get()) % int(self.numbers.get())==0:
            self.victoria+=1
            self.aciertos["text"]="Victorias:"+" "+str(self.victoria)
        else:
            self.perder+=1
            self.fallos["text"]="Fallos:"+" "+str(self.perder)
        self.valor.set(randint(1,120))
# aplicacion 
ventana=Aplicacion()