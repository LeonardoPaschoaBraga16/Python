#variaveis
casa = int(input('Insira o valor da casa: R$'))
sal = int(input('Insira o seu Salário: R$'))
fin = int(input('Insira o tempo de financiamento: '))

#cod-var
prec = float(casa/(fin*12))
por = ((sal*30)/100)

#código
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa, fin, prec))

if prec > por:
    print('O empréstimo não poderá ser efetuado, pois o preço do financiamento é maior que 30% do seu salário')
elif prec <= por:
    print('O emprestimo poderá ser efetuado com sucesso, pois o preço do financiamento é menor que 30% do seu salário')