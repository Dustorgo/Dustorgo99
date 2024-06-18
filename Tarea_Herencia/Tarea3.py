class Cuenta: 
    def __init__(self, numero_cuenta, saldo, nombre, cc,interes,ingreso,retiro):
      self.numero_cuenta=numero_cuenta
      self.saldo=saldo
      self.nombre=nombre
      self.cc=cc
      self.interes=interes
      self.ingreso=ingreso
      self.retiro=retiro

    def informacion (self):
      return (f"Numero de cuenta: {self.numero_cuenta} \n Saldo actual: {self.saldo} \n Nombre: {self.nombre} \n Cédula: {self.cc} \n Porcentaje interés: {self.interes}")

    def ingresar (self):
      ingreso = float(input("Cuál es el valor que desea ingresar? \n (Recuerde debe ser mayor al retiro)"))
      return (f"El valor de {ingreso} fue ingresado")

    def retirar (self):
      egreso = float(input("Cuál es valor que desea retirar?"))
      return (f"Se van a retirar ${egreso} de su cuenta")

    def actualizar_saldo (self):
      continuar = input(f"Su saldo actualizado tiene intereses del {self.interes}, desea continuar? ")
      if continuar == "Si":
          operacion = (self.ingreso - self.retiro)
          operacion2 = operacion * self.interes
          actualizacion = operacion - operacion2
          self.saldo = self.saldo + actualizacion
          return  (f"Su saldo actualizado es: {self.saldo} pesos")
      else:
        return (f"Su cuenta sin actualizar es de: {self.saldo} pesos")

class cuenta_corriente(Cuenta): #cuenta_corriente
    def __init__(self, numero_cuenta, saldo, cliente, cc,interes,ingreso,retiro): #Poner los atributos del padre
      super().__init__(numero_cuenta, saldo, cliente,cc,interes,ingreso,retiro)

    def info_cuenta_corriente(self):
      return f"{super().informacion()}"

    def ingresar_cuenta_corriente(self):
      return f"{super().ingresar()}"

    def retirar_cuenta_corriente(self):
      return f"{super().retirar()}"

    def actualizacion_cuenta_corriente(self):
      return f"{super().actualizar_saldo()}"

class cuenta_Ahorro(Cuenta): #cuenta_corriente
    def __init__(self, numero_cuenta, saldo, cliente, cc,interes,ingreso,retiro): #Poner los atributos del padre
      super().__init__(numero_cuenta, saldo, cliente,cc,interes,ingreso,retiro)

    def info_cuenta_ahorro(self):
      return f"{super().informacion()}"

    def ingresar_cuenta_ahorro(self):
      return f"{super().ingresar()}"

    def retirar_cuenta_ahorro(self):
      return f"{super().retirar()}"

    def actualizacion_cuenta_cahorro(self):
      return f"{super().actualizar_saldo()}"
    

cuenta1 = cuenta_corriente(123456, 12.300, "Duvan Ortiz", 3627191,0.015,3.000,1.000)
print (cuenta1.info_cuenta_corriente())
print (cuenta1.ingresar_cuenta_corriente())
print (cuenta1.retirar_cuenta_corriente())
print (cuenta1.actualizacion_cuenta_corriente())
