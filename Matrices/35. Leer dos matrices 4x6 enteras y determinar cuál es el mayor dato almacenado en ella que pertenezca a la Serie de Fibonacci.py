v1=[]

aux=0
aux2=1

for fib in range (1,100):
    
    v1.append(aux)
    suma=aux+aux2
    aux=aux2
    aux2=suma

print(v1)
#=================================================================================================================================


filas=int(input("De cuantas filas quiere sus 2 matrices? :               "))
columnas=int(input("de cuantas columnas quiere sus 2 matrices? :            "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:  

    print("\n")
    
    m1=[]
    m2=[]
   
  

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            valor=int(input("PRIMERA MATRIZ.     Fila {}, Columna {}         ".format(i+1, j+1)))
            m1[i].append(valor)
    

    print("\n")


    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            valor2=int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}         ".format(x+1, y+1)))
            m2[x].append(valor2)

    #=================================================================================================================================

    print("Esta es la primera matriz :")
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()





    print("\n")



    print("Esta es la segunda matriz :")
    print("\n")

    print()
    for fila in m2:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()
    
    #=================================================================================================================================


    mayor1=0

    for f in range(filas):
        for c in range (columnas):

            if v1.count(m1[f][c]) > 0 and m1[f][c] > mayor1:
                mayor1= m1[f][c]
    


    mayor2=0

    for f2 in range (filas):
        for c2 in range (columnas):

            if v1.count(m2[f2][c2]) > 0 and m2[f2][c2] > mayor2:
                mayor2= m2[f2][c2]

    

    if mayor1>0 and mayor2>0:
        print(f"El mayor numero de fibonnaci de la primera matriz es {mayor1}, mientras que el de la segunda matriz es {mayor2}")
    
    elif mayor1>0 and mayor2==0:
        print(f"el mayor numero de fibonnaci de la primera matriz es {mayor1}, mientras que las segunda matriz no contiene numeros de fibonacci")
    
    elif mayor1==0 and mayor2>0:
        print(f"la primera matriz no contiene numeros de fibonacci, mientras que la segunda matriz contiene {mayor2} numeros de fibonacci")
    
    else:
        print(f"Ninguna de las 2 matrices contiene numeros de fibonacci.")

    

            
    
        