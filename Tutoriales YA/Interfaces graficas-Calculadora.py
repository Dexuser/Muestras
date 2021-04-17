# intenta hacer una calculadora

import tkinter as tk
from tkinter import ttk

class Calculadora:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("310x270")
        #Usare un Stringvar para poder mostrar la pantalla
        self.valor=tk.StringVar()

        self.pantalla=ttk.Entry(self.root, textvariable=self.valor, font=10, state="readonly")
        self.pantalla.grid(column=0, row=0, ipadx=50, ipady=30)

        self.botones=ttk.Labelframe(self.root)
        self.botones.grid(column=0, row=1)
        self.componentes()
        self.root.mainloop()
    
    def componentes(self):
        self.boton=ttk.Button(self.botones, text="0", command=self.agregar0)
        self.boton.grid(column=0, row=3, columnspan=3, rowspan=3, sticky="nswe")

        self.boton1=ttk.Button(self.botones, text="1", command=self.agregar1)
        self.boton1.grid(column=0, row=2)
        self.boton2=ttk.Button(self.botones, text="2", command=self.agregar2)
        self.boton2.grid(column=1, row=2)
        self.boton3=ttk.Button(self.botones, text="3", command=self.agregar3)
        self.boton3.grid(column=2, row=2)

        self.boton4=ttk.Button(self.botones, text="4", command=self.agregar4)
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.botones, text="5", command=self.agregar5)
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.botones, text="6", command=self.agregar6)
        self.boton6.grid(column=2, row=1)

        self.boton7=ttk.Button(self.botones, text="7", command=self.agregar7)
        self.boton7.grid(column=0, row=0)
        self.boton8=ttk.Button(self.botones, text="8", command=self.agregar8)
        self.boton8.grid(column=1, row=0)
        self.boton9=ttk.Button(self.botones, text="9", command=self.agregar9)
        self.boton9.grid(column=2, row=0)

        self.botonsuma=ttk.Button(self.botones, text="+", command=self.sumar)
        self.botonsuma.grid(column=3, row=0)
        self.botonresta=ttk.Button(self.botones, text="-", command=self.resta)
        self.botonresta.grid(column=3, row=1)
        self.botonmult=ttk.Button(self.botones, text="*", command=self.mult)
        self.botonmult.grid(column=3, row=2)
        self.botondiv=ttk.Button(self.botones, text="/", command=self.div)
        self.botondiv.grid(column=3, row=3)
        self.botonigual=ttk.Button(self.botones, text="=", command=self.operar )
        self.botonigual.grid(column=3, row=4)

    def agregar0(self):
        aux=self.valor.get()
        aux+="0"
        self.valor.set(aux)

    def agregar1(self):
        aux=self.valor.get()
        aux+="1"
        self.valor.set(aux)

    def agregar2(self):
        aux=self.valor.get()
        aux+="2"

        self.valor.set(aux)

    def agregar3(self):
        aux=self.valor.get()
        aux+="3"
        self.valor.set(aux)

    def agregar4(self):
        aux=self.valor.get()
        aux+="4"
        self.valor.set(aux)

    def agregar5(self):
        aux=self.valor.get()
        aux+="5"
        self.valor.set(aux)

    def agregar6(self):
        aux=self.valor.get()
        aux+="6"
        self.valor.set(aux)

    def agregar7(self):
        aux=self.valor.get()
        aux+="7"
        self.valor.set(aux)

    def agregar8(self):
        aux=self.valor.get()
        aux+="8"
        self.valor.set(aux)

    def agregar9(self):
        aux=self.valor.get()
        aux+="9"
        self.valor.set(aux)
    
    def sumar(self):
        aux=self.valor.get()
        aux+="+"
        self.valor.set(aux)

    def resta(self):
        aux=self.valor.get()
        aux+="-"
        self.valor.set(aux)

    def mult(self):
        aux=self.valor.get()
        aux+="*"
        self.valor.set(aux)
    
    def div(self):
        aux=self.valor.get()
        aux+="/"
        self.valor.set(aux)
    
    def operar(self):
        self.valor.set(eval(self.valor.get()))

# LET'S GOOO
aplicacion=Calculadora()