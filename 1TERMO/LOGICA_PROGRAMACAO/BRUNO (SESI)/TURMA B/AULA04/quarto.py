# Conteúdo sobre lógica
# Exemplo 1
# print("Expressões lógicas ")
# idade = int(input("Digite sua idade:"))

# if idade >= 18:
#     print("Você é maior de idade.")
#     print("Pode tirar carta de motorista.")
# elif idade >= 16:
#     print("Você ainda não é maior, mas já pode votar.")
# else:
#     print("Você é menor de idade.")

# # if: "Se" a condição for verdadeira.
# # elif: "Senão, se" (usado para múltiplas condições).
# # else: "Senão" (executa se nenhuma das anteriores for verdadeira).

# # Exemplo 2
# print("Escolha sua modalidade?")
# print("Opção 1: TI")
# print("Opção 2: Humanas")
# print("Opção 1: Exatas")
# modalidade = int(input("Digite sua opção de modalidade por números"))
# if modalidade == 1:
#     print("Você escolheu TI")
# elif modalidade == 2:
#     print("Você escolheu Humanas")
# else: 
#     print("Você escolheu Exatas")

# Exemplo 3
print("Categoria de Series e Filmes")
print("Escolha uma categoria")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria")
if categoria == "S":
    print("Sua escolha foi para Séries")
elif categoria == "F":
    print("Sua escolha foi para Filmes")
else: 
    print("Você não escolheu nenhuma opção")
    print("Finalizando aplicativo")

# Exemplo 4
print("Calculadora com condições")
print("Escolha como quer calcular")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")
calculadora = float(input("Digite sua opção para calcular \n"))
if calculadora == 1:
    print("1 = Você escolheu soma")
    soma1 = int(input("Digite o primeiro valor \n"))
    soma2 = int(input("Digite o segundo valor \n"))
    print(soma1+soma2)
elif calculadora == 2:
    print("2 = Você escolheu subtração")
    sub1 = int(input("Digite o primeiro valor \n"))
    sub2 = int(input("Digite o segundo valor \n"))
    print("A subtração foi: ", sub1-sub2)
elif calculadora == 3:
    print("3 = Você escolheu multiplicação")
elif calculadora == 4:
    print("4 = Você escolheu divisão")
else:
    print("Você não escolheu nenhuma opção")
    print("Sair do programa")

# Exercicio 1
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota base de 50 é aprovado e menor que esse valor será reprovado
print("Cálculo de Notas")
n1 = int(input("Digite a primeira nota \n"))
n2 = int(input("Digite a segunda nota \n"))
media = (n1 + n2) / 2

if media >= 70:
    print("Aprovado")
elif media >= 50:
    print("Recuperação")
else:
    print("Reprovado")

# Exercício 2
# Criar um algoritmo para demonstrar a sinalização de um semaforo
print("Bem-Vindo ao Semaforo")
print(" 1 - Verde")
print(" 2 - Vermelho")
print(" 3 - Amarelo")
cores = int(input("Qual cor você deseja?"))

if cores == 1:
    print("Verde")
elif cores == 2:
    print("Vermelho")
elif cores == 3:
     print("Amarelo")
else:
    print("Somente essas cores!!")

# Exercicio 3
# Criar um algoritmo para aplicação de descontos para produtos como sapatos aplicar 10%, para produtos como roupas 5% e perfumes 2%
# Complementar: acrescentar um valor e uma quantidade para pode agora calcular e assim aplicar o desconto
print("Loja da Maria")
print("1 - Sapatos")
print("2 - Roupas")
print("3 - Perfumes")

opcao = int(input("Digite a opção de compra \n"))

if opcao == 1:
    v1 = float(input("Digite o valor do produto \n"))
    qt1 = int(input("Digite a quantidade do produto"))
    total1 = (v1 * qt1) * 10 / 100
    print("O valor da sua compra foi de: ", total1)

elif opcao == 2:
    v2 = float(input("Digite o valor do produto \n"))
    qt2 = int(input("Digite a quantidade do produto"))
    total2 = (v2 * qt2) * 5 / 100
    print("O valor da sua compra foi de: ", total2)


# Exercicio 4
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota 0 a 100 para ser aprovado será acima de 70 e menor que 50 esse valor será reprovado porém vamos acrescentar uma nova condição que entre 50 e 70 recuperação