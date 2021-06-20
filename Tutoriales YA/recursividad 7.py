# rango(desde, hasta) -> lista de números: similar a rango, pero 
# ahora se puede especificar el "desde". 
# Ej: rango(5, 10) -> [5,6,7,8,9,10]. No hace falta validar que desde sea 

def rango(desde, hasta):
	valores = []

	if hasta == desde:
		valores.append(hasta)
		return valores
	else:
		lista = rango(desde, hasta-1)
		lista.append(hasta)
		valores.extend(lista)
		return valores 

inicio = int(input("Desde que numero va a iniciar?:  "))
final = int(input("Hasta que numero se va a recorrer?:  "))
respuesta = rango(inicio, final)
print(respuesta)