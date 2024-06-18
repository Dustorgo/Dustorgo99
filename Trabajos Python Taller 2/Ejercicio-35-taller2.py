cadenaTotal=""
cantidad_a=0
caracter=input("Escribí un carácter:")
while (len(caracter)==1 and caracter!="0"):
    cadenaTotal=cadenaTotal+caracter
    if caracter=="a":
        cantidad_a=cantidad_a+1
    caracter=input("Escribí un carácter:")
print("El string completo es:", cadenaTotal)
print("Porcentaje de letras 'a':", (cantidad_a*100)/len(cadenaTotal))