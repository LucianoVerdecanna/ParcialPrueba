


cantidad_alumnos = int(input("Ingrese cuantos estudiantes ingresara : "))
lista_nombres = []
lista_edad = []
lista_nota_final = []
for alumno in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    lista_nombres += [nombre]

    edad = input("Ingrese la edad: ")
    lista_edad += [edad]

    nota_final = int(input("Ingrese la nota final del alumno: "))
    while nota_final > 10:
        nota_final = input("Nota invalida, ingrese nuevamente la nota: ")
    lista_nota_final += [int(nota_final)]

    for i in lista_nombres:
        if i == nombre:
            print(f"El nombre del alumno es {i}")  
    for i in lista_edad:
        if i == edad:
            print(f"Su edad es {i}")
    for i in lista_nota_final:
        if i == nota_final:
            print(f"Y su nota es {i}")


def promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
        suma = int(suma)
    
    return suma

promedio_notas = promedio(lista_nota_final) / len(lista_nota_final)
print(f"El promedio de todas las notas de los alumnos ingresados es de: {promedio_notas}")

def buscar_estudiante(nombre, lista):
    contador = 0
    for i in lista:
        if i == nombre:
            break
        elif contador == len(lista):
            print("El nombre que introdujo no se encuentra en la lista")
        else:
            contador += 1

    return contador

seguir =  "Si"
while seguir == "Si":
    nombre_a_buscar = input("Ingrese el nombre que desea buscar: ")
    print(f"El nombre del alumno que usted quiere saber es : {lista_nombres[buscar_estudiante(nombre_a_buscar, lista_nombres)]}")
    print(f"Su edad es de: {lista_edad[buscar_estudiante(nombre_a_buscar, lista_nombres)]} años")
    print(f"Su nota final es de: {lista_nota_final[buscar_estudiante(nombre_a_buscar, lista_nombres)]}")
    seguir =  input("Desea seguir?")  





def mayor_nota(lista):
    mejor_nota = 0
    for i in lista:
        if i > mayor_nota:
            mayor_nota = i

    for i in lista:
        contador = 0
        if i == mayor_nota:
            break
        else:
            contador += 1
    
    return contador

print(f"La mejor nota es de: {lista_nombres[mayor_nota(lista_nota_final)]}")




