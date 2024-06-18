cadena=input("Cadena de caracteres:")
letras="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
digitos="0123456789"
cantidadLetras=0
cantidadDigitos=0
cantidadSimbolos=0
cantidadMultiplos4=0
for i in cadena:
    if i in letras:
        cantidadLetras=cantidadLetras+1
    else:
        if i in digitos:
            cantidadDigitos=cantidadDigitos+1
            if int(i)%4 == 0:
                cantidadMultiplos4=cantidadMultiplos4+1
        else:
            cantidadSimbolos=cantidadSimbolos+1
print ("Cantidad de letras:", cantidadLetras)
print ("Cantidad de dígitos numéricos:", cantidadDigitos)
print ("Cantidad de símbolos:", cantidadSimbolos)
print ("Cantidad de múltiplos de 4:", cantidadMultiplos4)