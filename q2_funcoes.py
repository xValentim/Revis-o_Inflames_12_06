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

'''def eh_alcano(N_C, N_H):
    return N_H == 2 * N_C + 2

def eh_alcano(N_C, N_H):
    if N_H == 2 * N_C + 2:
        return True
    return False'''


def eh_alcano(N_C, N_H):
    if N_H == 2 * N_C + 2:
        return True
    else:
        return False

print(eh_alcano(10, 20))
print(eh_alcano(10, 22))