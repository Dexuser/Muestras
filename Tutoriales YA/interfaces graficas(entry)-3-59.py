# Confeccionar un programa que permita ingresar dos números en controles de tipo Entry,
# luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón.
import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Sumadora")

        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=5, textvariable=self.dato1)
        self.entry1.grid(column=0, row=0)

        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=5, textvariable=self.dato2)
        self.entry2.grid(column=2, row=0)

        self.label1=tk.Label(self.ventana1, text="+", foreground="blue")
        self.label1.grid(column=1, row=0)


        self.label2=tk.Label(self.ventana1, text="= Resultado", foreground="blue")
        self.label2.grid(column=3, row=0)


        self.boton1=tk.Button(self.ventana1, text="Sumar", command=self.suma_entrys ) 
        self.boton1.grid(column=1, row=1)   
        self.ventana1.mainloop()
    
    def suma_entrys(self):
        suma=int(self.dato1.get()) + int(self.dato2.get())
        self.label2["text"]="=",suma
        

# bloque principal
ventana=Aplicacion()