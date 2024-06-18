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

    def digitar_info (self):
      self.nombre = input("Digite su nombre: ")
      self.apellidos = input("Digite sus apellidos: ")
      self.CC = int(input("Digite su Cédula: "))

      return (f"Sus datos personales son: \n NOMBRE: {self.nombre} \n APELIIDOS: {self.apellidos} \n CC: {self.CC} \n INFORMACIÓN GUARDADA" )

    def datos_direccion (self):
      self.pais = input("Digite su pais: ")
      self.ciudad = input("Digite su ciudad: ")
      self.num_postal = int(input("Digite su código postal: "))
      self.calle = int(input("Digite el número de su calle: "))

      return (f"Los datos de su dirección son: \n PAIS: {self.pais} \n CIUDAD: {self.ciudad} \n CÓDIGO POSTAL: {self.num_postal} \n CALLE: {self.calle} \n INFORMACIÓN GUARDADA")

class Estudiante(Persona):
    def __init__(self, nombre, apellidos, CC, direccion): #Poner los atributos del padre
      super().__init__(nombre, apellidos, CC, direccion)
      self.id_estudiante=0

    def digitar_id (self):
      self.id_estudiante = int(input("Digite su ID de estudiante: "))
      return ("Se registró su ID")

    def informacion (self):
      return (f"Su información es: \n -Nombre: {self.nombre} \n -Apellidos: {self.apellidos} \n -CC: {self.CC} \n -Dirección: {self.direccion} \n -ID Estudiante: {self.id_estudiante}")

class Profesor(Persona):
    def __init__(self, nombre, apellidos, CC, direccion): #Poner los atributos del padre
      super().__init__(nombre, apellidos, CC, direccion)
      self.oficina=0

    def digitar_oficina (self):
      self.oficina = int(input("Digite su número de oficina: "))
      return ("Se registró su número de oficina")

    def informacion (self):
      return (f"Su información es: \n -Nombre: {self.nombre} \n -Apellidos: {self.apellidos} \n -CC: {self.CC} \n -Dirección: {self.direccion} \n -Num Oficina: {self.id_estudiante}")


persona1 = Direccion(" ", " ",7,5)