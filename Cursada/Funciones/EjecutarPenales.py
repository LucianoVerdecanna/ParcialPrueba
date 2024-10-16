mensaje = 0
mensaje_error = "No cumple con las condiciones"
def ejecutar_penales(mensaje, mensaje_error, reintentos):
    contador_total = 1
    contador_goles = 0
    contador_fallas = 0

    while contador_total <= 5:
        mensaje = input("Ingrese su resultado. Gol o Falla: ")
        contador_break = 0

        while mensaje != "Gol" and mensaje != "Falla":
            contador_break +=1
            if contador_break == reintentos:
                print("No tiene mas intentos. Su penal esta fallado!")
                contador_fallas += 1
                break
            else:
                print(mensaje_error)
                mensaje = input("Resultado no valido, escriba devuelta. Gol o Falla: ")

        if mensaje == "Gol":
            contador_goles += 1
        elif mensaje == "Falla":
            contador_fallas += 1
        
        contador_total += 1

    return contador_goles, contador_fallas

print("Turno equipo 1:")
goles1, fallas1 = ejecutar_penales(mensaje, mensaje_error, 5)
print(f"La cantidad de goles hechos por el equipo es de {goles1} y de fallas es de {fallas1}")

print("Turno equipo 2: ")
goles2,fallas2  = ejecutar_penales(mensaje, mensaje_error, 5)
print(f"La cantidad de goles hechos por el equipo es de {goles2} y de fallas es de {fallas2}")

if goles1 > goles2:
    print("El equipo 1 es el ganador")
else:
    print("El equipo 2 es el ganador")

