from os import system 

m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices? :            "))
columnas=int(input("De cuantas columnas quiere sus 2 matrices? :        "))

if filas<=0 or columnas<=0:

    while filas<=0 or columnas<=0:
    
        system("cls")


        print()
        print("las filas y/o columnas tienen que ser positivas")
        print()

        filas=int(input("De cuantas filas quiere sus 2 matrices? :          "))
        columnas=int(input("De cuantas filas quiere sus 2 matrices?:           "))


#============================================================================================================================================

else:

    print("\n")

    for i in range (filas):
        m1.append([])

        for j in range (columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.       Fila {}, Columna {}           ".format(i+1, j+1))))
        
    
    print("\n")


    for x in range (filas):
        m2.append([])

        for y in range (columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.       Fila {}, Columna {}           ".format(x+1, y+1))))
    
    #============================================================================================================================================

    print("\n")

    print("Esta es la primera matriz")
    

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #============================================================================================================================================

    print("\n")

    #============================================================================================================================================

    print("Esta es la segunda matriz")

    
    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #============================================================================================================================================


    acum_1=0
    cont_1=0
    for f in range (filas):
        for c in range (columnas):

            if m1[f][c] % 2==0:
                
                acum_1+= m1[f][c]
                cont_1+=1
    
    promedio= acum_1//cont_1

    #============================================================================================================================================
    print("\n")
    #============================================================================================================================================


    acum_2=0
    cont_2=0
    for f2 in range (filas):
        for c2 in range (columnas):

            if m2[f2][c2] % 2==0:
               
                acum_2+= m2[f2][c2]
                cont_2+=1
    
    promedio2= acum_2//cont_2

    #============================================================================================================================================

    if promedio == promedio2:
        print(f"El promedio de los numeros pares de la PRIMERA MATRIZ es igual a {promedio} y es igual al promedio de los pares de la SEGUNDA MATRIZ")
    
    else:
        print(f"El promedio de los numeros pares de la PRIMERA MATRIZ es igual a {promedio} y es diferente al promedio de los pares de la SEGUNDA MATRIZ")
    

    print("\n")


    if promedio2 == promedio:
        print(f"el promedio de los numeros pares de la SEGUNDA MATRIZ es igual a {promedio2} y es igual al promedio de los pares de la PRIMERA MATRIZ")
    
    else:
        print(f"El promedio de los numeros pares de la SEGUNDA MATRIZ es igual a {promedio2} y es diferente al promedio de los pares de la PRIMERA MATRIZ")