import random

n1 = input('Insira o nome da primeira pessoa: ')
n2 = input('Insira o nome da segunda pessoa: ')
n3 = input('Insira o nome da terceira pessoa: ')
n4 = input('Insira o nome da quarta pessoa: ')

pessoas = [n1, n2, n3, n4]

print('A ordem de apresentação será {}'.format(random.sample(pessoas,4)))
