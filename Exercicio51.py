#var
ini = float(input('Insira um termo: '))
prog = float(input('Insira uma razão: '))
cont = ini + prog

for pa in range(0,10 ):
    print(' {} =>'.format(ini), end=' ')
    ini = ini + prog

print('Fim do Programa')
