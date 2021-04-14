# utiliza el message Box
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Pruebas de messageboxs")
        self.ventana1.geometry("350x210")
        self.login=ttk.Labelframe(self.ventana1, text="Calculadora")
        self.login.grid(column=0, row=0, padx=5, pady=5)
        self.componentes_login()
        self.menu()
        self.calculo=ttk.LabelFrame(self.ventana1, text="Operadores")
        self.calculo.grid(column=0, row=1, padx=5, pady=5)
        self.operaciones()
        self.ventana1.mainloop()

    def componentes_login(self):
        self.login_label1=ttk.Label(self.login, text="primer valor:")
        self.login_label1.grid(column=0, row=0, padx=4, pady=4)
        self.valor1=tk.StringVar()
        self.login_Entry1=ttk.Entry(self.login, textvariable=self.valor1)
        self.login_Entry1.grid(column=1, row=0, padx=4, pady=4, sticky="we")
        self.login_label2=ttk.Label(self.login, text="Segundo valor:")
        self.login_label2.grid(column=0, row=1, padx=4, pady=4)
        self.valor2=tk.StringVar()
        self.login_entry2=ttk.Entry(self.login, textvariable=self.valor2)
        self.login_entry2.grid(column=1, row=1, padx=4, pady=4, sticky="we")
        self.login_label3=ttk.Label(self.login, text="El resultado es igual a:", foreground="blue")
        self.login_label3.grid(column=0, row=2, padx=4, pady=4)
        self.exitboton=ttk.Button(self.ventana1, text="Salir del programa", command=self.salir)
        self.exitboton.grid(column=0, row=3)
    
    def menu(self):
        self.menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1=tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Guia para el usuario", command=self.guia)
        self.opciones1.add_command(label="Acerca de...", command=self.acerca_de)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)
    
    def operaciones(self):
        self.sumaboton=ttk.Button(self.calculo, text="Sumar", command=self.sumar)
        self.sumaboton.grid(column=0, row=0, padx=4, pady=5)
        self.restaboton=ttk.Button(self.calculo, text="Restar", command=self.resta)
        self.restaboton.grid(column=1, row=0, padx=4, pady=4)
        self.multboton=ttk.Button(self.calculo, text="Multiplicar", command=self.multiplicar)
        self.multboton.grid(column=2, row=0, padx=4, pady=4)
        self.divboton=ttk.Button(self.calculo, text="Dividir", command=self.division)
        self.divboton.grid(column=3, row=0, padx=4, pady=4)

    def salir(self):
        preg=mb.askyesno("Salir del programa", "Esta seguro de que quiere cerrar este programa?")
        if preg==True:
            sys.exit(0)

    
    def sumar(self):
        if self.valor1.get()=="" or self.valor2.get()=="":
            mb.showerror("Error!!", "No puedes dejar ninguna de las barras de entradas vacias")
        else:
            resultado= str( int(self.valor1.get()) + int(self.valor2.get()) )
            self.login_label3["text"]="El resutado es igual a "+ resultado

    def resta(self):
        if self.valor1.get()=="" or self.valor2.get()=="":
            mb.showerror("Error!!", "No puedes dejar ninguna de las barras de entradas vacias")
        else:
            resultado= str( int(self.valor1.get()) - int(self.valor2.get()) )
            self.login_label3["text"]="El resultado es igual a "+ resultado

    def multiplicar(self):
        if self.valor1.get()=="" or self.valor2.get()=="":
            mb.showerror("Error!!", "No puedes dejar ninguna de las barras de entradas vacias")
        else:
            resultado= str( int(self.valor1.get()) * int(self.valor2.get()) )
            self.login_label3["text"]="El resultado es igual a "+ resultado

    def division(self):
        if self.valor1.get()=="" or self.valor2.get()=="":
            mb.showerror("Error!!", "No puedes dejar ninguna de las barras de entradas vacias")
        else:
            resultado= str( int(self.valor1.get()) // int(self.valor2.get()) )
            self.login_label3["text"]="El resultado es igual a "+ resultado

    def guia(self):
        mb.showinfo("Tutorial", "Despues de haber abierto el programa el usuario tendra que rellenar las 2 barras de entradas"\
        " con 2 numeros, luego tendra que pulsar alguno de los operadores que aparece mas abajo (botones),"\
        " el resultado de operar los 2 numeros con la operacion elegida aparecera abajo de las barras de entrada ")
    
    def acerca_de(self):
        mb.showinfo("Calculadora", "Este Programa fue creado por Luis Angel ureña perdomo con el proposito de" \
        " practicar los MessageBox de la libreria Tkinter, Gracias por tomarte el tiempo de probar este programa"\
        "\n"+"escrito en Python, usando Poo (OOP), hecho en 2021")

ventana=Aplicacion()

