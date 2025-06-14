class Nota:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
    
    def notaFinal(self):
        return self.nota1 + self.nota2

    def situacao(self):
        nfinal = self.notaFinal()
        if nfinal >= 60:
            return "APROVADO"
        else:
            return "REPROVADO"
  
