# Confeccionar una clase que permita carga el nombre y la edad de una persona.
# Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona:

    def inilizacion(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    
    def imprimir(self):
        print(f"{self.nombre} tiene {self.edad} años")
    
    def mayor_edad(self):
        if self.edad>=18:
            print("Y es mayor de edad")
        else:
            print("Y no es mayor de edad")


# bloque principal
persona1= Persona()
nom=input("Como se llama?:  ")
ed=int(input("Su edad es:   "))
persona1.inilizacion(nom,ed)
persona1.imprimir()
persona1.mayor_edad()