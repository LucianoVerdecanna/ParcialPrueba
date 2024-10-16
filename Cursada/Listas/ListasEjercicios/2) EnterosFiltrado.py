# Funcion que calcule el promedio de todos los numeros positivos

lista_numeros = [1, -1 , 10, 15 , -20]

def promedio_positivos(lista):
    sumador_positivos = 0
    for i in lista:
        if i > 0:
            sumador_positivos += i
    
    promedio = sumador_positivos / len(lista)
    return promedio

print(promedio_positivos(lista_numeros))
