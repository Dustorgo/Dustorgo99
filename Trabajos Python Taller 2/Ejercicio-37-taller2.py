multiplosDe3=0
numero=int(input("Número (-1 para terminar el programa):"))
while numero!=-1:
    if numero%3 == 0:
        multiplosDe3=multiplosDe3+1
    digitosPares=0
    digitosImpares=0
    while numero!=0:
        ultimodigito=numero%10
        if ultimodigito%2==0:
            digitosPares=digitosPares+1
        else:
            digitosImpares=digitosImpares+1
        numero=numero//10
    print("Dígitos pares:", digitosPares)
    print("Dígitos impares:", digitosImpares)
    numero=int(input("Número (-1 para terminar el programa):"))
print("Se ingresaron", multiplosDe3, "múltiplos de 3.")