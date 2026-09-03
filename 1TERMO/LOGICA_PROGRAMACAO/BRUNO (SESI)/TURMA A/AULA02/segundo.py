# Tipos de Dados
# int
# float

x = 10
y = 5.15

# Números e valores
print('10')
print(5.15)

#Textos = string
print('Meu nome é Bruno')

#Concatenar
print('Eu gosto de programar \n' + ' \n Python \n')

# Contas
n1 = 10
n2 = 5
print('O valores são', n1 - n2)

# Operadores matemáticos
#  + = soma
#  - = subtração
#  * = multiplicacao
#  / = divisão
#  ^ = expoente

# Exemplo 2
# n1 = input('Digite o primeiro valor')
# print('Os valores', n1)

# Exemplo 3
n2 = input('Digite o seu primeiro número: \n')
print('Seu primeiro foi: \n', n2)

# Exemplo 4
nome = input('Qual é seu nome? \n')
print('Seu nome é: \n', nome) #Aqui ficaria mais completo
print(nome) #Aqui mais simples

# Exemplo 5
# Duas perguntas
# 1ª Qual é seu Curso
# 2ª Qual é sua idade

curso = input('Qual é seu curso? \n')
print('Seu curso é \n', curso)

# Exemplo 6A
base = 10
altura = 5
area = (base * altura) / 2
print(area)  

# Exemplo 6B
# Com informações
base = float(input('Informe o valor da base: \n'))
altura = float(input('Informe o valor da altura: \n'))
area = (base * altura) / 2
print('Os seus cálculos são:', float(area))

#Exercício 1
# Criar uma calculadora com os operadores soma , subtrair

# Exercício 2: 
# Calculadora de IMC (Potência e Divisão)
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso pela altura ao quadrado ($altura^2$).

# Exercício 3: O Crachá (Variáveis e Strings)
# Crie três variáveis:
# Uma chamada nome com o seu nome (string).
# Uma chamada idade com a sua idade (int).
# Uma chamada profissao com sua profissão ou "Estudante" (string).
# Tarefa: Imprima uma única frase concatenando essas variáveis, no formato:
# "Olá, meu nome é [nome], tenho [idade] anos e sou [profissao]."
# (Dica: Você precisará converter o número inteiro da idade para string usando str(idade) para poder somar com textos).
nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
prof = input("Digite sua profissão")

print("Seu nome é: ", nome, "e sua idade foi" ,idade, "E sua profissão foi", prof)
print("teste",nome + "ola",idade)