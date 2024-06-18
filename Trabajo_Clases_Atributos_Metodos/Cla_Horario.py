class Horario:
    def __init__(self,fecha_atributo,hora_atributo,salon_atributo,estado_atributo,profesor_atributo):
        self.fecha=fecha_atributo
        self.hora=hora_atributo
        self.salon=salon_atributo
        self.estado=estado_atributo
        self.profesor=profesor_atributo
    
        print(f"soy un horario con fecha: {self.fecha}  con hora: {self.hora} con salon: {self.salon}  con estado{self.estado} y con profesor{self.profesor}")

    def generar_reporte_de_asistencia(self,reporte):
        print(f"Los estudiantes que asistieron a este horario fueron:{reporte} ")

    def agregar_estudiante(self,nombre):
        print(f"el estudiante: {nombre} fue agregado con exito")

    def eliminar_estudiante(self):
        print(f"Eliminado satisfactoriamente")

    def reporte_califaciones(self,estado):
        print(f"El reporte fue {estado}")

    def hora_finalizacion(self,hora):
        print(f"la hora de finalizacon es a las: {hora}")
        



#instanciar-cree un objeto que nacio de una clase 

horario1=Horario(" 15 Enero ", "21:45 ","345"," Activo"," Francisco H")
horario2=Horario(" 14 Mayo","13:56", "48"," Pendiente"," Carlos N")
horario3=Horario(" 15 Julio","14:56", "3"," Activo"," Francisco G")
horario4=Horario(" 27 Junio ","16:59", "4"," Ocupado"," Duvan O")
horario5=Horario("30 Diciembre"," 10:34", "8"," Mantenimiento","Fabian T")

horario3.asistencia(456)
horario5.agregar_estudiante("Juan Rojas ")
horario4.eliminar_estudiante()
horario1.reporte_califaciones("Regular")
horario2.hora_finalizacion("18:30")

