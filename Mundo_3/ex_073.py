# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,na ordem de colocação. Depois mostre:
# (X) Apenas os 5 primeiros colocados.
# () Os últimos 4 colocados.
# () Uma lista com os times em ordem alfabética.
# () Mostre a posição do Grêmio.


campeoes = ("Flamengo",    "Internacional",    "Atlético-MG",    "São Paulo",    "Fluminense",    "Grêmio",    "Palmeiras",    "Santos",    "Athletico-PR",    "Bragantino",    "Ceará",    "Corinthians",    "Atlético-GO",    "Bahia",    "Sport",    "Fortaleza",    "Vasco",    "Goiás",    "Coritiba",    "Botafogo",)

print(f'///////////// Os 5 primeiros campeões /////////////')
print('')

for i in range(0, 5):
    print(f'O {i+1} campeão foi {campeoes[i]}')

print('')
print('')
print(f'///////////// Os últimos 4 colocados foram /////////////')
print('')


# Pegando as últimas 5 posições e seus nomes:

for i in range(0, 5):
    ultimosColocados = campeoes[-i-1]
    posicao = campeoes.index(ultimosColocados)
    print(f'{ultimosColocados} ficou em {posicao + 1}° lugar')

