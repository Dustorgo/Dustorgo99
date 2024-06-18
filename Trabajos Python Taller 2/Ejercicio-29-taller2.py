Suma_Numeros_Positivos=0
Cantidad_Numeros_Positivos=0
Suma_Numeros_Negativos=0
for i in range(6):
   Numero=int(input("Digita un número: "))
   if Numero>0:
       Suma_Numeros_Positivos=Suma_Numeros_Positivos+Numero
       Cantidad_Numeros_Positivos=Cantidad_Numeros_Positivos+1
   else:
       Suma_Numeros_Negativos=Suma_Numeros_Negativos+Numero
print("Sumatoria de los negativos: ", Suma_Numeros_Negativos)
if Cantidad_Numeros_Positivos!=0:
   print("Promedio de los positivos: ",Suma_Numeros_Positivos/Cantidad_Numeros_Positivos)
