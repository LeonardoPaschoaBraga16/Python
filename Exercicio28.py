import random

print('João x1 simulator --- by Nathanileo Enterprises')

print('Pensei em um numero de 0 a 5, acerta ai ez')
num = [0, 1, 2, 3, 4, 5]
fun = random.choice(num)

ent = int(input('O numero pensado é? '))
print('O numero pensado é {}'.format(fun))

if ent == fun:
    print('Perdi o x1, merda, ele tem qi ;-;')
else:
    print('GANHEI O X1 SEU EEEZ LIXXO')