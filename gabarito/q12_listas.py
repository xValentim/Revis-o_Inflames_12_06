'''
Matrizes ou tabelas podem ser representadas por uma estrutura de lista de listas
acompanhe:
tabela = [
    [1, 2, 3],
    [4, 5, 6],
    [-7, 8, -9]
]

Veja que, escrito dessa forma, a lista se assemelha de fato a uma matriz de 3 linhas
e 3 colunas.

Dessa forma, faça uma função que recebe uma lista de listas (como o exemplo da tebela) 
e procura a linha i e a coluna j que possui um elemento negativo.
note que a tabela de exemplo possui dois numeros negativos:
o numero da linha 2 e coluna 0, ou seja tabela[2][0]
o numero da linha 2 e coluna 2, ou seja tabela[2][2]
Portanto, a função deve retornar uma lista de listas contendo a posição i,j 
cujo elemento é negativo. Caso não exista elemento negativo, retorne []

OBS.: Para o exemplo da tabela, a saida seria: [[2, 0], [2, 2]]
'''
tabela = [
    [1, 2, 3],
    [4, 5, 6],
    [-7, 8, -9]
]

def procura_negativos(tabela):
    posicoes_dos_negativos = []
    for i in range(len(tabela)):
        for j in range(len(tabela[0])):
            if tabela[i][j] < 0:
                posicoes_dos_negativos.append([i, j])
    return posicoes_dos_negativos

print(procura_negativos(tabela))