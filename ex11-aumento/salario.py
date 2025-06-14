class Salario:
    def __init__(self, salario: float):
        self.salario = salario
        self.porcentagem = 0

    def aumento(self) -> float:
        if self.salario <= 1000.00:
            self.porcentagem = 20
        elif self.salario <= 3000.00:
            self.porcentagem = 15
        elif self.salario <= 8000.00:
            self.porcentagem = 10
        else:
            self.porcentagem = 5

        return self.salario + (self.salario * self.porcentagem / 100)