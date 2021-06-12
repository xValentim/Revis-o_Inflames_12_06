'''
Dado um sistema de "n" massas (m1, m2, m3... mn). Cada massa ocupa uma posição xi, yi do plano cartesiano, 
o centro de massa (Xcm, Ycm) do sistema será a média ponderada dos eixos independentes, ou seja:

Xcm = (m1.x1 + m2.x2 + ... + mn.xn) / n
Ycm = (m1.y1 + m2.y2 + ... + mn.yn) / n

Faça uma função que recebe,
a lista das posições Xi's das massas: xis = [x1, x2, x3, ..., xn]
a lista das posições Yi's das massas: yis = [y1, y2, y3, ..., yn]
a lista dos valores das massas (pesos): mis = [m1, m2, m3, ..., mn]

e devolve uma lista contendo o Xcm e o Ycm, nessa ordem

'''

# Pythonic
def centro_de_massa(xis, yis, mis):
    n = len(mis)
    xis_2 = [(mis[i] / n) * xis[i] for i in range(n)]
    yis_2 = [(mis[i] / n) * yis[i] for i in range(n)]
    Xcm = sum(xis_2)
    Ycm = sum(yis_2)
    return [Xcm, Ycm]

