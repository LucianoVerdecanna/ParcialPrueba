# Crear una función que (utilizando la función del punto 11), muestre todos los
# números primos comprendidos entre entre la unidad y un número ingresado como
# parámetro. La función retorna la cantidad de números primos encontrados


def numero_flotante():
    return float(input("Ingrese un numero: "))

limite = numero_flotante()
def es_primo(limite):
    if limite < 2:
        return False
    for i in range(2, int(limite ** 0.5) + 1):
        if limite % i == 0:
            return False
    return True



def cant_num_primos(limite):
    contador = 0
    for num in range(1, int(limite) + 1):
        if es_primo(num):
            contador += 1
    
    return contador

print(f"Cantidad de números primos hasta {limite}: {cant_num_primos(limite)}")

# numero_pasado = 0

# def numero_flotante():
#     return float(input("Ingrese un número: "))

# def es_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# def cant_num_primos(limite):
#     contador = 0
#     for num in range(1, int(limite) + 1):  # Asegurarse de que el límite sea un entero
#         if es_primo(num):
#             contador += 1
#     return contador

# limite = numero_flotante()
# print(f"Cantidad de números primos hasta {limite}: {cant_num_primos(limite)}")
