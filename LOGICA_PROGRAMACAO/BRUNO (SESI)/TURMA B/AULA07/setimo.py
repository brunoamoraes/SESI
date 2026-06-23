# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# print("Registro de Operador")
# operador = input("Digite seu nome ... ")
# turno = input("Digite seu turno ... ")
# print(f"Operador {operador} registrado no Turno {turno}. Boa jornada!")

# # 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.
# print("Cálculo de Produção")
# producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora ... "))
# producao_turno = producao_hora * 8
# print(f"Quantidade de peças produzidas em um turno de 8 horas: {producao_turno}")

# # 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar # ≈ 14.5 PSI) e exiba com duas casas decimais.
# print("Conversor de Unidade")
# pressao_bar = float(input("Digite a pressão em Bar ... "))
# pressao_psi = pressao_bar * 14.5
# print(f"Pressão em PSI: {pressao_psi:.2f}")
# print(f"Pressão em PSI: {pressao_psi}",round(pressao_psi, 2))

# # 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# # aritmética simples delas.
# print("Inspeção de Peças")
# nota1 = float(input("Digite a nota da inspeção 1 (0 a 10) ... "))
# nota2 = float(input("Digite a nota da inspeção 2 (0 a 10) ... "))
# nota3 = float(input("Digite a nota da inspeção 3 (0 a 10) ... "))
# media = (nota1 + nota2 + nota3) / 3
# print(f"Média de qualidade da peça: {media:.2f}")
# print("Média de qualidade da peça: ", round(media,2))

# Foco: if, elif, else e operadores lógicos
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# print("Termostato Inteligente")
# temperatura = float(input("Digite a temperatura do motor em °C ... "))
# if temperatura < 40:
#     print("Baixa carga")
# elif 40 <= temperatura <= 70:
#     print("Normal")
# else:    
#     print("ALERTA: Resfriamento Ativado!")

# print("Termostato Inteligente - Versão 2")
# temperatura = float(input("Digite a temperatura do motor em °C ... "))
# if temperatura < 40:
#     print("Baixa carga")
# elif temperatura > 70:
#     print("ALERTA: Resfriamento Ativado!")
# else:    
#     print("Normal")

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
# print("Classificador de Lotes")
# codigo_produto = input("Digite o código do produto ... ")
# if codigo_produto == "A":
#     print("Alimentos")
# elif codigo_produto("E"):
#     print("Eletrônicos")
# else:
#     print("Desconhecido")

# print("Classificador de Lotes - Versão 2")
# codigo_produto = input("Digite o código do produto ... ")
# if codigo_produto.startswith == "A":
#     print("Alimentos")
# elif codigo_produto.startswith == "E":
#     print("Eletrônicos")
# else:
#     print("Desconhecido")


# # 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.
# print("Segurança de Operação")
# sensor_porta = input("Digite o status do sensor da porta (fechada/aberta) ... ")
# botao_emergencia = input("Digite o status do botão de emergência (ligado/desligado) ... ")
# if sensor_porta == "fechada" and botao_emergencia == "desligado":
#     print("A máquina pode iniciar.")
# else:
#     print("A máquina não pode iniciar.")

# # 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário, "Processo Otimizado".
# print("Cálculo de Descarte")
# total_pecas = int(input("Digite o total de peças produzidas ... "))
# total_defeituosas = int(input("Digite o total de peças defeituosas ... "))
# descarte_percentual = (total_defeituosas / total_pecas) * 100
# if descarte_percentual > 5:
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")
# print(f"Descarte percentual: {descarte_percentual:.2f}%")

# # 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.
# print("Validação de Medida")
# medida = float(input("Digite a medida da peça em mm ... "))
# if medida < 9.8:
#     print("A peça está abaixo da tolerância.")
# elif medida > 10.2:
#     print("A peça está acima da tolerância.")
# else:
#     print("A peça está dentro da tolerância.")

# # Foco: for e while
# # 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".
# print("Contagem Regressiva de Setup")
# for contagem in range(10, 0, -1):
#     print(contagem)
# print("Prensa Ativada!")

# # 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas. O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.
# print("Soma de Produção (Acumulador)")
# peso_total = 0
# while True:
#     peso_caixa = float(input("Digite o peso da caixa (0 para parar) ... "))
#     if peso_caixa == 0:
#         break
#     peso_total += peso_caixa
# print(f"Peso total acumulado: {peso_total:.2f} kg")

# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes. Ao final, mostre qual foi a maior temperatura lida.
# print("Múltiplas Leituras")
# temperaturas = [] 
# for i in range(1, 6):
#     temp = float(input(f"Digite a temperatura do sensor {i} em °C ... "))
#     temperaturas.append(temp)

# print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")
# print(f"Menor temperatura lida: {min(temperaturas):.2f} °C")
# print(f"Soma temperatura lida: {sum(temperaturas):.2f} °C")


# 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".
print("Painel de Login")
senha_correta = "admin123"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a senha do supervisor ... ")
    if senha == senha_correta:
        print("Acesso Permitido")
        break
    else:
        tentativas -= 1
        print(f"Acesso Negado. Tentativas restantes: {tentativas}")
if tentativas == 0:
    print("Painel Bloqueado")

print("Painel de Login - Versão 2")
senha_correta = "admin123"
tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha do supervisor ... ")
    if senha == senha_correta:
        print("Acesso Permitido")
        break
    else:
        tentativas += 1
        print(f"Acesso Negado. Tentativas restantes: {3 - tentativas}")
if tentativas == 3:
    print("Painel Bloqueado")

# 14.Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar abaixo de 10, avise: "Estoque Crítico!".
print("Simulador de Estoque")
estoque = 100
while True:
    print("\nMenu:")
    print("1. Adicionar itens")
    print("2. Remover itens")
    print("3. Sair")
    escolha = input("Escolha uma opção (1, 2 ou 3) ... ")
    
    if escolha == 1:
        quantidade = int(input("Digite a quantidade de itens a adicionar ... "))
        estoque += quantidade
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == "2":
        quantidade = int(input("Digite a quantidade de itens a remover ... "))
        estoque -= quantidade
        print(f"Estoque atualizado: {estoque} itens")
        if estoque < 10:
            print("Estoque Crítico!")
    elif escolha == "3":
        print("Saindo do simulador de estoque.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# 15.Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça, peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.
print("Relatório de Turno Completo")
total_pecas = 5
pecas_aprovadas = 0
for i in range(1, total_pecas + 1):
    diametro = float(input(f"Digite o diâmetro da peça {i} em mm ... "))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1
eficiencia = (pecas_aprovadas / total_pecas) * 100
print(f"Total de peças aprovadas: {pecas_aprovadas}")
print(f"Eficiência do lote: {eficiencia:.2f}%")
