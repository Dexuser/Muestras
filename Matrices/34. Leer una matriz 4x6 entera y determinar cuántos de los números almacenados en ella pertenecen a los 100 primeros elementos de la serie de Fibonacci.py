m1=[]
v1=[]

aux=0
aux2=1

for fib in range(1,100):

    v1.append(aux)
    suma=aux+aux2
    aux=aux2
    aux2=suma


filas=int(input("De cuantas filas quiere su matriz? :                "))
columnas=int(input("de cuantas columnas quiere su matriz ? :            "))




if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range (filas):
        m1.append([])

        for j in range (columnas):

            m1[i].append(int(input("Fila {}, Columna {}         ".format(i+1, j+1))))

    
    print("\n")



    print()

    for fila in m1:
        print("]", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()
        


    cont=0

    for f in range(filas):
        for c in range (columnas):

           # print(f"el count de {m1[f][c]} es de {v1.count(m1[f][c])} ")

            if v1.count(m1[f][c])>=1:
                cont+=1
                print(f"el numero {m1[f][c]} esta entre los 100 numeros de fibonnaci")
    

    if cont>0:

        print(f"Existen {cont} numeros de fibonacci que estan entre los 100 numeros de fibonacci.")

    else:
        print("No existen numeros entre los primeros 100 numeros de la serie de fibonacci en la matriz")
