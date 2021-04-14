#Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
#Desarrollar las funciones:
#1) Cargar por teclado.
#2) Listar los productos y precios.
#3) Imprimir los productos con precios comprendidos entre 10 y 15.



def carga_datos():
    productos=[]

    for i in range(5):
        aritculo=input("Nombre del articulo:        ")
        precio=int(input("Precio del articulo:      "))
        productos.append( (aritculo,precio) )
        print()
    return productos



def listado(catalogo):
    print(f"Los productos que tenemos son:")
    for nombre,precio in catalogo:
        print(f"{nombre} vale {precio}")



def Imprimir(catalogo):
    print("Productos cuyos precios se encuentran entre 10 y 15 pesos")
    for elemento in catalogo:
        if elemento[1]>=10 and elemento[1]<=15:
            print(f"el {elemento[0]} vale {elemento[1]} ")









# Bloque principal
articulos=carga_datos()
print()
listado(articulos)
print()
Imprimir(articulos)