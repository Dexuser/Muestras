# Base de datos mySQL (2).py

import mysql.connector


conexion = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="",
                                database="bd test")
aux = conexion.cursor()
aux.execute("show tables")
print(aux)
for tablas in aux:
    print(tablas)
aux.close()