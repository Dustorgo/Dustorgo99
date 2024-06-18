print ("Calculadora con una sola variable\n")

print("Menu de opciones")

print("1. Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Division Entera")
print("6.Exponente")
print("7.Modulo o resto\n")

numero=int(input("Digite la opcion que desee: "))
if numero==1:

    print ("Elegiste suma\n")
    numero=int(input("ingresa el primer numero: "))
    numero+= int(input("Ingresa el segundo numero: "))
    print("El resultado de la suma es: ", numero)
    
elif numero ==2:

    print ("Elegiste resta\n")
    numero=int(input("ingresa el primer numero: "))
    numero-= int(input("Ingresa el segundo numero: "))
    print("El resultado de la resta es: ", numero)

elif numero ==3:

    print ("Elegiste multiplicacion\n")
    numero=int(input("ingresa el primer numero: "))
    numero*= int(input("Ingresa el segundo numero: "))
    print("El resultado de la multiplicacion es: ", numero)

elif numero ==4:

    print ("Elegiste Division\n")
    numero=int(input("ingresa el primer numero: "))
    numero/= int(input("Ingresa el segundo numero: "))
    print("El resultado de la Division es: ", round(numero,3))

elif numero ==5:

    print ("Elegiste Division Entera\n")
    numero=int(input("ingresa el primer numero: "))
    numero//= int(input("Ingresa el segundo numero: "))
    print("El resultado de la division entera es: ", numero)

elif numero ==6:

    print ("Elegiste Exponente\n")
    numero=int(input("ingresa el primer numero: "))
    numero**= int(input("Ingresa el segundo numero: "))
    print("El resultado de la Exponente es: ", numero)

elif numero ==7:

    print ("Elegiste Modulo\n")
    numero=int(input("ingresa el primer numero: "))
    numero%= int(input("Ingresa el segundo numero: "))
    print("El resultado de la Modulo es: ", numero)

else:
    print("La opcion no existe\n")


print("El proceso ha llegado a su fin.")