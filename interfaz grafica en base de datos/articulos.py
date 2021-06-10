import mysql.connector  
from mysql.connector import cursor

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd test")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(articulo, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select articulo, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, articulo, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def eliminar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount
        
    def cambiar_dato(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set articulo=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount