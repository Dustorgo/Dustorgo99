import random
class Plataforma:
    def __init__(self,nombre_atributo,usuario_atributo,url_atributo,tipo_atributo,version_atributo):
        self.nombre=nombre_atributo
        self.usuario=usuario_atributo
        self.url=url_atributo
        self.tipo=tipo_atributo
        self.version=version_atributo
    
        print(f"soy una Plataforma con nombre: {self.nombre}  con usuario: {self.usuario} con url: {self.url}  soy tipo{self.tipo} y con version{self.version}")


    def iniciar_sesion(self,estado):
        print(f"tu sesion ha sido: {estado} ")

    def cerrar_sesion(self):
        self.iniciar_sesion("Cerrada")      #metodo dentro de otro metodo 

    def subir(self):
        print(f"El contenido se subio satisfactoriamente")

    def registrar(self,usuario):
        print(f"su usuario se ha regitrado, es el siguiente: {usuario}")
    
    def reporte_uso(self):
        print(f"El uso de la plataforma esta en:{random.randint(70,100)}% ")
    
#instanciar-cree un objeto que nacio de una clase 

plataforma1=Plataforma(" Umanizales  ","tumanizales", "www.umanizales.com"," educativa"," 4.7")
plataforma2=Plataforma(" Ejecafe","micafe "," wwww.ejecafe.com"," venta productos","3.5")
plataforma3=Plataforma(" Quindiocafe","quindiocoffee", "wwww.quindiocafe.com"," venta productos","2.3")
plataforma4=Plataforma(" Casaluker","houselukye", "www.casaluker.com"," venta cafe y afines"," 1.3")
plataforma5=Plataforma(" Ucatolica"," catolicatuk", "www.catolicaU.com"," educativa","3.1")


plataforma3.iniciar_sesion("Iniciada")
plataforma4.cerrar_sesion()
plataforma5.subir()
plataforma2.registrar("Candela1234")
plataforma1.reporte_uso()
