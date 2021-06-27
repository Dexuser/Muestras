# Solicitar al usuario que ingrese los nombres de pila de los alumnos
# de nivel primario, luego los de nivel secundario, finalizar el
# proceso cuando este ingrese X

primaria = set()
secundaria = set()

print("Curso de primaria, finalize introduciendo x")
while True:
	estudiante = input("Nombre de pila  ")
	if estudiante == "x" or estudiante =="X":
		break
	else:
		primaria.add(estudiante)

print("Curso de secundaria, finalize introduciendo x")
while True:
	estudiante = input("Nombre de pila  ")
	if estudiante == "x" or estudiante =="X":
		break
	else:
		secundaria.add(estudiante)

# Informar los nombres de todos los alumnos de nivel primario y secundario
# sin que se repitan
print("Los estudiantes de primaria son: ")
print(primaria)

print("los estudiantes de secundaria son")
print(secundaria)

# Los nombres que se repiten en ambos cursos
print("Los nombres que se repiten en ambos cursos son")
print(primaria.intersection(secundaria))

# Los nombres de nivel primario que no se repiten en secundaria
print("Los nombres de primaria que no se repiten en secundaria son")
print(primaria.difference(secundaria))