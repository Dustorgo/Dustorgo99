
class Marcador:

    def __init__(self,color_atributo,grosor_atributo,marca_atributo,tamano_atributo,cantidad_de_tinta_atributo):
        self.color=color_atributo
        self.grosor=grosor_atributo
        self.marca=marca_atributo
        self.tamano=tamano_atributo
        self.cantidad_de_tinta=cantidad_de_tinta_atributo
        self.texto=""

        print(f"soy un marcador nuevo con color: {self.color} con gruesor: {self.grosor} con marca: {self.marca} con tamano {self.tamano} y con cantidad de tinta {self.cantidad_de_tinta}")

    def escribir(self, texto):
        self.texto+=texto
        print("Escribiendo: ",texto)

    def borrar(self):
        print("borrando:",self.texto)
        self.texto=""
    
    def cargar_tinta(self,cantidad):
        print(f"estoy cargando: {cantidad} ")

    def ver_estado (self,estado):
        print(f"el estado de el marcador es: {estado}")

    def cambiar_color (self,nuevo_color):
        self.color=nuevo_color
        print(f"el nuevo color es: {nuevo_color}")
        
    

#instanciar-cree un objeto que nacio de una clase 

marcador1=Marcador("azul", "1,232m", "norma","1 cm","1,2 ml")
marcador2=Marcador("verde","1,334 cm", "matter","1,2 cm","1.4 ml")
marcador3=Marcador("rojo","1,23 cm", "papers","1,2 cm","1.1ml")
marcador4=Marcador("fucsia","1,16 cm", "nilon","2,4 cm","1.3ml")
marcador5=Marcador("rojo","1,13 cm", "mixon","7,0 cm","1.0ml")

marcador1.escribir("Hola vida mia de mi corazon")
marcador1.borrar()
marcador4.cargar_tinta(3)
marcador3.ver_estado("Excelente")
marcador5.cambiar_color("azul-marino")





