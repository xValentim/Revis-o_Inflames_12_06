'''
Para otimizar o tempo em que um professor passa tomando a média de 3 provas de seus alunos,
faça um programa que pergunta as 3 notas dos alunos e imprime a média final

Exemplo:
1)
Entrada: 10, 6, 5
Saída: 7

1)
Entrada: 10, 10, 7
Saída: 9
'''

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
print(f'Média: {(nota_1 + nota_2 + nota_3) / 3}')