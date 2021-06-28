import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from typing import Text
import Postarticulos

class FormularioArticulos:
	def __init__(self):
		self.articulo1=Postarticulos.Articulos()
		self.ventana1=tk.Tk()
		self.ventana1.title("Mantenimiento de artículos")
		self.cuaderno1 = ttk.Notebook(self.ventana1)        
		self.carga_articulos()
		self.consulta_por_codigo()
		self.listado_completo()
		self.eliminar_articulo()
		self.modificar()
		self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
		self.ventana1.mainloop()

	def carga_articulos(self):
		self.pagina1 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina1, text="Carga de artículos")
		self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
		self.label1=ttk.Label(self.labelframe1, text="Descripción:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.descripcioncarga=tk.StringVar()
		self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
		self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
		self.label2=ttk.Label(self.labelframe1, text="Precio:")        
		self.label2.grid(column=0, row=1, padx=4, pady=4)
		self.preciocarga=tk.StringVar()
		self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
		self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
		self.boton1.grid(column=1, row=2, padx=4, pady=4)

	def agregar(self):
		datos=(self.descripcioncarga.get(), self.preciocarga.get())
		self.articulo1.alta(datos)
		mb.showinfo("Información", "Los datos fueron cargados")
		self.descripcioncarga.set("")
		self.preciocarga.set("")

	def consulta_por_codigo(self):
		self.pagina2 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina2, text="Consulta por código")
		self.labelframe1=ttk.LabelFrame(self.pagina2, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
		self.label1=ttk.Label(self.labelframe1, text="Código:")
		self.label1.grid(column=0, row=0, padx=4, pady=4)
		self.codigo=tk.StringVar()
		self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigo)
		self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
		self.label2=ttk.Label(self.labelframe1, text="Descripción:")        
		self.label2.grid(column=0, row=1, padx=4, pady=4)
		self.descripcion=tk.StringVar()
		self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcion, state="readonly")
		self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
		self.label3=ttk.Label(self.labelframe1, text="Precio:")        
		self.label3.grid(column=0, row=2, padx=4, pady=4)
		self.precio=tk.StringVar()
		self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio, state="readonly")
		self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
		self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
		self.boton1.grid(column=1, row=3, padx=4, pady=4)

	def consultar(self):
		datos=(self.codigo.get(), )
		respuesta=self.articulo1.consulta(datos)
		if len(respuesta)>0:
			self.descripcion.set(respuesta[0][0])
			self.precio.set(respuesta[0][1])
		else:
			self.descripcion.set('')
			self.precio.set('')
			mb.showinfo("Información", "No existe un artículo con dicho código")

	def listado_completo(self):
		self.pagina3 = ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina3, text="Listado completo")
		self.labelframe1=ttk.LabelFrame(self.pagina3, text="Artículo")
		self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
		self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
		self.boton1.grid(column=0, row=0, padx=4, pady=4)
		self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
		self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

	def listar(self):
		respuesta=self.articulo1.recuperar_todos()
		self.scrolledtext1.delete("1.0", tk.END)        
		for fila in respuesta:
			self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")


	def eliminar_articulo(self):
		self.pagina4=ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina4, text="Borrar articulo")
		self.labelframe2=ttk.LabelFrame(self.pagina4, text="Articulo")
		self.labelframe2.grid(column=0, row=0, padx=5, pady=5)
		self.label4=ttk.Label(self.labelframe2, text="Codigo:")
		self.label4.grid(column=0, row=0, padx=5, pady=5)
		self.codigo2=tk.StringVar()
		self.codigo2_entry=ttk.Entry(self.labelframe2, textvariable=self.codigo2)
		self.codigo2_entry.grid(column=1, row=0, padx=5, pady=5)
		self.boton2=ttk.Button(self.labelframe2, text="Borrar", command=self.borrar)
		self.boton2.grid(column=1, row=1, padx=5, pady=5)
	
	def borrar(self):
		datos=(self.codigo2.get(), )
		respuesta=self.articulo1.borrar(datos)
		if respuesta > 0:
			mb.showinfo("Informacion", "El articulo fue eliminado correctamente")
		else:
			mb.showerror("Error!", "No existe ningun articulo con ese codigo")

	def modificar(self):
		self.pagina5=ttk.Frame(self.cuaderno1)
		self.cuaderno1.add(self.pagina5, text="Modificar articulo")
		self.labelframe3=ttk.Labelframe(self.pagina5, text="Articulo")
		self.labelframe3.grid(column=0, row=0, padx=5, pady=5)
		self.label5=ttk.Label(self.labelframe3, text="Codigo:")
		self.label5.grid(column=0, row=0, padx=5, pady=5)
		self.codigo3=tk.StringVar()
		self.codigo3_entry=ttk.Entry(self.labelframe3, textvariable=self.codigo3)
		self.codigo3_entry.grid(column=1, row=0, padx=5, pady=5)
		self.label6=ttk.Label(self.labelframe3, text="Descripcion:")
		self.label6.grid(column=0, row=1, padx=5, pady=5)
		self.descripcion2=tk.StringVar()
		self.descripcion2_entry=ttk.Entry(self.labelframe3, textvariable=self.descripcion2)
		self.descripcion2_entry.grid(column=1, row=1, padx=5, pady=5)
		self.label7=ttk.Label(self.labelframe3, text="Precio")
		self.label7.grid(column=0, row=2, padx=5, pady=5)
		self.precio2=tk.StringVar()
		self.precio2_entry=ttk.Entry(self.labelframe3, textvariable=self.precio2)
		self.precio2_entry.grid(column=1, row=2, padx=5, pady=5)
		self.boton3=ttk.Button(self.labelframe3, text="Modificar", command=self.editar)
		self.boton3.grid(column=1, row=3, padx=5, pady=5)
		self.boton4=ttk.Button(self.labelframe3, text="Consultar", command=self.consultar2)
		self.boton4.grid(column=1, row=4, padx=5, pady=5)
	
	def editar(self):
		datos=(self.descripcion2.get(), self.precio2.get(), self.codigo3.get())
		respuesta=self.articulo1.editar(datos)
		if respuesta > 0:
			mb.showinfo("Informacion", "Los datos fueron modificados correctamente")
		else:
			mb.showinfo("Error!", "No existen ningun articulo con ese codigo")

	def consultar2(self):
		datos=(self.codigo3.get(), )
		respuesta=self.articulo1.consulta(datos)
		if len(respuesta)>0:
			self.descripcion2.set(respuesta[0][0])
			self.precio2.set(respuesta[0][1])
		else:
			self.descripcion.set('')
			self.precio.set('')
			mb.showinfo("Información", "No existe un artículo con dicho código")

aplicacion1=FormularioArticulos()