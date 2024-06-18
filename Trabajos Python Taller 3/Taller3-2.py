
nombre = input("Introduce tu nombre: ")


apellido1 = input("Introduce tu primer apellido: ")


fullName = nombre + " " + apellido1

edad = input("Introduce tu edad: ")


try:
    edad = int(edad)
except ValueError:
    edad = None


if edad is not None:
    year = 2023 - edad


print("Nombre completo:", fullName)
if edad is not None:
    print("Año de nacimiento:", year)
    if edad < 18:
        print("Eres menor de edad, no podemos darte de alta hasta el año", year + 18)
    elif edad >= 18 and edad < 25:
        print("Tienes un 10% de descuento")
    elif edad >= 25:
        print("Lo sentimos, pero no tienes descuento")
    else:
        print("Premio, tienes un descuento especial del 20%")
else:
    print("Hay un error, no hemos podido calcular tu edad")
    print("Año de nacimiento: no puede calcularse")
