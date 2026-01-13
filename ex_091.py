# Um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem de vitória (sabendo que o vencedor tirou o maior número no dado).

from random import randint
from time import sleep
from operator import itemgetter


jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}

ranking = []

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)


print()
print('Ranking: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)


for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]}.')
    sleep(1)
































# Código antigo
""" 
from random import randint
from time import sleep

################## Tabela Cores ####################
cor_fim = '\033[m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'

preto = '\033[1;30m'
azul = '\033[1;34m'
magenta = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'
branco = '\033[1;97m'






################## Começo do cógido ####################
tabela = []

print(f'{amarelo}Valores Sorteados:{cor_fim} ')

# Inserindo os valores
jogadores = {
    'jogador1': randint(0, 4)
}


jogadores['jogador2'] = randint(0, 4)
while jogadores['jogador2'] == jogadores['jogador1']:
    jogadores['jogador2'] = randint(0, 4)

jogadores['jogador3'] = randint(0, 4)
while jogadores['jogador3'] == jogadores['jogador1'] or jogadores['jogador3'] == jogadores['jogador2']:
    jogadores['jogador3'] = randint(0, 4)

jogadores['jogador4'] = randint(0, 4)
while jogadores['jogador4'] == jogadores['jogador1'] or jogadores['jogador4'] == jogadores['jogador2'] or jogadores['jogador4'] == jogadores['jogador3']:
    jogadores['jogador4'] = randint(0, 4)


tabela.append(jogadores.copy())


# Imprimindo o resultado do sorteio de cada jogador.
for l in tabela:
    for k, v in jogadores.items():
        print(f'O jogador {k} tirou {v}')
        sleep(0.5)


# Colocar os números em ordem alfabética

# Posicionando o jogador 1.
if jogadores['jogador1'] < jogadores['jogador2']:
    jogadores['jogador1'], jogadores['jogador2'] = jogadores['jogador2'], jogadores['jogador1']
if jogadores['jogador1'] < jogadores['jogador3']:
    jogadores['jogador1'], jogadores['jogador3'] = jogadores['jogador3'], jogadores['jogador1']
if jogadores['jogador1'] < jogadores['jogador4']:
    jogadores['jogador1'], jogadores['jogador4'] = jogadores['jogador4'], jogadores['jogador1']

# Posicionando o jogador 2.
if jogadores['jogador2'] < jogadores['jogador3']:
    jogadores['jogador2'], jogadores['jogador3'] = jogadores['jogador3'], jogadores['jogador2']
if jogadores['jogador2'] < jogadores['jogador4']:
    jogadores['jogador2'], jogadores['jogador4'] = jogadores['jogador4'], jogadores['jogador2']

# Posicionando o jogador 2.
if jogadores['jogador3'] < jogadores['jogador4']:
    jogadores['jogador3'], jogadores['jogador4'] = jogadores['jogador4'], jogadores['jogador3']



# Resultado
print()
print(f'{verde}Resultado final:{cor_fim} ')
c = 0
for val in tabela:
    for k, v in jogadores.items():
        c += 1
        print(f'{c}o lugar: {k} com {v} pontos. ')

 """






































