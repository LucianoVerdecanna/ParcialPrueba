

def esalpha(letra):
    if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122):
        return True
    else:
        return False


def esnumero(letra):
    if ord(letra) >= 48 and ord(letra) <= 57:
        return True
    else:
        return False


def cadenaascii(cadena):
    bandera_cadena = True

    for i in cadena:
        if esalpha(i) == False:
            bandera_cadena = False
            
    if bandera_cadena == True:
        return cadena
    else:
        return False
        

def cifrado(cadena, desplazamiento):
    cadena_alterada = ""
    caracter_cifrado = 0
    for i in cadena:
        letra = ord(i) + desplazamiento
        if letra <= 90:
            caracter_cifrado = chr(letra)
            cadena_alterada += caracter_cifrado
        else:
            while letra > 90:
                distancia = letra - 90
                letra = 64 + distancia
            caracter_cifrado = chr(letra)
            cadena_alterada += caracter_cifrado
    return(cadena_alterada)

print(cifrado("LA SUERTE ESTA ECHADA", 8))

def descifrar(cadena, desplazamiento):
    cadena_alterada = ""
    caracter_cifrado = 0
    for i in cadena:
        letra = ord(i) - desplazamiento
        if letra >= 65:
            caracter_cifrado = chr(letra)
            cadena_alterada += caracter_cifrado
        else:
            distancia = letra - 65
            letra = 91 - distancia
            caracter_cifrado = chr(letra)
            cadena_alterada += caracter_cifrado
    return(cadena_alterada)

print(descifrar("YN-FHREGR-RFGN-RPUNQN" , 8))




            
        
