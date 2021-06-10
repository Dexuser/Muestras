import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect("bd1.db")
connection.execute("insert into articulos(descripcion, precio) values (?,?)", ("Aguijon Roma", 50))
connection.execute("insert into articulos(descripcion, precio) values (?,?)", ("Aguijon afilado", 250))
connection.execute("insert into articulos(descripcion, precio) values (?,?)", ("Aguijon estilizado", 800))
connection.execute("insert into articulos(descripcion, precio) values (?,?)", ("Aguijon en espiral", 2000))
connection.execute("insert into articulos(descripcion, precio) values (?,?)", ("Agujion Puro", 4000))
connection.commit()
connection.close()