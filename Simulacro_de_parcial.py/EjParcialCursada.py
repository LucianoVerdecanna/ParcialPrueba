from FuncionesParcial import *

sucursales = ["Santa Fe", "Cordoba", "Buenos Aires", "Salta"]
productos = ["Frutas", "Verduras", "Carnes", "Bebidas", "Lacteos"]
opcion = 1
bandera = True


while bandera == True:
    print("[1] Cargar existencias")
    print("[2] Cantidad total de productos por sucursal")
    print("[3] Reponer productos")
    print("[4] Maxima cantidad por tipo de producto")
    print("[5] Sucursal con mayor valor almacenado")
    print("[6] Sucursales con mas de 20.000 unidades")
    print("[7] Porcentaje de productos")
    print("[8] Informe de recaudacion")
    print("[0] Salir")
    print("")
    opcion = int(input("Que opcion desea elegir? "))
    

    match opcion:
        case 1:
            print(visualizar_matriz(4,5, cargar_existencia(sucursales, productos)))
            
        case 2:
            total_productos(sucursales)
        case 3:
            reponer_productos(sucursales, productos)
        case 4:
            mayor_cantidad_de_tipo_de_producto(sucursales, productos)

#         case 5:
#             sucursal_con_mayor_valor(listaDePrecios)
#         case 6:
#             Sucursales_con_mas_de_20000(sucursal)
#         case 7:
#             porcentaje_de_producto(tipoProducto)
#         case 8:
#             sucursales_segun_recaudacion(sucursales)
            # case _:
            #     bandera = False
        



    



