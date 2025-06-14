from salario import Salario

def main():
    salario = float(input("Digite o salário da pessoa: "))
    
    func1 = Salario(salario)
    novoSalario = func1.aumento()
    
    print(f"Novo salario R$ {novoSalario:.2f}")
    print(f"Aumento R$ {novoSalario - func1.salario:.2f}")
    print(f"Porcentagem = {func1.porcentagem}%")

if __name__ == "__main__":
    main()