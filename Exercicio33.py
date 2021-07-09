num1 = float(input('Insira o primeiro numero: '))
num2 = float(input('Insira o segundo numero: '))
num3 = float(input('Insira o terceir0 numero: '))


#Numero Maior
if num1 > num2 and num1 > num3:
    print('O maior numero é {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior numero é {}'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O maior numero é {}'.format(num3))

#Numero Menor
if num1 < num2 and num1 < num3:
    print('O menor numero é {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor numero é {}'.format(num2))
elif num3 < num1 and num3 < num2:
    print('O menor numero é {}'.format(num3))

print('fim')