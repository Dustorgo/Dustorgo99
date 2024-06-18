class Monitor:
    def __init__(self,nombre_atributo,apellido_atributo,codigo_monitor_atributo,fecha_inicio_atributo,estado_atributo):
        self.nombre=nombre_atributo
        self.apellido=apellido_atributo
        self.codigo_monitor=codigo_monitor_atributo
        self.fecha_inicio=fecha_inicio_atributo
        self.estado=estado_atributo
    
        print(f"soy un Monitor con nombre: {self.nombre}  con apellido: {self.apellido} con codigo_monitor: {self.codigo_monitor}  con fecha_inicio{self.fecha_inicio} y con estado{self.estado}")


    def ayudar_estudiante(self):
        print(f"Los monitores ayudan 4 veces a la semana a los estudiantes de las diferentes facultades")

    def reporte_actividades(self,actividades):
        print(f"Las actividades realizadas fueron: {actividades}")

    def evaluar_estudiante(self,dias):
        print(f"las evaluaciones se realizan todos los {dias} del mes")

    def actividades_realizar(self,hacer):
        print(f"las actividades a realizar son: {hacer}")

    def numeros_estudiantes(self):
        self.actividades_realizar("4 para los 35 estudiantes ayudados")    #metodos dentro de otros metodos 
#instanciar-cree un objeto que nacio de una clase 

monitor1=Monitor("Carlos M ", "Alfonso ","986"," 13 enero 2021"," activo")
monitor2=Monitor("Cristian G","Ortiz", "478"," 12 febrero 2022"," enfermo_inactivo")
monitor3=Monitor("JMauro G","Rojas", "453"," 16 julio 2012"," inactivo")
monitor4=Monitor("Correi H","Gutierrez", "534"," 23 agosto 2014"," vacaciones")
monitor5=Monitor("Fabian"," Torres", "458"," 24 mayo 2023","activo")

monitor3.ayudar_estudiante()
monitor5.reporte_actividades(87)
monitor2.evaluar_estudiante("viernes")
monitor1.actividades_realizar("Juegos,Evaluaciones,Salidas,Caminatas,Talleres")
monitor3.numeros_estudiantes()


