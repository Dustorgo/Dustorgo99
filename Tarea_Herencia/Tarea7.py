class Direccion: #Clase Padre
    def __init__(self,pais,ciudad,calle,num_postal):
      self.pais=str
      self.ciudad=str
      self.calle=int
      self.num_postal=int

class Persona(Direccion):
    def __init__(self, pais, ciudad, num_postal, calle):
      super().__init__(pais, ciudad, num_postal, calle)
      self.nombre=str
      self.apellidos=str
      self.CC=int
      self.tipo_persona= int

    def identificate (self):
        identificacion = input("Digite su ID: ")
        primeros_4_numeros = identificacion[:4]
        if primeros_4_numeros == "2023":
            return (f"Estudiante: {self.nombre} {self.apellidos} {self.CC} (ID: {self.id_estudiante})")
        else:
            return (f"Profesor: {self.nombre} {self.apellidos} {self.CC} (Despacho: {self.id_profesor})")

class Estudiante(Persona):
    def __init__(self, nombre, apellidos, CC, direccion, id_estudiante): #Poner los atributos del padre
      super().__init__(nombre, apellidos, CC, direccion)
      id_estudiante=int

    def identificador_estudiante (self):
      return f"{super().identificate()}"

class Profesor(Persona):
    def __init__(self, nombre, apellidos, CC, direccion,id_profesor): #Poner los atributos del padre
      super().__init__(nombre, apellidos, CC, direccion)
      id_profesor=int

    def identificador_profesor (self):
      return f"{super().identificate()}"

personas = []
#Estudiantes
personas.append(Estudiante("Juan", "Pérez", "123456789", Direccion("Calle 123", "Manizales", "123456", "Colombia"), 123456))
personas.append(Estudiante("María", "González", "987654321", Direccion("Carrera 45", "Bogotá", "789012", "Colombia"), 987654))

#Profesores
personas.append(Profesor("Pedro", "Martínez", "321098765", Direccion("Avenida 68", "Medellín", "345678", "Colombia"), 102))
personas.append(Profesor("Sandra", "López", "654321098", Direccion("Calle 72", "Cali", "987654", "Colombia"), 203))

#Personas
for persona in personas:
    print(f"{persona.nombre} {persona.apellidos} | {persona.CC}")



estudiante1=Persona("Duvan","Ortiz",62829,45)
print (estudiante1.identificate())