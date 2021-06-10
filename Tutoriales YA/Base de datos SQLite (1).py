import sqlite3

connection = sqlite3.connect("bd1.db")

try:
    connection.execute("""create table articulos(
        codigo integer primary key autoincrement,
        descripcion text,
        precio real
        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("la tabla articulos ya existe")
connection.close()