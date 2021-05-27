import mysql.connector

connection=mysql.connector.connect(host="localhost",
    user="root",
    passwd="")

cursor=connection.cursor()
sql="drop database if exists pruebas"
cursor.execute(sql)

sql="create database bd2"
cursor.execute(sql)

sql="use bd2"
cursor.execute(sql)

sql="""create table usuarios (
            nombre varchar(30) primary key,
            clave varchar(30)
    )"""
cursor.execute(sql)

connection.commit()
connection.close()
