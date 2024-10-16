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

nombre_carta = 0
precio = 0
precio_magicas = 0
precio_trampa = 0
precio_monstruo = 0
tipo_de_carta = 0 
rareza = 0
contador_raras = 0
contador_raras_filtradas = 0
contador_super_raras = 0
contador_ultra_raras = 0
contador_monstruo = 0
contador_magicas = 0
contador_trampa = 0
contador_total = 0
maximo_super_rara = 0
nombre_maximo_super_rara = 0
precio_total = 0
bandera = True

while bandera == True:
    nombre_carta = input("Ingrese el nombre de la carta: ")

    precio = input("Ingrese el precio: ") #Debe ser un nro positivo y no puede ser mayor a 50000
    precio = int(precio)
    while not(precio > 1 and precio < 200000):
        precio = input("El precio no es valido, ingreselo nuevamente: ")
        precio = int(precio)

    tipo_de_carta = input("Ingrese el tipo de carta: Magica, Monstruo o Trampa: ")
    while tipo_de_carta != "Magica" and tipo_de_carta != "Monstruo" and tipo_de_carta != "Trampa":
        tipo_de_carta = input("Ingresó un tipo de carta no valido, ingreselo nuevamente: ")

    rareza = input("Ingrese la rareza de la carta: Rara, Super Rara o Ultra Rara: ")
    while rareza != "Rara" and rareza != "Super Rara" and rareza != "Ultra Rara":
        rareza = input("La rareza ingresada no es valida, ingresela nuevamente: ")

    if rareza == "Rara":
        contador_raras +=1
        if (precio >= 50000 and precio <= 80000) and (tipo_de_carta == "Magica" or tipo_de_carta == "Trampa"):
            contador_raras_filtradas += 1
            

    if rareza == "Super Rara": #No hace falta usar bandera ya que el minimo es 1 y siempre va a ser mayor que 0
        contador_super_raras += 1
        if precio > maximo_super_rara:
            maximo_super_rara = precio
            nombre_maximo_super_rara = nombre_carta
    
    if rareza == "Ultra Rara":
        contador_ultra_raras += 1

    if tipo_de_carta == "Magica":
        contador_magicas += 1
        precio_magicas = precio_magicas + precio
    else:
        if tipo_de_carta == "Trampa":
            contador_trampa += 1
            precio_trampa = precio_trampa + precio
        else:
            contador_monstruo += 1
            precio_monstruo = precio_monstruo + precio
    
    contador_total += 1

    bandera = input("Desea ingresar otra carta? Si / No: ")
    if bandera == "No":
        bandera = False
    else:
        bandera = True

#Carta menos vendida
minimo_vendidas = contador_raras
tipo_menos_vendido = "Rara"
if minimo_vendidas > contador_super_raras:
    minimo_vendidas = contador_super_raras
    tipo_menos_vendido = "Super Rara"
    if minimo_vendidas > contador_ultra_raras:
        minimo_vendidas = contador_ultra_raras
        tipo_menos_vendido = "Ultra Rara"
else:
    if minimo_vendidas > contador_ultra_raras:
        minimo_vendidas = contador_ultra_raras
        tipo_menos_vendido = "Ultra Rara"

#Porcentaje
porcentaje_raras = contador_raras * (contador_total / 100)
porcentaje_raras = float(porcentaje_raras)
porcentaje_super_raras = contador_super_raras * (contador_total / 100)
porcentaje_super_raras = float(porcentaje_super_raras)
porcentaje_ultra_raras = contador_ultra_raras * (contador_total / 100)
porcentaje_ultra_raras = float(porcentaje_ultra_raras)

#Precio promedio
precio_promedio_magicas = 0
if contador_magicas > 0:
    precio_promedio_magicas = precio_magicas / contador_magicas
    precio_promedio_magicas = float(precio_promedio_magicas)

if contador_trampa > 0:
    precio_promedio_trampa = precio_trampa / contador_trampa
    precio_promedio_trampa = float(precio_promedio_trampa)


if contador_monstruo > 0:
    precio_promedio_monstruo = precio_monstruo / contador_monstruo
    precio_promedio_monstruo = float(precio_promedio_monstruo)


print(f"La cantidad de cartas raras, magicas o de trampa y que su valor sea entre 0 y 200000 es de {contador_raras_filtradas} carta")
print(f"El valor maximo de la carta super rara es de {maximo_super_rara} y su nombre es {nombre_maximo_super_rara}")
print(f"El porcentaje de las cartas raras es de {porcentaje_raras}%, de las super raras {porcentaje_super_raras}% y de las ultra raras {porcentaje_ultra_raras}%")
print(f"El precio promedio de las raras es de ${precio_promedio_magicas}, de las super raras es de ${precio_promedio_monstruo} /n y de las ultra raras es de ${precio_promedio_trampa}")
print(f"La carta menos vendida es {tipo_menos_vendido} ")
