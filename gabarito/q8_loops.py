'''
Quantos uns?
Escreva uma função que recebe um número e devolve a quantidade de vezes 
que o algarismo 1 ocorre nesse número. Ex: 1030110641 tem 4 ocorrências do algarismo 1.

O nome da sua função deve ser quantos_uns
'''

def quantos_uns(n):
    qtde = 0
    while n != 0:
        ultimo_algarismo = n % 10
        if ultimo_algarismo == 1:
            qtde += 1
        n = n // 10
    return qtde
