#Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario.

import tkinter as tk

class Aplicacion:
    
    def __init__(self):
        self.ventana1=tk.Tk()

        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=tk.Radiobutton(self.ventana1, text="Rojo", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text="Verde", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.radio3=tk.Radiobutton(self.ventana1, text="Azul", variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=2)

        self.boton1=tk.Button(self.ventana1, text="Cambiar color", command=self.cambiar_color)
        self.boton1.grid(column=0, row=3)

        self.ventana1.mainloop()
    
    def cambiar_color(self):
        if self.seleccion.get()==1:
            self.ventana1["bg"]="red"
        if self.seleccion.get()==2:
            self.ventana1["bg"]="green"
        if self.seleccion.get()==3:
            self.ventana1["bg"]="Blue"


# bloque principal

ventana=Aplicacion()
