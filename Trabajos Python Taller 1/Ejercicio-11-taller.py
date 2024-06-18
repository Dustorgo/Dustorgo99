Fecha=int(input("Digite su fecha con 8 numeros, recuerde el formato de DDMMAAAA: "))
Año=Fecha%10000 #me muestre los 4 ultimos
Dia=Fecha//1000000 #Que me elimine los primeros 6
Mes=(Fecha//10000)%100

print(Dia,("/"),Mes,("/"),Año,)


