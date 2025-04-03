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
    usuario['nome'] = str(input('Digite o nome: '))
    usuario['ano_nascimento'] = int(input('O ano de nascimento: '))
    usuario['idade'] = date.today().year - usuario['ano_nascimento']
    usuario['carteira_trabalho'] = int(input('O número da carteira de trabalho (0 não tem): '))

    # Dados de trabalho
    if usuario['carteira_trabalho'] != 0:
        usuario['ano_contratação'] = int(input('Digite o ano de contratção: '))
        usuario['ano_aposentadoria'] = (usuario['ano_contratação'] - usuario['ano_nascimento']) + 35
        usuario['salario'] = float(input('O salário atual: '))
    else:
        usuario['ano_contratação'] = 'nenhum'
        usuario['salario'] = 0
        usuario['ano_aposentadoria'] = 'nenhum'
        print('Usuário sem carteira ativa.')

    tabela_usuarios.append(usuario.copy())    
    
    continuar = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
    if continuar in 'n':
        break



for l in tabela_usuarios:
    for k, v in l.items():
        print(f'{k}.......{v}')
    print()







