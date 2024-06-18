
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print ("El factorial es: ",factorial)