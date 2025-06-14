from lancamento import Distancia

def main():
    print("Digite as três distancias:")
    dist1 = float(input())
    dist2 = float(input())
    dist3 = float(input())

    lancamento1 = Distancia(dist1, dist2, dist3)
    maior = lancamento1.maiorDistancia()
    print(f"MAIOR DISTANCIA = {maior:.2f}")
    
if __name__ == "__main__":
    main()