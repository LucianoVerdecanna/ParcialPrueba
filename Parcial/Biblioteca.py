import random
# 1. Generar una lista de números enteros aleatorios:Desarrollar una función que genere de manera aleatoria una lista de 50 
# números enteros positivos entre 1 y 100.

def lista_aleatoria():
    lista = []
    num = 0
    while len(lista) < 50:
        num = random.randint(1,100)
        lista = lista + [num]

    return lista


# 2.   Generar una matriz de caracteres alfanuméricos: Desarrollar una función que genere de manera aleatoria una matriz de 6 filas por 15
#  columnas (6 listas de 15 elementos cada una), compuesta de caracteres alfanuméricos (letras y dígitos).

def inicializar_matriz(cantidad_filas, cantidad_columnas, valor_inicial: str):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    return matriz



# 3.  Ordenar una lista de números enteros: Desarrollar una función que ordene una lista de números enteros, recibiendo como parámetro 
# el criterio de ordenamiento "ASC" o "DESC" (ascendente o descendente).

def buble_sort(array, forma:str):
    if forma == "Ascendente":
        bandera = False
        while bandera == False:
            bandera = True
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    aux = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = aux
                    bandera = False
    elif forma == "Descendente":
        bandera = False
        while bandera == False:
            bandera = True
            for i in range(len(array) - 1):
                if array[i] < array[i + 1]:
                    aux = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = aux
                    bandera = False
    return array


# 4. Validar el ingreso de una cadena alfanumérica: Desarrollar una función que valide el ingreso de una cadena de 
# caracteres alfanuméricos (letras y números), y que será utilizada en el menú de opciones. 

def cadena_caracteres(cadena):
    if cadena.isalpha():
        return True
    else:
        return False


def lista_filtrada(array, primer_valor, ultimo_valor):
    contador = 0
    for num in array:
        if primer_valor <= num <= ultimo_valor:
            contador += 1

    return contador


def visualizar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " | ")
        print("")


def matriz_ordenada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cadena = random.randint(0,122)
            cadena = chr(cadena)
            if cadena_caracteres(cadena):
                matriz[i][j] = cadena
            else:
                cadena = ord(cadena)
                matriz[i][j] = cadena
    return matriz


