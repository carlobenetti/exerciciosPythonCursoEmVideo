# Aprimore o desafio 93 para que ele funcione com vários jogadores.
# Incluindo um sistema de vizualização de detalher de aproveitamento de cada jogador.


jogador = {}
tabela_jogadores = []


while True:
    # Formando um jogador
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas_jogadas = int(input('Quantas partidas ele jogou? '))

    jogador['gols'] = []
    for i in range(0, partidas_jogadas):
        jogador['gols'].append(int(input(f'Quantos gols na {i+1} partida? ')))

    jogador['total'] = sum(jogador['gols'])

    tabela_jogadores.append(jogador.copy())
    
    
    
    continuar = str(input('Quer continuar? ')).strip().lower()[0]
    if continuar in 'n':
        break

print(f'ID  Nome  gols  total')
c = 0
for l in tabela_jogadores:
    c += 1
    print(f'{c}', end='..')
    print(f'{l['nome']}', end='..')
    print(f'{l['gols']}', end='..')
    print(f'{l['total']}', end='..')
    print()
print()
print(tabela_jogadores)

print()
for vr in range(0, len(tabela_jogadores)): 
    print(vr, end='? ')
ver = str(input('Deseja ver um jogador em específico? [s/n] ')).strip().lower()[0]
while True:
    if ver in 's':
        print()

        ver_jogador = int(input(f'ID do jogador escolhido: '))
        print(tabela_jogadores[ver_jogador])

        for vr in range(0, len(tabela_jogadores)): 
            print(vr, end='? ')
        
        print()
        ver = str(input('Deseja ver mais algum jogador em específico? [s/n] ')).strip().lower()[0]
    if ver in 'n':
        break


for vr in range(0, len(tabela_jogadores)): 
    print(vr, end='? ')
print()
ver = str(input('Tem certeza que não deseja ver um jogador em específico? [s/n] ')).strip().lower()[0]

if ver in 'n':
    print()

    ver_jogador = int(input(f'ID do jogador escolhido: '))
    print(tabela_jogadores[ver_jogador])

    for vr in range(0, len(tabela_jogadores)): 
        print(vr, end='? ')
    print()
    ver = str(input('Deseja ver mais algum jogador em específico? [s/n] ')).strip().lower()[0]

print('#### FIM DO PROGRAMA ###')











