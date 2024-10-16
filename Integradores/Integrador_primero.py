#Luciano Verdecanna
#Div 301
#Una librería que se especializa en venta de libros importados desea calcular ciertas métricas en base a las ventas de sus productos.
# Se ingresa de cada venta:
# Título del libro
# Género: (Ciencia ficción – Drama – Terror)
# Material del libro (rústica – tapa dura)
# Importe (No pueden ser números negativos ni mayor a los 30000)
titulo = 0
genero = 0
materia = 0
importe = 0
seguir = "Si"
minimo = 0
maximo = 0
libro_mas_caro = 0
titulo_drama_barato = 0
bandera_maximo = True
contador_drama = 0
contador_terror = 0
contador_ficcion = 0

while seguir == "Si":
    titulo = input("Ingrese el nombre del libro: ")

    genero = input("Ingrese si su libro es de Ciencia ficcion - Drama - Terror: " )
    while genero != "Ciencia ficcion" and genero != "Drama" and genero != "Terror":
        genero = input("Ingrese el genero del libro nuevamente: ")

    material = input("Ingrese si su libro es de material Rustico o de Tapa dura: ")
    while material != "Rustico" and material != "Tapa dura":
        material = input("Ingrese nuevamente el material de su libro: ")

    importe = input("Ingrese el importe de su libro: ")
    importe = int(importe)
    while importe < 0 or importe > 30000:
        importe = input("Su importe no es valido, ingreselo nuevamente: ")
        importe = int(importe)
    
    if genero == "Drama":
        contador_drama += 1
        if importe < minimo or contador_drama == 1:
            minimo = importe
            titulo_drama_barato = titulo

    elif genero == "Ciencia ficcion":
        contador_ficcion += 1
    else:
        contador_terror += 1
    
    if importe > maximo or bandera_maximo == True:
        maximo = importe
        libro_mas_caro = titulo
        bandera_maximo = False
    
        if genero == "Ciencia ficcion":
            contador_ficcion += 1
        else:
            contador_terror += 1


    seguir = input("Desea agregar otro libro? ")


    sumacontadores = contador_drama + contador_ficcion + contador_terror
    porcentaje_terror = contador_terror / sumacontadores * 100 
    porcentaje_drama = contador_drama / sumacontadores * 100
    porcentaje_ficcion = contador_ficcion / sumacontadores * 100     

if contador_drama > 0:
    print("No se ingreso ningun libro de genero drama")
else:
    print(f"el precio del libro mas barato es de {minimo} y se llama {titulo_drama_barato}")


print(f"el libro mas caro se llama {libro_mas_caro}")
print(f"El porcentaje de los libros de terror es de {porcentaje_terror} ")
print(f"El porcentaje de los libros de drama es de {porcentaje_drama}")
print(f"El porcentaje de los libros de drama es de {porcentaje_ficcion}")