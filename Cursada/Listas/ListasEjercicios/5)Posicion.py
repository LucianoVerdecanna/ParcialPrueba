lista_posicion = [0, 9, 2 , 7, 9]

def posicion(lista):
    valor_maximo = 0
    for i in lista:
        if valor_maximo < i:
            valor_maximo = i

    return lista.index(valor_maximo)



print(posicion(lista_posicion))
