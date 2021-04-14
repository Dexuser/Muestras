#Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno.
#Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
#Crear las siguientes funciones:
#1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
#2) Listado de todos los alumnos con sus notas
#3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.




def carga():
    alumnos={}

    for i in range(3):
        dni=int(input("Introduzca el DNI del estudiante:    "))

        materias=[]
        continuar="S"
        while continuar=="S":
            mat=input("materia que cursa el estudiante:     ")
            nota=int(input("Nota de dicha materia       "))
            materias.append( (mat,nota) )
            print()
            continuar=input("Desea agregar otra materia? R[S/N]:   ")
            print()

        alumnos[dni]=materias

    return alumnos



def listado(alumnos):

    for estudiante in alumnos:
        print(f"las materias que cursa el estudiante de DNI {estudiante}, y sus notas")
        for materia, nota in alumnos[estudiante]:
            print(f"en {materia} tiene {nota} como nota")
        print()  
         

def consulta(alumnos):
    dni=int(input("Introduzca el DNI del estudiante buscado     "))

    if dni in alumnos:
        print(f"las materias que cursa y sus notas son:")
        for materia, nota in alumnos[dni]:
            print(f"en {materia} tiene {nota} como nota")
        
    
    else:
        print("No existe ningun Alumno con ese DNI")



# bloque principal.
alumnos=carga()
print(alumnos)
listado(alumnos)
print()
consulta(alumnos)

        