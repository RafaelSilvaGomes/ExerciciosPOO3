from jogo import Jogo
def main():
    hInicial = int(input("Hora inicial: "))
    hFinal = int(input("Hora final: "))

    jogo1 = Jogo(hInicial, hFinal)
    resultado = jogo1.duracao()
    print(f"O JOGO DUROU {resultado} HORA(S)")

if __name__ == "__main__":
    main()