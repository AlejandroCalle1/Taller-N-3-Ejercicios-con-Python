def marco(texto):
    frase = texto.split()  
    palabra_larga = max(len(palabra) for palabra in frase)  

    print("*" * (palabra_larga + 4))

    for palabra in frase:
        print("* " + palabra + " *")  
    
    print("*" * (palabra_larga + 4))

marco("¿Qué te parece el reto?")