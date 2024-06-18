class Computador:
    def __init__(self,marca_atributo,modelo_atributo,estado_atributo,color_atributo,almacenamiento_atributo):
        self.marca=marca_atributo
        self.modelo=modelo_atributo
        self.estado=estado_atributo
        self.color=color_atributo
        self.almacenamiento =almacenamiento_atributo
    
        print(f"soy un nuevo computador con marca: {self.marca} modelo: {self.modelo} con estado: {self.estado} con color{self.color} y con almacenamiento {self.almacenamiento }")


    def encender(self,texto):
        print(f"Quieres activar la funcion, on or off: {texto}")

    def apagar (self,texto):
        self.encender(f"{texto}")       #metodo dentro de otro metodo 
  
    def reiniciar (self):
        print(f"El computador esta reiniciando")

    def imprimir_archivo(self,texto):
        print(f"El archivo se esta {texto}")

    def guardar_archivo(self):
        self.imprimir_archivo("guardando")      #metodo dentro de otro metodo
    
#instanciar-cree un objeto que nacio de una clase 

computador1=Computador("intel", " 2023", " regular"," azul "," 128 GB")
computador2=Computador("mac"," 2015", " bueno","negro","64 GB")
computador3=Computador("hp"," 2014", " medio"," verde"," 256 GB")
computador4=Computador("acer"," 2012", " excelente"," blanco"," 512 GB")
computador5=Computador("acer"," 2023", " medio"," gris"," 128 GB")

computador2.encender("on")
computador5.apagar("la funcion apagar esta activada")
computador4.reiniciar()
computador3.imprimir_archivo("imprimiendo")
computador1.guardar_archivo()
