# Sueldos de unas personas.

def sueldos():
    suel=[]         # en esta lista se guardara los sueldos de los empleados
    empleado=[]     # en esta lista se guardara los nombres de los empeados

    for i in range(10):                                         
        valor=input("Introduzca un empleado:    ")              # Se toma el nombre del empleado
        empleado.append(valor)                                  # se le agrega ala lista de empleados
        valor2=int(input("Introduzca el sueldo :     "))        # se toma el sueldo de dicho empleado
        suel.append(valor2)                                     # se le agrega ala lista de los sueldos de los empleados
        print()
    
    return [empleado, suel]                     # se retorna en modo de lista, las listas de los empleados y la lista de los sueldos (go to line 52)



def mostrar_sueldo(persona, pago):                                 

    for i in range(len(persona)):                                   # Se recorrera el contenido del parametro persona usando como indice I (lista_empleados)
        print(f"al empleado {persona[i]} se le paga : {pago[i]}")   # Y se printeara el nombre y su pago (lista_sueldo) [Se recorren ambas listas con I]
        



def sueldo_superior(persona, pago):                                         # go to line 56
    for i in range(len(persona)):                                               # recorremos el parametro persona (que es la lista de empleados)
        if pago[i]>4000:                                                        # y si su sueldo es mayor a 4000 (el sueldo del empleado esta en la misma posicion)
            print(f"el empleado {persona[i]} se le paga mas de 4000 pesos")     # lo printeamos



def promedio_sueldo(sueldo):            # go to line 58
    acum=0                              # Se declara un acumulador quien va a sumar todos los sueldos 
    for i in range(len(sueldo)):        # Se recorre la lista de los sueldos usando como indice I (lista sueldos)
        acum+= sueldo[i]                # y le sumamos al acumular cada uno de los sueldos 
    promedio= acum/10                   # Se saca el promedio
    print(f"El promedio de los sueldos introducidos es igual a {promedio}")     # Se printea ala pantalla
    return promedio                                                             # y se retorna ala variable promedio





def promedio_inferior(promedio):       # go to line 60
    
    for i in range(len(lista_empleados)):       # recorremos la lista de los empleados

        if lista_sueldos[i] < promedio:         # y si el sueldo de dicho empleado es menor que el promedio (el sueldo y el empleado estan en la misma posicion en ambas listas)
            print(f"el sueldo de {lista_empleados[i]} esta por debajo del promedio")    # se printea



# bloque principal

lista_empleados, lista_sueldos= sueldos()               # En estas variables se guardan el retorno de la funcion (sigue leyendo abajo)
print()
mostrar_sueldo(lista_empleados,lista_sueldos)  # con las dos variables anteriores se rellenan los parametros persona y pago de esta funcion (go to line 18)
print()
sueldo_superior(lista_empleados,lista_sueldos) # rellenamos los parametros persona y pago (go to line 26 again)
print()
promedio=promedio_sueldo(lista_sueldos)         # rellenamos el parametro sueldo (go to line 33 again) y cuando se nos retorne el promedio, 
print()                                         # guardarlo en la variable
promedio_inferior(promedio)                     # Se rellena el parametro de la funcion, el promedio que tenemos guardado en la variable promedio