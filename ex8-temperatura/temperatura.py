class Conversor:
    def __init__(self, temperatura: float):
        self.temperatura = temperatura

    def celsiusFahrenheit(self) -> float:
        return (self.temperatura * 9/5) + 32

    def fahrenheitCelsius(self) -> float:
        return (self.temperatura - 32) * 5/9
