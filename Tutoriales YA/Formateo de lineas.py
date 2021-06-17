numbers=[]
print("Introduzca todos los valores, introduzca end para mostrar la suma")
while True:
	try:
		value = input("siguiente numero: ")
		if value != "end":
			numbers.append(int(value))
	
		elif value == "end" and len(numbers) == 0:
			print("no se ha introducido algun valor aun")

		else:
			for element in numbers:
				print(f"{element:10}")
			print("-----------")
			print(f"{sum(numbers):10}")
			break
	except ValueError:
		print()
		print("Solamente se admiten numeros y la palabra end")
		print()