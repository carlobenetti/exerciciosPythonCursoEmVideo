# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois, ler a quantidade de gols feitos em cada partida.
# Salvar tudo isso em um dicionário, junto ao total de gols feitos no campeonato inteiro.




jogador = {}

jogador['nome'] = str(input('Digite o nome do jogador: '))

partidas_jogadas = int(input('Quantas partidas ele jogou? '))

jogador['gols'] = []

for i in range(0, partidas_jogadas):
    jogador['gols'].append(int(input(f'Quantos gols na {i+1} partida? ')))

jogador['total'] = sum(jogador['gols'])

# Detalhe dos dados obtidos
print()
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')    



# Gol em cada partida
print()
for p, v in enumerate(jogador['gols']):
    print(f'Na partida {p}, fez {v} gols.')

print()
print(f'Foram {jogador['total']} gols no total.')











