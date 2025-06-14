from telefonia import Plano

def main():
    minutos = int(input("Digite a quantidade de minutos: "))
    
    plano1 = Plano(minutos)
    valor = plano1.calcularValor()
    
    print(f"Valor a pagar: R$ {valor:.2f}")

if __name__ == "__main__":
    main()