# Realiza una list box, con frutas, seleccion multiple, y ponlas en una canasta
import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()

        self.label1=tk.Label(self.ventana1, text="Escoga sus frutas:")
        self.label1.grid(column=0, row=0)
        
        self.scroll1=tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)

        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1)
        self.listbox1.grid(column=1, row=1)
        self.listbox1.insert(0, "manzana")
        self.listbox1.insert(1, "pera")
        self.listbox1.insert(2, "uvas")
        self.listbox1.insert(3, "mango")
        self.listbox1.insert(4, "aguacate")
        self.listbox1.insert(5, "platano")
        self.listbox1.insert(6, "manzana de oro")
        self.listbox1.insert(7, "chinas")
        self.listbox1.insert(8, "naranjas")
        self.listbox1.insert(9, "sandia")
        self.listbox1.insert(10, "lechosa")

        self.scroll1.config(command=self.listbox1.yview)
        self.scroll1.grid(column=2, row=1, sticky="NS")

        self.boton1=tk.Button(self.ventana1, text="ver canasta", command=self.recuperar)
        self.boton1.grid(column=1, row=3)

        self.label2=tk.Label(self.ventana1, text="Prueba")
        self.label2.grid(column=1, row=4)

        self.ventana1.mainloop()

    def recuperar(self):
        
        if len( self.listbox1.curselection() )!=0:
            canasta=""

            for i in self.listbox1.curselection():
                canasta+= self.listbox1.get(i)+"\n"
            self.label2["text"]="En la canasta hay"+"\n"+canasta




ventana=Aplicacion()