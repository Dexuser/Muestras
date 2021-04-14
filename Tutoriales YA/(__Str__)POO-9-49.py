#Desarrollar un programa que implemente una clase llamada Jugador.
#Definir como atributos su nombre y puntaje.
#Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)

class Jugador:

    def __init__(self, nombre, puntos):
        self.nombre=nombre
        self.puntos=puntos
    
    def __str__(self):

        if self.puntos<1000:
            cadena=self.nombre+" Es principiante"
        else:
            cadena=self.nombre+" Es experto"
        return cadena


# bloque principal:
jugador1=Jugador("luis",999)
print(jugador1)