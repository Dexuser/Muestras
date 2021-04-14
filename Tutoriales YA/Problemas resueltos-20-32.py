#Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
#El programa debe tener las siguientes funciones:
#1)Carga de los nombres de empleados y sus últimos tres sueldos.
#2)Imprimir el monto total cobrado por cada empleado.
#3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
#Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
#empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]




def carga_empleado():
    empleado=[]

    for i in range(5):

        empleado.append([])
        v1=input("Introduzca el nombre del empleado:    ")
        empleado[i].append(v1)


        suel1=int(input("Introduzca el primer sueldo del empleado:      "))
        suel2=int(input("Introduzca el segundo sueldo del empleado:      "))
        suel3=int(input("Introduzca el tercer sueldo del empleado:      "))

        empleado[i].append( (suel1, suel2, suel3) )

        print()
    

    return empleado




def monto_sueldoempleado(datos):            

    pagos_emple=[]
    

    for y in range( len(datos) ):        # Se recorre la lista principal  por su longitud (Asi llegamos a cada Sub lista)
        monto_empleado=0            
        for x in range( len(datos[y])+1 ):      # Se recorre la la sublista (la que tenga el mismo subindice igual que el INDICE DEL FOR ANTERIOR) usando su longitud mas uno
            
            monto_empleado+= datos[y][1][x]       # Entonces, se suma los datos, (Explicacion detallada abajo)

        print(f"El monto del trimestre pagado a {datos[y][0]} es igual a {monto_empleado} ")    #Printeamos

        aux=monto_empleado                          # Asignamos a una variable Auxiliar para que tome el valor que tiene el monto_empleado ahora mismo
        pagos_emple.append(aux)                     # y agreamos el valor de Aux ala lista de pagos_emple
    
    return pagos_emple                              # Retornamos la lista con los pagos de los empleados 



def trimestre(sueldos,datos):                       #go to line(82)
    for i in range( len(sueldos) ):                 # recorremos la lista de los sueldos, en base a su longitud
        if sueldos[i]>10000:                        # si el sueldo es mayor a 10,000
            print(f"A {datos[i][0]} se le paga mas de 10000, gana: {sueldos[i]}")   # lo printeamos
















# bloque principal

trabajador=carga_empleado()
print(trabajador)
sueldos=monto_sueldoempleado(trabajador)
print()
trimestre(sueldos,trabajador) # llamamos ala funcion y le entregamos los parametros  sueldos, que tiene los suelos de los empleados, y trabajador, la lista
# con el nombre y el trimestre de los empleados. go to line(57)









# Primero que nada para simplificar la explicacion: llamaremos ala funcion carga_empleado, donde rellenaremos los datos y 
# lo cuardaremos a una variable llamada trabajador, introduciremos los siguientes datos:

#   [ ['luis', (1500, 2000, 2500)], ['Bryan', (3000, 3500, 4000)] ]

# Como puedes apreciar, es una lista anidada por 2 listas que son sublistas, a su vez estas sublistas estan anidadas por tuplas.
# Esta informacion se la pasaremos al parametro datos de la funcion  monto_sueldoempleado
# el proposito de esta funcion es el de mostrar el monto total del trimestre pagado a un emplereado de la empresa.
# en la lista anidada que llamare ahora como Macrolista, esta la informacion de los trabajodres, contenidas en las sublistas
# Esta el nombre del empleado, y a su vez en una TUPLA, los sueldos pagados a dichos empleados, Wala!, Ahi esta nuestro objetivo.
# Como Sacamos los sueldos  que estan contenidas en la tuplas de las sublistas de la macrolista?, wala, eso intentare explicar detalladamente.

# Recordemos que todos los datos de una lista tienen un indice que marca su lugar en la lista, con esto es que podremos sacarlos.
# y esto no excluye las listas anidadas.

# si apreciamos bien, la lista anterior, podemos descomponerlas en 3 indicess que nombrare, el macroindice (que es de la macrolista obviamente)
# el subindice (Indice de los datos contenidos en la Sublista de la Macro lista), y por el ultimo.... el T-indice (osea, el indice que marca el lugar 
# de los datos de la tupla)

#                      [      ['luis', (1500, 2000, 2500)]         ,            ['Bryan', (3000, 3500, 4000)]   ]
#                           |                             |                   |                              |
#                           ///////////////////////////////                  /////////////////////////////////
# Macro indices                            0                                                 1
# los macros indices, senalan la posicion de las Sublistas en la mactro lista


#                       [   'luis'     ,   (1500, 2000, 2500)    ]         ,       [    'Bryan'    ,   (3000, 3500, 4000)     ] 
#                        /////////////     //////////////////                           //////         //////////////////     
#  sub indices                0                    1                                      0                     1
# Los sub indices, denominan el lugar de los elementros de una sub lista


#                           (1500   ,   2000   ,   2500)                             ,             (3000   ,   3500,    4000)
#                           /////       ////       ////                                             ////       ////     ////
# T-indices                  0           1           2                                               0           1        2


# Ya con la mactro lista, descompuesta en sus indices, podemos llamar a datos Especificos dentro de la mactro lista.
# Ejemplo:

#     Quiero ver a sub lista que tenga el empleado luis. Como lo hago?:
# lo haremos llamando su posicion en la Mactro lista, osea usando su Macro indice:
# print( Empleado[0] ) al hacer esto, se nos debera mostrar en pantalla la sublista :   ['luis', (1500, 2000, 2500)]


# Quiero ver el sueldo pagado del trimestre de bryan:
# print ( Empleado[1][1] ) se nos debera  mostrar:       (3000, 3500, 4000)
# # esto es porque especificamos su  lugar
# Empleado[1] en la posicion  1, de la macrolista,  emplreado[1][1] en la posicion 1 de la sublista       
#


# quiero ver el sueldo pagado en el primer trimestre de luis:
# print(empleado[0][1][0])
# empleado[0] en la posicion 0 de la macrolista,  empleado[0][1], en la posicion 1 de la sublista, empleado[0][1][0], en la posicion 0 de la tupla
