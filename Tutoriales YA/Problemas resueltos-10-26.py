# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
# Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
# En el bloque principal iniciamos por asignación la lista de string:

def mayor_caracteres(lista):
    may_caracteres=0
    

    for i in range(len(lista)):

        if len(lista[i]) > may_caracteres:
            may_caracteres= len(lista[i])
            mayor_elemento= lista[i]
            lugar= i
    
    for x in range(len(lista)):

        if len(lista[x])==may_caracteres and x < lugar:
            return lista[x]

        


    return mayor_elemento
    





# bloque principal

lista_str=[]

for j in range(6):
    lista_str.append(input("introduzca un texto:    "))



print(f"el string con mas caracteres es: {mayor_caracteres(lista_str)}" )


        