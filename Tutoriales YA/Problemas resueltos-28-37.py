#Cargar una cadena por teclado luego:
#1) Imprimir los dos primeros caracteres.
#2) Imprimir los dos últimos
#3) Imprimir todos menos el primero y el último caracter.



def partes(texto):
    long=len(texto)

    print("los dos primeros caracteres del texto introducido")
    print(texto[:2])

    print()
    print("Los dos ultimos caracteres")
    print(texto[long-2:])
    print()

    print("Todo menos el primer y ultimo caracter")
    print(texto[1:long-1])













# Bloque principal.

texto=input("Introduzca un String:      ")
partes(texto)