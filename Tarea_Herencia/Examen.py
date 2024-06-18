class Empresa:
    def __init__(self, nombre, nit, tipo_empresa, empleados, edades, genero, es_cabeza_de_hogar, nomina):
        self.nombre = nombre
        self.nit = nit
        self.tipo_empresa = tipo_empresa
        self.empleados = empleados
        self.edades = edades
        self.genero = genero
        self.es_cabeza_de_hogar = es_cabeza_de_hogar
        self.nomina = nomina

    def crear_datos_iniciales(self):
        while True:
            self.nombre = input("Ingrese el nombre de la empresa: ")
            self.nit = input("Ingrese el NIT de la empresa: ")

            if not self.nombre or not self.nit:
                print("El nombre y el NIT no pueden estar vacíos. Inténtelo de nuevo.")
                continue

            if len(self.nit) != 10:
                print("El NIT debe ser un número de 10 dígitos. Inténtelo de nuevo.")
                continue

            break

    def ingresar_empleado(self):
        nombre = input("Ingrese el nombre completo del empleado: ")
        genero = input("Ingrese el género del empleado (F/M/O): ")
        cabeza_de_hogar = input("¿Es el empleado cabeza de hogar? (Sí/No): ")

        self.empleados.append(nombre)
        self.edades.append(int(input("Ingrese la edad del empleado: ")))
        self.genero.append(genero)
        self.es_cabeza_de_hogar.append(True if cabeza_de_hogar.lower() == 'sí' else False)
        self.nomina.append(float(input("Ingrese el salario del empleado: ")))

    def hombres(self):
        hombres = []
        for i in range(len(self.empleados)):
            if self.genero[i] == 'M':
                hombres.append(self.empleados[i])
        return hombres

    def total_nomina(self):
        return sum(self.nomina)


    #INSTANCIAMOS
empresa1 = Empresa("Jack Company", "1234567890", "Tipo1", ["Lina Maria Sepulveda", "Luis Miguel"], [18, 34],
                  ["F", "M"], [True, False], [1000, 1200])

empresa2 = Empresa("Duvan Company", "9876543210", "Tipo2", ["John Doe", "Jane Doe"], [25, 30], ["M", "F"], [False, True],
                  [1500, 2000])

empresa3 = Empresa("Jeremy Company", "5678901234", "Tipo3", ["Alice", "Bob"], [22, 28], ["F", "M"], [False, False],
                  [800, 900])


empresa1.crear_datos_iniciales()
empresa1.ingresar_empleado()
print("Hombres en la empresa:", empresa1.hombres())
print("Total de la nómina:", empresa1.total_nomina())