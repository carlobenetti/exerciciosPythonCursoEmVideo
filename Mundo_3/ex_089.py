# Crie um programa que leie o nome e duas notas de vários alunos, guarde tudo em uma lista composta.
# [] Mostre um boletim contendo a média de cada um.
# [] Permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
continuar = 's'

while continuar != 'n':
    # Cadastrando os valores e limpando a lista
    aluno = [[], [], []]
    aluno[0].append(str(input('Digite o nome do aluno: ')))
    aluno[1].append(float(input('Digite sua primeira nota: ')))
    aluno[2].append(float(input('Digite sua segunda nota: ')))
    boletim.append(aluno[:])
    aluno.clear()
    
    # Continuar o loop?
    continuar = str(input(f'Quer continuar? [S/N]: ')).strip().lower()[0]










# MOSTRANDO O BOLETIM
print('\n    MOSTRANDO O BOLETIM    ')
for items in range(0, len(boletim)):
    for subitems in range(0, 3):
        for nivel1 in range(0, 3):
            print(f'{boletim[items][subitems][nivel1]}', end='')
        print()
    print()



print('\n    BOLETIM CRU    ')
print(boletim)

