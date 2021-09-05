import random
#var
choice = ['Pedra','Papel','Tesoura','......ESCOPETA']
choimaq = random.choice(choice)

print('{:=^40}'.format(' Pedra, Papel ou Tesoura '))
print('')

inp = int(input('''Escolha sua jogada entre: 
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] ???
Escolha: '''))

print('')

print('A maquina escolheu {}'.format(choimaq))

print('')

if inp == 1:
    print('Você escolheu Pedra')
    print('')
    if inp == 1 and choimaq == 'Tesoura':
        print('Você ganhou da maquina, parabéns misero humano >:(')
    elif inp == 1 and choimaq == 'Papel':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')
    elif inp == 1 and choimaq == 'Pedra':
        print('Patético, deu em empate, eu queria ver alguem perdendo ;-;')
    elif inp == 1 and choimaq == '......ESCOPETA':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')

elif inp == 2:
    print('Você escolheu Papel')
    print('')
    if inp == 2 and choimaq == 'Pedra':
        print('Você ganhou da maquina, parabens misero humano >:(')
    elif inp == 2 and choimaq == 'Tesoura':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')
    elif inp == 2 and choimaq == 'Papel':
        print('Patético, deu em empate, eu queria ver alguem perdendo ;-;')
    elif inp == 2 and choimaq == '......ESCOPETA':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')

elif inp == 3:
    print('Você escolheu Tesoura')
    print('')
    if inp == 3 and choimaq == 'Papel':
        print('Você ganhou da maquina, parabens misero humano >:(')
    elif inp == 3 and choimaq == 'Pedra':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')
    elif inp == 3 and choimaq == 'Tesoura':
        print('Patético, deu em empate, eu queria ver alguem perdendo ;-;')
    elif inp == 3 and choimaq == '......ESCOPETA':
        print('Você perdeu pra maquina KAKAAKAKAAK, não aguenta partida com o robô né? KSKKSKSSK')

elif inp == 4:
    print('Você escolheu..... ESCOPETA!')
    print('')
    if inp == 4 and choimaq == 'Pedra' or choimaq == 'Papel' or choimaq == 'Tesoura':
        print('Você ganhou da maquina, parabens misero humano >:(')
    elif inp == 4 and choimaq == '......ESCOPETA':
        print('Você dois começaram a se atirar e mataram o programa no processo X( , reinicie o programa!')
else:
    print('Você escolheu.... O inexistente. Tu é burro(a)? só vai de 1 a 4, reinicie o programa!')











