maior = 0
menor = 0

for pso in range (1, 6):
    peso = float(input(f'Insira o peso da {pso}° pessoa: '))
    if pso == 1:
      menor = peso
      maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('')
print(f'O menor peso foi de Kg {menor}')
print('')
print(f'O maior peso foi de Kg {maior}')