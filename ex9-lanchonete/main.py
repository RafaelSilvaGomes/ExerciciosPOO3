from lanchonete import Venda

def main():
    codigo = int(input("Código do produto comprado: "))
    quantidade = int(input("Quantidade comprada: "))
    
    venda1 = Venda(codigo)
    total = venda1.valorVenda(quantidade)
    
    if total is not None:
        print(f"Valor a pagar: R$ {total:.2f}")

if __name__ == "__main__":
    main()