# Realizar un programa que contenga las siguientes funciones:
#1) Carga de una lista de 10 enteros.
#2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
#3) Imprimir una lista.

def carga():
    enteros=[]

    for i in range(10):
        valor=int(input("Introduzca un entero:  "))
        enteros.append(valor)
    
    return enteros


def mitad_lista(enteros):
    lista2=enteros[:5]
    return lista2


def Imprimir(lista):
    print("La mitad de la lista introducida es: ")
    for i in range(len(lista)):
        print(lista[i], end=",")
        


# bloque principal
enteros=carga()
mitad= mitad_lista(enteros)
Imprimir(mitad)
