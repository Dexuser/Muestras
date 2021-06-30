import tkinter as tk
from tkinter import ttk	

from Formulario import login
from Formulario import mensaje

class Aplicacion:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("300x300")
		self.root.title("Ventana principal")
		self.botones()
		self.root.mainloop()

	def botones(self):
		self.labelframe1 = ttk.Labelframe(self.root, text="Botones")
		self.labelframe1.grid(column=0, row=0, padx=5 ,pady=5)
		self.boton1 = ttk.Button(self.labelframe1, text="Abrir el Login", command=self.login)
		self.boton1.grid(column=0, row=0, padx=5, pady=5)
		self.boton2 = ttk.Button(self.labelframe1, text="Mensaje", command=self.mensaje)
		self.boton2.grid(column=0, row=1, padx=5, pady=5)

	def login(self):
		login.mostrar()
	
	def mensaje(self):
		mensaje.mensaje("HOla puta madre")

aplicacion = Aplicacion()