print('Alistamento militar')

#mod
from datetime import date

#var
ida = int(input('Insira o ano em que nasceu: '))
cal = date.today().year - ida
dif = cal - 18

#cod
print('Quem nasceu em {} tem {} anos em {}'.format(ida, cal, date.today().year))

#if
if cal < 18:
    print('faltam {} anos para seu alistamento no exercito, que será em {}'.format(dif, (date.today().year + dif)))
elif cal == 18:
    print('Você tem {} anos de idade, deve-se alistar imediatamente!!'.format(cal))
elif cal > 18:
    print('Você não pode mais de alistar, seu alistamento deveria ter sido em {}'.format(date.today().year - dif))
