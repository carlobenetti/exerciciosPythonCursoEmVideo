# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
# feitos em cada partida. No final, tudo isso será guardado num dicionário, incluindo o
# total de gols feitos durante o campeonato.

jogador = {}
partidas = []


jogador['Nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))

for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-'*15)
print(jogador)
print('-=-'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*15)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f' - Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
