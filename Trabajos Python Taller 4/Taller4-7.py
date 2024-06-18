objetivo = float(input("¿Cuántos euros quiere ahorrar?: "))

ahorrado = 0.0
while objetivo > ahorrado:
        ahorrado += float(input("¿Cuántos euros quiere meter en la hucha?: "))

print(f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.")
