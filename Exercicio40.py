print('Calculadora de média')
print('')

#var
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

#cod
med = (n1 + n2)/2

print('A média do aluno é {}'.format(med))
#if
if med < 5:
    print('A média do aluno(a) é menor que 5, logo, está REPROVADO')
elif med >= 5 and med <= 6.9:
    print('A média do aluno(a) é maior que 5 e menor que 6.9, logo, está de RECUPERAÇÃO')
elif med > 7:
    print('A média do aluno(a) é maior que 7, logo está Aprovado ;D')