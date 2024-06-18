class Lapiceros:
    def __init__(self,color_atributo,tamano_atributo,fabricante_atributo):
        self.color=color_atributo
        self.tamano=tamano_atributo
        self.fabricante=fabricante_atributo
    
        print(f"soy un lapicero nuevo con color: {self.color} con tamano: {self.tamano} y con fabricante: {self.fabricante}")

#instanciar-cree un objeto que nacio de una clase 

lapicero1=Lapiceros("azul", "1.23cm", "papers")
lapicero2=Lapiceros("gris","1,21 cm", "maters")
lapicero3=Lapiceros("rojo","1,10 cm", "metv")