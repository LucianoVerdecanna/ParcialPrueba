contraseña = 0
mayusculas = 0
minusculas = 0
numeros = 0
def contraseña_valida(contraseña):
    contraseña = input("Ingrese su contraseña: ")
    bandera_mayus = False
    bandera_minus = False
    bandera_num = False
    for i in contraseña:
        if palabra[i].isupper():
            bandera_mayus = True
        elif palabra[i].islower():
            bandera_minus = True
        elif palabra[i].isdigit():
            bandera_num = True
    if bandera_num == True and bandera_minus == True and bandera_mayus == True:
        return True
    else:
        return False   

        
print(contraseña_valida(contraseña))