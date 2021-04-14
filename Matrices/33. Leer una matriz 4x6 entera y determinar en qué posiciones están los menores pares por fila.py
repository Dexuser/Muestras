m1=[]

filas=int(input("De cuantas filas va a querer su matriz? :          "))
columnas=int(input("de cuantas columnas va a querer su matriz? :       "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range (filas):
        m1.append([])

        for j in range (columnas):
            valor=int(input("Fila {}, Columna {}         ".format(i+1, j+1)))
            m1[i].append(valor)
    
    
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()



    for f in range(filas):
        aux=0                       # Declaramos aux

        for c in range (columnas):

            if m1[f][c] % 2==0 and aux==0:      # esta parte fuerza a darle un valor par a Aux
                aux=m1[f][c]
            
            else:                                           # cuando un se tome otro valor de la matriz, se va a tomar siempre el else
                if m1[f][c] % 2==0 and m1[f][c] < aux:      # y se preguntara si el numero es par, si lo es, se preguntara si es menor y al valor
                    aux=m1[f][c]                            # anterior de aux, y si lo es lo tomara



            



        if aux==0:
            print(f"en la fila {f} no hay numeros pares")
        
        else:
            print(f"el menor numero par de la fila {f} es {aux}")


