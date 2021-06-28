import psycopg2

conexion = psycopg2.connect(database="Saw", user="postgres", password="nocosttogreat")
cursor = conexion.cursor()
sql = "insert into articulos(descripcion, precio) values (%s, %s)"
datos = ("Aguijon Roma", 5)
cursor.execute(sql, datos)
datos = ("Aguijon Restaurado", 200)
cursor.execute(sql, datos)
datos = ("Aguijon Estilizado", 1000)
cursor.execute(sql, datos)
datos = ("Aguijon Espiral", 1200)
cursor.execute(sql, datos)
datos = ("Aguijon Puro", 2000)
cursor.execute(sql, datos)
conexion.commit()
conexion.close()