from venda import Troco

def main():
    precoUn = float(input("Preço unitário do produto: "))
    qtde = int(input("Quantidade comprada: "))
    valorPago = float(input("Dinheiro recebido: "))

    venda1 = Troco(precoUn, qtde, valorPago)
    venda1.calcularTroco()

if __name__ == "__main__":
    main()