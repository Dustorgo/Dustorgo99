frase1=input("Digita la frase:")
caracter=input("Digita un carácter:")
nueva=""
for c in frase1:
    if c==caracter:
        nueva=nueva+"*"
    else:
        nueva=nueva+c
print(nueva)