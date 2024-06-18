class Parking:
    def __init__(self,capacidad_atributo,precio_atributo,estado_atributo,horario_atributo,ocupacion_actual_atributo):
        self.capacidad=capacidad_atributo
        self.precio=precio_atributo
        self.estado=estado_atributo
        self.horario=horario_atributo
        self.ocupacion_actual=ocupacion_actual_atributo
    
        print(f"soy una Parking con capacidad: {self.capacidad}  con precio: {self.precio} con estado: {self.estado}   horario{self.horario} y con ocupacion_actual{self.ocupacion_actual}")

    def reservar(self,fecha):
        print(f"La reserva quedo asignada para {fecha}")

    def obtener_precio (self):
        self.reservar("14-07-2023 con un valor de 3 euros")     #metodo dentro de otro metodo

    def verificar_disponibilidad(self,numero):
        print(f"La disponibilidad del parking es de {numero}")

    def liberar (self,estado):
        print(f"El puesto A342 esta {estado}")

    def obtener_informe (self):
        print("Hubo una capacidad maxima de 567 ocupadas y el valor recolectado es de 576 euros")

    
#instanciar-cree un objeto que nacio de una clase 

parking1=Parking("234","3 dolares", "activo","12:00 a 16:30","50")
parking2=Parking("123","5 dolares","activo","13:00 a 21:25","23")
parking3=Parking("954","10 dolares", "cerrado","10:00 a 23:00","560")
parking4=Parking("13","15 dolares", "cerrado","09:00 a 24:00","10")
parking5=Parking("46","23 dolares", "activo","08:00 a 22:30","24")


parking5.reservar("11-11-2023")
parking3.obtener_precio()
parking2.verificar_disponibilidad(745)
parking1.liberar("Liberado")
parking4.obtener_informe()
