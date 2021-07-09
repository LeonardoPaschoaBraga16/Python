km = float(input('Insira quantos Km você deseja viajar: '))

if km <= 200:
    print('Você irá viajar {}Km e pagará R${}'.format(km,km * 0.50))
elif km >= 200:
    print('Você irá viajar {}Km porem pagará R${} apenas, graças a nossa promoção :D'.format(km,km * 0.45))
    print('Tenha um bom dia :D')
