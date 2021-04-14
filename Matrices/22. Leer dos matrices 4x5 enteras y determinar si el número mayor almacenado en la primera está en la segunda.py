m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus matrices? :                     "))
columnas=int(input("De cuantas columnas quiere sus matrices? :                  "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")


    num_mayor=-30000

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            valor=int(input("Primera Matriz.     Fila {}, columna {} :       ".format(i+1, j+1)))


            if valor>num_mayor:
                num_mayor=valor

            m1[i].append(valor)


    #=======================================================================================================================================
    print("\n")
    
    for x in range (filas):
        m2.append([])

        for y in range(columnas):
            m2[x].append(int(input("Segunda matriz.     Fila {}, Columna {} :         ".format(x+1, y+1 ))))
    
    #=======================================================================================================================================


    print("\n")

    print("la primera matriz es :")

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]") 
    print()

    


    print("\n")

    print("la segunda matriz es :")

    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]") 
    print()



    comprobante=0
    for f2 in range(filas):
        for c2 in range(columnas):

            if m2[f2][c2]==num_mayor:
                comprobante+=1
    

    if comprobante>0:
        print(f"el numero mas grande de la PRIMERA matriz es {num_mayor} y si se encuentra en la SEGUNDA matriz")
    else:
        print(f"el numero mas grande de la PRIMERA matriz es {num_mayor} y NO se encuentra en la SEGUNDA matriz")
            



