#funcion len()

#opcion 1
print("Hola tiene",len("Hola"), "caracteres.")

#opcion 2

longitud=len("La geekipedia")

print("La geekipedia tiene", longitud,"caracteres")

#concatenacion 
nombre= "carlos"
edad=22
print("Hola {} tienes {} años de edad.".format(nombre,edad))

#f-strings

nombre1="Duvan"
edad=22
print(f"Hola {nombre1} tienes {edad} años de edad")

#metodo strip()
cadena="\tHola Ernesto\n"
print(cadena)

cadena= cadena.strip("s tHo\n\t")
print(cadena)
