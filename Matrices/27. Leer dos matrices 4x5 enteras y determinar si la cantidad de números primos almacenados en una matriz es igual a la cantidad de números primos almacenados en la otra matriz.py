m1=[]
m2=[]

filas=int(input("de cuantas filas quiere sus matrices? :            "))
columnas=int(input("de cuantas columnas quiere sus matrices? :         "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que positivas")

else:

    print("\n")

    #=======================================================================================================================================

    primos1=0
   

    for i in range(filas):
        m1.append([])

        for j in range (columnas):
            valor=int(input("PRIMERA MATRIZ.     Fila {}, Columna {}         ".format(i+1, j+1)))


            if  not valor > 1:
                pass


            else:

                cont=0
                for ind_prim in range(2,valor):
                    
                    prim= valor % ind_prim

                    if prim==0:
                        cont+=1

                if cont==0:
                    primos1+=1
                   

                cont=0




            m1[i].append(valor)


    print("\n")


    primos2=0

    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            valor2=int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}         ".format(x+1, y+1)))




            if  not valor2 > 1:
                pass


            else:
                
                cont2=0
                for ind_prim2 in range(2,valor2):
                    
                    prim= valor2 % ind_prim2

                    if prim==0:
                        cont2+=1

                if cont2==0:
                    primos2+=1
                   

                cont=0


            m2[x].append(valor2)

    #=======================================================================================================================================

    print("\n")

    if primos1 == primos2 and primos1>0 and primos2>0:
        print(f"las 2 matrices tienen la misma cantidad de numeros primos")
    
    elif primos1==0 and primos2==0:
        print(f"ningua de las matrices tienen numeros primos")

    
    else:
        print(f"las 2 matrices no tienen la misma cantidad de numeros primos, la primera matriz tiene {primos1}, mientras que la segunda tiene {primos2}")