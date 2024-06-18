class CuerpoCeleste:
    def __init__(self,nombre,masa,diametro,periodo_rotacion):
        self.nombre = str
        self.masa = masa
        self.diametro = diametro
        self.periodo_rotacion = periodo_rotacion

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, periodo_rotacion):
        super().__init__(nombre, masa, diametro, periodo_rotacion)
        self.periodo_traslacion = int
        self.distancia_media = int

    def encontrar_informacion(self):
      self.nombre = input("Digite el nombre del planeta que quiere informacion: ")
      if self.nombre == "Tierra":
        return "Información Planeta Tierra: \n Masa: 5.972 \n Diametro: 12742 \n Periodo de rotacion: 23.934472222 \n Periodo de traslación: 365.25636301 \n Distancia Media: 149.6"

class Satelite(CuerpoCeleste):
    def __init__(self, nombre, masa, diametro, periodo_rotacion, planeta):
        super().__init__(nombre, masa, diametro, periodo_rotacion)
        self.planeta = str

    def encontrar_informacion(self):
      self.nombre = input("Digite el nombre del satélite que quiere informacion: ")
      if self.nombre == "Luna":
        return "Información de la Luna: \n Masa: 7.348 \n Diametro: 3474 \n Periodo de rotacion: 27.32166 \n Planeta: Tierra"

planeta1=Planeta("Tierra",0,0,0)
print (planeta1.encontrar_informacion())

