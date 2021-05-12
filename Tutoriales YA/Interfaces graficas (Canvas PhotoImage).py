import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas1 = tk.Canvas(self.root, width=1000, height=1300, background="black")
        self.canvas1.grid(column=0, row=0)
        archivo1 = tk.PhotoImage(file="carta1.png")
        self.canvas1.create_image(30, 50, image=archivo1, anchor="nw")

        self.root.mainloop()


prueba= Aplicacion()