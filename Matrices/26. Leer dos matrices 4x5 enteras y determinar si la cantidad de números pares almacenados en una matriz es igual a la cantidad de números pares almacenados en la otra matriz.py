m1=[]
m2=[]

filas=int(input("de cuantas filas quiere sus matrices? :            "))
columnas=int(input("de cuantas columnas quiere sus matrices? :         "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que positivas")

else:

    print("\n")

    #=======================================================================================================================================

    pares1=0

    for i in range(filas):
        m1.append([])

        for j in range (columnas):
            valor=int(input("PRIMERA MATRIZ.     Fila {}, Columna {}         ".format(i+1, j+1)))

            if valor % 2 == 0:
                pares1+=1

            m1[i].append(valor)


    print("\n")


    pares2=0

    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            valor2=int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}         ".format(x+1, y+1)))

            if valor2 % 2 == 0:
                pares2+=1

            m2[x].append(valor2)

    #=======================================================================================================================================


    print("\n")

    print("esta es la PRIMERA MATRIZ :")

    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()




    
    print("\n")

    print("esta es la SEGUNDA MATRIZ :")

    print()
    for fila in m2:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()


    #=======================================================================================================================================


    if pares1 == pares2 and pares1>0 and pares2>0:
        print("Las 2 matrices tienen la misma cantidad de numeros pares")

    elif pares1==0 and pares2==0:
        print("Ninguna de las 2 matrices contiene numeros pares")
    
    else:
        print(f"Las 2 matrices no tienen la misma cantidad de numeros pares, la primera matriz tiene {pares1} pares mientras que la segunda tiene {pares2} pares")
