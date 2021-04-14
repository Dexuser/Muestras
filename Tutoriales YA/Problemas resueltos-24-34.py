#Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
#Desarrollar las siguientes funciones:
#1) Cargar por teclado los datos de 4 personas.
#2) Listado completo del diccionario.
#3) Consulta del nombre de una persona ingresando su número de documento.


def carga_documento():
    documentos={}
    for i in range(4):
        num=int(input("Introduzca el numero de documento de la persona:     "))
        nombre=input("Introduzca el nombre de la persona:       ")
        documentos[num]=nombre
        print()
    return documentos


def listado(documentos):
    print("Esta es la lista con todos los  nombres y su numero de documento")
    for clave in documentos:
        print(f"{clave} esta asociado a {documentos[clave]}")


def consulta(documentos):
    num=int(input("numero de documento de la persona buscada:       "))
    if num in documentos:
        print(f"el nombre de la persona es {documentos[num]}")
    else:
        print("no existe ninguna persona con ese numero de documento")







# bloque principal
documentos=carga_documento()
print()
listado(documentos)
print()
consulta(documentos)