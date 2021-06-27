#usa el Increment de spinbox

import tkinter as tk
from tkinter import ttk

class Aplicacion:

    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("300x200")
        self.spinbox=ttk.Spinbox(self.root, from_=0, to=120, increment=5, width=10)
        self.spinbox.grid(column=0, row=0)
        self.root.mainloop()


# aplicacion
ventana= Aplicacion()