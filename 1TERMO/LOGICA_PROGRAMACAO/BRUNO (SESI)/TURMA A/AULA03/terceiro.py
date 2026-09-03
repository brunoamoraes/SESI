# Condições lógicas
# if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usado para múltiplas condições).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).
# Exemplo 1
print("Verificar Maioridade")
idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é Adulto")
elif idade >= 16:
    print("Você não é Adulto mas pode votar")
else:
    print("Você é Adolescente")

# Sinais de > Maior e >= Maior Igual
# Sinais de < Menor e <= Menor Igual
# Sinais de == Igual 

# Exemplo 2
print("Loja")
print("Bem-Vindo ao Sistema do Brunão")
print("Opções:")
print(" 1 - Sapatos")
print(" 2 - Roupas")
print(" 3 - Perfumes")

escolha = int(input("Digite sua escolha pelo número da opção:"))
if escolha == 1:
    print("Você quer comprar sapatos, OK")
    v1 = float(input("Digite o valor do produto: "))
    qt1 = int(input("Digite a quantidade desejada: "))
    total = v1 * qt1
    print("Sua compra de sapatos foi um total de: ", total)
elif escolha == 2:
    print("Você escolheu Roupas")
elif escolha == 3:
    print("Você escolheu Perfumes")
else:
    print("Obrigado por utilizar o sistema do Brunão")

# Exemplo 3
print("Escolha uma opção para iniciar o Sistema")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria")
if categoria == "S":
    print("Você escolheu por Séries")
elif categoria == "F":
    print("Você escolheu por Filmes")
else: 
    print("Você não escolheu nenhuma das opções acima")
    print("Estamos encerrando o aplicativo")

# Exercício 1
# Crie um algoritmo que simule uma calculadora e que por opção de escolha permita calcular os operadores.
# Ex: Ao escolher a opção 1, ele irá calcula a soma e assim por diante. Sua calculadora deve conter todos os operadores
print("Minha Calculadora")
print("Operadores Matemáticos")
print("Para Somar - Digite Som")
print("Para Subtrair - Digite Sub")
print("Para Multiplicar - Digite Mult")
print("Para Dividir - Digite Div")
print("Digite X para sair")

operadores = input("Digite sua escolha de operadores")

if operadores == "Som":
    soma1 = float(input("Digite o primeiro valor"))
    soma2 = float(input("Digite o segundo valor"))
    tsoma = soma1 + soma2
    print("O cálculo de soma foi: ", tsoma)
elif operadores == "Sub":
    sub1 = float(input("Digite o primeiro valor"))
    sub2 = float(input("Digite o segundo valor"))
    tsub = sub1 - sub2
    print("O cálculo de subtração foi: ", tsub)

# Exercicio 2
# Calculo de idade: Deve apresentar o nome, curso, data nascimento (ano) e apresentar a idade sua no final


# Exercicio 3
# Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta).
# Atendimento em mesa com garçom 10%
# Atendimento em mesa sem garçom 5%

# if opcao == 1:
#     comanda = float(input("Digite o valor da conta"))
#     total = comanda *(10/100) + comanda

# Exercicio 4
# Criar um sistema para calcular o sucessor e antecessor de um valor

# Exercicio 5
# Criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%