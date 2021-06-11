import sqlite3

connection = sqlite3.connect("bd1.db")
precio = float(input("Introduzca un precio:  "))
cursor = connection.execute("select codigo, descripcion, precio from articulos where precio<?", (precio,))
filas = cursor.fetchall()
print(filas)
for i in filas:
	print(i)
connection.close()
