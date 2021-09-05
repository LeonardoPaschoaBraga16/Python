import datetime
velho = 0
novo = 0
ano = datetime.date.today().year


for rep in range (1, 8):
    nas = int(input(f'A data de nascimento da {rep}° pessoa é: '))
    dif = ano - nas
    if dif < 21:
        novo = novo + 1
    elif dif > 21:
        velho = velho + 1

print('')
print(f'{novo} pessoas não alcançaram a maioridade, {velho} alcançaram a maioridade ')