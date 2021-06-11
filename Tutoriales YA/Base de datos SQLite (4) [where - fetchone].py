import sqlite3

connection = sqlite3.connect("bd1.db")
codigo = int(input("Introduzca el codigo del articulo a consultar "))
cursor = connection.execute("select codigo,descripcion, precio from articulos where codigo<?", (codigo,))
fila = cursor.fetchone()
while True:
	print("uno por uno")
	print(fila)
	fila = cursor.fetchone()
	respuesta = input("Desea continuar en la proxima fila de la base? [s/n] \n")
	if respuesta == "n":
		break
connection.close()