# Clean Code - Aula 8
# Para que usar?
# Como usar?
# print("Clean Code - Aula 8")
# aula = 8
# print(f"Estamos na aula {aula} de Clean Code")

# # Manipulação de arquivos e Texto
# texto = "  Python é muito legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower())  # "python"
# print(texto.strip().capitalize())  # "Python"
# print(texto.strip().title())  # "Python"
# print(texto.strip().replace(" ", "_"))  # "Python"
# print(texto.strip().split())  # ["Python"]
  
# Escrevendo
with open("temperatura.txt", "w") as arquivo:
    arquivo.write("Estudar Python hoje!")
    arquivo.write("\nLer sobre Clean Code.")

# Lendo
with open("temperatura.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Execucão de comandos do sistema
import os # importa o módulo os para interagir com o sistema operacional
# Onde estou?
# print(os.getcwd())
# Listar arquivos na pasta
# print(os.listdir())
# print(os.listdir(".."))  # lista arquivos da pasta pai
# print(os.listdir("..\\.."))  # lista arquivos da pasta avô
# print(os.listdir("C:\\"))  # lista arquivos da raiz do C
# print(os.listdir("C:\\Users"))  # lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Public"))  # lista arquivos da pasta Public

# Outros comandos úteis:
# # Criar pasta
# os.mkdir("nova_pasta")
# # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2: 
# Crie um script que mostre o caminho da pasta atual.
import os
print(os.getcwd())

# # Exercicio 3:
# # Liste os arquivos da pasta atual.
print(os.listdir())

# # Exercicio 4:
# # Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta.
os.mkdir("projetos")
os.rename("projetos", "meus_projetos")
os.rmdir("meus_projetos")

# # Exercicio 5:
# # Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela.
with open("log.txt", "w") as arquivo:
    arquivo.write("Log de atividades")
with open("log.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# # Exemplo de dicionário:
# # Crie um dicionário com informações sobre uma pessoa e acesse um valor usando uma chave.
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo",
    "profissão": "Engenheira"
}
pessoa2 = {
    "nome": "Bruno",
    "idade": 25,
    "cidade": "SP",
    "profissão": "Designer"

}
animais = {
    "cachorro": "Labrador",
    "gato": "Siamês",
    "pássaro": "Canário"
}

print(pessoa["cidade"],pessoa["profissão"])
print(pessoa2["nome"], pessoa["idade"])
print(animais["cachorro"])

# Exemplo 2: Desligar o PC (comando para Windows)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")
#     # -s comando para desligar
#     # -t tempo definir
#     # -a cancelar desligamento

# with open("desliga.bat", "r") as desligar:
#     conteudo = desligar.read()
#     print(conteudo)

# Exercicio 7: Criar um arquivo de backup
# Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteúdo de "notas.txt" e escrever no novo arquivo.
# with open("notas.txt", "r") as notas:
#     conteudo = notas.read()
# with open("notas_backup.txt", "w") as backup:
#     backup.write(conteudo)

# Exemplo 2: Criar um script de limpeza de arquivos
# Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".tmp". O script deve exibir uma mensagem para cada arquivo excluído.
# pasta = os.listdir()
# for arquivo in pasta:
#     if arquivo.endswith(".txt"):
#         os.remove(arquivo) #remove ira apagar o arquivo
#         print(f"Arquivo {arquivo} excluído.")
# print("Limpeza de arquivos concluída.")

# Exercicio 8: Criar um script de monitoramento de temperatura
# Escreva um script que monitore a temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°C.
print("Monitoramento de Temperatura")
with open("temperatura.txt", "r") as temperatura_arquivo:
    temperatura1 = float(temperatura_arquivo.read())
    print(f"Temperatura atual: {temperatura1}°C")
    if temperatura1 > 70:
        print("ALERTA: Temperatura acima de 70°C! Resfriamento necessário.")
    else:
        print("Temperatura dentro do limite seguro.")

# tratamento de erros com python
# Erros comuns:
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário
# Exemplo de tratamento de erros
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
# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")
