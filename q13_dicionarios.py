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
e retornar o preco do produto.
ii) A segunda função deve receber uma lista de dicionários (lista de produtos), o numero do produto
e retornar a qtde vendida do produto.
iii) A terceira função deve receber uma lista de dicionários (lista de produtos), o numero do produto
e retornar o valor total de vendas do produto.
'''

produtos = [
    {'numero do produto': 0, 'preco do produto': 100, 'qtde vendida': 0},
    {'numero do produto': 1, 'preco do produto': 200, 'qtde vendida': 10},
    {'numero do produto': 2, 'preco do produto': 50, 'qtde vendida': 7},
    {'numero do produto': 3, 'preco do produto': 70, 'qtde vendida': 3}
]

# i)
def preco_do_produto(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['preco do produto']
print(preco_do_produto(produtos, 2))

# ii) 
def qtde_vendida(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['qtde vendida']
print(qtde_vendida(produtos, 2))

'''# iii.1) 
def valor_total(produtos, numero_do_produto):
    for produto in produtos:
        if produto['numero do produto'] == numero_do_produto:
            return produto['qtde vendida'] * produto['preco do produto']
print(valor_total(produtos, 2))'''

# iii.2) 
def valor_total(produtos, numero_do_produto):
    return qtde_vendida(produtos, numero_do_produto) * preco_do_produto(produtos, numero_do_produto)

print(valor_total(produtos, 2))