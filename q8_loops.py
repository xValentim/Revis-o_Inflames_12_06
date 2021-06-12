'''
Quantos uns?
Escreva uma função que recebe um número e devolve a quantidade de vezes 
que o algarismo 1 ocorre nesse número. Ex: 1030110641 tem 4 ocorrências do algarismo 1.

O nome da sua função deve ser quantos_uns
'''

def quantos_uns(n):
    numero = list(str(n))
    qtde_de_uns = numero.count('1')
    return qtde_de_uns


def quantos_uns(n):
    numero = str(n)
    qtde_de_uns = 0
    for algarismo in numero:
        if algarismo == '1':
            qtde_de_uns += 1
    return qtde_de_uns
    
