# Crea 2 matrices usando compresion de listas, verifica si el mayor numero de la primera matriz
# esta presente en la segunda matriz
# nota por lo visto las listas comprimidas aninadas elquivalen a 
"""
# s vendria siendo un iterable

for i in range(s) 
	for x in range(s)

por lo que tengo entendido las listas comprimidas anidadas se vienen leyendo
como si el primer ciclo for fuera el ultimo de unos for anidados, osea como si fuera 

for i in range(s)
	for x in range(s)  este

con esa idea en mente se prodrian hacer las matrices
"""

filas = int(input("De cuantas filas quieres su matriz?  "))
columnas = int(input("de cuantas columnas quiere su matriz   "))

m1 = [[input("1ra Mtiz, inserte una columna  ") for i in range(columnas)] for x in range(filas)]
m2 = [[input("2da Mtiz, inserte una columna  ") for i in range(columnas)] for x in range(filas)]

for fila in m1:
	maximo = max(fila)
	print(maximo)

for fila2 in m2:
	if maximo in fila2:
		print(f"El mayor elemento de la primera matriz es {maximo} y se encuentra en la segunda matriz")

print()
print()
for fila in m1:
	print("[", end="	")
	for elemento in fila:
		print("{:1}".format(elemento), end="	")
	print("]")
print()


print()
for fila in m2:
	print("[", end="	")
	for elemento in fila:
		print("{:1}".format(elemento), end="	")
	print("]")
print()