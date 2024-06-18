
class Formula:
  def _init_(self):
    return

  def primos(self, numero):
    arreglo_primos = []
    for numero_iteracion in range(1, numero+1):                        
      if self.es_divisible_por_dos(numero_iteracion) == False and self.es_divisible_por_tres(numero_iteracion) == False and self.es_divisible_por_cinco(numero_iteracion) == False:
        arreglo_primos.append(numero_iteracion)
    return arreglo_primos

  def es_divisible_por_dos(self, numero):
    return numero % 2 == 0

  def es_divisible_por_tres(self, numero):
    return numero % 3 == 0

  def es_divisible_por_cinco(self, number):
    return number % 5 == 0

formula_uno = Formula()
print(formula_uno.primos(30))

