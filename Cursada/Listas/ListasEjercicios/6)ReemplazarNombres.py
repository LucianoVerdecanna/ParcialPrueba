lista_nombres = ["Luciano","Sebastian","Agustin","Valentino"]
print(lista_nombres)
def reemplazar_nombres(lista, nombre_a_reemplazar, nombre_reemplazo):
    cantidad_reemplazos = 0
    for i in lista:
        if i == nombre_a_reemplazar:
            i = nombre_reemplazo
            cantidad_reemplazos += 1
    
    return cantidad_reemplazos

print(reemplazar_nombres(lista_nombres, "Sebastian", "Lucho"))
print(lista_nombres)
