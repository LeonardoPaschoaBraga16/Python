print('Comparador de Numero 3000 by Leonardo Paschoa')
#var
num1 = float(input('Insira um numero: '))
num2 = float(input('Insira outro numero: '))

#cod
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 == num2:
    print('{} é igual a {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
print('Fim de execução')
