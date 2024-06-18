import random
class Docente:
    def __init__(self,nombre_atributo,asignatura_atributo,identificacion_atributo,email_atributo,area_especializacion_atributo):
        self.nombre=nombre_atributo
        self.asignatura=asignatura_atributo
        self.identificacion=identificacion_atributo
        self.email=email_atributo
        self.area_especializacion =area_especializacion_atributo
    
        print(f"soy un nuevo Docente con nombre: {self.nombre} imparto la asignatura: {self.asignatura} mi identificacion como docente es: {self.identificacion} con email{self.email} y con area_especializacion {self.area_especializacion }")


    def dar_clase(self):
        print(f"doy clase los dias martes,jueves y viernes")

    def evaluar(self,argumento):
        print(f"Evaluo los dias {argumento} de las clases")

    def participar_reuniones(self):
        print(f"Participo {random.randint(6,15)} reuniones mensuales")

    def crear_examen(self,texto):
        print(f"los examenes se crean los ultimos {texto} dias de el mes")

    def generar_reportes_calificaciones(self):
        print(f"Gnero reportes el dia 30 de cada mes")
        


#instanciar-cree un objeto que nacio de una clase 

docente1=Docente("Mariano Flores", "Ing.sistemas", " A5768"," caasi@gmail.com "," Educacion")
docente2=Docente("Maria Florinde"," Medicina", " R5756"," maria@gmail.com ","Aprendizaje didactico")
docente3=Docente("Sara Ortega"," Ing.Redes", " A6865"," saraOrte@gmail.com ","Energias Renovables")
docente4=Docente("Minor Castro"," Contabilidad", " Q4576"," MinorCast@gmail.com "," Numeros binarios")
docente5=Docente("Omar Rios"," Adm.Empresas", " T5647"," Omar@gmail.com "," Contabilidad con finanzas en emprendimiento ")



docente1.evaluar("intermedios")
docente5.dar_clase()
docente4.crear_examen(23)
docente3.participar_reuniones()
docente2.generar_reportes_calificaciones()