#Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
#Debe mostrar un menú con las siguientes opciones:
#1- Carga de un contacto en la agenda.
#2- Listado completo de la agenda.
#3- Consulta ingresando el nombre de la persona.
#4- Modificación de su teléfono y mail.
#5- Finalizar programa.

class Agenda:

    def __init__(self):
        self.contactos={}
    
    def menu(self):
        opcion=0
        while opcion!=5:
            print("[1]- agregar un contacto")
            print("[2]- listado de los contactos")
            print("[3]- consultar a un contacto")
            print("[4]- modificar telefono y mail de un contacto")
            print("[5]- Finalizar el programa")
            opcion=int(input("Opcion: "))

            if opcion==1:
                self.carga()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificar()
    
    def carga(self):
        print("______________________________________")
        nombre=input("Nombre del contacto:  ")
        telf=int(input("Numero del contacto:  "))
        email=input("Email del contacto:   ")
        self.contactos[nombre]=(telf, email)
        print("______________________________________")
    
    def listado(self):
        print("______________________________________")
        for nombre in self.contactos:
            print(f"nombre: {nombre}, telf: {self.contactos[nombre][0]}, email: {self.contactos[nombre][1]}")
        print("______________________________________")

    def consulta(self):
        print("_______________________________________")
        nombre=input("Nombre de la persona a consultar:     ")
        if nombre in self.contactos:
            print(f"nombre: {nombre}, telf: {self.contactos[nombre][0]}, email: {self.contactos[nombre][1]}")
        else:
            print("No existe ningun contacto con ese nombre")
    
    def modificar(self):
        nombre=input("nombre del contacto a modificar: ")
        telf=int(input("Nuevo telefono:     "))
        email=input("nuevo correo:      ")
        if nombre in self.contactos:
            self.contactos[nombre]=(telf, email)
        else:
            print("No existe ningun contacto con ese nombre")


# Bloque principal:
Agenda=Agenda()
Agenda.menu()
Agenda.listado()

