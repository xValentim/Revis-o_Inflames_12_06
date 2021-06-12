'''
Faça um programa que imprime no terminal todos os numeros pares
de 0 até 99
'''
# Estrura de loop básica (while)
'''i = 0
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1 # i = i + 1'''

'''i = 0
while i < 100:
    print(i)
    i += 2 # i = i + 1

i = 0
while i < 50:
    print(i * 2)
    i += 1 # i = i + 1'''

# Estrura de loop básica (for)
for i in range(0, 100, 2):
    print(i)

for i in range(0, 100):
    if i % 2 == 0:
        print(i)

for i in range(0, 50):
    print(2 * i)