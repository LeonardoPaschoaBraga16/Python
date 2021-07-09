frase = str(input('Insira a frase: ')).strip()
var = frase.upper()
print('A letra A nessa frase aparece {} vezes'.format(var.count('A',0,)))
print('A letra A nessa frase aparece primeiro em {}'.format(var.find('A')+1))
print('A letra A nessa frase aparece por ultimo em {}'.format(var.rfind('A')+1))

