# # TKINTER

# # Componentes Widgets
# # tk: Tk() # Janela
# # lb: Label() # Rótulo
# # bt: Button() # Botão
# # et: Entry() # Caixa de texto

# import tkinter as tk
# from tkinter import Button, messagebox

# # 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha Primeira Janela GUI")
# janela.configure(bg="#f0f0f0") # Cor de fundo
# janela.geometry("400x200") #Largura x Altura

# # 2. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão")

# # 3. Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa aula de Tkinter",bg="#2ecc71", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text="Clique Aqui", font=("Arial", 11), bg="#2ecc71", fg="white", command=mostrar_mensagem)
# btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#cce2ee", command=janela.destroy)

# # 4. Posicionar os componentes
# lbl_titulo.pack(pady=20) # 'pady' adiciona um espaçamento vertical
# btn_clique.pack(pady=10)
# btn_close.pack(pady=5)

# # 5. Rodar o loop da interface
# janela.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def saudar_usuario():
#     # .get() serve para buscar o texto que vamos digitar

#     nome = campo_nome.get()
#     media1 = campo_media1.get()
#     # media2 = campo_media2.get()

#     # resultado = media1 + media2

#     try:

#         if nome == "":
#             messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
#         else:
#             messagebox.showinfo("Saudações Alunos", f"olá, {nome} ! Seja bem-vindo ao mundo das interfaces gráficas")
#     except ValueError:

# # Configurações da janela
# app = tk.Tk()
# app.title("Exemplo 1")        
# app.geometry("350x200")

# # Componentes
# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
# lbl_instrucao.pack(pady=10)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5) 

# campo_media1 = tk.Entry(app, font=("Arial", 12))

# btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)

# app.mainloop()

# # Exercício: Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuário. A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média. Ao clicar no botão, a média deve ser exibida em uma mensagem.
import tkinter as tk
from tkinter import Button

janela = tk.Tk()
janela.title("Exercício Média de Notas")
janela.geometry("400x300")

fred = Button(janela, fg="red", bg="blue")

fred["fg"] = "red"
fred["bg"] = "blue"

fred.config(fg="red", bg="blue")
selection = "red"
fred.config(fg=selection)


janela.mainloop()