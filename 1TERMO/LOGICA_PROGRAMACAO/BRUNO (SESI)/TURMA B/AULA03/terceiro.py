# Funções Def
# Exemplo 1
def saudacao(nome):
    return f"Olá, {nome}!"
mensagem = saudacao("Maria")
print(mensagem) 

# Exemplo 2
nome = input("Seu nome: ")
idade = int(input("Sua idade: ")) # Converte texto para inteiro
print(f"{nome} tem {idade} anos.")

#Exercício 1
# Cálculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semetre.
#os valores de notas são 0 a 100 no final exibir o resultado do ano e incluir nota de média do primeiro e segundo semestre

# Arrendodar casas decimas
# s1 = n1 + n2 + n3 /3
# print("media do semestre", round(s1,2)
# round(s1),2

# Exemplo 3
def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Você é o novo {cargo}.")

boas_vindas("Ana", "Desenvolvedora")
boas_vindas("Carlos", "Gerente")

# Exemplo 4
def configurar_conexao(servidor, porta=8080):
    print(f"Conectando a {servidor} na porta {porta}...")

configurar_conexao("192.168.1.1")        # Usa a porta 8080
configurar_conexao("10.0.0.1", 3000)     # Usa a porta 3000
configurar_conexao("192.168.1.2")
configurar_conexao("10.0.0.2",3001)

# Exercicio 2
# Calculo de idade: Deve apresentar o nome, curso, data nascimento e apresentar a idade sua no final

# Exercicio 3
# Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta).

# Exercicio 4
# Criar um sistema para calcular o sucessor e antecessor de um valor

# Exercicio 5
# Criar um algoritmo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%

