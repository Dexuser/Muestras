# Base de datos mySQL
import mysql.connector


conexion = mysql.connector.connect(host="localhost", user="root", passwd="")
auxiliar = conexion.cursor()
auxiliar.execute("show databases")
for bases in auxiliar:
    print(bases)
auxiliar.close()