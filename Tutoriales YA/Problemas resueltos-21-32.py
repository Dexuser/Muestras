#Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
#En una lista cargar en la primer componente el nombre del candidato y en la segunda componente
#  cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
#Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
#candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
# 1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
# 2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.



def cargar_candidato():

    candidatos=[]
    for i in range(3):
        nombre=input("Introduzca el nombre del candidato:      ")
        candidatos.append( (nombre, []) )
        #print(f" i vale {i}")
        #print(candidatos)


        cantidad=int(input(f"Cuantas provincias votaron por {nombre}?:      "))
        for y in range(cantidad):
            provincia=input("Introduzca el nombre de la provincia:      ")
            votos=int(input("Cuantos votos existen de esa provincia:     "))
            candidatos[i][1].append( (provincia,votos) )
            #print(f"en la segunda funcion i vale {i}")
            #print(candidatos)
            print()


    print(candidatos)
    return candidatos

def mostrar_datos(datos):

    for x in range( len(datos) ):
        votos_total=0
        for j in range( len(datos[x][1]) ):
            votos_total+= datos[x][1][j][1]
        
        print(f"el candidato {datos[x][0]} tiene un total de {votos_total} votos")









# bloque principal

postulantes=cargar_candidato()
mostrar_datos(postulantes)