import mysql.connector

connection=mysql.connector.connect(host="localhost",
    user="root",
    passwd="",
    database="bd test")

cursor=connection.cursor()
sql="insert into articulos(articulo, precio) values(%s, %s)"
data=[
    ("Largo agijon", 320.5),
    ("Marca del orgullo", 200),
    ("Alma del monarca", 600),
    ("Forma de Unn", 32.14)
    ]
cursor.executemany(sql, data)
print("el ultimo codigo autoincrement es :", cursor.lastrowid)
connection.commit()
connection.close()
