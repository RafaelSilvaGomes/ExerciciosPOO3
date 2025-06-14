from coordenadas import Coordenada

def main():
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))

    coord1 = Coordenada(x, y)
    quadrante = coord1.quadrante()
    print(quadrante)

if __name__ == "__main__":
    main()