while True:
    try:
        valor1 = int(input("Introduzca su primer valor "))
        valor2 = int(input("introduzca su segundo valor "))
        suma = valor1 + valor2
        print("la suma es igual a : ", suma)
    except ValueError:
        print("solamente introduzca numeros enteros")
        respuesta = input("Desea entrar otro par de valores? [s/n]")
        if respuesta == "n":
            break