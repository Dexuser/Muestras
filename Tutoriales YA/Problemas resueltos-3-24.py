#  Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
#  Llamarla desde el bloque principal del programa 3 veces con string distintos.

def mostrar_vocales(texto):
    cont=0
    longitud= len(texto)


    for i in range(longitud):

        if texto[i]=="a" or texto[i]=="e" or texto[i]=="i" or texto[i]=="o" or texto[i]=="u":
            cont+=1


    print(f"en el texto introducido hay  {cont} vocales")










#bloque principal
for y in range(3):
    mostrar_vocales(input("Introduzca un texto :    "))
    print()


