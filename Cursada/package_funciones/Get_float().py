mensaje_error = "El dato que ingreso no es correcto"
mensaje = 0
def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
    mensaje = float(input(f"Ingrese un numero entre {minimo} y {maximo} inclusive : "))
    contador = 1
    while mensaje >= maximo or mensaje <= minimo:
        if contador != reintentos:
            print(mensaje_error)
            mensaje = float(input("Ingrese su numero nuevamente: "))
            contador += 1
        else:
            mensaje = None
            return mensaje 
    return mensaje

print (get_int(mensaje, mensaje_error, 1, 8, 5))