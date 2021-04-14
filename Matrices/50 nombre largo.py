#50. Leer una matriz 5x5 y determinar si el promedio de los elementos que se encuentran en su
#diagonal está almacenado en ella. Mostrar en pantalla en qué posiciones exactas se encuentra
#dicho dato.


m1=[]
filas=int(input("De cuantas filas quiere su matriz?:              "))
columnas=int(input("De cuantas columnas quiere su matriz?:          "))

if filas<=0 or columnas<=0:
    print(f"las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range (filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("Fila {}, Columna {}         ".format(i+1, j+1))))



    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================


    acum=0
    cont=0

    for f in range(filas):
        
        acum+= m1[f][f]
        cont+=1
    

    promedio= acum // cont

    #==================================================================================================================================

    mayor_fila=0
    mayor_columna=0

    comprobante=False
    for f in range (filas):
        for c in range (columnas):

            if m1[f][c] == promedio:
                comprobante= True
                mayor_fila= f
                mayor_columna= c


    if comprobante==True:
        print(f"el promedio de la diagonal de la matriz es {promedio} y este promedio se encuentra en la posicion: Fila {mayor_fila}, columna {mayor_columna}")
    
    else:
        print(f"el promedio de la diagonal de la matriz es {promedio} y este no se encuenta en la matriz")



    
