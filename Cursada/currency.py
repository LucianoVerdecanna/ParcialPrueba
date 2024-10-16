pesos_colombianos = input("Ingrese la cantidad de pesos colombianos: ")
pesos_colombianos = int(pesos_colombianos)
while pesos_colombianos < 0:
    pesos_colombianos = input("Ingrese nuevamente su cantidad de pesos colombianos: ")
    pesos_colombianos = int(pesos_colombianos)

soles_peruanos = input("Ingrese la cantidad de soles peruanos: ")
soles_peruanos = int(soles_peruanos)
while soles_peruanos < 0:
    soles_peruanos = input("Ingrese nuevamente su cantidad de soles peruanos: ")
    soles_peruanos = int(soles_peruanos)

reales_brasileros = input("Ingrese la cantidad de reales brasileros: ")
reales_brasileros = int(reales_brasileros)
while reales_brasileros < 0:
    reales_brasileros = input("Ingrese nuevamente su cantidad de reales brasileros: ")
    reales_brasileros = int(reales_brasileros)


reales_a_dolar = reales_brasileros / 5.56

soles_a_dolar = soles_peruanos / 3.74

pesos_a_dolar = pesos_colombianos / 4085

total_dolares = reales_a_dolar + soles_a_dolar + pesos_a_dolar
total_dolares = int(total_dolares)

print(f"El total de dolares es de: ${total_dolares}")
