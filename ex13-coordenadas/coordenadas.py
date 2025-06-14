class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return "Q1"
        elif self.x < 0 and self.y > 0:
            return "Q2"
        elif self.x < 0 and self.y < 0:
            return "Q3"
        elif self.x > 0 and self.y < 0:
            return "Q4"
        else:
            return "Origem" if self.x == 0 and self.y == 0 else "Eixo X" if self.y == 0 else "Eixo Y"
