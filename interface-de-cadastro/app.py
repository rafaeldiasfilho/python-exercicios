import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Camiseta", "Calça", "Short", "Cueca"]
lista_produtos = []

janela = tk.Tk()

#Criação da função

def cadastrar_produto():
  descricao = entry_descricao.get()
  tipo = combobox_selecionar_tipo.get()
  quantidade= entry_quantidade.get()
  preco = entry_preco.get()
  data_criacao = dt.datetime.now()
  data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
  produto = len(lista_produtos)+1
  produto_str = "COD-{}".format(produto)
  lista_produtos.append((produto_str, descricao, tipo, quantidade, preco, data_criacao))

#Titulo da janela 
janela.title('Ferramenta de cadastro de produtos')

label_descricao = tk.Label(text="Descrição do produto")
label_descricao.grid(row=1, column=0, padx=10, pady= 10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_unidade = tk.Label(text="Tipo do produto")
label_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade= tk.Label(text="Quantidade de produto")
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade= tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_preco= tk.Label(text="Preço do produto")
label_preco.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_preco= tk.Entry()
entry_preco.grid(row=5, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Cadastrar produto", command=cadastrar_produto())
botao_criar_codigo.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)


janela.mainloop()

print(lista_produtos)