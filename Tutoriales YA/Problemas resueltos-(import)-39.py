#Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
#El operador debe tratar de adivinar el número ingresado.
#Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
#Mostrar cuando gana el jugador cuantos intentos necesitó.


import random

num=random.randint(1, 100)
num2=0
intentos=0
while num2!=num:
    num2=int(input("Introduzca un numero:   "))

    if num2==num:
        print(f"Ganaste, tomaste {intentos} intentos para llegar al numero generado ")
      


    else:

        if num2< num:
            print("El numero buscado es mas grande")
            intentos+=1
            print()

        else:
            if num2>num:
                print("el numero buscado es mas pequeño")
                intentos+=1
                print()