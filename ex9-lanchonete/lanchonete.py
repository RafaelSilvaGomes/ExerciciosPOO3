class Venda:
    def __init__(self, codigo: int):
        self.codigo = codigo
        self.produtos = {
            1: 5.00,
            2: 3.50,
            3: 4.80,
            4: 8.90,
            5: 7.32
        }
        
    def valorVenda(self, qtnd) -> float:
        return self.produtos.get(self.codigo, 0.0)*qtnd