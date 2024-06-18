import random
class Pregrado:
    def __init__(self,nombre_atributo,duracion_atributo,plan_de_estudio_atributo,codigo_atributo,totalidad_creditos_atributo):
        self.nombre=nombre_atributo
        self.duracion=duracion_atributo
        self.plan_de_estudio=plan_de_estudio_atributo
        self.codigo=codigo_atributo
        self.totalidad_creditos =totalidad_creditos_atributo
    
        print(f"soy un nuevo Pregrado con nombre: {self.nombre} duracion: {self.duracion} con plan_de_estudio: {self.plan_de_estudio} con codigo{self.codigo} y con totalidad_creditos {self.totalidad_creditos }")

    def estudiar(self,texto):
        print(f"Cuando vas a la U, ¿vas a? {texto}")

    def opinar_debates(self,texto):
        self.estudiar(f"{texto}")     #metodos dentro de otros metodos
        
    def examenes(self):
        print(f"tu ponderado de examenes es igual a: {random.randint(1,5)}")
        
    def tomar_notas(self,texto):
        print(f"Los dias {texto} se toman nota doble ")

    def asistir_clase(self):
        print(f"Los dias martes es obligatorio asitir")
#instanciar-cree un objeto que nacio de una clase 

pregrado1=Pregrado("Ing.sistemas", "5 años", " SNIES 3243"," 34554 "," 254")
pregrado2=Pregrado("Medicina"," 7 años", " SNIES 4453"," 54643","456")
pregrado3=Pregrado("Ing.Redes"," 5 años", " SNIES 4345"," 76864","765")
pregrado4=Pregrado("Contabilidad"," 3 años", " SNIES 6879"," 23445"," 424")
pregrado5=Pregrado("Adm.Empresas"," 4 años", " SNIES 7645"," 96786"," 878")


pregrado1.estudiar("Estudiar")
pregrado4.opinar_debates("Debatir")
pregrado2.examenes()
pregrado5.tomar_notas("Festivos,lunes y miercoles")
pregrado3.asistir_clase()