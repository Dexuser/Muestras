
def carga_cuadrado():
    print("Funcion que pide un numero y muestra su cuadrado")
    print()
    num=int(input("Introduzca un numero     "))

    print(f"el cuadrado de {num} es {num**2}")



def carga_productos():
    print("Funcion que pide 2 numeros y muestra el productos de estos")

    valor1=int(input("Introduzca su primer numero    "))
    valor2=int(input("Introduzca su segundo numero   "))

    producto= valor1 * valor2

    print(f"el producto de {valor1} por {valor2} es igual a {producto}")



#programa-1

carga_cuadrado()
print("\n")
carga_productos()

