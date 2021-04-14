m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices?:               "))
columnas=int(input("De cuantas Columnas quiere sus 2 matrices?:            "))

if filas<=0 or columnas<=0:
    print("Las filas y/o columnas tienen que ser positivas")

else:
    print("\n")

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.     Fila {}, Columna {},            ".format(i+1, j+1))))
    

    print("\n")



    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.     Fila {}, Columan {},            ".format(x+1, y+1))))

    

    #========================================================================================================================================================

    print("\n")


    print("La primera matriz es :")
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()





    print("\n")




    print("Esta es la segunda matriz:")
    print("\n")

    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #========================================================================================================================================================

    print("\n")

    mayor_1=0
    mayor_columna_1=0
    mayor_fila_1=0

    for f in range (filas):
        for c in range (columnas):



            if  m1[f][c] > mayor_1:
                mayor_1= m1[f][c]
                mayor_columna_1= c
                mayor_fila_1= f

    
    if m2[mayor_fila_1][mayor_columna_1] == mayor_1:
        print(f"el mayor numero de la primera matriz es {mayor_1}, esta en la fila {mayor_fila_1}, columna {mayor_columna_1},"\
                " Y el dato esta en el mismo lugar en la segunda matriz ")
    
    else:
         print(f"el mayor numero de la primera matriz {mayor_1} y dicho dato NO esta en la segunda matriz, o no esta en la misma posicion en la segunda matriz")





    print("\n")


    mayor_2=0
    mayor_columna_2=0
    mayor_fila_2=0

    for f2 in range (filas):
        for c2 in range (columnas):



            if m2[f2][c2] > mayor_2:
                mayor_2 = m2[f2][c2]
                mayor_columna_2= c2
                mayor_fila_2= f2
    

    if m1[mayor_fila_2][mayor_columna_2] == mayor_2:
        print(f"el mayor numero de la segunda matriz es {mayor_2}, esta en la fila {mayor_fila_2}, columna {mayor_columna_2},"\
                " Y el dato esta en el mismo lugar en la primera matriz ")
    
    else:
         print(f"el mayor numero de la segunda matriz es {mayor_2} y dicho dato NO esta en la primera matriz, o no en la misma posicion en la PRIMERA MATRIZ")
