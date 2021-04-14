#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
# inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
#  El nombre de la clase llamarla Triangulo.


class Triangulo:
     
     def inilizacion(self, lado1, lado2, lado3):
         self.lado1= lado1
         self.lado2= lado2
         self.lado3= lado3
    

     def mayor_lado(self):
        mayor= self.lado1
        if self.lado2>mayor:
            mayor=self.lado2
        
        if self.lado3>mayor:
            mayor=self.lado3
        print(f"el lado mas grande el triangulo mide: {mayor}")


     def equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")


# bloque principal
trian=Triangulo()
v1=int(input("primer lado del triangulo:    "))
v2=int(input("segundo lado del triangulo:    "))
v3=int(input("tercer lado del triangulo:    "))
trian.inilizacion(v1,v2,v3)
trian.mayor_lado()
trian.equilatero()
exit=input("pulse enter para finalizar el programa. ")