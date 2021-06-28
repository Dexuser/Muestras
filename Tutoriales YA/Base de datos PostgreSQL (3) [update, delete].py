
import psycopg2

conexion  = psycopg2.connect(database="Saw", user="postgres", password="nocosttogreat")
cursor = conexion.cursor()
sql = "delete from articulos where codigo=1"
cursor.execute(sql)
sql = "update articulos set precio=1250 where codigo=3"
cursor.execute(sql)
conexion.commit()

sql = "select * from articulos"
cursor.execute(sql)
for fila in cursor:
	print(fila)
conexion.close()