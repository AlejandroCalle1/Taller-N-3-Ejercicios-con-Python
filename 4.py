def amstrong(numero):
    convertir = str(numero)
    total=0
    for i in range(len(convertir)):
        total= total+(int(convertir[i]))**len(convertir)
        #Se va accediendo a los numeros de el numero que fue almacenado en (convertir)
    if total == numero:
        return True
    else:
        return False
print(amstrong(126))
