#Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer",
# al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.
import tkinter as tk

class Genero:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=tk.Button(self.ventana1, text="Varon", command=self.varon)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.mujer)
        self.boton2.grid(column=1, row=0)
        self.ventana1.mainloop()
    
    def varon(self):
        self.ventana1.title("Varon")
    
    def mujer(self):
        self.ventana1.title("Mujer")

# bloque principal
ventana=Genero()