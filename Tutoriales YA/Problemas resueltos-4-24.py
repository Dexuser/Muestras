#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
#  En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenador(v1, v2, v3):

    if v1<v2 and v1<v3:

        if v2<v3:
            print(f"de forma ordenada es:   {v1, v2, v3}")
        else:
            print(f"de forma ordenada es: {v1, v3, v2}")
    



    if v2<v1 and v2<v3:

        if v1<v3:
            print(f"de forma ordenada es:   {v2, v1, v3}")
        else:
            print(f"de forma ordenada es:   {v2, v3, v1} ")
    



    if v3<v1 and v3<v1:

        if v2<v1:
            print(f"de forma ordenada es:   {v3, v2, v1}")
        else:
            print(f"de forma ordenada es:   {v3, v1, v2}")





def carga():
    print("introduzca los 3 datos a ordenar")
    print()
    valor1=int(input("primer entero:    "))
    valor2=int(input("segundo entero:    "))
    valor3=int(input("tercer entero:    "))
    ordenador(valor1, valor2, valor3)



#bloque principal:

carga()