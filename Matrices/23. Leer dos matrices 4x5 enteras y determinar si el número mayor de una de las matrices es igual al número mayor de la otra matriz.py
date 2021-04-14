m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices? :              "))
columnas=int(input("de cuantas columnas quiere sus 2 matrices? :           "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:
    
    num_mayor1=-30000

    print("\n")

    for i in range(filas):
        m1.append([])

        for j in range (columnas):
            valor=int(input("Primera matriz.    Fila {}, Columna {}             ".format(i+1,j+1)))

            if valor>num_mayor1:
                num_mayor1=valor

            m1[i].append(valor)
    

    print("\n")

    num_mayor2=-40000

    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            valor2=int(input("Segunda matriz.      Fila {}, Columna {}          ".format(i+1, j+1)))

            if valor2>num_mayor2:
                num_mayor2=valor2

            m2[x].append(valor2)
        


    #==================================================================================================================================

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

    #==================================================================================================================================


    if num_mayor1==num_mayor2:
        print(f"El numero mas grande de las mastrices coinciden y es {num_mayor1}")
    
    else:
        print(f"el numero mas grande de las matrices NO coinciden, el numero mas grande de la primera matriz es {num_mayor1} y el de la segunda es {num_mayor2}")
