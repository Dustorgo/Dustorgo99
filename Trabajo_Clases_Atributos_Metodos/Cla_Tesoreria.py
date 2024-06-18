class Tesoreria:
    def __init__(self,transacciones_atributo,prestamos_atributo,saldo_en_caja_atributo,cuenta_universidad_atributo,horario_atencion_atributo):
        self.transacciones=transacciones_atributo
        self.prestamos=prestamos_atributo
        self.saldo_en_caja=saldo_en_caja_atributo
        self.cuenta_universidad=cuenta_universidad_atributo
        self.horario_atencion=horario_atencion_atributo
    
        print(f"soy una Tesoreria con transacciones: {self.transacciones}  con prestamos: {self.prestamos} con saldo_en_caja: {self.saldo_en_caja}   cuenta_universidad{self.cuenta_universidad} y con horario_atencion{self.horario_atencion}")



    def reporte_financiero(self,fecha):
        print(f"El reporte financiero fue realizado el dia:{fecha} ")

    def ingresos(self,valor):
        print(f"EL valor de los egresos es de: {valor} euros")

    def egresos(self):
        print("Los egresos son de 100 euros semanales")

    def fondos(self,numeros):
        print(f"La tesoreria conjunto con la universidad manejan aproximadamente 5 fondos los cuales el valor de que los estudiantes financian es de : {numeros} euros")

    def perdidas(self):
        print("las perdidas son de 4000 euros, por motivo de mala informacion de terceros a cerca de el prestigio de la universidad")
#instanciar-cree un objeto que nacio de una clase 

tesoreria1=Tesoreria("332","45", "1000 dolares","654737586","10:00 a 20:00")
tesoreria2=Tesoreria("445","345","3000 dolares","354665","11:00 a 19:00")
tesoreria3=Tesoreria("7","2", "14000 dolares","546345","13:00 a 16:00")
tesoreria4=Tesoreria("78","56", "10000 dolares","979656","09:00 a 16:00")
tesoreria5=Tesoreria("93","68", "26000 dolares","2167346","08:00 a 19:00")


tesoreria4.reporte_financiero("21-12-2023")
tesoreria1.ingresos(3000)
tesoreria2.egresos()
tesoreria5.fondos(15000)
tesoreria3.perdidas()