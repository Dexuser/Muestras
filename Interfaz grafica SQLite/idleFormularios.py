import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import idleArticulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=idleArticulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrar_articulo()
        self.modificacion()
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
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
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
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")

    def borrar_articulo(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar articulo")
        self.labelframe4=ttk.Labelframe(self.pagina4, text="articulo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=5)
        self.label4=ttk.Label(self.labelframe4, text="Codigo del articulo:")
        self.label4.grid(column=0, row=0, padx=4, pady=4)
        self.dato=StringVar()
        self.entrydato=ttk.Entry(self.labelframe4, textvariable=self.dato)
        self.entrydato.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Eliminar", command=self.eliminar)
        self.boton1.grid(column=1, row=1, padx=4, pady=5)
    
    def eliminar(self):
        codigo=(self.dato.get(), )
        respuesta=self.articulo1.baja(codigo)

        if respuesta > 0:
            mb.showinfo("Informacion!", "El articulo ha sido eliminado")
        else:
            mb.showerror("Error!", "No existe ningun articulo con ese codigo")
    
    def modificacion(self):
        self.pagina5=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificacar articulo")
        self.labelframe5=ttk.Labelframe(self.pagina5, text="Articulo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=5)
        self.label5=ttk.Label(self.labelframe5, text="Codigo del articulo")
        self.label5.grid(column=0, row=0, padx=4, pady=4)
        self.dato_mod=StringVar()
        self.entry_mod=ttk.Entry(self.labelframe5, textvariable=self.dato_mod)
        self.entry_mod.grid(column=1, row=0, padx=4, pady=4)
        self.label6=ttk.Label(self.labelframe5, text="Descripcion:")
        self.label6.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion_mod=StringVar()
        self.descripcion_mod_entry=ttk.Entry(self.labelframe5, textvariable=self.descripcion_mod)
        self.descripcion_mod_entry.grid(column=1, row=1, padx=4, pady=4)
        self.label7=ttk.Label(self.labelframe5, text="Precio:")
        self.label7.grid(column=0, row=2, padx=4, pady=4)
        self.precio_mod=tk.StringVar()
        self.precio_mod_entry=ttk.Entry(self.labelframe5, textvariable=self.precio_mod)
        self.precio_mod_entry.grid(column=1, row=2, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe5, text="Consultar", command=self.consulta_mod)
        self.boton2.grid(column=1, row=3, padx=4, pady=4)
        self.boton3=ttk.Button(self.labelframe5, text="Modificar", command=self.editar)
        self.boton3.grid(column=1, row=4, padx=4, pady=4)
    
    def consulta_mod(self):
        codigo=(self.dato_mod.get(), )
        respuesta=self.articulo1.consulta_mod(codigo)

        if len(respuesta) > 0:
            self.descripcion_mod.set(respuesta[0][0])
            self.precio_mod.set(respuesta[0][1])
        else:
            mb.showerror("Error!", "No existe ningun articulo con ese codigo")
            self.descripcion_mod.set("")
            self.precio_mod.set("")
    
    def editar(self):
        actualizacion=(self.descripcion_mod.get(), 
        self.precio_mod.get(),
        self.dato_mod.get()
        )
        respuesta=self.articulo1.modificacion(actualizacion)
        if respuesta > 0:
            mb.showinfo("Informacion", "EL articulo ha sido actualizado")
        else:
            mb.showerror("Error!", "No existe ningun articulo con ese codigo")

aplicacion=FormularioArticulos()