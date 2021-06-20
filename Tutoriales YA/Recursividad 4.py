# posiciones_de("Un tete a tete con Tete", "te")
#[3, 5, 10, 12, 21]

lugares = []
def posiciones_de(texto, palabra_buscada, indice=0, cont=1):

	a = texto.index(palabra_buscada, indice, len(texto))
	lugares.append(a)

	if cont != texto.count(palabra_buscada):
		posiciones_de(texto, palabra_buscada, a+1, cont+1)

posiciones_de("Coma un buen coco, los Cocos son buenos porque los cocos son h2o en un coco", "coco")
print(lugares)