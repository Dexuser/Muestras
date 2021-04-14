def busca_menor():
    print("Funcion que busca el menor de 3 numeros introducidos")
    print()

    valor3=int(input("Introduzca su primer numero:      "))
    valor4=int(input("Introduzca su segundo numero:      "))
    valor5=int(input("Introduzca su tercer numero:      "))

    menor= valor3

    if valor4<menor:
        menor= valor4
    

    if valor5<menor:
        menor=valor5

    
    print(f"el menor numero introducido es:  {menor}")




# Bloque principal

busca_menor()