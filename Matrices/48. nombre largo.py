#48. Leer dos matrices 5x5 entera y determinar si el promedio de los mayores elementos que
#pertenecen a la serie de Fibonacci de cada fila de una matriz es igual al promedio de los
#mayores elementos que pertenecen a la serie de Fibonacci de cada fila de la otra matriz


 #==================================================================================================================================
v1=[]
aux=0
axu2=1
for fib in range(1,100):
    
    v1.append(aux)
    suma=aux+axu2
    aux=axu2
    axu2=suma
 #==================================================================================================================================



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



    acum=0
    cont=0

    for f in range (filas):

        mayores=0

        for c in range (columnas):

            if v1.count(m1[f][c])>0 and m1[f][c] > mayores:
                mayores= m1[f][c]
        
        if mayores>0:
            print(f"el mayor Fibonacci de la fila {f} es {mayores}")
            acum+= mayores
            cont+=1


        else:
            print(f"No existen numeros de fibonacci en la fila {f}")

    
    promedio= acum // cont
    

    #==================================================================================================================================
    print("\n")
    #==================================================================================================================================



    acum2=0
    cont2=0

    for f2 in range (filas):

        mayores2=0

        for c2 in range (columnas):

            if v1.count(m2[f2][c2])>0 and m2[f2][c2] > mayores2:
                mayores2= m2[f2][c2]
        
        if mayores2>0:
            print(f"el mayor Fibonacci de la fila {f2} es {mayores2}")
            acum2+= mayores2
            cont2+=1


        else:
            print(f"No existen numeros de fibonacci en la fila {f2}")

    
    promedio2= acum2 // cont2

    #==================================================================================================================================


    if promedio == promedio2:
        print(f"el promedio de los mayores fibonaccis por fila de ambas matrices son iguales, que es {promedio}")
    
    else:
        print(f"el promedio de los mayores fibonaccis por fila de ambas matrices son diferentes, el promedio de la PRIMERA MATRIZ es {promedio}"\
            f" y el de la SEGUNDA MATRIZ es {promedio2}")




