# Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
# Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. 
# Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.


def tablas(numero, termino=10):

    print(f"La tabla del {numero}")
    for i in range(1,termino+1):
        mult= numero*i
        print(mult, end=",")

        # print(f"{numero}  x  {i} = {numero*i}   ",) opcion


# bloque principal

tablas(numero=5)