dia = int(input('Por quantos dias o carro foi usado: '))
km = float(input('Por quantos Km o carro  foi usado: '))

print('O preço a pagar é de: R${:.2f}'.format((dia*60)+(km*0.15)))

