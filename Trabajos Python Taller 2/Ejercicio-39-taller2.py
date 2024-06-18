longitudes=""
digito0=""
numero=input("Número:")
while int(numero)%10 != 0 and int(numero) >= 0:
    if len(numero)%3 == 0:
        longitudes=longitudes+numero+"-"
    if "0" in numero:
        digito0=digito0+numero+"-"
    numero=input("Número:")
print("Números cuya cantidad de dígitos es múltiplo de 3:", longitudes)
print("Números que contienen el 0:", digito0)