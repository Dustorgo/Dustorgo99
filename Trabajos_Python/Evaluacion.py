def frase_sin_espacios_letra_mayuscula():
    frase = input("Por favor, ingresa una frase: ")
    
    resultado = ""
    siguiente_letra_mayuscula = True

    for letra in frase:
        if letra == " ":
            siguiente_letra_mayuscula = True
        elif siguiente_letra_mayuscula:
            resultado += letra.upper()
            siguiente_letra_mayuscula = False
        else:
            resultado += letra.lower()

    print("Frase sin espacios con la siguiente letra en mayúscula:")
    print(resultado)


frase_sin_espacios_letra_mayuscula()