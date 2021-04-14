# Realiza una combobox donde pidas que eliga una comida favorita

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Encuesta")
        self.label1=ttk.Label(self.ventana1, text="Encuesta de un dia de Comidas!" +"\n" 
        "En esta encuesta tendras que poner tu nombre y tu comida favorita", foreground="blue")
        self.label1.grid(column=0, row=0)

        self.label2=ttk.Label(self.ventana1, text="Tu nombre: ", foreground="red")
        self.label2.grid(column=0, row=1)

        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.nombre)
        self.entry1.grid(column=1, row=1)

        self.label3=ttk.Label(self.ventana1, text="Elige tu comida favorita:")
        self.label3.grid(column=0, row=2)

        self.seleccion=tk.StringVar()
        opciones=("Tacos","Lasaña","Ribeye","Pizza","Canelones","Helado","Pollo frito","Pollo hervido")
        self.combobox1=ttk.Combobox(self.ventana1,
                                    width=20,
                                    textvariable=self.seleccion,
                                    value=opciones)
        self.combobox1.grid(column=1, row=2)

        self.boton1=ttk.Button(self.ventana1, text="Ingresar datos", command=self.ingresar_datos )
        self.boton1.grid(column=0, row=3)

        self.label4=ttk.Label(self.ventana1, text="Esperamos ansiosos tu Respuesta! :D")
        self.label4.grid(column=0, row=4)
        self.ventana1.mainloop()

    def ingresar_datos(self):
        self.label4.config(text="Gracias, ahora puede cerrar esta encuesta sin ningun problema")
         


# 
ventana=Aplicacion()
