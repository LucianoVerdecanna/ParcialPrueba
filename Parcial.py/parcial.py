#Luciano Verdecanna
#Div 301
# Usuarios vendedores de MercadoLibre
# Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas
# publicaciones.
# ● Los datos que se cargarán son:
# ● Nombre de usuario
# ● Edad (validar)
# ● Cantidad de productos (validar-número entero positivo).
# ● Número de publicaciones (validar-número entero positivo, hasta 1000).
# ● Tipo ("producto", "servicio", "subasta")
# ● Cuenta activa ("si", "no")
# Se necesita saber
# Tema C:
# 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “subasta”,
# cuya edad supere los 60 años.
# 2. Nombre y tipo de publicacion de menor edad con menos de 300 publicaciones.
# 3. Porcentaje de cuentas inactivas.
# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo
# “subasta”.
# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “inactiva”.

contador = 0
contador_subasta = 0
contador_mas_sesenta = 0
subasta_inactiva = 0
edad = 0
edad_subasta = 0
cantidad_productos = 0
producto_inactivo = 0
servicio_inactivo = 0
numero_publicaciones = 0
bandera_edad = True
menor_edad = 0

while contador < 10:
    nombre = input("Ingrese su nombre: ")

    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("Edad no valida, ingrese su edad nuevamente: ")
        edad = int(edad)

    cantidad_productos = input("Ingrese la cantidad de productos: ")
    cantidad_productos = int(cantidad_productos)
    while cantidad_productos <= 0:
        cantidad_productos = input("Ingrese nuevamente la cantidad de productos: ")
        cantidad_productos = int(cantidad_productos)
    
    numero_publicaciones = input("Ingrese la cantidad de publicaciones: ")
    numero_publicaciones = int(numero_publicaciones)
    while numero_publicaciones <= 0 or numero_publicaciones > 1000:
        numero_publicaciones = input("Ingrese nuevamente el numero de publicaciones: ")
        numero_publicaciones = int(numero_publicaciones)
    
    tipo = input("Ingrese el tipo de publicacion: ")
    while tipo != "producto" and tipo != "servicio" and tipo != "subasta":
        tipo = input("Tipo no valido, reingrese el tipo de publicacion: ")
    
    cuenta_activa = input("Su cuenta esta activa? si/no: ")
    while cuenta_activa != "si" and cuenta_activa != "no":
        cuenta_activa = input("No respondio la pregunta correctamente, su cuenta esta activa? si/no: ")
    
    # 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “subasta”, cuya edad supere los 60 años.
    if cuenta_activa == "si":
        if tipo == "subasta":
            contador_subasta += 1
            edad_subasta += edad
            if edad > 60:
                contador_mas_sesenta += 1
    elif cuenta_activa == "no":
        if tipo == "subasta":
            subasta_inactiva += 1
        elif tipo == "producto":
            producto_inactivo += 1 
        else:
            servicio_inactivo += 1
    
    # 2. Nombre y tipo del usuario de menor edad con menos de 300 publicaciones.
    if menor_edad > edad or bandera_edad == True:
        menor_edad = edad
        bandera_edad = False
        if numero_publicaciones < 300:
            tipo_del_menor = tipo
            nombre_menor = nombre
    
    contador += 1

# 3. Porcentaje de cuentas inactivas.
inactivas_total =  subasta_inactiva + producto_inactivo + servicio_inactivo
porcentaje_inactivas = (inactivas_total * 100) / 10
print (f"El porcentaje de cuentas inactivas es de %{porcentaje_inactivas}")

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “subasta”.
if contador_subasta > 0:
    promedio_subasta = edad_subasta / contador_subasta
    print(f"El promedio de edad de las personas que tienen publicaciones del tipo subasta es de {promedio_subasta} años")
else:
    print(f"No hay promedio de edad ya que no se ingresaron usuarios con tipo de publicacion")


# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “inactiva”.
maximo_publicaciones = subasta_inactiva
if maximo_publicaciones > producto_inactivo and maximo_publicaciones > servicio_inactivo:
    print(f"El tipo con mas publicaciones es SUBASTA!")
else:
    if maximo_publicaciones < producto_inactivo:
        maximo_publicaciones = producto_inactivo
        if maximo_publicaciones < servicio_inactivo:
            print("El tipo con mas publicaciones es SERVICIO!")
        else:
            print("El tipo con mas publicaciones es PRODUCTO!")
    
print(f"La cantidad de usuarios con la cuenta activa, mas de sesenta años y que tengan publicaciones del tipo subasta es de {contador_mas_sesenta}")
print(f"El nombre de la persona con menor edad y que tiene menos de 300 publicaciones es de {nombre_menor} y sus publicaciones son del tipo {tipo_del_menor}")

