'''
Uma função do segundo grau é representada pela seguinte expressão:
f(x) = a * (x ** 2) + b * x + c
Onde a, b e c são constante e x (input) é um valor pertencente ao domínio da função.
Faça uma função em python que recebe os valores de x, a, b e c e retorna o valor 
de f(x)

Exemplos:
1) 
Entrada: x = 0; a = 1; b = 1; c = 0 
Saida: f(x) = 0

2) 
Entrada: x = 1; a = 1; b = 1; c = 0 
Saida: f(x) = 2
'''

def segundo_grau(x, a, b, c):
    return a * (x ** 2) + b * x + c

def segundo_grau(x, a, b, c):
    y = a * (x ** 2) + b * x + c
    return y

print(segundo_grau(0, 1, 1, 0))
print(segundo_grau(1, 1, 1, 0))
