produto = str(input('Insira o nome do produto: '))
preco = float(input('Insira o preço atual do produto: '))
desconto = float(input('Insira o desconto para o produto: '))

print('O preço do produto {} com desconto de {}% é de R${}'.format(produto, desconto, preco-((preco*desconto)/100)))

