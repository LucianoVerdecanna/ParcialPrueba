lista = []
for i in range(0,3):
    objeto = input("Ingrese lo que quiere guardar en la lista: ")
    lugar = int(input("Ingrese el lugar donde lo quiere guardar: "))
    lista[lugar] = objeto

for i in lista:
    print(lista(i))
