# Factura F190374
nro_factura = 0
factura = 0
nombre = 0
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
contador = 0
total_de_caja = 0
for i in range (0,5):
    lista = []
    total = 0
    nro_factura += 1
    cantidad_chaqueta = 0
    cantidad_guantes = 0
    cantidad_gorro = 0
    seguir = "Si"
    nombre = input("Ingrese su nombre y apellido: ")
    while seguir == "Si":
        producto = input("Ingrese el producto que desea llevar: ")
        if producto == "Chaqueta":
            print(f"El producto que lleva es la chaqueta y cuesta {chaqueta * 1.21}")
            total = total + (chaqueta * 1.21)
            cantidad_chaqueta += 1
        elif producto == "Guantes":
            print(f"El producto que lleva son los guantes y cuesta {guantes * 1.21}")
            total = total + (guantes * 1.21)
            cantidad_guantes += 1
        elif producto == "Gorro":
            print(f"El producto que lleva es el gorro y cuesta {gorro * 1.21}")
            total = total + (gorro * 1.21)
            cantidad_gorro += 1

        lista = lista + [producto]
        seguir = input("Desea seguir comprando? ")

        

    print(f"Factura {nro_factura}")
    print(f"{nombre}")
    for producto in lista:
        if producto == "Chaqueta":
            print(f"{producto}       Unidades: {cantidad_chaqueta}  Subtotal: {chaqueta}  IVA: 21%   Total: ${chaqueta * 1.21}")
        elif producto == "Guantes":
            print(f"{producto}       Unidades: {cantidad_guantes}   Subtotal: {guantes}   IVA: 21%   Total: ${guantes * 1.21}")
        elif producto == "Gorro":
            print(f"{producto}       Unidades: {cantidad_gorro}     Subtotal: {gorro}     IVA: 21%   Total: ${gorro * 1.21}")
        
        print("---------------------")
        print (f"${total}")

    total_de_caja = total_de_caja + total


print(f"Lo recaudado por la caja es de ${total_de_caja}")



