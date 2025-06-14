class Troco:
    def __init__(self, precoUn, qtde, valorPago):
        self.precoUn = precoUn
        self.qtde = qtde
        self.valorPago = valorPago

    def calcularTroco(self):
        total = self.precoUn * self.qtde
        if self.valorPago < total:
            return print(f"DINHEIRO INSUFICIENTE. FALTAM {total - self.valorPago:.2f} REAIS")
        return print(f"TROCO = {self.valorPago - total:.2f}")