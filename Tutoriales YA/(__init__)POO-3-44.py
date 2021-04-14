#Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
# inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), 
# imprimir su perímetro y su superficie.

class Cuadrado:

    def __init__(self, lado1):
        self.lado= lado1
    
    def perimetro_superficie(self):
        superficie= self.lado**2
        perimetro= self.lado*4
        print(f"el perimetro del cuadrado vale: {perimetro}, y su superficie vale: {superficie}")

# bloque principal
figura=Cuadrado(5)
figura.perimetro_superficie()