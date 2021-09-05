print('Bem-Vindo a loja Casas Caralho')
print('')

#var
prc = float(input('Insira o preço da compra: R$'))
print('')

print('''Formas de pagamento:
[ 1 ] À vista 
[ 2 ] À vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')

#cod
opc = int(input('Qual será seu método de pagamento? '))
um = prc - ((prc * 10)/100)
dos = prc - ((prc * 5)/100)


#if
print('')

if opc == 1:
    print('A compra de R${} sairá por R${} com um desconto de 10%'.format(prc, um))
elif opc == 2:
    print('A compra de R${} sairá por R${} com um desconto de 5%'.format(prc, dos))
elif opc == 3:
    print('A compra sairá por R${} com duas parcelas de R${}'.format(prc, prc/2))
elif opc == 4:
    par = int(input('Quantas parcelas serão? '))
    print('')
    print('Sua compra de R${} sera parcelada em {} vezes, cada parcela sairá por R${:.2f} com juros. O preço final da compra será R${:.2f}'.format(prc, par, (prc/par) + (((prc/par) * 20)/100), par*((prc/par) + (((prc/par) * 20)/100))))
else:
    print('Tu é burro? só vai de 1 a 4 pô >:(')