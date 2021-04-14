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
            m1[i].append(int(input("Fila {}, Columna {}         ".format(i+1, j+1))))
    
    
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()




    for f in range(filas):  
        menores=0                           # aqui se almacenaran los menores de las filas (esta aqui para que se reinicie en cero en cada iteracion)

        for c in range (columnas):

                if m1[f][c]> menores:       # Se recorre la matriz, buscando cual es el numero mas grande en las filas
                    menores=m1[f][c]        # y se guardan en la variable

        for c2 in range (columnas):         # en misma dicha fila

            if m1[f][c2]<menores:           # Se buscara cual es el menor numero de la fila
                menores=m1[f][c2]
        
        print(f"El menor de la fila {f} es el dato {menores} ") # y se printeara

            
