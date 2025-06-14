from temperatura import Conversor

def main():
    escala = input("Você vai digitar a temperatura em qual escala (C/F)?" ).strip().upper()
    if escala == 'C':
        temp = float(input("Digite a temperatura em Celsius: "))
        temperatura1 = Conversor(temp)
        resultado = temperatura1.celsiusFahrenheit()
        print(f"Temperatura em Fahrenheit: {resultado:.2f}")
    
    else:
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        temperatura1 = Conversor(temp)
        resultado = temperatura1.fahrenheitCelsius()
        print(f"Temperatura em Celsius: {resultado:.2f}")

if __name__ == "__main__":
    main()