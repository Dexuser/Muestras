#Disponer varios objetos de la clase Checkbutton con nombres de navegadores web.
#el título de la ventana mostrar todos los nombres de navegadores seleccionados.

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text="Google", variable=self.seleccion1, command=self.mostrar)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1, text="Opera", variable=self.seleccion2, command=self.mostrar) 
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1, text="Firefox", variable=self.seleccion3, command=self.mostrar)
        self.check3.grid(column=0, row=2)
        self.ventana1.mainloop()

    def mostrar(self):
        navegadores=""
        if self.seleccion1.get()==1:
           navegadores+="Google,"
        if self.seleccion2.get()==1:
            navegadores+="Opera,"
        if self.seleccion3.get()==1:
            navegadores+="Firefox,"
        self.ventana1.title(navegadores)

    
 


    


# Bloque principal
ventana=Aplicacion()
