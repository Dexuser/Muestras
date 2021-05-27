# Base de datos mySQl [select].py

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="bd test")
cursor = conexion1.cursor()
cursor.execute("select codigo, articulo, precio from articulos")
for fila in cursor:
    print(fila)
conexion1.close()