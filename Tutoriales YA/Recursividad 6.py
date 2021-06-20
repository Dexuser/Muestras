# Recursividad 6
# rangoHasta(n) -> Lista de números: dado un número "n", retorna la
# lista de números desde el 0 hasta el N incluído.
# Por ejemplo: rangoHasta(5) -> [0,1,2,3,4,5].


def rangoHasta(numero):
    valores = []
    if numero == 0:
        valores.append(numero)
        return valores
    else:
        lista = rangoHasta(numero-1)
        lista.append(numero)
        valores.extend(lista)
        return valores
    


valor = int(input("Introduzca un valor:  "))
resultado = rangoHasta(numero=valor)
print(resultado)