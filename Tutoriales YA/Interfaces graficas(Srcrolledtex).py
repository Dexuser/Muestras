# Crea interfaz visual donde hayan 2 Scrolldedtext y un entry
# en el primer scrolldedtext el usuario debe introducir un texto y en el entry
# un string, en el segundo Scrolltext debe aparecer el texto que introducio
# sin el string que introdujo

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class Aplicacion:
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Eliminador de caracteres")
        self.introduccion=st.ScrolledText(self.root, width=50, height=10)
        self.introduccion.grid(column=0, row=0, padx=5, pady=5)
        self.root_componentes()
        self.salida=st.ScrolledText(self.root, width=50, height=10)
        self.salida.grid(column=0, row=2, padx=5, pady=5)
        self.root.mainloop()

    def root_componentes(self):
        self.eliminar=ttk.Labelframe(self.root, text="Elminiar")
        self.eliminar.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.label1=ttk.Label(self.eliminar, text="Que caracter quiere elminar del texto?", foreground="blue")
        self.label1.grid(column=0, row=0, padx=3, pady=3)
        self.palabra=tk.StringVar()
        self.entry=ttk.Entry(self.eliminar, textvariable=self.palabra)
        self.entry.grid(column=1, row=0, padx=3, pady=3)
        self.boton=ttk.Button(self.eliminar, text="Eliminar", command=self.quitar_palabra)
        self.boton.grid(column=1, row=1, padx=3, pady=3)
    
    def quitar_palabra(self):
        
        aux=self.introduccion.get("1.0", tk.END)
        nuevo_texto=""
        for i in aux:
            if i==self.palabra.get():
                continue
            nuevo_texto+=i
        self.salida.delete("1.0", tk.END)
        self.salida.insert("1.0", nuevo_texto)


# Prueba
ventana=Aplicacion()