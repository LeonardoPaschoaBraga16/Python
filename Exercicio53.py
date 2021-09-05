frs = str(input('Insira uma frase: ')).strip()
inv = frs[::-1]
jnt1 = ''.join(frs.split())
jnt2 = ''.join(inv.split())

print(f'A frase {jnt1.upper()} ao contrário é {jnt2.upper()}')

if jnt1 == jnt2:
    print(f'A frase \'{frs}\' É um Palindromo')
else:
    print(f'A frase \'{frs}\' NÃO É um Palindromo')