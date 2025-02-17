# Crie um programa que leie o nome e duas notas de vários alunos, guarde tudo em uma lista composta.
# [] Mostre um boletim contendo a média de cada um.
# [] Permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
continuar = 's'
counter = 0



# Cadastrando o boletim.
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


# print(boletim)


print()
print(f'No NOME    Nota1  Nota2   MÉDIA')
print('-'*30)
for pos, linhas in enumerate(range(0, len(boletim))):
    print(f'{pos} {boletim[linhas][0][0]:^8}  {boletim[linhas][1][0]:^4}  {boletim[linhas][2][0]:^4}    {boletim[linhas][1][0] + boletim[linhas][2][0]:^4}  ')
print()

continuar = 's'
exibirAluno = 'n'

while continuar != 'n':
    print()
    exibirAluno = str(input('Deseja exibir um aluno? [S/N]: ')).strip().lower()[0]
    if exibirAluno == 'n':
        print('Certo...')
    if exibirAluno == 's':
        # Perguntando e exibindo o aluno pedido.
        print()
        aluno = int(input('Qual aluno você deseja exibir? '))
        if aluno > len(boletim):
            print()
            print('Amigo, Não há tantos alunos assim. Tente novamente.')
        else:
            for  pos, linhas in enumerate(range(0, len(boletim))):
                if linhas == aluno:
                    print(f'{pos} {boletim[linhas][0][0]:^8}  {boletim[linhas][1][0]:^4}  {boletim[linhas][2][0]:^4}    {boletim[linhas][1][0] + boletim[linhas][2][0]:^4}  ')
            print()
    if exibirAluno not in 'ns':
        print()
        print('Desculpe, você não digitou sim ou não. Tente de novo.')
    print()
    continuar = str(input('\nDeseja continuar? [S/N]: ')).strip().lower()[0]
    
