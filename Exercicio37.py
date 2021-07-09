#Var
num = int(input('Digite um numero: '))

#code
choice = int(input('''Escolha um método de conversão: ')
[1] para Binário
[2] para Octal
[3] para Hexadecimal
 Insira: '''))

#metodos
tal = bin(num)
sus = oct(num)
mal = hex(num)

#if
if choice == 1:
    print('{} convertido para Binário é igual a {}'.format(num, tal[2:]))
elif choice == 2:
    print('{} convertido para Octal é igual a {}'.format(num, sus[2:]))
elif choice == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, mal[2:]))
elif choice != 1 or choice != 2 or choice != 3:
    print('Insira um numero entre 1 e 3, reinicie o programa!')

