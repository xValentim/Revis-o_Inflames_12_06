'''
Você foi contratado por um cursinho para desenvolver um sistema que ajudará 
a computar as notas dos alunos nos simulados.
O simulado é composto por 5 provas, com notas de 0 a 10,
A primeira prova vale 5% da nota final
A segunda prova vale 15% da nota final
A terceira prova vale 20% da nota final
A quarta prova vale 20% da nota final
A quinta prova vale 40% da nota final
O aluno será reprovado no simulado se alguma das situções abaixo acontecer:
1) Ao menos uma das notas é menor que 4
2) A média final é menor que 4

Faça uma função que recebe 5 notas no seu argumento e retorna "Reprovado" 
caso a situação 1) ou 2) aconteça e "Aprovado" caso contrário.

Sua função deve se chamar simulado
'''

def simulado(n1, n2, n3, n4, n5):
    if n1 < 4 or n2 < 4 or n3 < 4 or n4 < 4 or n5 < 4:
        return 'Reprovado' 
    media = 0.05 * n1 + 0.15 * n2 + 0.20 * n3 + 0.20 * n4 + 0.40 * n5
    if media < 4:
        return 'Reprovado'
    return 'Aprovado'