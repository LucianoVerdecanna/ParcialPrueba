# Factura F190374
Factura = int(input("Ingrese el numero de factura: "))
nombre = input("Ingrese su nombre y apellido: ")
producto = 0
seguir = "Si"
chaqueta = 82.64
guantes = 16.53
gorro = 16.53
cantidad_guantes = 0
cantidad_chaqueta = 0
cantidad_gorro = 0
total = 0
lista = []
ista_precios = []

producto = input("Ingrese su producto: ")
precio = input("Ingrese el precio del producto: ")
    
lista = lista + [producto]
lista_precio = lista + [precio]


for producto in lista:
    print(f"{producto} {precio(lista_precio)}")

def precio(lista_precio):
    for precio in lista_precio:
        return precio
