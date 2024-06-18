contraseña = "contraseña"

contraseña2 = input("Introduce la contraseña: ")

contraseña2 = contraseña2.lower()


if contraseña2 == contraseña.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
