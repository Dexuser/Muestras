m1=[]
num_mayor_menor=-30000


filas=int(input("De cuantas filas quiere su matriz? :           "))
columnas=int(input("De cuantas columnas quiere su matriz? :        "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")


    for i in range (filas):
        m1.append([])

        for j in range(columnas):
            valor=int(input("Fila {}, Columna {}         ".format(i+1, j+1)))

            if valor>num_mayor_menor:
                num_mayor_menor=valor

            m1[i].append(valor)



    print("\n")



    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()


    #print(f"el numero mas grande es {num_mayor}")


    for f in range(filas):
        for c in range(columnas):

            if m1[f][c] < num_mayor_menor:
                num_mayor_menor= m1[f][c]
    


    cont=0
    
    for f in range(filas):
        for c in range(columnas):

            if m1[f][c]==num_mayor_menor:
                cont+=1
    
    print(f"el numero menor es {num_mayor_menor} y se repite {cont} veces")