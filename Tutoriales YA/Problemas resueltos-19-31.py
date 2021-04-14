#Confeccionar un programa con las siguientes funciones:
#1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
#2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados 
# y muestre el nombre del empleado con sueldo mayor.
#En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar 
# a la función que muestra el nombre de empleado con sueldo mayor.


def carga():
    Empleado=[]

    v1=input("Introduzca el nombre del empleado:    ")
    Empleado.append(v1)
    v2=int(input("Introduzca el sueldo del empleado:    "))
    Empleado.append(v2)

    Aux=tuple(Empleado)

    return Aux

def mayor_sueldo(data1, data2):

    if data1[1]==data2[1]:
        print("Los sueldos de los dos empleados es el mismo")
    else:
        if data1[1]>data2[1]:
            print(f"el empleado {data1[0]} es quien tiene mejor sueldo, gana {data1[1]}")
        else:
            print(f"el empleado {data2[0]} es quien tiene mejor sueldo, gana {data2[1]}")










#Bloque principal

empleado1=carga()
print(empleado1)
empleado2=carga()

mayor_sueldo(empleado1, empleado2)


