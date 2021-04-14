import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba de notebooks(Y repasada a anteriores temas)")
        self.ventana1.geometry("300x300")
        self.cuaderno1=ttk.Notebook(self.ventana1)
        

        #Pagina uno
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Checkbutton")
        self.label1=ttk.Label(self.pagina1, text="Eliga algunas frutas")
        self.label1.grid(column=0, row=0)
        self.opcion1=tk.IntVar()
        self.check1=ttk.Checkbutton(self.pagina1,text="manzana", variable=self.opcion1, command=self.activar)
        self.check1.grid(column=0, row=1)
        self.opcion2=tk.IntVar()
        self.check2=ttk.Checkbutton(self.pagina1, text="Pera", variable=self.opcion2, command=self.activar)
        self.check2.grid(column=0, row=2)
        self.opcion3=tk.IntVar()
        self.check3=ttk.Checkbutton(self.pagina1, text="aguacate", variable=self.opcion3, command=self.activar)
        self.check3.grid(column=0, row=3)
        self.label2=ttk.Label(self.pagina1, text="Usted ha seleccionado:", foreground="blue")
        self.label2.grid(column=4, row=0, )
        self.boton1=ttk.Button(self.pagina1, text="Mostrar selecciones:", command=self.frutas, state="disabled")
        self.boton1.grid(column=0, row=4)
        
        #pagina dos
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="RadioButton")
        self.label3=ttk.Label(self.pagina2, text="Eliga su Navegador Favorito", foreground="blue")
        self.label3.place(x=5, y=5)
        #RadioButtons.
        self.seleccion1=tk.IntVar()
        self.radio1=ttk.Radiobutton(self.pagina2, text="Google", variable=self.seleccion1, value=1, command=self.navegador)
        self.radio1.place(x=5, y=25)
        self.radio2=ttk.Radiobutton(self.pagina2, text="Opera", variable=self.seleccion1, value=2, command=self.navegador)
        self.radio2.place(x=5, y=45)
        self.radio3=ttk.Radiobutton(self.pagina2, text="FireFox", variable=self.seleccion1, value=3, command=self.navegador)
      
        self.radio3.place(x=5, y=65)
        self.navegador()

        self.label4=ttk.Label(self.pagina2, text="Tomese su tiempo...",)
        self.label4.place(x=5, y=85)


        self.cuaderno1.grid(column=0, row=0)
        self.ventana1.mainloop()

    # funciones de la primera pagina
    def activar(self):
        if self.opcion1.get()==1 or self.opcion2.get()==1 or self.opcion3.get()==1:
            self.boton1["state"]="normal"
        else:
            self.boton1["state"]="disabled"

    def frutas(self):
        frutas=""
        if self.opcion1.get()==1:
            frutas+= "manzana"+"\n"
        if self.opcion2.get()==1:
            frutas+= "pera"+"\n"
        if self.opcion3.get()==1:
            frutas+= "aguacate"+"\n"
        self.label2["text"]="Usted ha seleccionado"+"\n"+frutas

    def navegador(self):
        if self.seleccion1.get()==1:
            self.label4["text"]="Okay, ahora se que le gusta Google"
        if self.seleccion1.get()==2:
            self.label4["text"]="Okay, ahora se que le gusta Opera"
        if self.seleccion1.get()==3:
            self.label4["text"]="Okay, ahora se que le gusta Firefox"
# objeto
ventana=Aplicacion()