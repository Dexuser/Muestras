# intenta hacer una calculadora

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from tkinter import scrolledtext as st
from tkinter.constants import INSERT 




class Calculadora:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("580x270")
        
        #Usare un Stringvar para poder mostrar la pantalla
        self.valor=tk.StringVar()
        self.pantalla=ttk.Entry(self.root, textvariable=self.valor, font=10, state="readonly")
        self.pantalla.grid(column=0, row=0, ipadx=50, ipady=30, sticky="n")
        # componentes
        self.botones=ttk.Labelframe(self.root)
        self.botones.grid(column=0, row=1, sticky="n")
        self.componentes()
        self.calculos()
        # historial
        self.historial = open("historial", "w")
        self.historial.close()
        self.root.mainloop()

    def calculos(self):
        self.text = st.ScrolledText(self.root, width=30, height=10)
        self.text.grid(column=1, row=0, rowspan=2, sticky="ns")


    def componentes(self):
        self.refrescar = ttk.Button(self.botones, text="C", command=self.refrescar)
        self.refrescar.grid(column=0, row=0)
        self.borrar = ttk.Button(self.botones, text="borrar", command=self.borrar)
        self.borrar.grid(column=3, row=0)


        #ultimo boton
        self.boton=ttk.Button(self.botones, text="0", command=self.agregar0)
        self.boton.grid(column=0, row=4, columnspan=3, rowspan=3, sticky="nswe")
        # tercera fila de botones
        self.boton1=ttk.Button(self.botones, text="1", command=self.agregar1)
        self.boton1.grid(column=0, row=3)
        self.boton2=ttk.Button(self.botones, text="2", command=self.agregar2)
        self.boton2.grid(column=1, row=3)
        self.boton3=ttk.Button(self.botones, text="3", command=self.agregar3)
        self.boton3.grid(column=2, row=3)
        # segunda fila de bontones
        self.boton4=ttk.Button(self.botones, text="4", command=self.agregar4)
        self.boton4.grid(column=0, row=2)
        self.boton5=ttk.Button(self.botones, text="5", command=self.agregar5)
        self.boton5.grid(column=1, row=2)
        self.boton6=ttk.Button(self.botones, text="6", command=self.agregar6)
        self.boton6.grid(column=2, row=2)
        # primera fila de botones
        self.boton7=ttk.Button(self.botones, text="7", command=self.agregar7)
        self.boton7.grid(column=0, row=1)
        self.boton8=ttk.Button(self.botones, text="8", command=self.agregar8)
        self.boton8.grid(column=1, row=1)
        self.boton9=ttk.Button(self.botones, text="9", command=self.agregar9)
        self.boton9.grid(column=2, row=1)
        # operadores 
        self.botonsuma=ttk.Button(self.botones, text="+", command=self.sumar)
        self.botonsuma.grid(column=3, row=1)
        self.botonresta=ttk.Button(self.botones, text="-", command=self.resta)
        self.botonresta.grid(column=3, row=2)
        self.botonmult=ttk.Button(self.botones, text="*", command=self.mult)
        self.botonmult.grid(column=3, row=3)
        self.botondiv=ttk.Button(self.botones, text="/", command=self.div)
        self.botondiv.grid(column=3, row=4)
        self.botonigual=ttk.Button(self.botones, text="=", command=self.operar )
        self.botonigual.grid(column=3, row=5)
    def borrar(self):
        largo = len(self.valor.get())
        aux = self.valor.get()[:largo-1]
        self.valor.set(aux)
        
    def refrescar(self):
        self.valor.set("")

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
        if self.valor.get()=="":
            ms.showerror("Error!", "aun no se ha digitado ningun digito ni operador")
        else:
            self.historial = open("historial", "a")
            self.historial.write(self.valor.get()+ " = " + str(eval(self.valor.get())) +"\n")
            self.valor.set(eval(self.valor.get()))
            self.historial.close()
            self.historial = open("historial", "r")
            contenido = self.historial.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(1.0, contenido)
            self.historial.close()
# LET'S GOOO
aplicacion=Calculadora()