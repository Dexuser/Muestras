import sqlite3

connection = sqlite3.connect("bd1.db")
cursor = connection.execute("select codigo, descripcion, precio from articulos")
for i in cursor:
    print(i)
connection.close()