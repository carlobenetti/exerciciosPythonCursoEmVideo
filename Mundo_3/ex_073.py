# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,na ordem de colocação. Depois mostre:
# (X) Apenas os 5 primeiros colocados.
# (X) Os últimos 4 colocados.
# (X) Uma lista com os times em ordem alfabética.
# (X) Mostre a posição do Coritiba.


campeoes = ("Flamengo",    "Internacional",    "Atlético-MG",    "Grêmio",    "Fluminense",    "São Paulo",    "Palmeiras",    "Santos",    "Athletico-PR",    "Bragantino",    "Ceará",    "Corinthians",    "Atlético-GO",    "Bahia",    "Sport",    "Fortaleza",    "Vasco",    "Goiás",    "Coritiba",    "Botafogo",)

#Lista de times
print(' ')
print(campeoes)

#5 Primeiros times
print(' ')
print(f'Os 5 primeiros times são: {campeoes[0:5]}')


#4 ultimos colocados
print(' ')
print(f'OS últimos 4 times foram: {campeoes[-4:]}')

#Em ordem alfabética
print(f'Em ordem alfabética: {sorted(campeoes)}')

#Posição do Coritiba
print(f'O coritiba está na posição: {campeoes.index('Coritiba')-1}')


