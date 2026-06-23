import tkinter as tk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Exemplo de Tkinter com Label, Entry e Button")
janela.geometry("300x200")

def classificar_lote():
    try:
        codigo = campo_codigo.get()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um código válido.")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {str(e)}")
    if codigo.startswith("A"):
        resultado.config(text="Alimentos")
    elif codigo.startswith("E"):
        resultado.config(text="Eletrônicos")
    else:
        resultado.config(text="Desconecido")

label_codigo = tk.Label(janela, text="Código do Produto:")
label_codigo.grid()

campo_codigo = tk.Entry(janela)
campo_codigo.grid()
botao_classificar = tk.Button(janela, text="Classificar", command=classificar_lote)
botao_classificar.grid()
resultado = tk.Label(janela, text="")
resultado.grid()
janela.mainloop()
