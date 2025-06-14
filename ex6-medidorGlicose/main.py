from medidor import Glicose

def main():
    medida = float(input("Digite a medida da glicose: "))
    
    glicose1 = Glicose(medida)
    classificacao = glicose1.classificar()
    
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()