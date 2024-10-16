# Funcion que calcula el producto de todos los elementos de la lista que reciba como parametro
multiplicador = 0
lista_numeros = [2,3,4]
def multiplicador_numeros(lista):
    multiplicador = 1
    for i in lista:
        multiplicador *= i
    
    return multiplicador
    
print(multiplicador_numeros(lista_numeros))