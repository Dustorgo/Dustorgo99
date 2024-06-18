class Lapicero:
    def __init__(self,color_atributo,tamano_atributo,fabricante_atributo,numero_de_serie_atributo,cantidad_de_tinta_atributo):
        self.color=color_atributo
        self.tamano=tamano_atributo
        self.fabricante=fabricante_atributo
        self.numero_de_serie=numero_de_serie_atributo
        self.cantidad_de_tinta=cantidad_de_tinta_atributo
    
        print(f"soy un lapicero nuevo con color: {self.color} con tamano: {self.tamano} con fabricante: {self.fabricante} con numero de serie {self.numero_de_serie} y con cantidad de {self.cantidad_de_tinta}")

    def escribir(self,texto):
        print(f"Estoy escribiendo: {texto}")

    def cargar(self,cantidad):
        print(f"cargando {cantidad} de tinta")
        self.cantidad_de_tinta += cantidad

    def llenar(self):    #metodo dentro de otro metodo
        self.cargar(2)

    def bloquear_clic(self):
        print(f"El clic esta bloqueado")

    def tachar(self,texto):
        print(f"tachando {texto}")

    def personalizar_apariencia(self,nuevo_color,nuevo_tamano):
        self.color=nuevo_color
        self.tamano=nuevo_tamano
        print(f"El nuevo color es {nuevo_color} y tamano es {nuevo_tamano}")

        


#instanciar-cree un objeto que nacio de una clase 

lapicero1=Lapicero("azul", "1,23cm", "papers","32432",1.2)
lapicero2=Lapicero("gris","1,21 cm", "maters","45442",1.4)
lapicero3=Lapicero("verde","1,13 cm", "metv","64343",1.1)
lapicero4=Lapicero("negro","1,12 cm", "maters","54563",1.3)
lapicero5=Lapicero("rojo","1,10 cm", "papers","72344",1.0)

lapicero1.escribir("Hola, vida util ")
lapicero3.cargar(1.5)
lapicero2.bloquear_clic()
lapicero1.tachar("Este mensaje es erroneo")
lapicero4.personalizar_apariencia("gris","1.97cm")
lapicero1.llenar()


