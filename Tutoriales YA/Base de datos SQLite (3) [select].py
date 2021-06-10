import sqlite3

connection = sqlite3.connect("bd1.db")
cursor = connection.execute("select descripcion, precio from articulos")
print(cursor)
for i in cursor:
    print(i)
