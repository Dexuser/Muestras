#Elaborar una función que nos retorne el perímetro de un cuadrado
#  pasando como parámetros el valor de un lado.


def devolver_perimetro(lado):
    per= lado*4
    return per




# bloque principal

valor=int(input("Ingrese el lado de un cuadrado:        "))

print(f"el perimetro del cuadrado es igual a {devolver_perimetro(valor)}")
