import tkinter as tk
from tkinter import ttk

class Aplicacion:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Login")
		self.labelframe1 = ttk.Labelframe(self.root, text="Login")
		self.labelframe1.grid(column=0, row=1, padx=5, pady=5)
		self.login()

	def login(self):
		self.label1 = ttk.Label(self.labelframe1, text="Ingrese usuario")
		self.label1.grid(column=0, row=0, padx=5, pady=5)
		self.entry1 = ttk.Entry(self.labelframe1)
		self.entry1.grid(column=1, row=0, padx=5, pady=5)
		self.label2 = ttk.Label(self.labelframe1, text="Contraseña:")
		self.label2.grid(column=0, row=1, )
		self.entry2 = ttk.Entry(self.labelframe1, show="*")
		self.entry2.grid(column=1, row=1, padx=5, pady=5)
		self.boton1 = ttk.Button(self.labelframe1, text="Ingresar", command=self.ingresar)
		self.boton1.grid(column=1, row=2, padx=5, pady=5)
	
	def ingresar(self):
		self.root.destroy()

def mostrar():
	aplicacion = Aplicacion()