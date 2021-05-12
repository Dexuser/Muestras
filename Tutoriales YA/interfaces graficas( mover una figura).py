# Crear 100 cuadrados de color rojo y disponerlos en el control Canvas
# en posiciones aleatorias. Permitir desplazar con el mouse cualquiera de los cuadrados.
import tkinter as tk
from random import randint

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas1 = tk.Canvas(self.root, width=800, height=800, background="black")
        self.canvas1.grid(column=0, row=0)
        self.generar_cuadrado()
        self.canvas1.tag_bind("cuadrado", "<ButtonPress-1>",self.tomar_cuadrado)
        self.canvas1.tag_bind("cuadrado", "<Button1-Motion>", self.mover_cuadrado)
        self.cuadrado= None
        self.root.mainloop()

    def generar_cuadrado(self):
        for i in range(101):
            x = randint(40, 760)
            y = randint(40, 760)
            self.canvas1.create_rectangle(x,y,x+30,y+30, fill="red", tag="cuadrado")

    def tomar_cuadrado(self, evento):
        cuadrado = self.canvas1.find_withtag(tk.CURRENT)
        self.cuadrado = (cuadrado, evento.x, evento.y)
        print(self.cuadrado)
    
    def mover_cuadrado(self, evento):
        x, y = evento.x, evento.y
        cuadrado, x1, y1 = self.cuadrado
        self.canvas1.move(cuadrado, x - x1, y - y1)
        self.cuadrado = (cuadrado, x, y)

prueba = Aplicacion()