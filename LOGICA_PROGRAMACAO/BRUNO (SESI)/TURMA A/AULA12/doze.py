# Tratamento de Erros
# Erros comuns:
# - SyntaxError: Erro de sintaxe, geralmente causado por erros de digitação ou estrutura incorreta do código.
# - NameError: Ocorre quando uma variável ou função é referenciada antes de ser definida. 
# - TypeError: Acontece quando uma operação é aplicada a um tipo de dado inadequado.

# Exemplo de tratamento de erros usando try-except
# def dividir(a, b):
#     try:
#         resultado = a / b
#         print(f"O resultado da divisão é: {resultado}")
#     except ZeroDivisionError:
#         print("Erro: Não é possível dividir por zero.")
#     except TypeError:
#         print("Erro: Os valores devem ser números.")
#     except NameError:
#         print("Erro")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")
# dividir(10, 0) 

# 1
import tkinter as tk
from tkinter import messagebox

# 4
# .get e DEF para iniciar processos de função em bloco

def calcular_media():
    primeiro_valor = int(ent_primeiro_valor.get())
    segundo_valor = int(ent_segundo_valor.get())

    try:
        if primeiro_valor == 0 and segundo_valor == 0:
            messagebox.showwarning("Verificar", "Inserir valores diferentes de 0")
        calculo_media = primeiro_valor / segundo_valor
        messagebox.showinfo("Resultado", f"Calculo de média {calculo_media}")
    except ZeroDivisionError:
            messagebox.showerror("Erro", "Você digitou um valor 0")
    except TypeError:
            messagebox.showerror("Erro", "Inserir numeros válidos")
    except NameError:
            messagebox.showerror("Erro", "Inserir numeros")
    except ValueError:
        messagebox.showerror("Erro", "Inserir numeros válidos")

        

# 2
janela = tk.Tk()
janela.title("Tratamento de Erros")
janela.geometry("500x500")

# 3
# Label
lbl_primeiro_valor = tk.Label(janela, text="Digite o primeiro valor")
# lbl_primeiro_valor.pack() - Centraliza conteúdo na tela
lbl_primeiro_valor.grid(row=0, column=0, padx=10, pady=10)
lbl_segundo_valor = tk.Label(janela, text="Digite o segundo valor")
lbl_segundo_valor.grid(row=1,column=0,padx=10, pady=10)

# Entrys
ent_primeiro_valor = tk.Entry(janela, width=20)
ent_primeiro_valor.grid(row=0, column=1, padx=10,pady=10)
ent_segundo_valor = tk.Entry(janela, width=20)
ent_segundo_valor.grid(row=1, column=1, padx=10,pady=10)

# Botão
btn_calcular_valor = tk.Button(janela, text="Calcular", command=calcular_media)
btn_calcular_valor.grid(row=2, column=1, padx=10,pady=10)


# 5
janela.mainloop()