'''
Escreva uma função que recebe um número e verifica se ele é ou não um número primo. 
Um número é primo se ele não for divisível por nenhum outro número entre 2 e ele mesmo. 
Ou seja, verifique o resto da divisão do valor recebido por todos os números entre 2 e ele 
próprio. Se o resto de uma dessas divisões for igual a zero, o número não é primo. 
Observe que 0, 1 e os números negativos não são primos e que 2 é o único número primo que é par.

Sua função deve retornar True ou False.

O nome da sua função deve ser eh_primo
'''

def eh_primo(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    ultimo_teste = int(n ** 0.5)
    for i in range(3, ultimo_teste + 1, 2):
        if n % i == 0:
            return False
    return True