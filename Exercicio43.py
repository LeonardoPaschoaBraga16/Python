print('Calculadora IMC')
print(' ')

#var
peso = float(input('Insira seu peso: '))
alt = float(input('Insira sua Altura: '))

#cod
imc = peso/(alt * alt)

print('')
print('O seu imc é {:.2f}'.format(imc))


#if
if imc < 18.5:
    print('Seu imc é: Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Seu imc é: Peso ideal')
elif imc > 25 and imc <= 30:
    print('Seu imc é: Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Seu imc é: Obesidade')
elif imc > 40:
    print('Seu imc é: Obesidade Mórbida')
