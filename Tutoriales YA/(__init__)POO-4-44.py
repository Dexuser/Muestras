#Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__,
#calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:
    
    def __init__(self):
        self.valor1=int(input("Introduzca el primer valor:   "))
        self.valor2=int(input("Introduzca el segundo valor:  "))
    
    def suma(self):
        self.adicion= self.valor1+self.valor2
        print(f"La suma de los numeros es igual a: {self.adicion}")
    
    def resta(self):
        self.rest= self.valor1-self.valor2
        print(f"la resta de los numeros es igual a: {self.rest}")
    
    def multiplicacion(self):
        self.mult= self.valor1*self.valor2
        print(f"la multiplicacion de los numeros es igual a {self.mult}")
    
    def division(self):
        self.div= self.valor1//self.valor2
        print(f"la division de los numeros es igual a {self.div}")



# bloque principal:

valores=Operaciones()
valores.suma()
valores.resta()
valores.multiplicacion()
valores.division()

