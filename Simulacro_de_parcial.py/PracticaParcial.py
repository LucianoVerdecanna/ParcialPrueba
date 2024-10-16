from FuncionesParcial import buble_sort


# def ordenar_vector(array, booleano):
#     if booleano == True:
#         buble_sort_descendente(array)
#     else:
#         buble_sort(array)
    
#     return array

# print(ordenar_vector(array, True))

# array1 = [2, 4, 10, 7, 11, 1]
# array2 = [12, 6, 8, 0, 9]

# def intercalar_vectores(array1, array2, forma):
#     lista = []
#     if forma == "Ascendente":
#         lista1 = buble_sort(array1)
#         lista2 = buble_sort(array2)
#         lista = lista1 + lista2
#         lista = buble_sort(lista)
#     else:
#         lista = buble_sort_descendente(array1) + buble_sort_descendente(array2)
#         lista = buble_sort_descendente(lista)
    
#     return lista

# print (intercalar_vectores(array1, array2, "Descendente"))
array = [5, 3, 7, 10, 1, 22, -3, -6, -2, 0]

def buble_sort_descendente(array):
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

def intercalar_vectores(array):
    
    lista_negativos = []
    lista_positivos = []

    for i in range(len(array)):
        if array[i] >= 0:
            lista_positivos += [array[i]]
        elif array[i] < 0:
            lista_negativos += [array[i]]

    lista_descendiente = buble_sort_descendente(lista_negativos)
    lista_ascendente = buble_sort(lista_positivos)
    lista = lista_descendiente + lista_ascendente

    return lista

print(intercalar_vectores(array))

