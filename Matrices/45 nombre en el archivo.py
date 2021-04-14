# 45. Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números mayores de
#cada fila de una matriz es igual al promedio de los números mayores de cada fila de la otra
#matriz.

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


    print()
    for fila in m2:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #==================================================================================================================================

    acum_mayor_1=0
    cont_mayor_1=0
    
    for f in range (filas):

        mayores=0

        for c in range (columnas):

            if m1[f][c] > mayores:
                mayores= m1[f][c]
        
        acum_mayor_1+= mayores
        cont_mayor_1+=1

      #  print(f"el mayor numero de la fila {f} es {mayores}")
    


    promedio_mayor_1= acum_mayor_1 // cont_mayor_1
  #  print(f"el promedio de los numeros mayores de la primera matriz es {promedio_mayor_1}")

    #==================================================================================================================================


    acum_mayor_2=0
    cont_mayor_2=0

    for f2 in range (filas):
        
        mayores2=0

        for c2 in range (columnas):

            if m2[f2][c2] > mayores2:
                mayores2= m2[f2][c2]
        
        acum_mayor_2+= mayores2
        cont_mayor_2+=1

    #    print(f"el mayor numero de la fila {f2} de la segunda matriz es {mayores2}")
    

    promedio_mayor_2= acum_mayor_2 // cont_mayor_2
   # print(f"el promedio de los numeros mayores de la Segunda matriz es {promedio_mayor_2}")

   #==================================================================================================================================

    if promedio_mayor_1 == promedio_mayor_2:

       print(f"el promedio de Ambas matrices es igual a a {promedio_mayor_1}")
    
    else:
        print(f"El promedio de ambas matrices son diferentes, el promedio de la primera matriz es {promedio_mayor_1} y el de la segunda es {promedio_mayor_2}")