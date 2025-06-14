class Distancia:
    def __init__(self, dist1, dist2, dist3):
        self.dist1 = dist1
        self.dist2 = dist2
        self.dist3 = dist3

    def maiorDistancia(self):
        maior = self.dist1
        if self.dist2 > maior:
            maior = self.dist2
        elif self.dist3 > maior:
            maior = self.dist3
        return maior