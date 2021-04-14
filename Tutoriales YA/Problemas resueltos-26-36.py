#Crear un diccionario en Python para almacenar los datos de empleados de una empresa.
#La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
#Desarrollar las siguientes funciones:
#1) Carga de datos de empleados.
#2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
#3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"




def carga():
    empleados={}

    continuar="s"                                                               # mantenemos el bucle pidiendoselo al usuario
    while continuar=="s":
        legajo=int(input("Legado del empleado:  "))
        nombre=input("Nombre del empleado:      ")
        profesion=input("Profesion:             ")
        sueldo=float(input("Sueldo:             "))
        empleados[legajo]= [nombre, profesion, sueldo]                          # es una lista para poder modificar el sueldo
        print()
        continuar=input("Desea agregar otro empleado?  R:[s/n]      ")

    return empleados


def cambiar_sueldo(empleados):

    legajo=int(input("Introduzca el legajo a buscar:    "))
    if legajo in empleados:
        new_suel=float(input("Introduzca el nuevo sueldo:       "))     # Nuevo sueldo
        empleados[legajo][2]=new_suel
    else:
        print("No existe ningun empleado con ese legajo")
        


def mostrar_datos(empleados):
    print("Nombre y sueldo de todos los analistas de sistemas de la empresa:    ")
    for legajo in empleados:
        aux= empleados[legajo][1].lower()           # Usamos lower para poder compararlo con aux, osea, volvemos el string minusculo
        if aux=="analista de sistemas":
                print(empleados[legajo][0], empleados[legajo][2])














# bloque principal
empleados=carga()
print()
print("Lista de empleados antes de cambiar los sueldos")
for elementos in empleados:
    print(elementos, empleados[elementos])
print()


cambiar_sueldo(empleados)
print()
mostrar_datos(empleados)