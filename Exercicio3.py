x1 = input('Digite algo: ')

print('O tipo primitivo do objeto é: {},'.format(type(x1)) )
print('O Objeto é numérico? {}. O objeto é um texto? {}. O Objeto é um texto numérico? {}. O objeto está maiusculo? {}. O objeto está minusculo? {}.'.format(x1.isnumeric(), x1.isalpha(), x1.isalnum(), x1.isupper(), x1.islower()))
