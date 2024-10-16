lista_maximo = [ 3, 1, 6, 8, 0]

def valor_maximo(lista):
    valor_maximo = 0
    for i in lista:
        if valor_maximo < i:
            valor_maximo = i

    return valor_maximo


print(valor_maximo(lista_maximo))