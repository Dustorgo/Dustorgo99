def maximo(a,b):
  if x>y:
    return x
  else:
    return y

 
def minimo(a,b):
  if x<y:
    return x
  else:
    return y

 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

#Solución: Las funciones no utilizan sus parámetros a, b sino las variables globales x, y. Para corregir el error se deben utilizar los parámetros dentro del cuerpo de ambas funciones.