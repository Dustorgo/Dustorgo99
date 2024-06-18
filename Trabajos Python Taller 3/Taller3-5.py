def num_semanas(horas):
    return horas // (24 * 7)


def num_dias(horas):
    return horas // 24


def num_horas(horas):
    return horas


def main():
    horas = int(input("Introduce el número total de horas: "))

    opcion = int(input("Elige una opción: 1. Semanas, 2. Días, 3. Horas: "))

    if opcion == 1:
        print("El número total de semanas es:", num_semanas(horas))
    elif opcion == 2:
        print("El número total de días es:", num_dias(horas))
    elif opcion == 3:
        print("El número total de horas es:", num_horas(horas))
    else:
        print("Opción incorrecta")


if __name__ == "__main__":
    main()
