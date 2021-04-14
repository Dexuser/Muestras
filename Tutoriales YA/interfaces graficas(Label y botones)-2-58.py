#Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento
import tkinter as tk
class Numeros:
    nums=[]
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text=Numeros.nums, foreground="red")
        self.label1.grid(column=0, row=0)

        self.boton1=tk.Button(self.ventana1, text="1", command=self.numero1)
        self.boton1.grid(column=1, row=1)
        self.boton2=tk.Button(self.ventana1, text="2", command=self.numero2)
        self.boton2.grid(column=2, row=1)
        self.boton3=tk.Button(self.ventana1, text="3", command=self.numero3)
        self.boton3.grid(column=3, row=1)
        self.boton4=tk.Button(self.ventana1, text="4", command=self.numero4)
        self.boton4.grid(column=4, row=1)
        self.boton5=tk.Button(self.ventana1, text="5", command=self.numero5)
        self.boton5.grid(column=5, row=1)

        self.ventana1.mainloop()
        
    def numero1(self):
        Numeros.nums.append(1)
        self.label1["text"]=Numeros.nums
    def numero2(self):
        Numeros.nums.append(2)
        self.label1["text"]=Numeros.nums
    def numero3(self):
        Numeros.nums.append(3)
        self.label1["text"]=Numeros.nums
    def numero4(self):
        Numeros.nums.append(4)
        self.label1["text"]=Numeros.nums
    def numero5(self):
        Numeros.nums.append(5)
        self.label1["text"]=Numeros.nums

# bloque principal

ventana=Numeros()