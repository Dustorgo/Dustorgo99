class Figuras:

    def __init__(self,peso,color,nombre):
        self.peso=peso
        self.color=color
        self.nombre=nombre

class Cuadrado(Figuras):
    def __init__(self,peso,color,nombre,lado_izquierdo,lado_abajo):
        super().__init__(peso,color,nombre)
        self.lado_izquierdo=lado_izquierdo
        self.lado_abajo=lado_abajo

    def calcular_area(self):
        return self.lado_izquierdo*self.lado_abajo
    
class Circulo(Figuras):
    def __init__(self,peso,color,nombre,radio):
        super().__init__(peso,color,nombre)
        self.radio=radio
    
    def calcular_area(self):
        return 3.1416 * self.radio **2
    
class Triangulo(Figuras):
    def __init__(self,peso,color,nombre,base,altura):
        super().__init__(peso,color,nombre)
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return (self.base*self.altura)/2
    

Cuadrado1=Cuadrado(10,"Azul","Cuadrado",6,6)
Circulo1=Circulo(12,"Rojo","Circulo",4)
Triangulo1=Triangulo(15,"Verde","Triangulo",4,5)

print(f"El area de su circulo es: {Cuadrado1.calcular_area()} cm")
print(f"El area de su cuadrado es: {Circulo1.calcular_area()} cm")
print(f"El area de su triangulo es: {Triangulo1.calcular_area()} cm")









