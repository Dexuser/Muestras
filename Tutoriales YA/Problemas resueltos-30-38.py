#Confeccionar un programa con las siguientes funciones:
#1) Cargar una lista con 5 palabras.
#2) Intercambiar la primer palabra con la última.
#3) Imprimir la lista


def carga():
    lista=[]
    for i in range(5):
        palabras=input("Introduzca una palabra:     ")
        lista.append(palabras)
    return lista


def intercambio(palabras):
    aux= palabras[0]
    palabras[0]= palabras[-1]
    palabras[-1]= aux


def imprimir(palabras):
    for i in palabras:
        print(i)






# bloque principal
lista= carga()

print("La lista de palabras introducida antes del cambio:  ")
imprimir(lista)
print()
print()
intercambio(lista)
print("la lista de palabras introducidas despues del cambio: ")
print()
imprimir(lista)