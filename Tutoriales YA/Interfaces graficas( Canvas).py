# Implementar un grafico estadistico de tipo barra porcentual

import tkinter as tk
from tkinter import ttk

class Grafico:
    def __init__(self):
        self.root=tk.Tk()
        self.labelframe1=ttk.Labelframe(self.root, text="Partidos politicos")
        self.labelframe1.grid(column=0, row=0, padx=3, pady=3, sticky="w")
        self.lf_entradadatos()
        self.canvas=tk.Canvas(self.root, width=600, height=400, background="salmon")
        self.canvas.grid(column=0, row=1)
        self.root.mainloop()

    def lf_entradadatos(self):
        self.label1=ttk.Label(self.labelframe1, text="Partido A:")
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=3, pady=3)
        self.label2=ttk.Label(self.labelframe1, text="Partido B:")
        self.label2.grid(column=0, row=1, padx=3, pady=3)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=3, pady=3)
        self.label3=ttk.Label(self.labelframe1, text="Partido C:")
        self.label3.grid(column=0, row=2, padx=3, pady=3)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=3, pady=3)
        self.boton1=ttk.Button(self.labelframe1, text="Generar grafico", command=self.barras_porcentuales)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=3, pady=3,sticky="we")

    def barras_porcentuales(self):
        self.canvas.delete(tk.ALL)
        datos1= int(self.dato1.get())
        datos2= int(self.dato2.get())
        datos3= int(self.dato3.get())
        suma= datos1+datos2+datos3
        porcentaje1= datos1/suma*100
        porcentaje2= datos2/suma*100
        porcentaje3= datos3/suma*100
        longitud1= datos1*500/suma  
        longitud2= datos2*500/suma
        longitud3= datos3*500/suma
        self.canvas.create_rectangle(10,170,10+longitud1,230, fill="red")
        self.canvas.create_text(50, 190, text="{0:.2f}%".format(porcentaje1), font="Arial", fill="white")
        self.canvas.create_rectangle(10+longitud1,170,10+longitud1+longitud2,230, fill="green")
        self.canvas.create_text(50+longitud1,190, text="{0:.2f}%".format(porcentaje2), font="Arial", fill="white")
        self.canvas.create_rectangle(10+longitud1+longitud2,170,10+longitud1+longitud2+longitud3,230, fill="blue")
        self.canvas.create_text(50+longitud1+longitud2,190, text="{0:.2f}%".format(porcentaje3), font="Arial", fill="white")
        
ventana=Grafico()