som = 0
maior = 0
menor = 0
idah = 0
mrd = 0
old = ''

for tab in range (1,5):
    print(5*'='+ f'{tab}° Pessoa'+ 5*'=')
    nom = str(input(f'Insira o nome da {tab}° pessoa: ')).strip()
    ida = int(input(f'Insira a idade da {tab}° pessoa: '))
    som = som + ida
    sex = str(input(f'Insira o sexo da {tab}° pessoa [M/F]: ')).strip()
    if sex == 'M':
        idah = ida
    if sex == 'F' and ida < 20:
        mrd = mrd + 1
    print('')
    if tab == 1:
        maior = idah
        old = nom
    else:
        if idah > maior:
            maior = idah
            old = nom



med = som / 4
print(f'A média de idade é {med}')
print(f'O nome do homem mais velho é {old}')
print(f'O numero de mulheres menores de 20 anos é {mrd}')

