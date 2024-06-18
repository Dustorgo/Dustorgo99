
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M o H): ")


nombre = nombre.lower()


if sexo == "m":
    if nombre < "m":
        grupo = "A"
    else:
        grupo = "B"


else:
    if nombre > "n":
        grupo = "A"
    else:
        grupo = "B"


print("Tu grupo es:", grupo)
