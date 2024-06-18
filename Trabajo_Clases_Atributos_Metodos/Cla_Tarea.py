class Tarea:
    def __init__(self,descripcion_atributo,fecha_entrega_atributo,porcentaje_atributo,estado_atributo,profesor_pertenece_atributo):
        self.descripcion=descripcion_atributo
        self.fecha_entrega=fecha_entrega_atributo
        self.porcentaje=porcentaje_atributo
        self.estado=estado_atributo
        self.profesor_pertenece=profesor_pertenece_atributo
    
        print(f"soy una Tarea con descripcion: {self.descripcion}  con fecha_entrega: {self.fecha_entrega} con porcentaje: {self.porcentaje}   estado{self.estado} y con profesor_pertenece{self.profesor_pertenece}")

    def realizar(self):
        print("Realizando la tarea")

    def corregir(self,estado):
        print(f"Tarea en proceso y esta siendo {estado}")

    def completar_tarea(self,estado):
        print(f"tarea {estado}")

    def calificacion(self):
        self.completar_tarea("completada y la calificacion es de 4.5")          #metodo dentro de otro metodo

    def informe(self,informe):
        print(f"El informe es el siguiente: {informe}")

#instanciar-cree un objeto que nacio de una clase 

tarea1=Tarea("hacer triangulos ","12-julio", "10%","espera","Marcos Julio Guonzales")
tarea2=Tarea("hacer crucigrama ","13 junio","23%","espera","Duvan Emilio Gutierrez")
tarea3=Tarea("hacer ciudad con semaforos ","23 agosto", "12%","enviada a corregir","Mario Francisco Rojas")
tarea4=Tarea("dibujar casa ","27 septiembre", "23%","no entregada","Muric Samont Legleth")
tarea5=Tarea("pintar cuadro de davinci ","23 octubre ", "34%","entregada","Patric Court Meshi")


tarea4.realizar()
tarea2.corregir("corregida por directriz del docente")
tarea1.completar_tarea("completada")
tarea5.calificacion()
tarea3.informe("Todo lo relacionado con la actividad es con fines netamente educativos que aportan a la creatividad individual de cada uno de los alumnos")


