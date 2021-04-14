#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def devolver_promedio(v1, v2, v3):

    promedio= (v1+v2+v3)/3

    return promedio





#bloque  principal

valor1=int(input("introduzca su primer numero :         "))
valor2=int(input("introduzca su segundo numero :        "))
valor3=int(input("Introduzca su tercer numero :         "))

print(f"el promedio de los tres numeros introducidos es igual a : {devolver_promedio(valor1,valor2,valor3)}")