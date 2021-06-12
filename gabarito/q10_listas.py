'''
Faça uma função que recebe uma lista e devolve a soma de todos os elementos da lista
'''

# Soluação 1
def soma_elementos(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma += lista[i]
        i += 1
    return soma

# Solução 2
def soma_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

# Solução 3
def soma_elementos(lista):
    soma = 0 
    for elemento in lista:
        soma += elemento
    return soma

# Solução 4
# Pythonic
def soma_elementos(lista):
    return sum(lista)