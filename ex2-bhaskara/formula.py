class bhaskara:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c
    
    def raiz(self):
        d = self.delta()
        return (-self.b + d ** 0.5) / (2 * self.a)
    
    def raiz2(self):
        d = self.delta()
        return (-self.b - d ** 0.5) / (2 * self.a)
    
