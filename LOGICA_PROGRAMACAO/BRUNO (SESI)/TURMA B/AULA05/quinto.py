# 1. O Laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# # Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# # Imagine que você queira armazenar 10 carros
# for carros in range(10):
#     print(f"Quantidade de carros {carros}")

# # Exemplo 2
# # Contar até 4
# for a in range(5):
#     print(a)

# # Exemplo 3
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# maquinas = ["Máquina 1", "Máquina 2"]

# for item in pecas:
#     print(f"Item em estoque: {item}")
#     for maq in maquinas:
#         print(f"Máquinas que temos {maq}")

# # Exercício 1
# # 1. Contador de Produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído".

# print("Contador de ciclos de produção")
# for ciclo in range(1, 10):
#     print(f"Processando ciclos de peças {ciclo}...")
#     print(f"Peça nº {ciclo}. processada com sucesso")
#     print("Ciclo de produção concluído")

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi.

# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

# numero = int(input("Digite o valor"))

# print(f"Tabuada do {numero}:")
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# 2. O Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

# Repete enquanto a temperatura estiver segura
# Início
# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3  # Simulando o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Interação
# opcao = ""

# while opcao != "sair" and "SAIR":
#     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper().lower()
#     if opcao != "sair" and "SAIR":
#         print(f"Dado '{opcao}' registrado no banco de dados.")
# print("Sistema encerrado.")


for i in range(1, 11):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# Exercicio 4
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três.
# qualquer opcao diferente sair do menu

# Exercicio 5
# Monitor de Pressão Crítica (while)
# Crie um simulador onde o usuário deve digitar a pressão atual de um compressor.
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura.
# Assim que o usuário digitar um valor maior ou igual a 100, o loop para e exibe a mensagem: "ALERTA: Pressão crítica atingida! Desligando sistema."

# Exercício 6 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# Exercício 7 - Validação de Senha de Operador (while)
# Simule o painel de uma máquina que só liga com a senha correta.
# A senha correta é "1234".
# Enquanto o usuário errar a senha, o programa deve dizer "Acesso Negado. Tente novamente:".
# Quando ele acertar, o loop encerra com a mensagem "Sistema Iniciado. Bem-vindo, Operador!".

# Exercício 8 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".