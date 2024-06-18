num1,num2= 0,1
while num2 <= 1597:
    print (num1, num2, end= " ")
    num1= num1+num2
    num2=num1+num2

#Ejemplo para break

print ("\nWhile con la sentencia break\n")
contador= 0 
while contador<10:
    contador+=1
    if contador==5:
        break
    print("Valor actual de la variable es: ", contador)
print ("El programa ha finalizado")


#Ejemplo para continue

print ("\nWhile con la sentencia break\n")
contador= 0 
while contador<10:
    contador+=1
    if contador==5:
        continue
    print("Valor actual de la variable es: ", contador)
print ("El programa ha finalizado")
