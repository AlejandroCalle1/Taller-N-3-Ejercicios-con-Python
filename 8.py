url="https://retosdeprogramacion.com?year=2023&challenge=0"
parametros=url.split("?")
parametros = parametros[1].split("&")
for parametro in parametros:
    if "=" in parametro:
        valores = parametro.split("=")[1]  
        print(valores)
