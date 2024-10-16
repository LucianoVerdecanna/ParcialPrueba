import random

numero_secreto = random.randint(1, 100)

numero_usuario = int(input("Ingrese un numero del 1 al 100: "))

intentos = 1

while numero_usuario != numero_secreto:

    if numero_secreto > numero_usuario:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    
    numero_usuario = int(input("Ingrese un numero: "))
    
    intentos += 1


print(f"Felicitaciones, lo has logrado, el numero era {numero_secreto}")
print(f"Lo logro en {intentos} intentos")