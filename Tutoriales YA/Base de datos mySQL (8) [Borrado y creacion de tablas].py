import mysql.connector

connection=mysql.connector.connect(host="localhost",
    user="root",
    passwd="",
    database="bd2")

cursor=connection.cursor()
sql="drop table if exists usuarios"
cursor.execute(sql)

sql="""create table usuarios(
            nombre varchar(30) primary key,
            clave varchar(30)
            )"""
cursor.execute(sql)
connection.commit()
connection.close()
