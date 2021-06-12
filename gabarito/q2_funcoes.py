'''
Na química orgânica, um alcano possui a seguinte fórmula molecular:
C(n) H(2n+2)
Ou seja, para cada "n" átomos de carbono, existirão 2n+2 átomos de 
hidrogênio

Faça uma função que recebe o numero de átomos de carbono e o numero de átomos
de Hidrogênio e devolve True se o composto for alcano e False caso contrário.

Exemplos:
1)
Entrada: C = 10; H = 22
Saída: True

2) 
Entrada: C = 10; H = 20
Saída: False

Sua função deve se chamar eh_alcano.
'''

# Solução 1
def eh_alcano(n_C, n_H):
    if 2 * n_C + 2 == n_H:
        return True
    return False

'''# Solução 2
def eh_alcano(n_C, n_H):
    return 2 * n_C + 2 == n_H'''

print(eh_alcano(10, 22))
print(eh_alcano(10, 20))