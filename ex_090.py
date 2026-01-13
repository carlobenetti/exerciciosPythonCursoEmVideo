# Faça um programa que leia nome e média de um aluno.
# Guardando também a situação em um dicionário.
# No final mostre o conteúdo da estrutura na tela.


aluno = {}
turma = []


while True:
    # Alimentando as variáveis
    aluno['nome'] = str(input('Digi o nome: '))
    aluno['media'] = float(input('Digite a média: '))
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    if aluno['media'] < 7:
        aluno['situacao'] = 'reprovado'
    turma.append(aluno.copy())


    # Fim Loop
    continuar = str(input('Continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        break


for a in turma:
    for k, v in a.items():
        print(f'O {k} é {v}.')
    print()






