
# mensaje_error = "El dato que ingreso no es correcto"
# mensaje = 0
# def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
#     mensaje = int(input(f"Ingrese un numero entre {minimo} y {maximo} inclusive : "))
#     contador = 1
#     while mensaje >= maximo or mensaje <= minimo:
#         if contador != reintentos:
#             print(mensaje_error)
#             mensaje = int(input("Ingrese su numero nuevamente: "))
#             contador += 1
#         else:
#             mensaje = None
#             return mensaje 
#     return mensaje

# print (get_int(mensaje, mensaje_error, 1, 8, 5))

def get_string(longitud: int) -> str|None:
    palabra = input("Ingrese una palabra: ")
    contador = 0
    while len(palabra)>= longitud:
        contador += 1
        if contador != reintentos:
            mensaje_error = "Demasiado largo"
            palabra = input("Reingrese su palabra: ")
        else:
            palabra = None
            return palabra
    return palabra
palabra = ""
reintentos = 5
contador = 0
print (get_string(5))
