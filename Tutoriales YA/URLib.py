# Confeccionar una aplicación visual con tkinter que permita ingresar
# en un control de tipo 'Entry' la URL de un sitio web y al presionar
# un botón recuperar los datos y mostrarlos en un control de tipo 'ScrolledText':
from urllib import request
from urllib import error
import tkinter as tk
from tkinter import ttk	
from tkinter import scrolledtext as st


class ConexionInternet:

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Acceso a internet")
		self.interfaz()
		self.root.mainloop()

	def interfaz(self):
		self.label1 = ttk.Label(self.root, text="Introduzca una URL")
		self.label1.grid(column=0, row=0, pady=10)
		self.url = tk.StringVar()
		self.url_entry = ttk.Entry(self.root, textvariable=self.url, width=100)
		self.url_entry.grid(column=0, row=1, pady=10)
		self.boton1 = ttk.Button(self.root, text="Recuperar", command=self.recuperar)
		self.boton1.grid(column=0, row=2, pady=10)
		self.contenido = st.ScrolledText(self.root, width=100, height=30)
		self.contenido.grid(column=0, row=3, padx=10, pady=10)


	def recuperar(self):
		try:
			data = request.urlopen( self.url.get() )
			print(data)
			auxliar = data.read()
			print(auxliar)
			contenido = auxliar.decode("utf-8")
			self.contenido.delete(1.0, tk.END)
			self.contenido.insert(1.0, contenido)
		except error.HTTPError as httperror:
			print(f"El servidor mando el codigo {httperror.code}")
			print(f"El recurso que se intenta acceder esta inhabilitado o ya no existe")
aplicacion = ConexionInternet()