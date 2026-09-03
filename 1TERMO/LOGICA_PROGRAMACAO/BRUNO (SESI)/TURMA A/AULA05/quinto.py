# 1. O Laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# Imagine que você queira atingir uma meta de produção de 5 carros e numera-los
# for carros in range (1,6):
#     print(f"Produção de carros diária {carros}...")

# # Exemplo 2
# Contar até 4
# for i in range(5):
#     print(i)

# # Exemplo 3
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipospecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

# for item in pecas:
#     print(f"Item em estoque: {item}")
#     for tipos in tipospecas:
#         print(f"Minha lista de tipos de peças {tipospecas}")

# Exemplo 4
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos

# print("Loja de Peças do Brunão")
# print("Bem-Vindo ao nosso Sistema")
# print("Escolha uma das opções")
# print("1 - Peças")
# print("2 - Tipos de Peças")

# opcao = int(input("Digite sua opção de pesquisa: "))
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipospecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]

# if opcao == 1:
#     for item in pecas:
#         print(f"Item em estoque: {item}")
#         print("Fim da Lista")
# elif opcao == 2:
#     for item2 in pecas:
#         print(f"Item em estoque: {item2}")
#         print("Fim da Lista")
# else:
#         print("Encerrando sistema")

# # Exercício 1
# # 1. Contador de Produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído".

# for ciclo in range(1,11):
#      print(f"Peça nº {ciclo} processado com sucesso...")
# print("Ciclo de produção concluído...")

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas , 5 mangas , 10 melancias e 13 abacaxi.

# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

# numero = int(input("Digite o valor"))
# print(f"Tabuada do {numero}:")
# for tabuada in range(1, 11):
#     resultado = numero * tabuada
#     print(f"{numero} x {tabuada} = {resultado}")

# 2. O Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

# Repete enquanto a temperatura estiver segura
# Início
# import time
# temperatura = 25
# while temperatura <= 40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(2)
#     temperatura += 3  # Simulando o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Interação
# != diferente
# lower minisculo
# upper maiusculo
opcao = ""
while opcao != "sair" and "SAIR":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper().lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados.")
print("Sistema encerrado.")

# and e or
# and comparações verdadeiras e iguais
# or comparações verdadeiras e não iguais

# Exercicio 4
# Monitor de Pressão Crítica (while)
# Crie um simulador onde o usuário deve digitar a pressão atual de um compressor.
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura.
# Assim que o usuário digitar um valor maior ou igual a 100, o loop para e exibe a mensagem: "ALERTA: Pressão crítica atingida! Desligando sistema."

import time
pressao = int(input("Digite o valor da pressão "))
while pressao <= 100:
    print(f"PSI atual: {pressao}°C. Gerando nova leitura...")
    time.sleep(2)   
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exercicio 
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três.
# qualquer opcao diferente sair do menu

# Exercício 4 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

