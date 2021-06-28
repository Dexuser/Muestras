import psycopg2

conexion = psycopg2.connect(database="Saw", user="postgres", password="nocosttogreat")
cursor = conexion.cursor()
cursor.execute("select * from articulos")
for fila in cursor:
	print(fila)
conexion.close()