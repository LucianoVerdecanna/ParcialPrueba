from TableroNaval import inicializar_matriz

matriz = inicializar_matriz(5,6,0)

print("--------- Bienvenidos al cine ---------------")
print("")
asientos_ocupados = 0
asientos_vacios = 0
seguir = "Si"
while seguir == "Si":
    print("[1] Ver sala de cine")
    print("[2] Elegir Asiento")
    print("[3] Cantidad de asientos libres y ocupados")
    opcion = input("Elija una opcion: ")
    
    match opcion:
        case "1":
            print("--------- Sala actual: ----------------------")
            print("")
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    print(matriz[i][j], end= " ")
                print("")
            print("")
        case "2":
            fila = int(input("Seleccione una fila: "))
            while fila > 4:
                fila = int(input("No existe esa fila. Seleccione nuevamente su fila: "))   

            columna = int(input("Seleccione una columna: "))
            while columna > 5:
                columna = int(input("No existe esa columna. Seleccione nuevamente la columna: "))

            if matriz[fila][columna] == 0:
                matriz[fila][columna] = 1
            elif matriz[fila][columna] == 1:
                print("El asiento no esta disponible")            
        case _:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == 0:
                        asientos_vacios += 1
                    else:
                        asientos_ocupados += 1
            print(f"Hay {asientos_vacios} asientos vacios y hay {asientos_ocupados} asientos ocupados")
    
    print("")

    seguir = input("Desea volver al menu? ")
    


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end= " ")
    print("")

