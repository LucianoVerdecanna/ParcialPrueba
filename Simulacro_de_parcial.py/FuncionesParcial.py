def inicializar_matriz(cantidad_filas, cantidad_columnas, valor_inicial):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    return matriz


# def visualizar_matriz(matriz):
#     for fila in matriz:
#         print(fila)


def visualizar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print("")
    


#SelectSort

def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min]> array[j]:
                min = j
        aux = array[i]
        array[i] = array[min]
        array[min] = aux


# print(select_sort(array))

#Bubble sort

def buble_sort(array):
    bandera = False
    while bandera == False:
        bandera = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux
                bandera = False
    
    return array
    


