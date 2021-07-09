num = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
num3 = float(input('Insira o terceiro valor: '))

if num < num2 + num3 and num2 < num + num3 and num3 < num2 + num3:
    print('Com as medidas acima pode-se criar um triangulo')
else:
    print('Não se pode criar um triangulo com as medidas acima')

