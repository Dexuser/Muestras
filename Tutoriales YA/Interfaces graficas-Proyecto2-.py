import tkinter as tk
import sys
class Contrato:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Contrato")
        self.ventana1["bg"]="MistyRose2"

        self.label1=tk.Label(self.ventana1, text="LEA ESTE TEXTO", foreground="red")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="Al yo firmar este contrato, yo"\
            " Bryan Ureña Perdomo, afirmo que soy Pto, y ser un wey que nada mas le gusta"\
            " Antojar en Skullgirls.")
        self.label2.grid(column=0, row=1)

        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.radio1=tk.Radiobutton(self.ventana1, text="Si", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=2)
        self.radio2=tk.Radiobutton(self.ventana1, text="Si", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=3)

        self.boton1=tk.Button(self.ventana1, text="Aceptar", foreground="red", command=self.final)
        self.boton1.grid(column=0, row=4)
        self.ventana1.mainloop()

    def final(self):
        self.ventana1.title("Eres puto ahora")
        sys.exit(0)
        
# bloque principal
Alguien=Contrato()