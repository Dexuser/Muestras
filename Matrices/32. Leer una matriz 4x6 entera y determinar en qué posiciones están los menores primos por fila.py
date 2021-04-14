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
            valor=int(input("Fila {}, Columna {}         ".format(i+1, j+1)))
            m1[i].append(valor)
    
    
    print("\n")

    print()
    for fila in m1:
        print("[", end="    ")

        for elemento in fila:
            print("{:6}".format(elemento), end="    ")
        print("]")
    print()



    

    for f in range(filas):

        
        aux=0                               # Declaramos a Aux

        for c in range(columnas):   
            cont=0                      # declaramos al contador
            
            if m1[f][c] <=1:            # los numeros primos tienen que ser mayores que uno
                continue    

            for ind in range(2,m1[f][c]):       # Sacamos los primos
                

                prim= m1[f][c] % ind        
              

                if prim==0:
                    cont+=1
            
            if cont==0 and aux==0:      #Si el dato es primo, y la variable Aux es igual a cero
                aux=m1[f][c]            # aux tomara el valor primo (el bucle va a seguir, para forzar a usar el else)
            
            else:
                if cont==0 and  m1[f][c]<aux:       # Si el dato es primo, y es menor que el valor que tomo aux anteriormente
                    aux= m1[f][c]                   # aux tomara ese valor
                
               
        # En la primera parte, obligamos a que Aux tome un valor primo para poder forzar el Else (lineas 56 y 57)
        # como ya aux tiene valor, podremos hacer la tarea de verificar si es primo y menor que aux,
        # como tenemnos que decir los menores primos de cada fila, aux esta en la identacion de las filas (linea 36) para que cada
        # vez que cambiemos de fila, reiniciemos aux en cero, y podamos volver a repetir el proceso de la linea 56 hasta la linea 61
        # Recuerda leer el codigo, Logicamente, no de manera como lo hace un computador (Es mas bien para aclarar Que hace el computador, y no como lo hace)


            
        if aux==0:
            print(f"en la fila {f} no hay primos")

        else:
            print(f"el menor primo de la fila {f} es {aux}")




            
           




