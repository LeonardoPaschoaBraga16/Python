cont = 0
plus = 0
for cnt in range (3, 501, +3):
    if cnt % 2 == 0:
        cnt+1
    elif cnt % 3 == 0:
        plus = plus + cnt
        cont = cont + 1


print('O Resultado da soma dos {} numeros é {}'.format(cont, plus))
