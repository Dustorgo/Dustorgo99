




class Empresa:
    def __init__(self, nombre, nit, tipo_empresa):
        self.nombre = nombre
        self.nit = nit
        self.tipo_empresa = tipo_empresa
        self.empleados = []
        self.edades = []
        self.genero = []
        self.es_cabeza_de_hogar = []
        self.nomina = []

    def crear_datos_iniciales(self):
        while True:
            nombre = input("Ingrese el nombre de la empresa: ")
            nit = input("Ingrese el NIT de la empresa (10 dígitos): ")

            if nombre.strip() and nit.isdigit() and len(nit) == 10:
                self.nombre = nombre
                self.nit = nit
                break
            else:
                print("Nombre y NIT son obligatorios. El NIT debe tener 10 dígitos.")

    def ingresar_empleado(self):
        nombre_completo = input("Ingrese el nombre completo del empleado: ")
        genero = input("Ingrese el género del empleado (F/M/O): ")
        es_cabeza_de_hogar = input("¿Es cabeza de hogar? (True/False): ")

        self.empleados.append(nombre_completo)
        self.genero.append(genero)
        self.es_cabeza_de_hogar.append(es_cabeza_de_hogar)

    def mostrar_informacion(self):
        print("Nombre de la empresa:", self.nombre)
        print("NIT de la empresa:", self.nit)
        print("Tipo de empresa:", self.tipo_empresa)
        print("Empleados:", self.empleados)
        print("Edades:", self.edades)
        print("Género:", self.genero)
        print("Es cabeza de hogar:", self.es_cabeza_de_hogar)
        print("Nómina:", self.nomina)


empresa1 = Empresa("Jack company", "1234567890", "TipoZ")
empresa2 = Empresa("Duvan Company", "9876543210", "TipoB")
empresa3 = Empresa("Jeremy Company", "5555666677", "TipoY")


empresa1.crear_datos_iniciales()
empresa2.crear_datos_iniciales()
empresa3.crear_datos_iniciales()


empresa1.ingresar_empleado()
empresa2.ingresar_empleado()
empresa3.ingresar_empleado()


print("\nInformación de Empresa 1:")
empresa1.mostrar_informacion()

print("\nInformación de Empresa 2:")
empresa2.mostrar_informacion()

print("\nInformación de Empresa 3:")
empresa3.mostrar_informacion()