# Suponer una lista de las compras hechas por clientes de una empresa
# a lo largo del un mes, la cual contiene tuplas con informacion de
# cada venta, siendo su formato el siguiente:
# ( cliente, dia del mes, monto, domicilio del cliente)
# Ejemplo:
# [
#	("Nuria Costa", 5, 12780.78, "Calle de las flores 335"),
#	("Jorge Russo", 7, 699, "Mirasol 218"),
#	("Nuria Costa", 7, 532.90, "Calle de las flores 335"),
# 	("Julian Rodrigez", 12, 5715.99, "La mancha 761"),
#	("Jorge Russo", 15, 958, "Mirasol 218")
# ]
# Escribir una funcion que reciba como parametro una lista con
# el formato mencionado anteriormente y que esta retorne los 
# domicilios de cada cliente al cual se le debe enviar una factura
# de compra, Note que los clientes pueden haber vuelto a comprar asi
# que cuando se vayan a retornar los domicilios solamente aparezcan 
# una vez


def domicilios(datos):
	conjunto = set()
	for fila in datos:
		conjunto.add(fila[3])
	return conjunto

informacion = [
	("Nuria Costa", 5, 12780.78, "Calle de las flores 335"),
	("Jorge Russo", 7, 699, "Mirasol 218"),
	("Nuria Costa", 7, 532.90, "Calle de las flores 335"),
	("Julian Rodrigez", 12, 5715.99, "La mancha 761"),
	("Jorge Russo", 15, 958, "Mirasol 218")
	]

ubicacion = domicilios(informacion)
print(ubicacion)