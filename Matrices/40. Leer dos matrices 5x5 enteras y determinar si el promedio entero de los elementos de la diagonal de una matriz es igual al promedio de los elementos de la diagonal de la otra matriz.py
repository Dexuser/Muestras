m1=[]
m2=[]

filas=int(input("De cuantas filas va a querer sus 2 matrices? :                     "))
columnas=int(input("De cuantas columnas va a querer sus 2 matrices? :                  "))

if filas<=0 or columnas<=0:
    print(f"Las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range(filas):
        m1.append([])    

        for j in range(columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.     Fila {}, Columna {}             ".format(i+1, j+1))))
    


    print("\n")



    for x in range (filas):
        m2.append([])

        for y in range (columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.         Fila {}, Columna {}         ".format(x+1, y+1))))

    #=================================================================================================================================

    print("\n")

    print("esta es la primera matriz :")
    print()

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()




    print("\n")


    print("esta es la segunda matrz:")
    print()


    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()


    #=================================================================================================================================

    # promedio de la diagonal de la primera matriz

    promedio=0
    acum=0
    for f in range (filas):

        acum+= m1[f][f]

    promedio= acum/5


    #=================================================================================================================================

    # promedio de la diagonal de la segunda
    promedio2=0
    acum2=0

    for f2 in range (filas):

        acum2+= m2[f2][f2]

    promedio2= acum2/5

    #=================================================================================================================================


    if promedio == promedio2:
        print(f"el promedio de la diagonal de la PRIMERA MATRIZ es {promedio} y es igual al promedio de la SEGUNDA MATRIZ")
    
    else:
        print(f"el promedio de la diagonal de la PRIMERA MATRIZ es {promedio} y es es diferente al promedio de la digonal de la SEGUNDA MATRIZ")

    
    print("\n")


    if promedio2 == promedio:
        print(f"el promedio de la diagonal de la SEGUNDA MATRIZ es {promedio2} y es igual al promedio de la PRIMERA MATRIZ")

    else:
        print(f"el promedio de la diagonal de la SEGUNDA MATRIZ ES {promedio2} y es diferente al promedio de la diagonal de la PRIMERA MATRIZ")