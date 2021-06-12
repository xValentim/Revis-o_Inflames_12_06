N, M = [int(i) for i in input("").split()]
pais = [int(j) for j in input("").split()]
compareceram = [int(k) for k in input("").split()]

geracoes = [[0]]
geracao_atual = geracoes[0]
for i in range(len(pais)):
    descendente = i + 1
    pai = pais[i]


