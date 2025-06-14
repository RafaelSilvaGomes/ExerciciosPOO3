class Multiplos:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def verificar(self):
        if self.n1%self.n2 == 0 or self.n2%self.n1 == 0:
            return print("São múltiplos")
        else:
            return print("Não são múltiplos")