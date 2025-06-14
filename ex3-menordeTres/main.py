from menor import Menor
def main():
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    c = int(input("Terceiro valor: "))

    menor1 = Menor(a, b, c)
    resultado = menor1.calcularMenor()
    
    print(f"MENOR = {resultado}")

if __name__ == "__main__":
    main()