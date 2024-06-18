import random
class Silla:
    def __init__(self,material_atributo,capacidad_atributo,estilo_atributo,color_atributo,ubicacion_atributo):
        self.material=material_atributo
        self.capacidad=capacidad_atributo
        self.estilo=estilo_atributo
        self.color=color_atributo
        self.ubicacion=ubicacion_atributo
    
        print(f"soy una silla nueva con material: {self.material} con capacidad: {self.capacidad} con estilo: {self.estilo} con color {self.estilo} y ubicacion {self.ubicacion}")

    def sentarse(self,texto):
        print(f"¿te vas a sentar? {texto}")

    def girar(self):
        print(f"Esta girada al maximo su silla")

    def ajustar_altura(self):
        print(f"la altura en estos momentos es de: {random.uniform(2,20)} cm sobre el suelo, si deseas la puedes ajustar")

    def levantar(self,texto):
        print(f"Si deseas levantar la silla tu edad debe ser mayor a 12 años, cual es tu edad: {texto}")

    def mover(self,texto):
        self.levantar(f"{texto} Estas moviendo la silla")   #metodo dentro de otro metodo 

#instanciar-cree un objeto que nacio de una clase 

silla1=Silla("Plastico", "2", "Antiguo","Negra","Salon 2")
silla2=Silla("Carbon","1", "Clasico","Roja","Salon 4")
silla3=Silla("Madera","3", "Futurista","Blanca","Salon 21")
silla4=Silla("Policarbonato","3","Maderoso", "Gris","Salon 14")
silla5=Silla("Metal","2","Clasico","Verde","Salon 34")

silla1.sentarse("Si caballero")
silla5.ajustar_altura()
silla3.girar()
silla2.levantar("11 años, lo siento no puedes")
silla4.mover("20 años")

