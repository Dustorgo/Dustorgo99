lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron ",lineas," líneas completas")