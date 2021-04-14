#Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.

texto=input("Introduzca un String:      ")
print("El string invertido es:  ")
aux=(-1)
for i in range(len(texto)):
   # print(aux)
    print(texto[aux],end="")
    aux-=1