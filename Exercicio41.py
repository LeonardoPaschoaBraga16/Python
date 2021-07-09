print('Classificador de atletas')
print(' ')

#mod
from datetime import date


#var
dat = int(input('Insira sua data de nascimento: '))

#cod
ida = date.today().year - dat


#if
if ida <= 9:
    print('Classificação: Mirim')
elif ida > 9 and ida <= 14:
    print('Classificação: Infantil')
elif ida > 14 and ida <= 19:
    print('Classificação: Junior')
elif ida > 19 and ida <= 25:
    print('Classificação: Sênior')
elif ida > 25:
    print('Classificação: Master')
