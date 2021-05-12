#Disponer un botón y mostrar al azar una de las tres cartas del problema anterior. 
#Cada vez que se presione el botón generar un valor aleatorio y a partir de dicho valor mostrar una carta.

import tkinter as tk
from random import randint

# Deberias intentar cambiar carta1.png o las otras imagenes
# por alguna que tengas para que funcione este codigo

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.boton1 = tk.Button(self.root, text="Mostrar carta aleatoria", command=self.mostrar_carta)
        self.boton1.grid(column=0, row=0)
        self.canvas1 = tk.Canvas(self.root, width=300, height=400, background="black")
        self.canvas1.grid(column=0, row=1)
        self.carta1 = tk.PhotoImage(file="carta1.png")
        self.carta2 = tk.PhotoImage(file="carta2.png")
        self.carta3 = tk.PhotoImage(file="carta3.png")
        self.root.mainloop()
    
    def mostrar_carta(self):
        self.canvas1.delete(tk.ALL)
        number=randint(1,3)
        if number == 1:
            self.canvas1.create_image(50, 50, image=self.carta1, anchor="nw")
        elif number == 2:
            self.canvas1.create_image(50,50, image=self.carta2, anchor="nw")
        elif number == 3:
            self.canvas1.create_image(50,50, image=self.carta3, anchor="nw")

prueba= Aplicacion()