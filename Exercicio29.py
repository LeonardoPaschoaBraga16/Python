vel = float(input('Qual é a velocidade atual do carro? '))

if vel <= 80:
    print('Interessante amigo, tenha um bom dia :D')
else:
    print('Limite de velocidade de 80Km/h excedido, vai pagar uma multa de R${} vagabundo >:('.format((vel - 80) * 7))
