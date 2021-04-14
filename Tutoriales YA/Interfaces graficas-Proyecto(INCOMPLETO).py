# intenta hacer una calculadora

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("170x300")
        self.componentes()
        self.ventana1.mainloop()

    def componentes(self):
        self.constante=""
        self.ans=0
        self.mostrar_cons=ttk.Label(self.ventana1, text=self.constante)
        self.mostrar_cons.config(foreground="red", font=50)
        self.mostrar_cons.pack(anchor="nw")
        
        self.boton=ttk.Button(self.ventana1, text="0", command=self.agregar0)
        self.boton.place(x=5, y=250, width=80, height=40)
        self.boton1=ttk.Button(self.ventana1, text="1", command=self.agregar1)
        self.boton1.place(x=5, y=210, width=40, height=40)
        self.boton2=ttk.Button(self.ventana1, text="2", command=self.agregar2)
        self.boton2.place(x=45, y=210, width=40, height=40)
        self.boton3=ttk.Button(self.ventana1, text="3", command=self.agregar3)
        self.boton3.place(x=85, y=210, width=40, height=40)
        self.boton4=ttk.Button(self.ventana1, text="4", command=self.agregar4)
        self.boton4.place(x=5, y=170, width=40, height=40)
        self.boton5=ttk.Button(self.ventana1, text="5", command=self.agregar5)
        self.boton5.place(x=45, y=170, width=40, height=40)
        self.boton6=ttk.Button(self.ventana1, text="6", command=self.agregar6)
        self.boton6.place(x=85, y=170, width=40, height=40)
        self.boton7=ttk.Button(self.ventana1, text="7", command=self.agregar7)
        self.boton7.place(x=5, y=130, width=40, height=40)
        self.boton8=ttk.Button(self.ventana1, text="8", command=self.agregar8)
        self.boton8.place(x=45, y=130, width=40, height=40)
        self.boton9=ttk.Button(self.ventana1, text="9", command=self.agregar9)
        self.boton9.place(x=85, y=130, width=40, height=40)
        self.botonsuma=ttk.Button(self.ventana1, text="+", command=self.sumar)
        self.botonsuma.place(x=125, y=130, width=40, height=40)
        self.botonresta=ttk.Button(self.ventana1, text="-", command=self.resta)
        self.botonresta.place(x=125, y=170, width=40, height=40)
        self.botonmult=ttk.Button(self.ventana1, text="*",  command=self.mult)
        self.botonmult.place(x=125, y=210, width=40, height=40)
        self.botondiv=ttk.Button(self.ventana1, text="/", command=self.div)
        self.botondiv.place(x=125, y=250, width=40, height=40)
        self.botonigual=ttk.Button(self.ventana1, text="=",command=self.operar )
        self.botonigual.place(x=85, y=250, width=40, height=40)

    def agregar0(self):
        self.constante+="0"
        self.mostrar_cons["text"]=self.constante
    def agregar1(self):
        self.constante+="1"
        self.mostrar_cons["text"]=self.constante
    def agregar2(self):
        self.constante+="2"
        self.mostrar_cons["text"]=self.constante
    def agregar3(self):
        self.constante+="3"
        self.mostrar_cons["text"]=self.constante
    def agregar4(self):
        self.constante+="4"
        self.mostrar_cons["text"]=self.constante
    def agregar5(self):
        self.constante+="5"
        self.mostrar_cons["text"]=self.constante
    def agregar6(self):
        self.constante+="6"
        self.mostrar_cons["text"]=self.constante
    def agregar7(self):
        self.constante+="7"
        self.mostrar_cons["text"]=self.constante
    def agregar8(self):
        self.constante+="8"
        self.mostrar_cons["text"]=self.constante
    def agregar9(self):
        self.constante+="9"
        self.mostrar_cons["text"]=self.constante
    
    def sumar(self):
        self.constante+="+"
        self.mostrar_cons["text"]=self.constante
    def resta(self):
        self.constante+="-"
        self.mostrar_cons["text"]=self.constante
    def mult(self):
        self.constante+="*"
        self.mostrar_cons["text"]=self.constante
    def div(self):
        self.constante+=""
        self.mostrar_cons["text"]=self.constante

    def operar(self):
        resultado=0
        for i in range(len(self.constante)):
            if self.constante[i]=="+":
                self.constante=str((int(self.constante[:i]) + int(self.constante[i:])))
                self.mostrar_cons["text"]=self.constante

            

        



# A
ventana=Aplicacion()