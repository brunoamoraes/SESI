def main():
    print("Bem-vindo à Brigada de Incêndio!")
    print("Vamos verificar se você está apto para participar da brigada.")
    
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Desculpe, você precisa ter pelo menos 18 anos para participar da brigada.")
        return
    
    apto_fisicamente = input("Você está apto fisicamente para realizar atividades de combate a incêndios? (sim/não): ").lower()
    if apto_fisicamente != "sim":
        print("Desculpe, é necessário estar apto fisicamente para participar da brigada.")
        return
    
    treinamento_concluido = input("Você já concluiu o treinamento de combate a incêndios? (sim/não): ").lower()
    if treinamento_concluido != "sim":
        print("Desculpe, é necessário ter concluído o treinamento para participar da brigada.")
        return
    
    print("Parabéns! Você está apto para participar da Brigada de Incêndio!")
    


if __name__ == "__main__":    main()

