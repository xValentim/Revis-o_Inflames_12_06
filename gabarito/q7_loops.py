'''
Faça um programa que imprime no terminal todos os numeros pares
de 0 até 100
'''

# Loop while
# Solução 1
i = 0
while i <= 100:
    print(i)
    i += 2

# Solução 2
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# Solução 3
i = 0
while i <= 50:
    print(i * 2)
    i += 1

# Loop for
# Solução 1
for i in range(100 + 1):
    if i % 2 == 0:
        print(i)

# Solução 2
for i in range(100 + 1, 2):
    print(i)
