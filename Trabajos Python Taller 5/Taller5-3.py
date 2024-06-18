def esPar(numero):
   return numero%2 == 0

def sumatoriaDigitos(numero):
   total=0
   while numero != 0:
       ultimoDigito=numero%10
       total=total+ultimoDigito
       numero=numero//10
   return total

cantidadImpares=0
n=int(input("Escribí un número:"))
while sumatoriaDigitos(n)<1000 and sumatoriaDigitos(n)%3!=0:
    if not esPar(n):
        cantidadImpares=cantidadImpares+1
    n=int(input("Escribí un número:"))
print("Cantidad de impares:", cantidadImpares)

