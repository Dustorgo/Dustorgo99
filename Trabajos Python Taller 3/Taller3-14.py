Edad=int(input("Cual es tu edad: "))

if Edad >=0 and Edad <4:
    print("Felicidades, tu entrada es gratis")
elif Edad >=4 and Edad<18:
    print("Lo siento debes pagar un valor de 5€")
else:
    print("Debes pagar 10€")