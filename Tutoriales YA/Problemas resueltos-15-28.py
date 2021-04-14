#Confeccionar una función que reciba entre 2 y 5 enteros.
# La misma nos debe retornar la suma de dichos valores. 
# Debe tener tres parámetros por defecto.

def enteros(v1,v2,v3=0,v4=0,v5=0):
    suma= v1+v2+v3+v4+v5

    return suma



#Bloque principal:

print(f"La suma de los entereos introducidos son: {enteros(10,20)}")
