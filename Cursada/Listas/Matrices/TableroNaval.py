import random

def inicializar_matriz(cantidad_filas, cantidad_columnas, valor_inicial):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    
    return matriz


