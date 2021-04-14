m1=[]
v1=[]

filas=int(input("De cuantas filas quiere su matriz? :           "))
columnas=int(input("De cuantas columnas quiere su matriz? :        "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")


    for i in range (filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("Fila {}, Columna {}         ".format(i+1, j+1))))



    print("\n")



    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()



    cont=0

    for F in range(filas):
        for C in range (columnas):
            
           

            for f2 in range(filas):
                for c2 in range(columnas):

                    if m1[F][C] == m1[f2][c2]:
                        cont+=1
                
            if cont>=3 and v1.count(m1[F][C])==0:
                print(f"el dato {m1[F][C]} se ha repetido 3 o mas veces en la matriz")
                v1.append(m1[F][C])
                
            cont=0

       
               
                
                


