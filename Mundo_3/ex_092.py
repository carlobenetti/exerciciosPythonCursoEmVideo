# Um programa que 
# [X] leia nome, ano de nascimento, e carteira de trabalho.
# [ ] Cadastre-os (com idade) em um dicionário 
# Se por acaso a CTPS for diferente de zero 
#   -> O dicionário receberá tambem o ano de contratação e o salário.
# Calcule e acresente com a idade, com quantos anos a pessoa vai se aposentar.
# OBS: Aposentadoria apenas após 35 anos de contribuição.

from datetime import date
usuario = {} # Dados da pessoa





# usuario['nome'] = str(input('Digite o nome: '))
usuario['ano_nascimento'] = int(input('O ano de nascimento: '))
usuario['idade'] = date.today().year - usuario['ano_nascimento']
# usuario['carteira_trabalho'] = int(input('O número da carteira de trabalho (0 não tem): '))
# usuario['ano_contratação'] = int(input('O ano de contratação: '))
# usuario['salario'] = float(input('Digite o salário: '))


print(usuario['idade'])











