def area(tipo, base, altura):
    if tipo == "triangulo":
        return (base * altura) / 2
    elif tipo == "rectangulo":
        return base * altura
    elif tipo == "cuadrado":
        return base ** 2
print("Ingrese la figura a la cual quiere sacar su área")
tipo = input("Las figuras que puede usar son: triangulo, cuadrado, rectangulo: ")
base = float(input("Ingrese la base o lado: "))
if tipo == "cuadrado":
    altura = base
else:
    altura = float(input("Ingrese la altura: "))


final = area(tipo, base, altura)
print("El area del ",tipo,"es ",final)

