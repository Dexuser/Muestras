#36. Leer dos matrices 4x6 enteras y determinar si el mayor número almacenado en una de ellas que pertenezca a la Serie de Fibonacci
#  es igual al mayor número almacenado en la otra matriz que pertenezca a la Serie de Fibonacci.

#===========================================================================================================================================================

v1=[]                                                   # Este es el vector que almacenara numeros de fibonacci

aux=0
aux2=1

for fib in range (1,100):

    v1.append(aux)
    suma=aux+aux2
    aux=aux2
    aux2=suma


#===========================================================================================================================================================
m1=[]
m2=[]

filas=int(input("De cuantas filas quiere sus 2 matrices?:           "))
columnas=int(input("De cuantas Columnas quiere sus 2 matrices?:        "))

if filas<=0 or columnas<=0:
    print("las filas y/o columnas tienen que ser positivas")

else:

    print("\n")

    for i in range(filas):
        m1.append([])

        for j in range(columnas):
            m1[i].append(int(input("PRIMERA MATRIZ.     Fila {}, Columna {}         ".format(i+1, j+1))))

    
    print("\n")


    for x in range(filas):
        m2.append([])

        for y in range(columnas):
            m2[x].append(int(input("SEGUNDA MATRIZ.     Fila {}, Columna {}         ".format(x+1, y+1))))
    

    #===========================================================================================================================================================
    print("\n")


    print("Esta es la primera matriz :")
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()



    
    print("\n")                                                 # Esto printea las matrices






    print("Esta es la segunda matriz:")
    print("\n")

    print()
    for fila in m2:
        print("[", end="    ")
        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()

    #===========================================================================================================================================================

    mayor_fib1=0                #Mayor numero fibonacci de la primera matriz

    for f in range(filas):
        for c in range(columnas):

            if v1.count(m1[f][c])>0 and m1[f][c] > mayor_fib1:
                mayor_fib1= m1[f][c]
    

    #print(f"el mayor # fibonacci de la PRIMERA MATRIZ es : {mayor_fib1}")





    print("\n")






    mayor_fib2=0                #Mayor numero fibonacci de la segunda matriz

    for f2 in range(filas):
        for c2 in range(columnas):

            if v1.count(m2[f2][c2])>0 and m2[f2][c2] > mayor_fib2:
                mayor_fib2= m2[f2][c2]
    
   # print(f"el mayor # fibonacci de la SEGUNDA MATRIZ es : {mayor_fib2}")
    


    if mayor_fib1 == mayor_fib2:
        print(f"Los mayores numeros de fibonacci de las matrices son iguales, que es {mayor_fib1}")
    
    else:
        print(f"Los mayores numeros de fibonacci de las matrices son diferentes, El mayor Fibonacci de la PRIMERA MATRIZ es {mayor_fib1}"\
             f", mientras que el de la SEGUNDA MATRIZ es {mayor_fib2}")
