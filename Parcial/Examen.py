import random
from Biblioteca import *

#  El programa debe contar con un menú de opciones que permita realizar las siguientes operaciones:
#  1.  Generar la lista de números enteros aleatorios utilizando la función desarrollada en el punto 
# 2. Ordenar la lista de números generada anteriormente, utilizando la función desarrollada en el punto 3.
# 3. Buscar cuántos números están en un rango dado: Solicitar al usuario que ingrese un rango (por ejemplo, entre 10
# y 50) e informar cuántos números de la lista generada en el punto 1 caen dentro de dicho rango.
# El informe deberá seguir este formato:

#  CANTIDAD DE NÚMEROS EN EL RANGO [Valor Inicial-Valor Final]: Cantidad

# 4. Del ítem anterior, obtener: El número máximo y mínimo que se encuentre dentro del rango, e informar su valor.

# 5. Generar la matriz de caracteres alfanuméricos, utilizando la función desarrollada en el punto 2.
# Notas:
# Se recomienda que el código sea comentado adecuadamente y sea modular.
# Cada una de las funciones debe recibir los parámetros necesarios para funcionar de manera independiente del menú.
# Se debe validar el ingreso correcto de los datos para las opciones que lo requieran.

print("-------------MENÚ--------------")
print("[1] Generar lista de 50 numeros aleatorios")
print("[2] Ordenar lista de numeros generada")
print("[3] Buscar cuantos numeros estan en un rango dado")
print("[4] Numero maximo y minimo dentro del rango e informar su valor")
print("[5] Generar matriz de caracteres alfanumericos")
matriz = inicializar_matriz(6,15,0)
opcion = 0
array = lista_aleatoria()
while opcion != 6:
    opcion = int(input("Seleccione una opcion: "))
    match opcion:
        case 1:
            print("Se ha generado una lista aleatoria")
            print(array)


        case 2:
            forma = input("De que forma desea mostrar los numeros? Ascendente/Descendente: ")
            print(f"La lista de manera {forma} quedaria de la siguiente forma: {buble_sort(array, forma)}")
        
        case 3:
            rango_inicial = int(input("Ingrese su numero inicial: "))
            rango_final = int(input("Ingrese su numero final: "))
            
            print(f"La cantidad de numeros entre {rango_inicial} y {rango_final} es de: {lista_filtrada(array, rango_inicial, rango_final)}")
            
        
        case 4:
            maximo = 0
            for i in array:
                if i >= maximo:
                    maximo = i
            
            minimo = array[0]
            for i in array:
                if minimo > i:
                    minimo = i
    
            print(f"El numero maximo en la lista aleatoria es de: {maximo} y el minimo es de: {minimo}")
                
        case 5:
            print(visualizar_matriz(matriz_ordenada(matriz)))

        

