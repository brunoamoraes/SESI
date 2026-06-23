# Modelo Tkinter com Label, Entry e Button para classificar lotes de produtos com base no código inserido pelo usuário. O código do produto é verificado para determinar se pertence à categoria "Alimentos", "Eletrônicos" ou "Desconhecido".

# Mudanças na importação da bibiolteca
from tkinter import *

# Mudança na criação da janela
janela = Tk()
janela.title("Classificador de Lotes")
janela.geometry("300x200")

# mudanças no processo de classificação do lote, utilizando o método .startswith() para verificar o início do código inserido pelo usuário.
def classificar_lote():
    codigo = campo_codigo.get()
    if codigo.startswith("A"):
        resultado.config(text="Alimentos")
    elif codigo.startswith("E"):
        resultado.config(text="Eletrônicos")
    else:
        resultado.config(text="Desconhecido")

label_codigo = Label(janela, text="Código do Produto:")
label_codigo.pack()

campo_codigo = Entry(janela)
campo_codigo.pack()

botao_classificar = Button(janela, text="Classificar", command=classificar_lote)
botao_classificar.pack()

# mudanças na criação do label para exibir resultado
resultado = Label(janela, text="")
resultado.pack()

janela.mainloop()