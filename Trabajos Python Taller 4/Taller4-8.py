objetivo = float(input("¿Cuántos euros quiere ahorrar?: "))
while objetivo < 0:
    print("Por favor, escriba una cantidad positiva.")
    objetivo = float(input("¿Cuántos euros quiere ahorrar?: "))
    
ahorrado = 0.0
while objetivo > ahorrado:
    ahorro = float(input("¿Cuántos euros quiere meter en la hucha?: "))
    while ahorro < 0:
            print("Por favor, escriba una cantidad positiva.")
            ahorro = float(input("¿Cuántos euros quiere meter en la hucha?: "))
    ahorrado += ahorro

print(f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.")