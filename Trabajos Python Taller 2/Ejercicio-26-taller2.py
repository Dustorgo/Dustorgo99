frase1=input("Digita la frase: ")
vocales="aeiou"
cantidad=0
for i in frase1:
    if i in vocales:
        cantidad=cantidad+1
print("Vocales:", cantidad)