# Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80] 

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
        break  # O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligado. Aguardando manutenção.")


materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue  # Pula o restante do código abaixo e vai para a próxima peça
    
    # Este código só roda se a peça for de metal
    print(f"Processando peça de {peca}. Furando e polindo...")

print("Fim do lote de produção.")

# Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).
from time import sleep
for i in range(1,11):
    if i == 5:
        print(f"Falha ao ler o nº {i}")
        sleep(1.8)
        continue
    print(i)
    sleep(0.7)
print("Acabou")

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

# Exercício 4 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.
# Exemplo 1
# for i in range(5):
#     consumo = float(input("Digite o consumo"))
#     total = consumo + i
#     print(f"O valor de consumo é {total}")

# # Exempo 2
# total = 0
# for i in range(1,6):
#     consumo = float(input(f"Digite o consumo da {i} máquina"))
#     total += consumo
#     print(f"Consumo total da fabrica {total}")

# Exercício 5 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

# Exercício 6 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema:
# O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.

# Exercício 8: Sistema Inteligente de Manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo esta hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica."
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."