#Definir una función que cargue una lista con palabras y la retorne.
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.


def carga_palabras():
    palabras=[]
    cantidad=int(input(f"Cuantas palabras quieres introducir?:   "))

    for i in range(cantidad):
        palabra=input("Introduzca su palabra:       ")
        palabras.append(palabra)


    return palabras

def caracteres_mayor5(texto):

    print("Todas las palabras que poseen mas de 5 caracteres:")
    for elemento in texto:
        if len(elemento)>5:
            print(elemento)






# bloque principal

palabras=carga_palabras()
print()
caracteres_mayor5(palabras)