def dibujarFigura(tipo, tamaño):
    if tipo == "cuadrado":
        for i in range(tamaño):
            print("* " * tamaño)
    elif tipo == "triangulo":
        for i in range(1,tamaño +1):
            print("* " * i)
    
tamaño = int(input("Introduce el tamaño que deseas: "))
tipo = input("Introduce la figura a dibujar (cuadrado o triangulo): ")

dibujarFigura(tipo, tamaño)