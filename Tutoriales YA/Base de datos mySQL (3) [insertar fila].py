# Base de datos mySQL (3) [insertar filas].py

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="bd test")
cursor = conexion1.cursor()
sql = "insert into articulos(articulo, precio) values (%s, %s)"
datos = ("Aguijon puro", 500)
cursor.execute(sql, datos)
datos = ("Corazon de cristal", 200)
cursor.execute(sql, datos)
datos = ("Alas del monarca", 250)
cursor.execute(sql, datos)
conexion1.commit()
conexion1.close()