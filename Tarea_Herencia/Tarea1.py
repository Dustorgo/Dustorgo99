class Vehicule:

  def __init__(self, speed,passengers,fuelType):
    self.speed= speed
    self.passengers = passengers
    self.fuelType = fuelType


  def go(self):
    return("El vehiculo se inicio")

  def stop(self):
    return("El vehiculo esta en reposo")
  
  def changeDirection (self):
    return("La direccion cambio hacia tu izquierda")
  

class Car(Vehicule):
  def __init__(self,speed,passengers,fuelType,modelType,Doors,Automaker):

    super().__init__(speed,passengers,fuelType)
    self.modelType=modelType
    self.Doors=Doors
    self.Automaker=Automaker

  def Radio(self):
    return("La radio esta encendida")

  def windshieldWiper(self):
    return("El parabrisa esta en modo activado")

  def changedirection(self):
    return("El vehiculo ha cambiado de direccion hacia la derecha")


Car1=Car(140,4 ,"Diesel","2004",4,"Mazda")


print(Car1.go())
print(Car1.stop())
print(Car1.changeDirection())
print(Car1.Radio())
print(Car1.windshieldWiper())


  
