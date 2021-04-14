#Calcular el factorial de un número ingresado por teclado.

from math import factorial

num=int(input("Introduzca un entero:    "))
if num>0:
    facto=factorial(num)
    print(f"El factorial del numero {num} es igual a {facto}")

else:
    print("El factorial no esta definido para numeros negativos")