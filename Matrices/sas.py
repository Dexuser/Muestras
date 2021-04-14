#
#    comprobante=False                   # Declaramos el comprobante de la primera matriz
#    acum_1=0                            # Declaramos el acumulador de la primera matriz
#    cont_1=0                            # Declaramos el contador de la primera matriz
#
#
#
#    for f in range (filas):                     # Recorremos la primera matriz
#        for c in range (columnas):
#
#            if m1[f][c] % 10 == 4:              # y si hay algun dato que termine en 4
#                acum_1+= m1[f][c]               # Se le sumara al acumulador
#                cont_1+=1                       # y se contara
#    
#
#
#
#
#    if cont_1>0:                               # esta parte revisa si existen o no existen numeros terminados en 4 en la matriz
#        promedio_1= acum_1 // cont_1            # si exiten, se sacara el promedio del acumulador entre la cantidad de datos
#
#
#
#
#
#        cont_1=0                                # Despues de sacar el promedio reiniciamos el contador para poder reutilizarlo
#
#        for f in range (filas):                 # recorremos la segunda matriz
#            for c in range(columnas):
#
#                if m2[f][c] == promedio_1:      # si la segunda matriz contiene el promedio de la primera matriz lo va contar tantas veces este
#                    cont_1+=1                   
#
#
#        comprobante=True                        # y el comprobante ahora es True
#
#
#    else:
#        print(f"No existen ningun numero terminado en digito 4 en la primera matriz")   # si el contador no tiene ningun numero terminado en 4 lo dira
#
#
#
#   
#
#
#
#
#
#
#
#    #==================================================================================================================================
#    print("\n")
#    #==================================================================================================================================
#
#    comprobante_2=False                             # Tecnicamente es el mismo proceso anterior, solo que primeramente
#    acum_2=0                                    # revisamos si existen numeros terminados en 4 en la segunda matriz
#    cont_2=0                                    # si existen sacara su promedio y recorrera la primera matriz con tal de encontrar el promedio
#
#    for f2 in range (filas):
#        for c2 in range (columnas):
#
#            if m2[f2][c2] % 10 == 4:
#                acum_2+= m2[f2][c2]
#                cont_2+=1
#    
#    if cont_2>0:
#        promedio_2= acum_2 // cont_2
#
#
#
#
#
#
#
#        cont_2=0
#
#        for f2 in range (filas):
#            for c2 in range (columnas):
#
#                if m1[f2][c2] == promedio_2:
#                    cont_2+=1
#
#
#        comprobante_2=True
#
#        
#
#
#
#
#
#
#
#    #==================================================================================================================================
#
#    print("\n")
#
#
#    if comprobante==True:     # La funcion clave del comprobante es habilitar o inhabilitar esta opcion, dependiendo si existen numeros terminados en 4 o no
#
#        if cont_1>=3:
#            print(f"el promedio de los numeros terminados en 4 de la PRIMERA MATRIZ es igual a {promedio_1} y se ha repetido almenos {cont_1} veces en la SEGUNDA MATRiZ")
#
#        elif cont_1==0:
#            print(f"el promedio de los numeros terminados en 4 en la PRIMERA MATRIZ es igual a {promedio_1} y no se encuentra en la SEGUNDA MATRIZ")
#
#        else:
#            print(f"el promedio de los numeros terminados en 4 de la PRIMERA MATRIZ es igual a {promedio_1} y se encuentra repetido menos de 3 veces en la SEGUNDA MATRIZ")
#    
#
#
#
#    else:
#        pass        
#
#
#    #==================================================================================================================================
#    print("\n")
#    #==================================================================================================================================
#
#
#    if comprobante_2==True: # lo mismo sucede aca
#
#
#
#        if cont_2>=3:
#            print(f"el promedio de los numeros terminados en 4 de la SEGUNDA MATRIZ es igual a {promedio_2} y se ha repetido almenos {cont_2} veces en la PRIMERA MATRIZ")
#
#        elif cont_2==0:
#            print(f"el promedio de los numeros terminados en 4 en la SEGUNDA MATRIZ es igual a {promedio_2} y no se encuentra en la PRIMERA MATRIZ")
#
#        else:
#            print(f"el promedio de los numeros terminados en 4 de la SEGUNDA MATRIZ es igual a {promedio_2} y se ha repetido menos de 3 veces en la PRIMERA MATRIZ")
#
#
#
#
#    else:
#        pass