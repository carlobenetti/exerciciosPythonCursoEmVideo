# Faça um programa que leia nome e média de um aluno, guardando também a situação em
# um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
situacao = []

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'em recuperação'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')










#for e in brasil:
 #   for k, v in e.items():
  #      print(f'{k} = {v}')
   #     print('-'*15)










