from formula import bhaskara
def main():
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))

    bhask1 = bhaskara(a, b, c)

    d = bhask1.delta()
    if d < 0:
        print("Esta equacao nao possui raizes reais")
    elif d == 0:
        raiz = bhask1.raiz()
        print(f"X = {raiz}")
    else:
        raiz1 = bhask1.raiz()
        raiz2 = bhask1.raiz2()
        print(f"X1 = {raiz1:.4f}")
        print(f"X2 = {raiz2:.4f}")

if __name__ == "__main__":
    main()