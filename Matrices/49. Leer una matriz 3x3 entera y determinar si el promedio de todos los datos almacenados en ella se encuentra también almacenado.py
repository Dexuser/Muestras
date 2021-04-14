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






    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================

    print("Esta es la  matriz")

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


    acum=0
    cont=0

    for f in range (filas):
        for c in range(filas):
            
            acum+= m1[f][c]
            cont+=1
    

    promedio= acum //  cont
    #==================================================================================================================================

    comprobante=False
    for f in range (filas):
        for c in range (filas):

            if m1[f][c]==promedio:

                comprobante=True
    


    if comprobante==True:
        print(f"el promedio de los datos de la matriz es {promedio} y este se encuentra almacenado en la misma matriz")
    else:
        print(f"el promedio de los datos de la matriz es {promedio} y este no se encuentra almacenado en los datos de la matriz")