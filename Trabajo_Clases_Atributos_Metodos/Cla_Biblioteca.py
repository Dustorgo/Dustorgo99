class Biblioteca:
    def __init__(self,libros_atributo,periodicos_atributo,recursos_digitales_atributo,personal_atributo,revistas_atributo):
        self.libros=libros_atributo
        self.periodicos=periodicos_atributo
        self.recursos_digitales=recursos_digitales_atributo
        self.personal=personal_atributo
        self.revistas=revistas_atributo
    
        print(f"soy una Biblioteca con libros: {self.libros}  con periodicos: {self.periodicos} con recursos_digitales: {self.recursos_digitales}   personal{self.personal} y con revistas{self.revistas}")


    def prestar_recursos(self,estado):
        print(f"El libro Quijote de la mancha su estado actual es: {estado}")

    def devolver_recursos(self):
        self.prestar_recursos("Devuelto")       #metodo dentro de otro metodo

    def reservar_recursos (self):
        self.prestar_recursos("reservado para el dia 15-julio-2024 a nombre de Juan Castrillon") #metodo dentro de otro metodo

    def recomendar(self,recomendo):
        print(f"El libro recomendado de esta semana es: {recomendo}")

    def generar_reporte(self,prestamos):
        print(f"El total de libros prestados es de: {prestamos}")
#instanciar-cree un objeto que nacio de una clase 

biblioteca1=Biblioteca("321","3", "345","2","5")
biblioteca2=Biblioteca("345","2","234"," 3","3")
biblioteca3=Biblioteca("1678 ","3", "2353","4","7")
biblioteca4=Biblioteca("1324 ","5", "1674"," 5","9")
biblioteca5=Biblioteca("1682 ","2", "1100","6","3")


biblioteca3.prestar_recursos("prestado")
biblioteca4.devolver_recursos()
biblioteca1.reservar_recursos()
biblioteca2.recomendar("El principito y los angeles azules")
biblioteca5.generar_reporte(1245)