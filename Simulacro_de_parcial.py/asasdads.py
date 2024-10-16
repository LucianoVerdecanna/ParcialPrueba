#Bubble sort

array = [5, 2, 1, 55, 84, 13, 20, 11, 10]

# def buble_sort(array):
#     bandera = False
#     while bandera == False:
#         bandera = True
#         for i in range(len(array) - 1):
#             if array[i] > array[i + 1]:
#                 aux = array[i]
#                 array[i] = array[i + 1]
#                 array[i + 1] = aux
#                 bandera = False
    
#     return array

# print(buble_sort(array))

#SelectSort

# def select_sort(array):
#     for i in range(len(array)):
#         min = i
#         for j in range(i+1, len(array)):
#             if array[min]> array[j]:
#                 min = j
#         aux = array[i]
#         array[i] = array[min]
#         array[min] = aux

#     return array

# print(select_sort(array))

#QuickSort

def particionado(array):
    pivote = array[0]
    menores = []
    mayores = []

    for i in range(1, len(array)):
        if array[i] < pivote:
            menores = menores + array[i]
        else:
            mayores = mayores + array[i]
    
        return menores, pivote, mayores

def quick_sort(array):
    if len(array) < 2:
        return array
    
    menores, pivote, mayores = particionado(array)
    return quick_sort(menores) [pivote], quick_sort(mayores)

print(quick_sort(array))

    
