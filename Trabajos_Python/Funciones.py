def quitar(frase):
    palabras = frase.split()
    frase1 = ""
    for i, palabra in enumerate(palabras):
        if i == 0:  
            frase1+= palabra
        else:
            frase1 += " " + palabra[0].upper() + palabra[1:]

    return frase1
if __name__ == "__main__":
    frase = input("Escriba una frase: ")
    print(quitar(frase))
