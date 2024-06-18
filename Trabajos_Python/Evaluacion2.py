def frase_sin_espacios_letra_mayuscula():
    frase = input("Por favor, ingresa una frase: ")
    
    # Inicializar una cadena para almacenar el resultado
    resultado = ""
    
    # Variable para controlar si la siguiente letra debe ser mayúscula
    siguiente_letra_mayuscula = True

    for letra in frase:
        if letra == " ":
            siguiente_letra_mayuscula = True
        elif siguiente_letra_mayuscula:
            resultado += letra[0].upper()
            siguiente_letra_mayuscula = False
        else:
            resultado += letra.lower()

    print("Frase sin espacios con la siguiente letra en mayúscula:")
    print(resultado)

# Llamar a la función para probarla
frase_sin_espacios_letra_mayuscula()