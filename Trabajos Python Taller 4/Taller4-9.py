password_1 = input("Escriba su contraseña: ")
limite = 3
print(f"Tiene {limite} intentos para confirmar su contraseña.")
password_2 = input("Escriba de nuevo su contraseña: ")
contador = 1

while password_1 != password_2 and contador < limite:
    print("Las contraseñas no coinciden. Inténtelo de nuevo.")
    password_2 = input("Escriba de nuevo su contraseña: ")
    contador += 1

if password_1 == password_2:
    print("Contraseña confirmada. ¡Hasta la vista!")
else:
    print("Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!")