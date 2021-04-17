
import tkinter as tk
import tkinter as tk
from random import randint



class Novia:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("300x300")
        self.label1=tk.Label(self.ventana1, text="Quieres ser mi novia", foreground="red")
        self.label1.grid(column=2, row=0)

        self.boton1=tk.Button(self.ventana1, text="Si", command=self.acepto)
        self.boton1.grid(column=0, row=1)
        self.boton2=tk.Button(self.ventana1, text="No", command=self.plan_B)
        self.boton2.grid(column=1, row=1)
        self.ventana1.mainloop()


    def acepto(self):
        self.label1["text"]="SIII, Sabia que me querias"

    def plan_B(self):
        num1=randint(1,5)
        num2=randint(1,5)
        self.boton2.grid(column=num1, row=num2)





# bloque principal
ventana=Novia()