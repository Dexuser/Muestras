from random import randint as booba


def carga():
    palabras=[]
    for i in range(5):
        palabras.append(input("Introduzca una palabra:      "))

    return palabras



def random_word(palabras):
    x= booba(0,4)
    print(palabras[x])








