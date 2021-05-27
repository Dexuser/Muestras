
import mysql.connector

conexion = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="bd test")
cursor = conexion.cursor()
cursor.execute("delete from articulos where codigo=3")
cursor.execute("update articulos set articulo='Oscuridad descendiente' where codigo=4")
conexion.commit()
conexion.close()