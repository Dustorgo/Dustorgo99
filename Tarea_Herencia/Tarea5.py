class Alarma: #Clase Padre
    def __init__(self):
      self.sensor=int
      self.umbral=40 #Son 40 unidades de decibel

#Suponiendo que en esta situación, la alarma se tiene que activar cuando se escuche que cierran la puerta principal de la casa

    def comprobar(self):
      self.sensor = int(input("Valor en unidades de decibel percibidas por el sensor: "))
      if self.sensor < self.umbral:
        return ("Timbre en espera hasta que el umbral auditivo sea mayor")
      else:
        return ("Timbre activado: PI! PI! PI! PI!")

class alarma_luminosa(Alarma):
    def __init__(self):
      self.sensor=int
      self.umbral=40

    def comprobar_para_alarma_luminosa(self):
      con_luz = f"{super().comprobar()}"

      if con_luz == "Timbre activado: PI! PI! PI! PI!":
        print ("Se enciende las luces rojas y azules")

      return con_luz
    

alarma1=alarma_luminosa()
print (alarma1.comprobar_para_alarma_luminosa())