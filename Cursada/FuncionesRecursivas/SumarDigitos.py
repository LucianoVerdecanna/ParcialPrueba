def sumar_digitos(numero: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
