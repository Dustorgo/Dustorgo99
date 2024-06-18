print("\nPrograma para determinar ¿Cual es el numero mas grande\n")

Num1=float(input("Escribe el primer numero: "))
Num2=float(input("Escribe el segundo numero: "))
Num3=float(input("Escribe el tercer numero: "))

if (Num1>Num2>Num3):
    print("El numero", Num1,"Es el numero mas grande de los tres")
elif (Num2>Num3):
    print("El numero", Num2, "Es el numero mas grande de los tres")
else:
    print("El numero",Num3,"Es el numero mas grande de los tres ")

