# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

# DEF funções em bloco
def cadastrar_usuario():
    #.get
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_curso_usuario.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" and curso_usuario == "" and nome_escola == "":
        messagebox.showwarning("Bem-Vindo", "Digite seu nome e seu curso e escolha sua escola")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}! seu curso é {curso_usuario} e sua escola é {nome_escola}")


# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("500x500")
janela.configure(bg="blue")

# 1 - Etapa Componentes
# Labels = Rótulos ou nossos antigos prints
lbl_nome_usuario = tk.Label(janela, text="Digite seu nome.:", font=("Arial", 14),fg="green")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)
lbl_curso_usuario = tk.Label(janela, text="Digite seu curso.:", font=("Arial", 14), fg="green")
lbl_curso_usuario.grid(row=1, column=0, pady=10, padx=10)
lbl_nome_escola = tk.Label(janela, text="Escolha sua Escola.:", font=("Arial", 14), fg="green" )
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)

# Entrys = Caixa de texto antigos input
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_curso_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_curso_usuario.grid(row=1, column=1, pady=10, padx=10)

# ComboBox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, values=["SESI408","SESI5"], width=30, font=("Arial", 14), state="readonly")
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

#Botões = Botões de clique
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), fg="green", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)
btn_fechar_janela = tk.Button(janela, text="Fechar", command=janela.destroy)
btn_fechar_janela.grid(row=6, column=1, pady=10, padx=10)

# 4 - Etapa Loop
janela.mainloop()

