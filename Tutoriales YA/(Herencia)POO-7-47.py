#Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. 
# Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
#Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. 
# Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
#En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.


class Cuenta:

    def __init__(self, titular, monto):
        self.titular= titular
        self.monto= monto
    
    def imprimir(self):
        print(f"titular: {self.titular}, monto: {self.monto}")



class plazo_fijo(Cuenta):

    def __init__(self, titular, monto, interes, plazo):
        super().__init__(titular, monto)
        self.interes= interes

    def operar(self):
        monto_total= (self.monto*self.interes/100)+self.monto
        print(f"el capital invertido mas interes es igual a {monto_total}")
    




class caja_ahorro(Cuenta):

    def __init__(self, titular, monto):
        super().__init__(titular, monto)
    
    def depositar(self, deposito):
        self.monto+= deposito
    
    def retirar(self, retiro):
        self.monto-= retiro


# Bloque principal:

deposito1=plazo_fijo("luis",3000,3,30)
deposito1.imprimir()
deposito1.operar()


print("\n")

deposito2=caja_ahorro("ana", 5000)
deposito2.imprimir()
deposito2.depositar(500)
deposito2.imprimir()
deposito2.retirar(300)
deposito2.imprimir()

        


    