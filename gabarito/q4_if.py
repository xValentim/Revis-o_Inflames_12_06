'''
Faça uma função que recebe um número natural e devolve 'par' se o número for par
e 'impar' se o número for ímpar

Exemplo:
1)
Entrada: 10
Saída: par

2)
Entrada: 9
Saída: impar

sua função deve se chamar paridade
'''

def paridade(n):
    if n % 2 == 0:
        return 'par'
    return 'impar'