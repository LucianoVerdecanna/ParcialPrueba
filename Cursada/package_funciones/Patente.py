# Desarrollar una función que verifique que una placa de auto es válida. Este tipo de validación se puede aplicar en sistemas de registro de vehículos, donde es necesario verificar que las placas ingresadas cumplen con un formato estándar. Este ejemplo muestra cómo manipular strings carácter por carácter para verificar y asegurar que cumplan ciertas reglas y formatos específicos.



def validar_placa():
    placa = input("Ingrese su patente: ")

    if len(placa) != 7:
        return False
    
    if placa[:3].isupper() and placa[2:5].isdigit() and placa[5:7].isupper():
        return True
    else:
        return False
        
if validar_placa():
    print("Tu patente es valida!")
else:
    print("Tu patente es invalida.")
                

