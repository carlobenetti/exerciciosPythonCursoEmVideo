# Crie um programa que leie o nome e duas notas de vários alunos, guarde tudo em uma lista composta.
# [] Mostre um boletim contendo a média de cada um.
# [] Permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = [[['Carlo'], [4.5], [3.7]], [['Mario'], [4], [5.9]], [['Mario'], [2.5], [10]]]



counter = 0

print(f'No NOME    Nota1  Nota2   MÉDIA')
print('-'*30)
for pos, linhas in enumerate(range(0, len(boletim))):
    print(f'{pos} {boletim[linhas][0][0]:^8}  {boletim[linhas][1][0]:^4}  {boletim[linhas][2][0]:^4}    {boletim[linhas][1][0] + boletim[linhas][2][0]:^4}  ')
print()





