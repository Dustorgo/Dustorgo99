class Salon:
    def __init__(self,capacidad_atributo,ubicacion_atributo,numero_atributo,estado_atributo,equipamiento_atributo):
        self.capacidad=capacidad_atributo
        self.ubicacion=ubicacion_atributo
        self.numero=numero_atributo
        self.estado=estado_atributo
        self.equipamiento=equipamiento_atributo
    
        print(f"soy un nuevo Salon con capacidad: {self.capacidad} personas con ubicacion: {self.ubicacion} con numero: {self.numero} con estado{self.estado} y con equipamiento{self.equipamiento}")



    def reservar(self,hora):
        print(f"tu hora de reserva es a las {hora}")

    def abrir (self):
        self.reservar(f"18:30 y luego puedes abrir el salon")    #metodo dentro de otro metodo

    def cerrar(self):
        self.reservar(f"20:45 luego de la salida por favor cerrar el salon")

    def cancelar_reserva(self, argumento):
        print(f"tu reserva esta separada para el dia de hoy a las {argumento} ")

    def listar_actividades(self,actividades):
        print(f"las actividades a realizar el dia de hoy por los grupos de exposicion son las siguientes: {actividades}")

#instanciar-cree un objeto que nacio de una clase 

salon1=Salon("342 ", "Oficina 23", "6"," Excelente"," Full")
salon2=Salon("434","Oficina 5", "4","mal estado"," Tecnologico")
salon3=Salon("21","Oficina 45", "3"," regular"," Redes 5G")
salon4=Salon("23","Oficina 3", "54"," bueno"," Telescopio 4A ")
salon5=Salon("12","Oficina 34", "8"," bajo","Full-Laboratorio Medico")


salon3.reservar("16:35")
salon4.abrir()
salon1.cerrar()
salon2.cancelar_reserva ("23:45, por favor estar 10 minutos antes")
salon5.listar_actividades("juegos ludicos,presentaciones verbales y virtuales, maraton universitaria ")