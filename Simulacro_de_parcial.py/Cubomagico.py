from FuncionesParcial import visualizar_matriz
from FuncionesParcial import inicializar_matriz

matriz = inicializar_matriz(4,4,0)
ver_matriz = visualizar_matriz(2,2, matriz)


def comprobar_si_es_repetido(lista, numero):
    for i in lista:
        if i == numero:
            return True

def suma_diagonales(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                suma += matriz[i][j]
numero = 0

def cubo_magico(matriz):
    lista_de_numeros = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            numero = int(input("Ingrese un numero: "))
            while comprobar_si_es_repetido(lista_de_numeros, numero) == True:
                numero = int(input("Ingrese nuevamente un numero: "))
            matriz[i][j] = numero
            lista_de_numeros = lista_de_numeros + [numero]
    
    suma_diagonales(matriz)
    
    return matriz, suma_diagonales(matriz)
    
print(cubo_magico(matriz))


