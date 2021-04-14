m1=[]
m2=[]

filas=int(input("de cuantas filas quiere sus matrices? :                "))
columnas=int(input("de cuantas columnas quiere sus matrices? :             "))

if filas<=0 or columnas<=0:
    print("las filas y/o columanas tienen qu eser positivas")

else:
    
    print("\n")

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("Primera matriz.     Fila {}, Columna {}        ".format(i+1, j+1))))
    
    


    print("\n")


    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            m2[x].append(int(input("Segunda matriz.     Fila {}, columna {}         ".format(i+1, j+1))))
        
    

    #=====================================================================================================================


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

    #=====================================================================================================================


    mayor_prim1=0
    cont=0

    for f1 in range(filas):
        for c1 in range(columnas):

            if m1[f1][c1]<=1:
                continue

            for ind_prim in range(2,m1[f1][c1]):

                prim= m1[f1][c1] % ind_prim

                if prim==0:
                    cont+=1
            
            if cont==0 and m1[f1][c1] > mayor_prim1:
                mayor_prim1= m1[f1][c1]
                
            cont=0

    #=====================================================================================================================
    
    mayor_prim2=0
    cont2=0

    for f2 in range(filas):
        for c2 in range(columnas):

            if m1[f2][c2]<=1:
                continue

            for ind_prim2 in range(2,m2[f2][c2]):

                prim= m2[f2][c2] % ind_prim2

                if prim==0:
                    cont2+=1
            
            if cont2==0 and m2[f2][c2] > mayor_prim2:
                mayor_prim2= m2[f2][c2]
                
            cont2=0
    


    if mayor_prim1==mayor_prim2:
        print(f"el mayor numero primo de las matrices coinciden y es {mayor_prim1}")
    
    else:
        print(f"los mayores numeros primos de las 2 matrices no coinciden, el mayor numero primo de la primera matriz es {mayor_prim1}, y el de la segunda es {mayor_prim2}")