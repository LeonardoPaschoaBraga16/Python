sm = 0


for cnt in range(1, 7):
    num = int(input('Insira o {}° numero '.format(cnt)))
    if num % 2 == 0:
        sm = sm + num

print('A soma é {}'.format(sm))