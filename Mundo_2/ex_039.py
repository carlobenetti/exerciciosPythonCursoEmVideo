# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se ja passou do tempo do alistamento
# seu programa tambem devera mostrar o tempo que falta ou passou do prazo

from datetime import date
#Tabela de cores
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
fim_cor = '\033[m'

sexo = int(input(f'''Qual o seu genero?
Digite [0] para homem e [1] para mulher.
Escolha sua opção: '''))

if sexo == 1:
    print('Você não precisa se alistar, tenha um bom dia.')
elif sexo == 0:
    year_born = int(input('Digite o ano do seu nascimento: '))
    year_current = date.today().year
    age = year_current - year_born
    year_alistamento = year_born + 18
    print(f'Sua idade é de {age} anos.')
    print(f'O seu ano de alistamento é: {year_alistamento}')
    if age > 18:
        print(f'''{vermelho}Você já passou do tempo de se alistar.{fim_cor} 
        -> Você deveria ter se alistado a {year_current - year_alistamento} anos.''')
    elif age == 18:
        print(f'{amarelo}Está na hora de você se alistar.{fim_cor}')
    elif age < 18:
        print(f'''{verde}Você ainda ira se alistar no exercíto.{fim_cor}.
        ->Faltam {18 - age} anos para você se alistar no exército.''')

        