from multiplos import Multiplos
        
def main():
    print("Digite dois numeros inteiros: ")
    n1 = int(input())
    n2 = int(input())

    multiplos = Multiplos(n1, n2)
    multiplos.verificar()
    
if __name__ == "__main__":
    main()