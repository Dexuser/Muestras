#Plantear una función que reciba un string en mayúsculas o minúsculas
#  y retorne la cantidad de letras 'a' o 'A'.


def contar_Aa(texto):
    cont=0
    longitud= len(texto)

    for i in range(longitud):

        if texto[i]=="A" or texto[i]=="a":
            cont+=1


    return cont

#bloque principal

parrafo=input("Introduzca su texto:  ")

print(f"Su texto contiene {contar_Aa(parrafo)} A o a ")



