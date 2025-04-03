# Um programa que 
# [X] leia nome, ano de nascimento, e carteira de trabalho.
# [X] Cadastre-os (com idade) em um dicionário 
# [X] Se por acaso a CTPS for diferente de zero 
# [X] -> O dicionário receberá tambem o ano de contratação e o salário.
# [X] Calcule e acresente com a idade, com quantos anos a pessoa vai se aposentar.
# OBS: Aposentadoria apenas após 35 anos de contribuição.

from datetime import date
usuario = {} # Dados da pessoa
tabela_usuarios = []

while True:
    # Dados normais
    tabela_usuarios['nome'] = str(input('Digite o nome: '))
    tabela_usuarios['ano_nascimento'] = int(input('O ano de nascimento: '))
    tabela_usuarios['idade'] = date.today().year - tabela_usuarios['ano_nascimento']
    tabela_usuarios['carteira_trabalho'] = int(input('O número da carteira de trabalho (0 não tem): '))

    # Dados de trabalho
    if tabela_usuarios['carteira_trabalho'] != 0:
        tabela_usuarios['ano_contratação'] = int(input('Digite o ano de contratção: '))
        tabela_usuarios['ano_aposentadoria'] = (tabela_usuarios['ano_contratação'] - tabela_usuarios['ano_nascimento']) + 35
        tabela_usuarios['salario'] = float(input('O salário atual: '))
    else:
        tabela_usuarios['ano_contratação'] = 'nenhum'
        tabela_usuarios['salario'] = 0
        tabela_usuarios['ano_aposentadoria'] = 'nenhum'
        print('Usuário sem carteira ativa.')

    tabela_usuarios.append(tabela_usuarios.copy())    
    
    continuar = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
    if continuar in 'n':
        break



for l in tabela_usuarios:
    for k, v in l.items():
        print(f'{k}.......{v}')
    print()
















print(f'- Média de idade = {sum(i['idade'] for i in usuario)/len(usuario)}')
print()

print(f'- As mulheres cadastradas foram:')
for mulheres in usuario:
    if mulheres['sexo'] == 'F':
        print(mulheres['nome'] )

print()
print(f'- Pessoas a cima da média:')
for idade in usuario:
    if idade['idade'] > sum(i['idade'] for i in usuario)/len(usuario):
        for k, v in idade.items():
            print(f'{k} = {v};', end=' ')
        print()
print()

print('<< ENCERRADO >>')





