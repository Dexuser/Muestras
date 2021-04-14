
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



    acum_prim_1=0
    cont_prim_1=0

    for f in range (filas):
        for c in range (columnas):

            if m1[f][c]<=1:
                continue

            cont=0

            for ind_prim in range (2,m1[f][c]):

                prim= m1[f][c] % ind_prim


                if prim == 0:
                    cont+=1
            
            if cont==0:
                #print(f"el numero {m1[f][c]} es primo")
                acum_prim_1+= m1[f][c]
                cont_prim_1+=1


    promedio_prim_1= acum_prim_1 // cont_prim_1

 




    comprobante_1=False

    for f in range (filas):
        for c  in range (columnas):

            if m2[f][c] == promedio_prim_1:
                comprobante_1=True
    

    #============================================================================================================================================


    acum_prim_2=0
    cont_prim_2=0

    for f2 in range (filas):
        for c2 in range (columnas):

            if m2[f2][c2]<=1:
                continue

            
            cont2=0

            for ind_prim in range(2,m2[f2][c2]):

                prim= m2[f2][c2]  %  ind_prim

                if prim==0:
                    cont2+=1
            
            if cont2==0:
                acum_prim_2+= m2[f2][c2]
                cont_prim_2+=1
        

    promedio_prim_2= acum_prim_2 // cont_prim_2




    comprobante_2=False

    for f2 in range (filas):
        for c2 in range (columnas):

            if m1[f2][c2] == promedio_prim_2:
                comprobante_2=True

     #============================================================================================================================================


    if comprobante_1==True:
         print(f"el promedio de los numeros primos de la PRIMERA MATRIZ es igual a {promedio_prim_1} y este esta almacenado en la SEGUNDA MATRIZ")
    
    else:
        print(f"El promdio de los numeros primos de la PRIMERA MATRIZ es igual a {promedio_prim_1} y este no se encuentra almacenado en la SEGUNDA MATRIZ")

    
    print("\n")


    if comprobante_2==True:
        print(f"el promedio de los numeros primos de la SEGUNDA MATRIZ es igual a {promedio_prim_2} y este esta almacenado en la PRIMERA MATRIZ")
    
    else:
        print(f"El promedio de los numeros primos de la SEGUNDA MATRIZ es igual a {promedio_prim_2} y este no se encuentra almacenado en la PRIMERA MATRIZ")
