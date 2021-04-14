#47. Leer dos matrices 5x5 enteras y determinar si el promedio de los mayores números primos por
#cada fila de una matriz es igual al promedio de los mayores números primos por cada columna
#de la otra matriz.


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




    print("\n")



    for x in range (filas):
        m2.append([])

        for y in range (columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}             ".format(x+1, y+1))))

    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================

    print("Esta es la primera matriz")

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

    print("Esta es la Segunda matriz")

    print()
    for fila in m2:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #==================================================================================================================================




    #primera parte / filas de la primera matriz

    acum_prim_1=0                   # declaramos el acumulador,                  
    cont_prim_1=0                   # y el contador

    for f in range (filas):        

        mayor_prim_1=0              # Declaramos esta variable en la sangria de filas para que se reinicie cada vez que cambiemos de fila
        

        for c in range (columnas):  

            if m1[f][c]<=1:             # los primos son mayores que uno, todos los datos que no cumplan esto son descartados
                continue
            



            cont=0                                  # el contador nos verifica si el dato de la matriz es primo

            for ind_prim in range (2,m1[f][c]):     # y este bucle, va a buscar si el dato tiene otros divisores aparte del uno y el mismo

                prim= m1[f][c] % ind_prim

                if prim==0:
                    cont+=1
            
            if cont==0 and m1[f][c] > mayor_prim_1:         # si el dato es primo, y es mas grande que la variable mayores primos (mayor_prim_1,)
                mayor_prim_1 = m1[f][c]                     # lo almacenara en dicha variable 


        
        if mayor_prim_1!=0:                                              # si el mayor primo de esa fila es difernte de cero
            print(f"el mayor primo de la fila {f} es {mayor_prim_1}")       # se printea
            acum_prim_1+= mayor_prim_1                                  # se le suma el dato al  acumulador
            cont_prim_1+=1                                          # y se cuenta esa suma


    else:
        print(f"en la fila {f} no existen numeros primos")      # sino, avisamos que no exiten primos, y por ende, no se suma ni se cuentan datos

        
    print()


    
    promedio_prim_1= acum_prim_1 // cont_prim_1                 # Sacamos el promedio
    print(f"el promedio de los mayores numeros primos por fila de la primera matriz es igual a {promedio_prim_1}")
    print()



















    acum_prim_1=0               # Primera parte /columnas de la segunda matriz
    cont_prim_1=0   

    for f in range (filas):     
        
        mayores=0                   # declaramos a mayores
        mayor_col=0                 # y a mayor columna
        
        for c in range (columnas):

            if m2[c][f] <=1:            # los numeros primos tienen que ser mayores que uno
                continue                # para recorrer columnas, y no filas, basta con invertir sus lugares, para que recorramos columnas y no filas
            


            cont=0                                  

            for ind_prim in range (2,m2[c][f]):

                prim= m2[c][f] % ind_prim

                if prim==0:
                    cont+=1
            
            if cont==0 and m2[c][f] > mayores:
                
                mayores= m2[c][f]
                mayor_col= f

        if mayores!=0:
            print(f"el mayor numero primo de las columna {mayor_col} de la segunda matriz es {mayores}")
            acum_prim_1+= mayores
            cont_prim_1+=1
        

        else:
            print(f"en la columna {f} no existen numeros primos")

    print()


    promedio_prim_2=  acum_prim_1 // cont_prim_1
    print(f"el promedio de los mayores primos por columna de la SEGUNDA MATRIZ es igual a a {promedio_prim_2}")
    print()










    if promedio_prim_1 == promedio_prim_2:
        print(f"El promedio de la PRIMERA y SEGUNDA matriz son iguales")
    
    else:
        print(f"el promedio de los mayores primos por fila de la PRIMEA MAITRZ es diferente al promedio de los mayores primos por columnas de la SEGUNDA Matriz")
    

    #=================================================================================================================================================================


    #tecnicamente, esto es lo mismo de arriba, pero que menos de la primera matriz ala segunda, es la segunda matriz ala primera



    promedio_prim_2=0
    promedio_prim_1=0

    print("\n")
    print("\n")
    print("Segunda parte")
    print("\n")




    # Segunda parte, filas de la segunda matriz






    acum_prim_2=0
    cont_prim_2=0

    for f2 in range (filas):

        mayor_prim_2=0

        for c2 in range (columnas):

            if m2[f2][c2]<=1:
                continue
            


            cont2=0

            for ind_prim in range (2,m2[f2][c2]):

                prim= m2[f2][c2] % ind_prim

                if prim==0:
                    cont2+=1
            
            if cont2==0 and m2[f2][c2] > mayor_prim_2:
                mayor_prim_2 = m2[f2][c2]
        
        if mayor_prim_2!=0:
            print(f"(Segunda matriz)  el mayor primo de la fila {f2} es {mayor_prim_2} ")
            acum_prim_2+= mayor_prim_2
            cont_prim_2+=1
        
        else:
            print(f"en la fila {f2}, no existen numeros primos")

    print()


    promedio_prim_2= acum_prim_2 // cont_prim_2
    print(f"El promedio de los mayores numeros primos por fila de la SEGUNDA MAITRZ es igual a {promedio_prim_2}")
    print()












    # Segunda parte / columnas de la primera matriz

    acum_prim_2=0
    cont_prim_2=0

    for f2 in range (filas):

        mayor_col_2=0
        mayores_2=0

        for c2 in range (columnas):

            if m1[c2][f2]<=1:
                continue
            


            cont2=0

            for ind_prim in range (2,m1[c2][f2]):

                prim= m1[c2][f2] % ind_prim

                if prim==0:
                    cont2+=1
            
            if cont2==0 and m1[c2][f2] > mayores_2:
                mayores_2= m1[c2][f2]
                mayor_col_2= f2
        
        if mayores_2:
            print(f"(SEGUNDA MATRIZ) el mayor numero primo de la columna {mayor_col_2} de la PRIMERA MATRIZ es {mayores_2}")
            acum_prim_2+= mayores_2
            cont_prim_2+=1
        
        else:
            print(f"(SEGUNDA MATRIZ) en la columna {mayor_col_2} de la PRIMERA MATRIZ no existen numeros primos")


    print()

    promedio_prim_1= acum_prim_2 // cont_prim_2
    print(f"(SEGUNDA MATRIZ) el promedio de los mayores primos por columna de la PRIMERA MATRIZ es igual a {promedio_prim_1}")
    print()








    if promedio_prim_2 == promedio_prim_1:
        print("(SEGUNDA MATRIZ), el promedio de la SEGUNDA Y PRIMERA matriz son iguales")
    
    else:
        print(f"El promedio de los mayores primos por fila de la SEGUNDA MATRIZ"\
            "es diferente al promedio de los mayores primos por columnas de la PRIMERA MATRIZ")

