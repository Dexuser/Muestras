# hacer una funcion que calcule la superficie de un rectangulo y la retorne
# la funcion como parametros los valores de 2 de sus lados
# en el bloque principal, cargar los dados de 2 rectagulos y ver cual es mas grande


def superficie_rectangulo(base,altura):     
     superfice=base*altura
     return superfice




# bloque principal

valor1=int(input("introduzca la base del rectangulo:        "))
valor2=int(input("Introduzca la altura del rectangulo:      "))
print()
valor3=int(input("introduzca la base del segundo rectangulo:        "))
valor4=int(input("introduzca la altura del segundo rectangulo:      "))

superficie_1= superficie_rectangulo(valor1,valor2)
superficie_2= superficie_rectangulo(valor3,valor4)

print()
print(f"la superfice del primer rectangulo es {superficie_1},"\
    f" y la del segundo es {superficie_2}")


if superficie_1==superficie_2:
    print("la superficie de ambos rectangulos son la misma")

else:
    
    if superficie_1>superficie_2:
        print("el primer rectangulo tiene la superficie mas grande")
    
    else:
        print("la superficie del segundo rectangulo es la mas grande")


