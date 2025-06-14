from notas import Nota

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    aluno1 = Nota(nota1, nota2)
    
    print(f"NOTA FINAL: {aluno1.notaFinal():.1f}")
    print(f"{aluno1.situacao()}")

if __name__ == "__main__":
    main()