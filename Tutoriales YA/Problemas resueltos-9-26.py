#Crear una lista de enteros por asignación.
#Definir una función que reciba una lista de enteros
#y un segundo parámetro de tipo entero. Dentro de la función
#mostrar cada elemento de la lista multiplicado por el valor entero enviado.


def multiplicar(lista, mult):
    for i in range(len(lista)):
        prod = lista[i] * mult
        print(f"{lista[i]}  x  {mult}   =  {prod}")


#bloque principal.

lista_valores=[]
for x in range(5):
    lista_valores.append(int(input("Introduzca un entero ala lista: ")))

print()
mult=int(input("Numero con que multiplicaremos: "))

multiplicar(lista_valores,mult)



