def cuenta_regresiva(numero):
    
    if numero == 0:
        return 0
    else:
        print(numero)
        return cuenta_regresiva(numero - 1)
    

print(cuenta_regresiva(9))
