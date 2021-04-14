#Confeccionar una función que reciba una serie de edades
# y me retorne la cantidad que son mayores o iguales a 18
# (como mínimo se envía un entero a la función)


#def mayores_18(v1,*edades):
#    print("Las edades mayores o igual a 18 años son: ")
#    if v1>=18:
#        print(v1,end=",")
#
#        for i in range(len(edades)):
#            
#            if edades[i]>=18:
#                print(edades[i], end=",")
#
#
#
#
## bloque principal
#
#mayores_18(18,20,15,16,18,30,23,17,10)
#

#===========================================================================================================================
# Cometiste un fallo, leiste mal, tenias que devolver la cantidad de mayores de edad, y no usaste un return
#===========================================================================================================================
# Asi es como tenia que hacerlo
#===========================================================================================================================
def mayores_18(v1,*edades):
    cont=0

    if v1>=18:
        cont+=1
    
    for i in range(len(edades)):
        
        if edades[i]>=18:
            cont+=1

    return cont



# Bloque principal

Mas_18=mayores_18(18,20,15,16,18,30,23,17,10)
print(Mas_18)