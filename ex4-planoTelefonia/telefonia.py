class Plano:
    def __init__(self, minutos):
        self.minutos = minutos
        
    def calcularValor(self):
        if self.minutos <= 100:
            return 50.0
        else:
            excedente = self.minutos - 100
            valorExcedente = excedente * 2.0
            return 50.0 + valorExcedente