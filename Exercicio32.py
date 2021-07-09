from datetime import date

ano = int(input('Insira um ano especifico, digite 0 para usar o ano atual: '))

if ano == 0:
    ano = date.today().year

var = ano / 4
int = var % 2

if int == 0:
    print('É um ano bissexto!!')
else:
    print('Não é um ano bissexto!!')
