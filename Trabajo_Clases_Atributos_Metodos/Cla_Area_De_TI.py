class Area_de_TI:
    def __init__(self,equipo_atributo,software_atributo,redes_atributo,personal_atributo,ubicacion_oficina_atributo):
        self.equipo=equipo_atributo
        self.software=software_atributo
        self.redes=redes_atributo
        self.personal=personal_atributo
        self.ubicacion_oficina=ubicacion_oficina_atributo
    
        print(f"soy la Area_de_TI con equipo: {self.equipo}  con software: {self.software} con redes: {self.redes}   personal{self.personal} y con ubicacion_oficina{self.ubicacion_oficina}")

    def instalar_equipos(self,numero):
        print(f"hay {numero} ordenadores instalados en la torre emblematica")

    def instalar_software(self):
        print("todos los ordenadores tienen instalado el software universitario")

    def configurar_redes(self,redes):
        print(f"cuentan con {redes} privadas")

    def infraestructura(self,estado):
        print(f"el estado {estado} de la infraestrucutra se esta trabajando para mejorarlo dia a dia  ")

    def ofrecer_servicios(self):
        print("Nuestros servicios de fibra optica esta siendo ofrecido a la comunidad universitaria, interesados dirigirse a el piso 14, Area de TI ")


#instanciar-cree un objeto que nacio de una clase 

area_de_TI1=Area_de_TI("3","Porxtr", "3","2","Oficina 54")
area_de_TI2=Area_de_TI("2","Ergutg","4","7","Oficina 2")
area_de_TI3=Area_de_TI("4","Laciut", "1","9","Oficina 4")
area_de_TI4=Area_de_TI("6","Micrufhg", "2","8","Oficina 34")
area_de_TI5=Area_de_TI("9","Sioutr", "3","10","Oficina 23")

area_de_TI1.instalar_equipos(1987)
area_de_TI4.instalar_software()
area_de_TI3.configurar_redes("234")
area_de_TI2.infraestructura("regular")
area_de_TI5.ofrecer_servicios()
