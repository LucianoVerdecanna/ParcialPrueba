def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif base == 0:
        return 0
    else:
        return base * calcular_potencia(base, exponente - 1)
    

print(calcular_potencia(0, 5))