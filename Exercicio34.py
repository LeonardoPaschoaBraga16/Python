salario = float(input('Insira seu salário: '))



if salario > 1250.00:
    print('O salário que era de {} passará a ser de {}'.format(salario,salario + ((salario * 10) / 100)))
elif salario < 1250.00:
    print('O salário que era de {} passará a ser de {}'.format(salario, salario + ((salario * 15) / 100)))
