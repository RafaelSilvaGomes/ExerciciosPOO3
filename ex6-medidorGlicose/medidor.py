class Glicose:
    def __init__(self, medida):
        self.medida = medida

    def classificar(self):
        if self.medida <= 100:
            return "normal"
        elif 100 < self.medida <= 140:
            return "elevado"
        else:
            return "diabetes"