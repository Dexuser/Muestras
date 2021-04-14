#46. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números menores
#cada fila de una matriz corresponde a alguno de los datos almacenados en las “esquinas” de la
#otra matriz.

m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices? :                  "))
columnas=int(input("De cuantas columnas quiere sus 2 matrices? :               "))

if filas<=0 or columnas<=0:
    print(f"las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range (filas):
        m1.append([])

        for j in range (columnas):
            m1[i].append(int(input("PRIMERA FILA.       Fila {}, Columna {}             ".format(i+1, j+1))))




    print("\n")



    for x in range (filas):
        m2.append([])

        for y in range (columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}             ".format(x+1, y+1))))

    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================

    print("Esta es la primera matriz")

    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================


    print()
    for fila in m2:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #==================================================================================================================================

    acum_menor_1=0
    cont_menor_1=0

    for f in range (filas):

        menores=0

        for c in range (columnas):

            if menores==0:
                menores= m1[f][c]
            
              

            else:
                if m1[f][c] < menores:
                    
                    menores= m1[f][c]

                acum_menor_1+= menores
                cont_menor_1+=1 

       # print(f"el menor de la fila {f} es el {menores}")


    promedio_menor_1= acum_menor_1 // cont_menor_1

    print(f"el promedio de los menores de la primera matriz es {promedio_menor_1}")




    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================


    acum_menor_2=0
    cont_menor_2=0

    for f2 in range (filas):

        menores2=0

        for c2 in range (columnas):

            if menores2==0:
                menores2= m2[f2][c2]
            
              

            else:
                if m2[f2][c2] < menores2:
                    
                    menores2= m2[f2][c2]

                acum_menor_2+= menores2
                cont_menor_2+=1 

       # print(f"el menor de la fila {f} es el {menores}")


    promedio_menor_2= acum_menor_2 // cont_menor_2

    print(f"el promedio de los menores de la SEGUNDA MATRIZ es {promedio_menor_2}")


    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================





    comprobante=0

    if promedio_menor_1 == m2[0][0]:
        print(f"el promedio de la PRIMERA MATRIZ se encuentra en la esquina Superior izquierda de la SEGUNDA MATRIZ")
        comprobante+=1
    print()
    
    
    if promedio_menor_1 == m2[0][columnas-1]:
        print(f"El promedio de la PRIMERA MATRIZ se encuentra en la esquina superior derecha de la SEGUNDA MATRIZ")
        comprobante+=1
    print()
    
    if promedio_menor_1 == m2[filas-1][0]:
        print(f"el promedio de la PRIMERA MATRIZ se encuentra en la esquina inferior izquierda de la SEGUNDA MATRIZ")
        comprobante+=1
    print()
    
    if promedio_menor_1 == m2[filas-1][columnas-1]:
        print(f"el promedio de la PRIMERA MATRIZ se encuentra en la esquina inferior derecha de la SEGUNDA MATRIZ")
        comprobante+=1
    print()


    if comprobante==0:
        print(f"el promedio de la PRIMERA MATRIZ no se encuentra en ninguna esquina de la segunda matriz")





    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================






    comprobante2=0


    if promedio_menor_2 == m1[0][0]:
        print(f"el promedio de la SEGUNDA MATRIZ se encuentra en la esquina Superior izquierda de la PRIMERA MATRIZ")
        comprobante2+=1
        print()
    
    
    if promedio_menor_2 == m1[0][columnas-1]:
        print(f"El promedio de la SEGUNDA MATRIZ se encuentra en la esquina superior derecha de la PRIMERA MATRIZ")
        comprobante2+=1
        print()
    
    if promedio_menor_2 == m1[filas-1][0]:
        print(f"el promedio de la SEGUNDA MATRIZ se encuentra en la esquina inferior izquierda de la PRIMERA MATRIZ")
        comprobante2+=1
        print()
    
    if promedio_menor_2 == m1[filas-1][columnas-1]:
        print(f"el promedio de la SEGUNDA  MATRIZ se encuentra en la esquina inferior derecha de la PRIMERA MATRIZ")
        comprobante2+=1
        print()


    if comprobante2==0:
        print(f"el promedio de la SEGUNDA MATRIZ no se encuentra en ninguna esquina de la PRIMERA MATRIZ")
        print()



