cateto1 = input("Ingrese el valor del cateto 1: ")
cateto1 = int(cateto1)
while cateto1 < 0:
    cateto1 = input("Reingrese nuevamente el valor: ")
    cateto1 = int(cateto1)

cateto2 = input("Ingrese el valor del cateto 2: ")
cateto2 = int(cateto2)
while cateto2 < 0:
    cateto2 = input("Reingrese nuevamente el valor: ")
    cateto2 = int(cateto2)

do = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5

print(f"El valor de la hipotenusa es de: {do}")