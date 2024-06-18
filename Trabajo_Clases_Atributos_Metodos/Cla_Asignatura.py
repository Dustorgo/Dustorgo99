import random
class Asignatura:
    def __init__(self,codigo_atributo,credito_atributo,aula_atributo,profesor_atributo,contenido_atributo):
        self.codigo=codigo_atributo
        self.credito=credito_atributo
        self.aula=aula_atributo
        self.profesor=profesor_atributo
        self.contenido=contenido_atributo
    
        print(f"soy una nueva asignatura con codigo: {self.codigo} equivale a credito: {self.credito} con aula: {self.aula} con profesor{self.profesor} y con contenido{self.contenido}")

    def registrar(self,texto):
        print(f"¿deseas matricular? {texto}")
    
    def impartir(self,texto):
        self.registrar(f"la anterior area con el docente ¿{texto}?")

    def desregistrar(self,texto):
        print(f"Que curso deseas retirar de tu matricula: {texto}")

    def calificar_estudiante(self):
        print(f"Tu calificacion general del semestre sera evaluado sobre 10 y el tuyo es {random.randint(0,10)}")
    
    def evaluar (self):
        print(f"si tu nota es superior a 2.5 ganaste el parcial evaluativo, tu nota es: {random.uniform(0,5)}")

    #def calificar (self)


#instanciar-cree un objeto que nacio de una clase 

Asignatura1=Asignatura("323234", "4", "67"," Alejandro Mariano"," Tablas SPE")
Asignatura2=Asignatura("4324234","3", "4","Jose Martinez"," Virus S")
Asignatura3=Asignatura("34553","2", "23"," Lionel Morales"," Microbios")
Asignatura4=Asignatura("23253","6", "534"," Francisco Rojas"," Eucalipto y afines")
Asignatura5=Asignatura("252543","2", "345"," Mario Ortiz"," Importanciad del agua")


Asignatura5.registrar("Si, Matematicas")
Asignatura2.impartir("Francisco Rojas")
Asignatura2.evaluar()
Asignatura1.desregistrar("Contexto Universitario")
Asignatura3.calificar_estudiante()


