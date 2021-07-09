func = str(input('Insira o nome do funcionário: '))
salario = float(input('Insira o salário atual do funcionário: '))
aumento = float(input('Insira o aumento para o funcionário: '))

print('O salario do funcionário {} com aumento de {}% é de R${:.2f}'.format(func, aumento, salario+((salario*aumento)/100)))
