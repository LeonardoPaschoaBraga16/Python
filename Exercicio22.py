nome = str(input('Insira seu nome: ')).strip()

print('Analisando seu nome...')

print('O seu nome em maiusculas é {}'.format(nome.upper()))

print('O seu nome em minusculas é {}'.format(nome.lower()))

print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

dividido = nome.split()

print('O seu primeiro é {} nome tem {}'.format(dividido[0],len(dividido[0])))



