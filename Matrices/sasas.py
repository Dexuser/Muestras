m1=[]

filas=int(input("Wey fila       "   ))
columnas=(int(input("Wey columna      ")))

print("\n")


for i in range(filas):
    m1.append([])

    for j in range (columnas):
        m1[i].append(int(input("Fila {}, columna {}             ".format(i+1, j+1   ))))


print("\n")

print()
for fila in m1:
    print("[", end="    ")
    for elemento in fila:
        print("{:6}".format(elemento), end="    ")
    print("]")
print()



for f in range (filas):

    mayores=0
    mayor_col=0

    for c in range(columnas):


        if m1[c][f] <=1:
            continue


        cont=0

        for ind_prim in range (2,m1[c][f]):

            prim= m1[c][f] % ind_prim

            if prim==0:
                cont+=1
        
        if cont==0 and m1[c][f] > mayores:

            mayores= m1[c][f]
            mayor_col= c
    
    print(f"el mayor numero primo de la columna {mayor_col} es  {mayores}")

