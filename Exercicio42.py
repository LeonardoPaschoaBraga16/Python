print('Analizador de triangulos 2.0')
print(' ')

#var
num = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
num3 = float(input('Insira o terceiro valor: '))

#if
if num == num2 == num3:
    print('Com as medidas acima pode-se criar um triangulo Equilátero')
elif num == num2 != num3 or num == num3 != num2 or num2 == num3 != num and num < num2 + num3 and num2 < num + num3 and num3 < num2 + num3:
    print('Com as medidas acima pode-se criar um triangulo Isóceles')
elif num != num2 != num3 and num < num2 + num3 and num2 < num + num3 and num3 < num2 + num3:
    print('Com as medidas acima pode-se criar um triangulo Escaleno')
else:
    print('Não se pode criar um triangulo com as medidas acima')



