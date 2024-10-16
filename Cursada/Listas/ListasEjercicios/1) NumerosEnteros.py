#Funcion que reciba una lista de enteros y devuelva el promedio de todos

listaNumeros = [2,7,9,10]
def enteros_promedio(lista):
    sumador = 0
    for i in lista:
        sumador = sumador + i
    
    promedio = sumador / len(listaNumeros)
    return promedio
    
print(enteros_promedio(listaNumeros))
    

    