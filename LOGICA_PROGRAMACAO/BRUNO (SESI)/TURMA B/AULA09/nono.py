#  tratamento de erros com python
# Erros comuns:
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário

# Exemplo de tratamento de erros
# from ast import Name
# from math import e


# print("Exemplo de tratamento de erros")
# try:
#     num1 = int(input("Digite o primeiro número ... "))
#     num2 = int(input("Digite o segundo número ... "))
#     resultado = num1 / num2
#     print(f"O resultado da divisão é: {resultado:.2f}")

# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# except NameError:
#     print("Erro: Variável não definida.")   

# if num1 > 100:
#     print("O número digitado é maior que 100.")
#     for i in range(1, 6):
#         print(f"{num1} x {i} = {num1 * i}")
#         if num1 * i > 1000:
#             print("O resultado da multiplicação é maior que 1000.")
#             try:
#                 pass
#             except Exception as e:
#                 print(f"Ocorreu um erro inesperado: {e}")
# else:
#     print("O número digitado é menor ou igual a 100.")

# exercicio 1:
# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.
# - ZeroDivisionError: se a lista de números estiver vazia.
# try:
#     num = int(input("Digite um número inteiro ... "))
#     numeros = []
#     for i in range(num):
#         numero = float(input(f"Digite o número {i + 1} ... "))
#         numeros.append(numero)
    
# media = sum(numeros) / len(numeros)
#     print(f"A média dos números é: {media:.2f}")
# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
# except ZeroDivisionError:
#     print("Erro: A lista de números está vazia.")
# texto = "Python"
# print(texto.strip().count("python"))


# Exercicio 2:
# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja uma string.
try:
    palavras = input("Digite uma lista de palavras separadas por espaço ... ").split()    
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    print("Contagem de palavras:")
    for palavra, contagem in contagem.items():
        print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite uma lista de palavras separadas por espaço.")

# Exercicio 3:
# Escrever um programa mais simples com testes de tratamento de erros, como por exemplo, solicitar ao usuário um número. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número.
# - ZeroDivisionError: se o usuário digitar zero como divisor.


