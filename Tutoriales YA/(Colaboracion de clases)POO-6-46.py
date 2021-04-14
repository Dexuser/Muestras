#Plantear una clase Club y otra clase Socio.
# La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
# En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
# La clase Club debe tener como atributos 3 objetos de la clase Socio.
# Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.

class Socio:
    
    def __init__(self):
        self.nombre=input("Nombre del socio:  ")
        self.antiguedad=int(input("Cuantos años se unio?:  "))

    def return_datos(self):
        return (self.nombre, self.antiguedad)

class Club:

    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()
    
    def mayor_tiempo(self):
        if self.socio1.return_datos()[1]>self.socio2.return_datos()[1] and \
           self.socio1.return_datos()[1]>self.socio3.return_datos()[1]:
           print(f"{self.socio1.return_datos()[0]} es el socio mas antiguo")
        
        else:
            if self.socio2.return_datos()[1]>self.socio3.return_datos()[1]:
                print(f"{self.socio2.return_datos()[0]} es el socio mas antiguo")
            
            else:
                print(f"{self.socio3.return_datos()[0]} es el socio mas antiguo")
        

# bloque principal:
club=Club()
club.mayor_tiempo()
