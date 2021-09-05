num = int(input('Insira o valor: '))
cng = 0 + num
vez = 0


print('')

for cont in range(1, cng+1):

    if num % cont == 0 or cont / 1 == num:
        print(f'\033[0;31m {cont}\033[m', end=' ')
        vez = vez + 1
    else:
        print(f'\033[0;33m {cont}\033[m', end=' ')

print('')
print('')
print(f'O numero {num} foi dividido {vez} vezes')

if vez == 2:
    print('')
    print(f'{num} É um numero primo')
else:
    print('')
    print(f'{num} NÃO é um numero primo')