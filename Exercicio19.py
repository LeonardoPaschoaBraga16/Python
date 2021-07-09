import random

aluno1 = input('Insira o nome de um aluno: ')
aluno2 = input('Insira o nome de um aluno: ')
aluno3 = input('Insira o nome de um aluno: ')

alunos = [aluno1, aluno2, aluno3]

print('O aluno(a) sorteado foi {}'.format(random.choice(alunos)))

