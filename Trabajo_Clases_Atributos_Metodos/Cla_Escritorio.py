class Escritorio:
    def __init__(self,ubicacion_atributo,equipos_atributo,usuarios_atributo,capacidad_atributo,estado_atributo):
        self.ubicacion=ubicacion_atributo
        self.equipos=equipos_atributo
        self.usuarios=usuarios_atributo
        self.capacidad=capacidad_atributo
        self.estado=estado_atributo
    
        print(f"soy una Escritorio con ubicacion: {self.ubicacion}  con equipos: {self.equipos} con usuarios: {self.usuarios}   capacidad{self.capacidad} y con estado{self.estado}")


    def reservar_escritorio(self,fecha):
        print(f"La reserva es para la fecha: {fecha}")

    def liberar_escritorio(self):
        self.reservar_escritorio("21-12-2023 y se libera a las 19:00 horas")   #metodo dentro de otro metodo

    def agregar_equipo (self):
        self.reservar_escritorio("12-09-2023 y se debe agregar un equipo marca Acer")    #metodo dentro de otro metodo


    def verificar_disponibilidad(self,estado):
        print(f"La disponibilidad de los escritorios bajos, color azul es de: {estado}")

    def cancelar_reserva (self):
        self.reservar_escritorio("21-12-2023 esta cancelada")       #metodo dentro de otro metodo
#instanciar-cree un objeto que nacio de una clase 

escritorio1=Escritorio("Salon 3","3 PC gamer", "developmente123","2","malo")
escritorio2=Escritorio("Salon 34","5 Pc profesionales","tanaka341","1","regular")
escritorio3=Escritorio("Salon 56","6 PC basicos", "tufrutica456","4","regular")
escritorio4=Escritorio("Salon 1","2 PC profesionales", "tasika968","1","excelente")
escritorio5=Escritorio("Salon 56","1 PC gamer", "tumali839","2","bueno")


escritorio2.reservar_escritorio("31-12-2023")
escritorio4.liberar_escritorio()
escritorio1.agregar_equipo()
escritorio3.verificar_disponibilidad(2456)
escritorio5.cancelar_reserva()
