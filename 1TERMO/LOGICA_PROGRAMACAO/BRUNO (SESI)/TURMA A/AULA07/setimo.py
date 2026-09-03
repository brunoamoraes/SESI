# Revisão Somativa - Aula 7
# print("Revisão Somativa - Aula 7")

# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!"
print("Registro de Veículo")
modelo_veiculo = input("Informe é o modelo do veículo?")
placa_veiculo = input("Informe é a placa do veículo?")
print(f"Veículo {modelo_veiculo} de placa {placa_veiculo} registrado no sistema. Boa viagem!")

# 2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.
print("Cálculo de Autonomia")
capacidade_tanque = float(input("Digite a capacidade do tanque litros"))
consumo_medio = float(input("Digite o consumo do caminhão em km/l"))
distancia_total = capacidade_tanque * consumo_medio
print(f"Capacidade {capacidade_tanque} do tanque e sua distancia {consumo_medio} em média KM/L e o total {distancia_total}")

# 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD  approx 5,00~BRL$ e exiba com duas casas decimais.
print("Conversor de Moeda (Frete Internacional)")
valor_frete = float(input("Valor de frete em Dolar"))
conversao_real = float(input("Valor da taxa em reais "))
total_conversao = valor_frete * conversao_real
print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversao_real} e o total do frete {total_conversao:.2f}") # :.2f para exibir com duas casas decimais
print("O valor do frete foi",valor_frete,"E a taxa aplicada foi de",conversao_real,"e o total do frete",round(total_conversao,2)) # round para exibir com duas casas decimais

# 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista.Exiba a média aritmética simples do tempo dessas entregas.
print("Média de Entregas")
rota1 = int(input("Digite a primeira rota em horas"))
rota2 = int(input("Digite a segunda rota em horas"))
rota3 = int(input("Digite a terceira rota em horas"))
media_rota = (rota1 + rota2 + rota3) /3
print(f"A média de entregas da rotas realizadas foi de... {media_rota:.2f}")

# Foco: if, elif, else e operadores lógicos
# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".
print("Monitor de Carga - Peso em Toneladas")
peso_caminhao = float(input("Informe o peso do caminhão em Toneladas"))
if peso_caminhao <= 10:
    print("Carga Leve -)")
elif peso_caminhao < 25:
    print("Carga Padrão --)")
elif peso_caminhao >= 25:
    print("ALERTA: Excesso de Peso! ---)")
else:
    print("Digite outro valor ----)")
# else:
#     print("ALERTA: Excesso de Peso! ---)")

# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região Internacional".
print("Classificador de Destino - Código de Cargas")
print("Código de Cargas = N - Norte S - Sul e Outros Internacional")
codigo_carga = input("Inserir o código da Carga em N ou S ou O").upper()
if codigo_carga == "N":
    print("Região Norte")
elif codigo_carga == "S":
    print("Região Sul")
elif codigo_carga == "O":
    print("Região Internacional")
else:
    print("Região Internacional")
    
# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o motorista_identificado == "sim". Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.
print("Liberação de Saída - Checklist e Motorista")
checklist = input("O Checklist foi realizado (Concluído ou Não Concluído)")
motorista = input("O motorista foi identificado (Sim ou Não)")
# and = verdadeiro verdadeiro
# or = verdadeiro e falso
if checklist == "Concluído" and motorista == "Sim":
    print("Iniciar Rota - Boa Viagem")
else:
    print("Voltar e realizar o Checklist! :(")

# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar Rotas", caso contrário, "Logística Eficiente".
print("Cálculo de Atrasos")
entregas_agendadas = int(input("Quantidade de entregas agendadas"))
entregas_atraso = int(input("Quantidade de entregas com atraso"))
total = entregas_atraso / entregas_agendadas
if total > 0.10:
    print("Necessário Otimizar Rotas")
else:
    print("Logística Eficiente")

# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI. Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.
print("Validação de Calibragem - Pressão dos Pneus")
carga_pressao = float(input("Digite e medida da pressão em PSI dos Pneus"))
if carga_pressao <= 100:
    print("Abaixo do recomendado")
elif carga_pressao >=110:
    print("Acima do recomendado") 
else:
    print("Dentro do padrão recomendado")

# Foco: for e while
# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
from math import tan
import time
print("Contagem de Embarque")
for embarque in range(5,0,-1):
    time.sleep(1)
    print(f"Embarque em: :) {embarque}")
    
# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de vários pedidos.O loop para quando o usuário digitar 0. No fim, mostre o faturamento total acumulado.
print("Somatório de Frete (Acumulador)")
faturamento = 0
frete = 1

while frete != 0:
    frete = float(input("Valor do Frete ou 0 para encerrar"))
    faturamento += frete
print(f"Faturamento total foi de {faturamento}")

print("Somatório de Frete (Acumulador) - Versão 2.0")
faturamento = 0
while True:
    valor = float(input("Valor do Frete ou 0 para finalizar"))
    if valor == 0:
        break
    faturamento += valor
print(f"Faturamento total {faturamento}em Reais")

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.
print("Monitoramento de Frota - Quilometragem")
maior_km = 0
for i in range(1,6):
    km = float(input(f"Digite a quilometragem do veículo {i}"))
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada foi de {maior_km} km")

var = 0
print("Monitoramento de Frota - Km - Versão 2.0")
veiculo1 = int(input("Informe a KM do veiculo 1"))
for km in range(2,6):
    veiculos = float(input(f"Informe a KM do veiculo{km}registrada"))
    if veiculos > var:
        var = var + veiculos
    print(f"A maior KM foi de {var}")
    
# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador ("track99").Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se esgotar, exiba "Rastreamento Bloqueado".
print("Sistema de Rastreio")
erros = 0
tentativas = 3

while erros != 3:
    codigo = input("Insira o código de acesso")
    if codigo != "track99":
        erros = erros + 1
        tentativas = tentativas - 1
        print(f"Codigo incorreto você possui {tentativas}")
    else:
        break
    if erros == 3:
        print("Rastreamento bloqueado!")
    else:
        print("Acesso liberado :)")


print("Sistema de Rastreio - Versão 2")
acesso_negado = 0
while acesso_negado != 3:
    codigo = input("Digite o código de acesso do rastreador")
    if codigo != "track99":
        acesso_negado = acesso_negado + 1
        print("Acesso Negado :(")
        print("Rastreamento Bloqueado! ")
    elif codigo:
        print("Acesso Liberado")
        break

# 14.Gerenciador de Combustível: Comece com um tanque de 500 litros. Crie um
# menu (while) onde o usuário pode: (1) Abastecer o tanque da base, (2) Retirar
# combustível para um caminhão ou (3) Sair. ○ Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".
print("Gerenciador de Combustível")
tanque = 500
while True:
    print("1 - Abastecer")
    print("2 - Retirar")
    print("3 - Sair")
    opcao = input("Escolha uma opção")
    if opcao == "1":
        valor = float(input("Quantidade a abastecer"))
        tanque += valor
        print(f"Tanque atual: {tanque}")
    elif opcao == "2":
        valor = float(input("Quantidade a retirar"))
        if valor > tanque:
            print("Quantidade indisponível")
        else:
            tanque -= valor
            print(f"Tanque atual {tanque}")
    elif opcao == "3":
        print("Encerrando o Sistema")
        break
    else:
        print("Opção Inválida")
        if tanque < 50:
            print("Reserva Critica")

# 15.Relatório de Inspeção de Pneus: Use um for para processar 5 pneus. Para cada um, peça a profundidade do sulco (em mm). ○ Se o pneu for aprovado (maior ou igual a 1.6mm), conte-o.
# ○ No final do loop, exiba o total de pneus aprovados e a porcentagem de conformidade da frota.
print("Relatório de Inspeção de Pneus")
contagem = 0
total = 5
for pneu in range(1,6):
    medida = float(input(f"Medida do sulco do pneu {pneu} em mm"))
    if medida >= 1.6:
        contagem = contagem + 1
        print("Pneu aprovado e adicionado a contagem :)")
    else:
        print("Pneu fora das medidas regulares não foi adicionado a contagem")
        pass 
    porcentagem = (contagem / total) * 100
    print(f"Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem}% de conformidade")
print("Encerrando inspeção de Pneus")
