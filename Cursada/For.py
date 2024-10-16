# def suma(num1, num2):
#     resultado = num1 + num2
#     resultado = int(resultado)
#     return resultado

# def resta(num1, num2):
#     resultado = num1 - num2
#     return resultado

# def multiplicacion(num1, num2):
#     resultado = num1 * num2
#     return resultado

# def division(num1, num2):
#     resultado = num1 / num2
#     return resultado

# pregunta = input("Que calculo quiere hacer: Suma, Resta, Multiplicacion o Division. En caso de no queres seguir ponga F ")
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el primer numero: "))
# while pregunta != "F":
#     while pregunta != "Suma" and pregunta != "Resta" and pregunta != "Multiplicacion" and pregunta != "Division" and pregunta != "F":
#         pregunta = input("Respuesta no valida, reingrese su respuesta: ")
#     if pregunta == "Suma":
#         print (suma(num1, num2))
#     elif pregunta == "Resta":
#         print (resta(num1, num2))
#     elif pregunta == "Multiplicacion":
#         print (multiplicacion(num1, num2))
#     elif pregunta == "Division":
#         print (division(num1, num2))
#     else:
#         print("Se apago la computadora")

#     pregunta = input("Que calculo quiere hacer: Suma, Resta, Multiplicacion o Division. En caso de no queres seguir ponga F ")

#  Mostrar los números ascendentes desde el 1 al 10
# for num in range(1,11):
#     print(num)

# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado
# num1 = input("Ingrese un numero: ")
# num1 = int(num1)
# for num in range(0, num1):
#     print(num)

# print(num1)

# Ingresar un número y mostrar la tabla de multiplicar de ese número.
num1 = input("Ingrese el numero del cual desea que se haga la tabla: ")
num1 = int(num1)
for i in range(1,11):
    print(f"{num1} x {i} = {num1 * i}" )

# Imprimir los números múltiplos de 3 entre el 1 y el 10
# for i in range(1,10):
#     if i % 3 == 0:
#         print(i)

# Mostrar los números pares que hay desde la unidad hasta el número 50
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)

#  Realizar un programa que permita mostrar una pirámide de números.
# num = ""
# for i in range (1,11):
#     num = str(num) + str(i)
#     print(num)