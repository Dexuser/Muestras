m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices? :                  "))
columnas=int(input("De cuantas columnas quiere sus 2 matrices? :               "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")


    for i in range(filas):
        m1.append([])


        for j in range(columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.     Fila {}, Columna {}             ".format(i+1, j+1))))
    

    
    print("\n")


    for x in range(filas):
        m2.append([])


        for y in range(columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}             ".format(x+1, y+1))))

    
    #======================================================================================================================================================
    print("\n")


    print("Esta es la primera matriz:")
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()





    print("\n")






    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()


    #======================================================================================================================================================


    promedio=0
    #Esquinas de M1.

    esquina_1= m1[0][0]
    esquina_2= m1[0][columnas-1]
    esquina_3= m1[filas-1][0]
    esquina_4= m1[filas-1][columnas-1]



    promedio= (esquina_1 + esquina_2 + esquina_3 + esquina_4)/4

    #======================================================================================================================================================


    print("\n")


    #======================================================================================================================================================


    # Esquinas de m2


    promedio2=0
    

    esquina_6= m2[0][0]
    esquina_7= m2[0][columnas-1]
    esquina_8= m2[filas-1][0]
    esquina_9= m2[filas-1][columnas-1]



    promedio2= (esquina_6 + esquina_7 + esquina_8 + esquina_9)/4

    
     #======================================================================================================================================================


    if promedio == promedio2:
        print(f"el promedio de las esquinas de la PRIMERA MATRIZ es : {promedio} y es igual al promedio de las esquinas de la SEGUNDA MATRIZ")

    else:
        print(F"El promedio de las esquinas de la PRIMERA AMTRIZ es : {promedio} y es diferente al promedio de la SEGUNDA MATRIZ")

    
    print("\n")


    if promedio2 == promedio:
        print(f"el promedio de las esquinas de la SEGUNDA MATRIZ es : {promedio2} y es igual al promedio de las esquinas de la PRIMERA MATRIZ")

    else:

        print(f"el promedio de las esquinas de la SEGUNDA MATRIZ es {promedio2} y es diferente al promedio de la PRIMERA MATRIZ")





