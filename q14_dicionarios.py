'''
Média de notas
Foi criado um dicionário em Python para cada turma de design de software, 
o dicionário possui o nome do aluno e sua média final. Esses dicionários foram colocados em uma lista. 
Faça uma função recebe essa lista e calcule a média dos alunos de todas as turmas.

Por exemplo:

Para a lista alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ], 
a função calcula_media(alunos) retorna o valor 6.0

O nome da sua função deve ser calcula_media
'''

alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]

def calcula_media(lista_de_turmas):

    soma_notas = 0
    qtde = 0
    for turma in lista_de_turmas:
        lista_de_valores = turma.values()
        soma_notas += sum(lista_de_valores)
        qtde += len(lista_de_valores)
    media = soma_notas / qtde
    return media

print(calcula_media(alunos))
