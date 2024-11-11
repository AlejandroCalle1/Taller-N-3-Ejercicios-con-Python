def conversor(horario, cantidad):
    if horario == "dias":
        return cantidad * 86400000
    elif horario == "horas":
        return cantidad * 3600000
    elif horario == "minutos":
        return cantidad * 60000
    elif horario == "segundos":
        return cantidad * 1000

print("Este programa convierte días, horas, minutos o segundos a milisegundos ")
horario = input("Ingrese la unidad de tiempo (dias, horas, minutos, segundos): ")
cantidad = int(input("Ingrese la cantidad a convertir: "))
resultado = conversor(horario, cantidad)
print("El resultado en milisegundos es:", resultado)
