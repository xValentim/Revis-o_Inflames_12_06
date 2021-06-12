# Problema da OBI primeira fase completo

N = int(input(""))
x1, y1 = [int(i) for i in input("").split()]
x2, y2 = [int(j) for j in input("").split()]
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
flag = False
# corte horizontal
if (y1 <= N / 2 and y2 > N / 2) or (y2 <= N / 2 and y1 > N / 2):
    flag = True
# corte vertical
elif (x1 <= N / 2 and x2 > N / 2) or (x2 <= N / 2 and x1 > N / 2):
    flag = True

if flag:
    print("S")
else:
    print("N")