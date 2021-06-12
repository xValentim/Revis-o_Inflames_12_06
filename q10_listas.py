'''
Faça uma função que recebe uma lista e devolve a soma de todos os elementos da lista
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # soma = 55

# Pythonic
def soma_elementos(lista):
    return sum(lista)


def soma_elementos(lista):
    soma = sum(lista)
    return soma 


'''def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma '''

'''def soma_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        elemento = lista[i]
        soma += elemento
    return soma '''

'''def soma_elementos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        elemento = lista[i]
        soma += elemento
        i += 1
    return soma '''

print(soma_elementos(lista))




