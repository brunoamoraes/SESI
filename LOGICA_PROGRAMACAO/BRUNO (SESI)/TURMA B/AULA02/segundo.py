# Funções

# a = 1  # a é uma variavel
# b = 2
# c = a + b
# print('O valor de A e B é: ', c)

# Variáveis são formas de armazenar informações

# Função Input
# Irá permitir inserir informações
# input("Qual é seu nome?")

# Operadores Matemáticos
# + = soma
# - = subtração
# * = multiplicação
# / = divisão

# Exemplo 1
# \n quebra linha
# v1 = input("Digite \n o primeiro valor: \n")
# v2 = input("Digite o segundo valor: \n")
# vtotal = v1 + v2
# print("Qual é o resultado?", vtotal)

# int = retorna valores inteiro Ex: 1, -5
# float = valores com casas decimais Ex 10.2 , -10.1

# Exemplo 2
# x1 = int(input('Digite o valor da subtração 1: \n'))
# x2 = int(input('Digite o valor da subtração 2: \n'))
# xtotal = x1 - x2
# print('Qual é o valor do X \n', xtotal)

# Exemplo 3 e Exemplo 4
# Multiplicar e Dividir
# print("Vamos Calcular? \n")
# print("Iniciamos a multiplicação \n")
# m1 = int(input("Qual é o primeiro valor? \n"))
# m2 = int(input("Qual é o segundo valor \n"))
# mtotal = m1 * m2
# print("O valor da multiplicação é?", int(mtotal))

# print(" Vamos dividir \n")
# d1 = float(input(" Digite o primeiro valor desejado \n"))
# d2 = float(input(" Digite o segundo valor desejado \n"))
# dtotal = d1 / d2
# print("Sua divisão é: \n", dtotal)

#Concatenar
print('Eu gosto de programar \n' + ' \n Python \n' )

# Exercicio 1
# Apresente as mensagens
# O programa deve permitir que você digite seu nome, seu curso e sua idade e também seu hobbie

print("Exercício 1 \n")
nome = input("Digite seu nome \n")
curso = str(input("Digite seu curso \n"))
idade = int(input("Digite sua idade \n"))
print("As informações são: \n", "Seu nome é \n", nome + "Sua idade é? \n", idade + "")
print("Seu nome é", nome)
print("Seu nome é", idade)
print("Seu nome é", curso)


# Exercício 2: 
# Calculadora de IMC (Potência e Divisão)
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso pela altura ao quadrado (peso / altura * altura)
print("Bem-VIndo a nossa Calculadora de IMC")

# Exercício 3:
# Calculara completa com os quatros operadores matemáticos
print("Calculadora")
n1 = float(input("Digite o valor \n"))
n2 = float(input("Digite o outro valor \n"))
print("A soma é \n", n1 + n2)
print("A subtração é \n", n1 - n2)

# Converter  em string
# adicao = n1 + n2
# print("A soma é ", str(adicao))

# Exercício 4
# Mercado do Brunão
# O mercado deve registrar venda de itens e um relatório de cupom fiscal no fim da compra
print("Mercado Senai \n")
print("Iniciar Compras \n")
produto = input("Digite o produto: \n")
valor = float(input("Digite o valor do produto: \n"))
qtde = float(input("Digite a quantidade \n"))
total = valor * qtde
print("Sua compra foi \n" + produto + str(valor) + str(qtde))