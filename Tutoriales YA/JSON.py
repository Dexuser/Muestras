# mediante el sitio web:
# https://jsonplaceholder.typicode.com/
# (Que se puede utiliziar para recupear datos con diferentes formatos
# por ejemplo Json y probar nuestros Scripts, recuperar los datos de la pagina
# https://jsonplaceholder.typicode.com/posts
# Como los datos vienen en un array se tiene que iterar sobre cada uno
# de los diccionarios que contiene, y mostrar sus valores usando sus claves
from urllib import request
import json

pagina = request.urlopen("https://jsonplaceholder.typicode.com/posts")
aux = pagina.read().decode("utf-8")
data = json.loads(aux)
#print(data)
for contenido in data:
	print( f"userId: { contenido['userId'] }" )
	print( f"id: { contenido['id'] }" )
	print( f"title: { contenido['title'] }")
	print( f"body: { contenido['body'] }")
	print("-" * 80)