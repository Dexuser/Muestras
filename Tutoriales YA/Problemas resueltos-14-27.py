#Confeccionar un programa que permita:
#1) Cargar una lista de 10 elementos enteros.
#2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
#3) Imprimir las dos listas generadas.



def carga():
    nums=[]

    for i in range(10):
        v1=int(input("Introduzca un entero:     "))
        nums.append(v1)

    return nums

def ordenador(lista):
    negativos=[]
    positivos=[]

    for i in lista:
        if i==0:
            continue
        if i>0:
            positivos.append(i)
        
        else:
             negativos.append(i)


    return [positivos, negativos]


def mostrar(posi, nega):

    print("Los numeros positivos introducidos son")
    print(posi)
    print()
    print()
    print("Y los numeros negativos introducidos son:")
    print(nega)











# bloque principal

enteros=carga()
print()
positivos, negativos=ordenador(enteros)
print()
mostrar(positivos, negativos)