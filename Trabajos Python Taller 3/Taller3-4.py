def es_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


def main():

    a = float(input("Introduce el primer lado del triángulo: "))
    b = float(input("Introduce el segundo lado del triángulo: "))
    c = float(input("Introduce el tercer lado del triángulo: "))

    if es_triangulo(a, b, c):
        print("Los tres lados forman un triángulo")
        print("El tipo de triángulo es:", tipo_triangulo(a, b, c))
    else:
        print("Los tres lados no forman un triángulo")


if __name__ == "__main__":
    main()
