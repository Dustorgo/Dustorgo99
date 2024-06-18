class Alumno:             #creacion de la clase                                                        
    
      #atributos
    def __init__(self,nombre_atributo,apellido_atributo,edad_atributo,identificacion_atributo,curso_pertenece_atributo):
        self.nombre=nombre_atributo
        self.apellido=apellido_atributo
        self.edad=edad_atributo
        self.identificacion=identificacion_atributo
        self.curso_al_que_pertenece=curso_pertenece_atributo
    
        print(f"soy un alumno nuevo con nombre: {self.nombre} con apellido: {self.apellido} con edad: {self.edad} con numero de identificacion {self.identificacion} y pertenezco a el curso {self.curso_pertenece}")

         #metodos 
    def estudiar(self,texto):
        print(f"Que estas haciendo hoy: {texto}")
    
    def opinar_en_debates(self,opinion):
        print(f"Dame tu opinion frente a el debate: {opinion}")

    def examenes(self,calificar):
        print(f"Tu nota es: {calificar}")
    
    def tomar_nota(self):                  #metodo dentro de otro metodo
        self.examenes(5)
    
    def asistir_clase(self):               #metodo dentro de otro metodo
        self.estudiar("asistiendo a clase")



#instanciar-cree un objeto que nacio de una clase 

Alumno1=Alumno("Angel", "Martinez", "12","111232224","4B")
Alumno2=Alumno("Camilo","Garcia", "67","11125343","8")
Alumno3=Alumno("Sebastian","Ortiz", "24","1978677","12")
Alumno4=Alumno("Maria","Lopez", "16","3243545","12")
Alumno5=Alumno("Camila","Rojas", "24","4326754","4A")
#pongo a prueba los metodos,para mirar si son funcionales o no 
Alumno1.estudiar("Estoy estudiando")
Alumno2.opinar_en_debates("Lo mejor de la epoca es renacer y no tener que vivir nuevamente")
Alumno4.examenes(3)
Alumno3.asistir_clase()
Alumno5.tomar_nota()



