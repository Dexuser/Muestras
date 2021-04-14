# Confeccionar un programa con las siguientes funciones:
# 1)Cargar una lista de 5 enteros.
# 2)Retornar el mayor y menor valor de la lista mediante una tupla.
# Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.


def carga_lista():
    lista=[]

    for i in range(5):
        valor=int(input("Introduzca un entero:      "))
        lista.append(valor)
    return lista

def mayor_menor(lista):
    grande=lista[0]
    pequeno=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>grande:
            grande=lista[i]
        
        else:
            if lista[i]<pequeno:
                pequeno=lista[i]
    
    return (grande, pequeno)











# bloque principal

lista=carga_lista()
aux=mayor_menor(lista)
mayor, menor=aux

print(f"El mayor numero introducido es {mayor} y el mas pequeño es {menor}")
