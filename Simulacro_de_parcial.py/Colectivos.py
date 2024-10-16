# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total
# tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú de usuarios:
import random
from FuncionesParcial import inicializar_matriz
from FuncionesParcial import visualizar_matriz

lista_legajos = []

while len(lista_legajos) <= 14:
    legajo = random.randint(1,15)
    if legajo not in lista_legajos:
        lista_legajos = lista_legajos + [legajo]


matriz = inicializar_matriz(3,5,0)
ver_matriz = visualizar_matriz(matriz)

def cargar_planilla(matriz, linea: int, coche: int, recaudacion: int):
    
    matriz[linea][coche] = recaudacion_viaje
    return matriz
        



opcion = 0
while opcion != 6:
    print("------------------MENÚ------------------")
    print("[1] Cargar plantilla")
    print("[2] Mostrar la recaudación de cada coche y línea (mostrar la matriz)")
    print("[3]  Calcular y mostrar recaudación por línea.")
    print("[4] Calcular y mostrar recaudación por coche")
    print("[5] Calcular y mostrar la recaudación total.")
    print("[6]  Salir.")

    opcion = int(input("Que opcion desea ver: "))

    match opcion:
        case 1:
            seguir = "Si"
            while seguir == "Si":
                numero_identificacion = int(input("Ingrese su legajo: "))
                if numero_identificacion in lista_legajos:
                    linea = int(input("Ingrese la linea de su colectivo: "))
                    while linea < 0 or linea > 2:
                        linea = int(input("Ingrese la linea de su colectivo nuevamente: "))
                        
                    coche = int(input("Ingrese su coche: "))
                    while coche > 4 or coche < 0:
                        coche = int(input("Ingrese su coche nuevamente: "))
            
                    recaudacion_viaje = int(input("Ingrese la recaudacion de su viaje: "))

                    print(f"El chofer pertenece a la linea {linea}")
                    print(f"El coche en el que anda el chofer es el coche N°{coche}")
                    print(f"La recaudacion del viaje fue de: ${recaudacion_viaje}")
                    seguir = input("Desea continuar? Si/No ")
                else:
                    print("Su legajo no se encuentra en la lista")


        case 2:
            print(visualizar_matriz(cargar_planilla(matriz, linea, coche, recaudacion_viaje)))
        
        case 3:
            for i in range(len(matriz)):
                recaudacion_linea = 0
                print(f"Cargando la recaudacion de la linea {i}...")
                for j in range(len(matriz[i])):
                    recaudacion_linea += matriz[i][j]
                print(f"La recaudacion total de la linea {i} es de {recaudacion_linea}")
        
        case 4:
            for j in range(len(matriz[0])):
                recaucacion_coche = 0
                print(f"Cargando la recaudacion del coche {j}...")
                for i in range(len(matriz)):
                    recaucacion_coche += matriz[i][j]
                print(f"La recaudacion del coche {j} es de: ${recaucacion_coche}")
        
        case 5:
            recaudacion_total = 0
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    recaudacion_total += matriz[i][j]
            print(f"Lo recaudado entre las 3 lineas y los 5 coches es de {recaudacion_total}")
                    




