nome = str(input('Insira seu nome completo: ' )).strip()
div = nome.split()

print('O seu primeiro nome é {}'.format(div[0]))
print('O seu ultimo nome é {}'.format(div[len(div)-1]))
