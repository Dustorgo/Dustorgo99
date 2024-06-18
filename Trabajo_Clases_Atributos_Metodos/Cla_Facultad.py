class Facultad:
    def __init__(self,nombre_atributo,decano_atributo,personal_atributo,codigo_atributo,area_de_facultad_atributo):
        self.nombre=nombre_atributo
        self.decano=decano_atributo
        self.personal=personal_atributo
        self.codigo=codigo_atributo
        self.area_de_facultad=area_de_facultad_atributo
    
        print(f"soy una Facultad con nombre: {self.nombre}  con decano: {self.decano} con personal: {self.personal}  con codigo{self.codigo} y con area_de_facultad{self.area_de_facultad}")

    def matriculados(self, numero_matriculados):
        print(f"Hay {numero_matriculados} matriculados en este semestre")
    
    def ofrecer_cursos(self, cursos):
        print(f"En este momento hay 3 cursos disponibles: {cursos}")

    def ofrecer_programas(self,programas):
        print(f"Hay 1 programa disponible: {programas}")
    
    def reporte_egresados(self,egresados):
        print(f"Los egresados son: {egresados} ")

    def reporte_matriculados(self, matriculados):
        print(f"Las personas matriculadas a nivel general asciende a: {matriculados}")


    


#instanciar-cree un objeto que nacio de una clase 

facultad1=Facultad("Ciencias de ingenieria ", "Mario A ","6"," 3435"," Tecnologica")
facultad2=Facultad("Ciencias de Salud","Carlos G", "4"," 546"," Cuerpos")
facultad3=Facultad("Juridicas","Sergio T", "3"," 567"," Demandas")
facultad4=Facultad("Contables","Martha G", "54"," 321"," Calculos de excel")
facultad5=Facultad("Administrativas"," Duvan T", "8"," 789","Empresa EPM")


facultad3.matriculados(27)
facultad4.ofrecer_cursos("Seguridad,programacion,datos")
facultad1.ofrecer_programas("Economia")
facultad5.reporte_egresados(56)
facultad2.reporte_matriculados("600 estudiantes")