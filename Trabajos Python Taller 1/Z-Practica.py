
print("sistema para calcular el proedio de un alumno:")

Nombre=input("cual es tu nombre: ")

matematicas = float(input(Nombre + " dame tu calificacion de matematicas: "))
quimica = int(input(Nombre+ " dame tu calificacion de quimica: "))
biologia = float(input(Nombre+ " dame tu calificacion de biologia : "))

promedio= (matematicas+quimica+biologia) / 3
promedio=int(promedio)

if promedio >= 6:
    print(" Aprobaste " + Nombre + " felicidades, con un promedio de: ",promedio)
elif promedio ==5:
    print(Nombre+ " Quedaste en espera por el docente tu promedio es: ", promedio)       
else:
    print ( Nombre+ " Sigue intentandolo tu promedio es de : ", promedio)

print("fin.")

