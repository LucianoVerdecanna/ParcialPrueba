# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
# función deberá seguir el siguiente prototipo:

# from package_funciones import Get_Int


def calcular_fibonacci(numero: int):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci (numero - 1) + calcular_fibonacci(numero - 2)
    

print(calcular_fibonacci(2))