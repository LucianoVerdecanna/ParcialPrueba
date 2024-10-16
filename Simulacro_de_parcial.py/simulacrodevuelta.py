# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# desea ingresar en el sistema las ventas realizadas en el día de la fecha y a partir de ello, conocer ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que él lo decida.

# Nombre de carta
# Precio (número positivo, no puede ser mayor a 200000)
# Tipo (Mágica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

# Una vez finalizado el ingreso de datos se desea conocer:

# Cantidad de cartas de rareza Rara cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
# El nombre y tipo de la carta con mayor precio de la rareza Super Rara.
# El porcentaje de rara, super rara y ultra rara hay sobre el total
# Determinar el precio promedio por cada tipo de carta
# Determinar cuál fue el tipo de carta menos vendida

seguir = "Si"
contador_raras = 0
contador_raras_filtradas = 0
contador_super_raras = 0
contador_ultra_raras = 0
contador_total = 0
contador_magicas = 0
contador_trampa = 0
contador_monstruo = 0
bandera_precio = True
precio_maximo = 0
precio_magicas = 0
precio_monstruo = 0
precio_trampa = 0
nombre_maximo = ""

while seguir == "Si":
    nombre = input("ingrese el nombre de su carta: ")

    precio = input("Ingrese el precio de su carta: ")
    precio = float(precio)
    while precio < 0 or precio > 200000:
        precio = input("Reingrese el precio de su carta: ")
        precio = float(precio)
    
    tipo = input("Ingrese el tipo de carta: ")
    while tipo != "Magica" and tipo != "Monstruo" and tipo != "Trampa":
        tipo = input("Reingrese el tipo de su carta: ")

    rareza = input("Ingrese la rareza de su carta: ")
    while rareza != "Rara" and rareza != "Super Rara" and rareza != "Ultra Rara":
        rareza = input("Reingrese la rareza de su carta: ")

    #Cantidad de cartas de rareza Rara cuyo precio oscile en 50000 y 80000 y sea de tipo Mágica o Trampa.
    if rareza == "Rara":
        contador_raras += 1
        if precio > 50000 and precio < 80000 and (tipo == "Magica" or tipo == "Trampa"):
            contador_raras_filtradas += 1

    # El nombre y tipo de la carta con mayor precio de la rareza Super Rara.
    elif rareza == "Super Rara":
        contador_super_raras += 1
        if precio > precio_maximo or bandera_precio == True:
            precio_maximo = precio
            nombre_maximo = nombre
            bandera_precio == False
    else:
        contador_ultra_raras += 1
    
    if tipo == "Magica":
        precio_magicas += precio
        contador_magicas += 1
    elif tipo == "Monstruo":
        precio_monstruo += precio
        contador_monstruo += 1
    else:
        precio_trampa += precio
        contador_trampa += 1

    contador_total += 1

    seguir = input("Desea continuar? ")

#El porcentaje de rara, super rara y ultra rara hay sobre el total
porcentaje_raras = contador_raras * contador_total / 100
porcentaje_super_raras = contador_super_raras * contador_total / 100
porcentaje_ultra_raras = contador_ultra_raras * contador_total / 100

#Determinar el precio promedio por cada tipo de carta
if contador_magicas > 0:
    precio_promedio_magicas = precio_magicas / contador_magicas
    precio_promedio_magicas = float(precio_promedio_magicas)
    print(f"El promedio del precio de las cartas de tipo Magicas es de ${precio_promedio_magicas}")

if contador_monstruo > 0:
    precio_promedio_monstruo = precio_monstruo / contador_monstruo
    precio_promedio_monstruo = float(precio_promedio_monstruo)
    print(f"El promedio del precio de las cartas de tipo Monstruo es de ${precio_promedio_monstruo}")

if contador_monstruo > 0:
    precio_promedio_trampa = precio_trampa / contador_trampa
    precio_promedio_trampa = float(precio_promedio_trampa)
    print(f"El promedio del precio de las cartas de tipo Trampa es de ${precio_promedio_trampa}")

#Determinar cuál fue el tipo de carta menos vendida
minimo_vendidas = contador_raras
minimo_vendida = ""
if minimo_vendidas > contador_super_raras:
    minimo_vendidas = contador_super_raras
    minimo_vendida = "Super Rara"
    if minimo_vendidas > contador_ultra_raras:
        minimo_vendidas = contador_ultra_raras
        minimo_vendida = "Ultra Raras"
elif minimo_vendidas > contador_ultra_raras:
        minimo_vendidas = contador_ultra_raras
        minimo_vendida = "Ultra Raras"
else:
    minimo_vendida = "Rara"
    

print(f"Cartas raras filtradas: {contador_raras_filtradas}")
print(f"El nombre de la carta de mayor valor es de {nombre_maximo} y su valor es de ${precio_maximo}")
print(f"Porcentajes: Raras %{porcentaje_raras}, Ultra Rara %{porcentaje_ultra_raras} y Super Rara %{porcentaje_super_raras}")
print(f"El tipo menos vendido es {minimo_vendida}")