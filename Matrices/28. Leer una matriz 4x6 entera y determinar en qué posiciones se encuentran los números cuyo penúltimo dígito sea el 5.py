m1=[]
m2=[]

filas=int(input("De cuantas filas quiere su matriz? :            "))
columnas=int(input("De cuantas columnas quiere su matriz? :         "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.     Fila {}, Columna {}         ".format(i+1, j+1))))

    


    for f1 in range(filas):
        for c1 in range(columnas):

            if m1[f1][c1]<0:

                if ( ( (m1[f1][c1]*(-1) ) % 100 ) )//10==5:
                    print(f"En la fila {f1}, columna {c1} hay un numero cuyo penultimo digito es 5")

            else:
                if (m1[f1][c1] % 100)//10==5:
                    print(f"En la fila {f1}, columna {c1} hay un numero cuyo penultimo digito es 5")


                #print(f"En la fila {f1+1}, columna {c1+1} hay un numero cuyo penultimo digito es 5") de esta manera, queda con la matriz que se muestra en la cosola
                # en el sentido de que no va a comenzar con cero, sino que comenzara con uno cuando se muestre en pantalla






    





