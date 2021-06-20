#Para esto recordar que el caso más básico es el 0 que es par. Luego un numero es par si su anterior es impar. Y un numero es impar si su anterior es par.
#Ej esPar(4) si esImpar(3)
#   esImpar(3) si esPar(2)
#   esPar(2) si esImpar(1)
#   esImpar(1) si esPar(0)
#   esPar(0) ? SI !
def es_par(n):
    if n == 0:
        return True
    
    if es_impar(n-1):
        return True
    else:
        return False
        
def es_impar(n):
    if n == 0:
        return False
    
    if es_par(n-1):
        return True
    else:
        return False

valor = int(input("Introduzca un valor para saber si es par o impar "))
print(es_par(valor))
