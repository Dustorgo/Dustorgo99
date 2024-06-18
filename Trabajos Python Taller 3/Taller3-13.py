

puntuacion = float(input("Introduce tu puntuación: "))


if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2.400
else:
    nivel = "Meritorio"
    dinero = 2.400 * puntuacion


print("Tu nivel de rendimiento es:", nivel)
print("Recibirás:", dinero, "€")
