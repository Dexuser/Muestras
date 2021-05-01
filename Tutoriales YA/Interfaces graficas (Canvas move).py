# Modificar el problema que desplaza un cuadrado con las teclas de flechas
# de tal modo que la figura no pueda salir del espacio definido para el Canvas.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas1 = tk.Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.cuadrado = self.canvas1.create_rectangle(100,10,150,60, fill="red")
        self.root.bind("<KeyPress>", self.mover_cuadrado)
        
        self.root.mainloop()

    def mover_cuadrado(self, evento):
        x1, y1, x2, y2 = self.canvas1.coords(self.cuadrado)
        print(x1,y1,x2,y2)
        if evento.keysym=='Right':
            if x2+4<=600:
                self.canvas1.move(self.cuadrado, 4, 0)
        if evento.keysym=='Left':
            if x1-4>=0:
                self.canvas1.move(self.cuadrado, -4, 0)
        if evento.keysym=='Down':
            if y2+4<=400:
                self.canvas1.move(self.cuadrado, 0, 4)
        if evento.keysym=='Up':
            if y1-4>=0:
                self.canvas1.move(self.cuadrado, 0, -4)

prueba= Aplicacion()