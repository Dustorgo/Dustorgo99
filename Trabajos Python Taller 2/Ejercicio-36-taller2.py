numero=int(input("Escribí un número:"))
total=0
while numero != 0:
    ultimoDigito=numero%10
    total=total+ultimoDigito
    numero=numero//10
print("Suma de los dígitos:", total)