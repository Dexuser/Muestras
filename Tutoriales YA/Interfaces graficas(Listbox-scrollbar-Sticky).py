# Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país.
# Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()

        self.label1=tk.Label(self.ventana1, text="Su nombre:")
        self.label1.grid(column=0, row=0)

        self.nombre=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=40, textvariable=self.nombre, )
        self.entry1.grid(column=1, row=0)

        self.scroll1=tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)        # Creamos un Objeto Scrollbar, ponemos donde aparecera, y si orientacion (verti/hori)
        

        self.listbox1=tk.Listbox(self.ventana1, yscrollcommand=self.scroll1.set) # Objeto listbox, poneoms donde aparece, y le damos al parametro yscrollcoman el objeto Scrollbar 
        self.listbox1.grid(column=0, row=2)                                     # Aparentemente, el Listbox y el scrollbar, deben estar en el mismo row

        self.scroll1.configure(command=self.listbox1.yview)                     # al objeto escrollbar, le agregamos al parametro command nuestro listbox y ponemos al lado "yview"
        self.scroll1.grid(column=1, row=2, sticky="NS")      # Aparentemente, el Listbox y el scrollbar, deben estar en el mismo row x 2, agregamos el parametro sticky                  

        self.listbox1.insert(0, "Republica Dominicana")         # Insertamos los items del list box
        self.listbox1.insert(1, "Brasil")
        self.listbox1.insert(2, "Mexico")
        self.listbox1.insert(3, "Estados Unidos")
        self.listbox1.insert(4, "Cuba")
        self.listbox1.insert(5, "Puerto rico")
        self.listbox1.insert(6, "Venezuela")
        self.listbox1.insert(7, "España")
        self.listbox1.insert(8, "Canada")
        self.listbox1.insert(9, "Russia")
        self.listbox1.insert(10, "Chile")
        self.listbox1.insert(11, "Bolivia")

        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar_datos)
        self.boton1.grid(column=1, row=3)
        self.ventana1.mainloop()
    def ingresar_datos(self):
        if len(self.listbox1.curselection())!=0:
            self.ventana1.title("Nombre: "+ self.nombre.get() +", Pais: "+ self.listbox1.get(self.listbox1.curselection()[0])) 

    # si la lo longitud de los elemenos selecionados no es cero pasamos a
    # a tomar el nombre introducido con get, y tomamos el primer elemento (get), de la lista de items seleccionados
    # del listbox (curseselection) ( que es una tupla), y lo convertimos a str, y por ultimo lo concatenamos

ventana=Aplicacion()