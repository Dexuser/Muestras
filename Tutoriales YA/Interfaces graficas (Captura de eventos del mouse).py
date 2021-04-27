# usa la captura de eventos del mouse

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.root=tk.Tk()
        self.canvas=tk.Canvas(self.root, width=600, height=400, background="black")
        self.canvas.bind("<Motion>", self.movimiento)
        self.canvas.bind("<Button-1>", self.presicion_mouse)
        self.canvas.grid(column=0, row=0)
        self.root.mainloop()
    
    def movimiento(self, eventos):
        self.root.title(str(eventos.x)+","+str(eventos.y))
    
    def presicion_mouse(self, eventos):
        self.canvas.create_rectangle(eventos.x-5, eventos.y-5, eventos.x+5, eventos.y+5, fill="red")



ventana=Aplicacion()