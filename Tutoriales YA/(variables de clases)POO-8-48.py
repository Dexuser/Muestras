#Plantear una clase llamada Jugador.
#Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
#Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
#Definir en el bloque principal dos objetos de la clase Jugador.
#Reducir dicha variable hasta llegar a cero.

class Jugador:
    minutos=30

    def __init__(self, nombre, puntaje):
        self.nombre= nombre
        self.puntaje= puntaje
    
    def imprimir(self):
        print(f"nombre: {self.nombre} tiene como puntaje: {self.puntaje} puntos")
    
    def pasar_tiempo(self):
        Jugador.minutos-=1
        if Jugador.minutos>0:
            print(f"Quedan todavia {Jugador.minutos} minutos")
        else:
            print("Se acabaron los 30 minutos")
    


# bloque principal:
jugador1=Jugador("jose", 123)
jugador1.imprimir()
jugador2=Jugador("maria",130)
jugador2.imprimir()

while Jugador.minutos!=0:
    jugador1.pasar_tiempo()
    jugador2.pasar_tiempo()
    