'''
Uma loja contratou você para desenvolver um sistema que os ajudasse a registrar de maneira mais prática seus produtos.
O seu sistema deve registrar o numero do produto, o valor do produto e a quantidade vendida.
Para tanto, será utilizado uma lista de dicionários da seguinte forma:
produtos = [
    {'numero do produto': 0, 'preco do produto': 100, 'qtde vendida': 0},
    {'numero do produto': 1, 'preco do produto': 200, 'qtde vendida': 10},
    {'numero do produto': 2, 'preco do produto': 50, 'qtde vendida': 7},
    {'numero do produto': 3, 'preco do produto': 70, 'qtde vendida': 3}
]

Nesse sentido, desenvolva três funções:
i) A primeira função deve receber uma lista de dicionários (lista de produtos), o numero do produto
e retorna o preco do produto.
ii) A segunda função deve receber uma lista de dicionários (lista de produtos), o numero do produto
e retorna a qtde vendida do produto.
iii) A terceira função deve receber uma lista de dicionários (lista de produtos), o numero do produto
e retorna a valor total de vendas do produto.

OBS.: Caso o numero de produto não esteja na lista de produtos, retorne []
'''

produtos = [
    {'numero do produto': 0, 'preco do produto': 100, 'qtde vendida': 0},
    {'numero do produto': 1, 'preco do produto': 200, 'qtde vendida': 10},
    {'numero do produto': 2, 'preco do produto': 50, 'qtde vendida': 7},
    {'numero do produto': 3, 'preco do produto': 70, 'qtde vendida': 3}
]

# i)
# solução 1
def preco_do_produto(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['preco do produto']
    return []

# solução 2
def preco_do_produto(produtos, numero_do_produto):
    for i in range(len(produtos)):
        if produtos[i]['numero do produto'] == numero_do_produto:
            return produtos[i]['preco do produto']
    return []

# ii)
# solução 1
def qtde_vendida(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['qtde vendida']
    return []

# solução 2
def qtde_vendida(produtos, numero_do_produto):
    for i in range(len(produtos)):
        if produtos[i]['numero do produto'] == numero_do_produto:
            return produtos[i]['qtde vendida']
    return []

# iii)
# solução 1
def total_de_vendas(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['qtde vendida'] * produto['preco do produto']
    return []

# solução 2
def total_de_vendas(produtos, numero_do_produto):
    for i in range(len(produtos)):
        if produtos[i]['numero do produto'] == numero_do_produto:
            return produtos[i]['qtde vendida'] * produtos[i]['preco do produto']
    return []

# solução 3
def total_de_vendas(produtos, numero_do_produto):
    return preco_do_produto(produtos, numero_do_produto) * qtde_vendida(produtos, numero_do_produto)