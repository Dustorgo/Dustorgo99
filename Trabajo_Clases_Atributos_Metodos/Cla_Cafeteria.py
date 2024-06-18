import random
class Cafeteria:
    def __init__(self,productos_atributo,personal_atributo,inventario_atributo,direccion_atributo,nombre_atributo):
        self.productos=productos_atributo
        self.personal=personal_atributo
        self.inventario=inventario_atributo
        self.direccion=direccion_atributo
        self.nombre=nombre_atributo
    
        print(f"soy una Cafeteria con productos: {self.productos} y tengo a personal: {self.personal} con inventario de : {self.inventario} productos con direccion{self.direccion} y con nombre{self.nombre}")


    def vender(self,texto):
        print(f"Su compra tiene un valor de {texto}")

    def facturar(self,texto):
        self.vender(f"{texto}")    #metodo dentro de otro metodo

    def reponer_inventario(self,reposicion):
        print(f"En estos momentos {reposicion}")


    def reservar_mesa(self):
        print(f"Su reserva es para el dia {random.randint(1,30)}")

    def limpiar_cafeteria(self,hora):
        print(f"la cafeteria limpia su mesa {hora} minutos despues")
        

    
#instanciar-cree un objeto que nacio de una clase 

cafeteria1=Cafeteria("chucherias", " 3", " 323"," Calle 5 N 14 "," Tu paladar")
cafeteria2=Cafeteria("afines de pizza"," 1", " 123","Carrera 15 N 3-45","Tu fooding")
cafeteria3=Cafeteria("pegajosos"," 2", " 543"," Avenida Food 34- 53"," Pieta")
cafeteria4=Cafeteria("papatas bbq y afines"," 2", " 152"," Esquina 453-768"," Locas Patatas")
cafeteria5=Cafeteria("galletas oreo, bebidas energizantes"," 4", " 172"," Avenida 247 N 473-55"," Galletas bañadas")

cafeteria4.vender(32)
cafeteria5.facturar("32 estamos generando factura")
cafeteria2.reponer_inventario("estamos reponiendo las chocolatinas")
cafeteria1.limpiar_cafeteria(2)
cafeteria1.reservar_mesa()
