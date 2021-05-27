import mysql.connector

connection=mysql.connector.connect(host="localhost",
        user="root",
        passwd="",
        database="bd test")
cursor=connection.cursor()
sql="insert into articulos(articulo,precio) values (%s, %s)"
data=("Coraza de Baldur", 60)
cursor.execute(sql, data)
print("el ultimo codigo autoincrement generado es :", cursor.lastrowid)
connection.commit()
connection.close()

