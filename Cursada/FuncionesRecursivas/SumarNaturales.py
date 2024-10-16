def sumar_naturales(numero: int) -> int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

print(sumar_naturales(5))


def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif base == 0:
        return 0
    else:
        return base * calcular_potencia(base, exponente - 1)
    

print(calcular_potencia(0, 5))


def sumar_digitos(numero: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

