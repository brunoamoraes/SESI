# # Lista de temperaturas lidas pelo sensor por minuto
# leituras = [30, 20, 70, 75, 82, 98, 110,40,10, 85, 80] 
# baixos = [10, 20 , 30 , 40, 50, 40, 10]


# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
# for temp1 in baixos:
#     if temp < 50:
#         print(f"CRÍTICO: {temp1}°C detectado! Acionando parada de emergência.")
#         break
#     else:
#         print(f"Temperatura está em {temp1}°C. Operação com valores baixo.")
# print("Checar Sistema. Aguardando manutenção.")

# # Exemplo 2
# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
# for temp in leituras:
#     if temp < 50:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break
#     else:
#         print(f"Temperatura está em {temp}°C. Operação com valores baixo.")
# print("Checar Sistema. Aguardando manutenção.")

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue  # Pula o restante do código abaixo e vai para a próxima peça
    
#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produção.")

# Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).
# from time import sleep
# for num in range(1,11):
#     if num == 5:
#         print(f"Falha ao imprimir o nº {num}")
#         sleep(1.8)
#         continue
#     print(f"Listando números {num}")
#     sleep(2)
# print("Fim!")

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa
# from time import sleep
# for i in range(1,11):
#     sleep(0.5)
#     print("Verde")
# print("Siga em frente")

# for i in range(1,11):
#     sleep(1)
#     print("Amarelo")
# print("Cuidado")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for pecas in medidas:
#     if pecas > 50:
#         print(f"Peça {pecas} Aprovada.. :)")
#     else:
#         print(f"Peça {pecas} Rejeitada")

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8, 52.3, 49.0, 51.0]
# for peso in sacos:
#     if 49.0 <= peso <= 51.0:
#         print(f"Saco com peso {peso}kg: Aceitável")
#     else:
#         print(f"Saco com peso {peso}kg: Rejeitado - Fora do limite aceitável")

# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema:
# O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.

# Exercício 7: Sistema Inteligente de Manutenção
estufa = 0
while estufa < 5:
    temp = float(input("Digite a temperatura da estufa: "))
    if temp < 0:
        print("Erro de leitura no sensor. Por favor, insira uma temperatura válida.")
        continue
    elif temp > 150:
        print("ALERTA CRÍTICO: Risco de Explosão!")
        break
    else:
        print(f"Peça {estufa + 1} processada com sucesso a {temp}°C.")
        estufa += 1

# Exercicio 8 - Monitoramento de Vibração
# Uma máquina industrial tem um sensor de vibração que registra os seguintes valores em mm/s: [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]. O limite de vibração aceitável é de até 1.5 mm/s.
# Crie um programa que percorra a lista de vibração e:
# - Se a vibração for maior que 1.5 mm/s, exiba "ALERTA: Vibração excessiva detectada!" e continue para a próxima leitura.
# - Se a vibração for menor ou igual a 1.5 mm/s, exiba "Vibração dentro do limite aceitável." para cada leitura.

