# programa para escribir a mano alzada

import tkinter as tk 

class Aplicacion:
    
    def __init__(self):
        self.root=tk.Tk()
        self.canvas1=tk.Canvas(self.root, width=600, height=400, background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind("<ButtonPress-1>", self.presionar)
        self.canvas1.bind("<Motion>", self.trazo)
        self.canvas1.bind("<ButtonRelease-1>", self.soltar)
        self.presion= False
        self.root.mainloop()
    
    def presionar(self, evento):
        self.presion=True
        self.origenx= evento.x
        self.origeny= evento.y

    def trazo(self, evento):
        if self.presion:
            self.canvas1.create_line(self.origenx, self.origeny, evento.x, evento.y, fill="red")
            self.origenx= evento.x
            self.origeny= evento.y
    
    def soltar(self, evento):
        self.presion=False



ventana= Aplicacion()
