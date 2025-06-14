class Jogo:
    def __init__(self, hInicial, hFinal):
        self.hInicial = hInicial
        self.hFinal = hFinal    

    def duracao(self):
        if self.hFinal < self.hInicial:
            self.hFinal += 24

        tempo = self.hFinal -self.hInicial

        if tempo == 0:
            tempo = 24

        return tempo
