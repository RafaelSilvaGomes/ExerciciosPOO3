class Menor:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcularMenor(self):
        menor = self.a
        if self.b < menor:
            menor = self.b
        if self.c < menor:
            menor = self.c
        return menor