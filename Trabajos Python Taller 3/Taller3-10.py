edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))


if edad >= 16:
    if ingresos >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")
else:
    print("No tienes que tributar")
