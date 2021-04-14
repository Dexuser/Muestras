# Articulos y sus precios
#1) Cargar los nombres de articulos y sus precios.
#2) Imprimir los nombres y precios.
#3) Imprimir el nombre de artículo con un precio mayor
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado



def articulos():
    arti=[]
    precio=[]

    for i in range(5):
        v1=input("Ingrese el nombre de un articulo:     ")
        arti.append(v1)
        v2=int(input("Ingrese el precio del articulo:       "))
        precio.append(v2)
        print()

    return [arti, precio]




def mostrar_artiprecios(objeto, valor):
    print("Los articulos que vendemos son:")
    
    for i in range(len(objeto)):
        print(f"{objeto[i]} vale {valor[i]} pesos")



def mayor_artiprecio(objeto, valor):
    mayor_precio= valor[0]
    mayor_objeto= objeto[0]
    for i in range(1,len(objeto)):
        if valor[i] > mayor_precio:
            mayor_precio= valor[i]
            mayor_objeto= objeto[i]

    print(f"el articulo con el precio mas elevado es : {mayor_objeto}")



def busca_precio(objeto,valor):
    num=int(input("Introduzca un precio :"))
    print("Los articulos con menor o igual precio al introducido son:")

    for i in range(len(objeto)):
        if valor[i] <= num:
            print(f"{objeto[i]} vale {valor[i]}")






# Bloque principal
articulo, precio=articulos()
print()
mostrar_artiprecios(articulo, precio)
print()
mayor_artiprecio(articulo, precio)
print()
busca_precio(articulo, precio)
