#Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.


def productos(lista):

    producto=1
    for i in range(len(lista)):

        producto= producto*lista[i]
    

    return producto





#bloque principal

valores=[]

for i in range(5):
    valores.append(int(input("Introduzca un entero:  ")))


print(f"El producto de los numeros introducidos es igual a : {productos(valores)}")

        