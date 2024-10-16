# Una empresa internacional está realizando un estudio de mercado para decidir cuál será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.

# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:

# Nombre
# Edad (no menor a 18)
# Tiene suscripción a algún servicio de streaming (sí-no)
# Género (Masculino - Femenino - No binario - Otro)
# Voto (Hulu, Vix+, CODA)
# Se solicita realizar las siguientes búsquedas:

# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu.
# 2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
# 3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
# 4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
# 5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.

seguir = "Si"
contador_total = 0
contador_hulu = 0
contador_coda = 0
contador_vix = 0
contador_hulu_filtrado = 0
contador_coda_filtrado = 0
min_edad_hulu = 0
edad_votantes_vix = 0
genero_hulu = ""
nombre_hulu = ""
bandera_hulu = True
while seguir == "Si":
    nombre = input("Ingrese su nombre: ")

    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("Debe ser mayor de  18, ingrese nuevamente su edad: ")
        edad = int(edad)

    suscripcion = input("Tiene suscripcion? Si/No ")
    while suscripcion != "Si" and suscripcion != "No":
        suscripcion = input("Respusta no valida, tiene suscripcion? Si/No ")
    
    genero = input("Ingrese su genero: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "No binario" and genero != "Otro":
        genero = input("Genero no valido, reingrese su genero: ")

    voto = input("Ingrese su voto: ")
    while voto != "Hulu" and voto != "Vix+" and voto != "CODA":
        voto = input("Plataforma no identificada, Reingresela: ")

#Nombre, género y edad del encuestado de menor edad que votó por Hulu.
    if voto == "Hulu":
        contador_hulu += 1
        if min_edad_hulu > edad or bandera_hulu == True:
            min_edad_hulu = edad
            genero_hulu = genero
            nombre_hulu = nombre
            bandera_hulu = False
#Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu.
        if genero == "Masculino" and ((edad >= 18 and edad <= 25) or (edad >= 36 and edad <= 49)):
            contador_hulu_filtrado += 1
    elif voto == "CODA":
        contador_coda += 1
        if edad > 25 and suscripcion == "Si":
            contador_coda_filtrado += 1
    else:
        contador_vix += 1
        edad_votantes_vix += edad

    contador_total += 1 
    
    seguir = input("Desea continuar? ")

#Determinar el promedio de edad de los encuestados que votaron por Vix+.
promedio_edad_vix = edad_votantes_vix / contador_vix 
print(f"El promedio de edad de las personas que tienen una suscripcion y votaron por Vix+ es de {promedio_edad_vix}")

# Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
if contador_coda > 0:
    porcentaje_coda = (contador_coda * contador_total) / 100
    porcentaje_coda = float (porcentaje_coda)
    print(f"El porcentaje de personas que votaron a CODA es de {porcentaje_coda}")

#Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
maximo_voto = contador_coda
maximo_votado = "CODA"
if maximo_voto < contador_hulu:
    maximo_voto = contador_hulu
    maximo_votado = "Hulu"
    if maximo_voto < contador_vix:
        maximo_voto = contador_vix
        maximo_votado = "Vix+"
elif maximo_voto < contador_vix:
    maximo_voto = contador_vix
    maximo_votado = "Vix+"

print(f"Las personas encuestadas de  género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu es de {contador_hulu_filtrado}")
print(f"La persona de menor edad que voto por Hulu tiene {min_edad_hulu}, es de genero {genero_hulu} y su nombre es {nombre_hulu}")
print(f"La franquicia que tuvo mas votos es {maximo_votado}")
