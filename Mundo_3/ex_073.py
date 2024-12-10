# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,na ordem de colocação. Depois mostre:
# (X) Apenas os 5 primeiros colocados.
# (X) Os últimos 4 colocados.
# () Uma lista com os times em ordem alfabética.
# () Mostre a posição do Grêmio.


campeoes = ("Flamengo",    "Internacional",    "Atlético-MG",    "Grêmio",    "Fluminense",    "São Paulo",    "Palmeiras",    "Santos",    "Athletico-PR",    "Bragantino",    "Ceará",    "Corinthians",    "Atlético-GO",    "Bahia",    "Sport",    "Fortaleza",    "Vasco",    "Goiás",    "Coritiba",    "Botafogo",)

print(f'///////////// Os 5 primeiros campeões /////////////')
for i in range(0, 5):
    print(f'O {i+1} campeão foi {campeoes[i]}')

print('')
print('')
print(f'///////////// Os últimos 4 colocados foram /////////////')


# Pegando as últimas 5 posições e seus nomes:
for i in range(0, 5):
    ultimosColocados = campeoes[-i-1]
    posicao = campeoes.index(ultimosColocados)
    print(f'{ultimosColocados} ficou em {posicao + 1}° lugar')




# Exibindo a tupla em ordem alfabética.
print('')
print('')
print(f'///////////// Colocados em ordem alfabética /////////////')
ordemAlfabetica = sorted(campeoes)
for x in range(len(campeoes)):
    if x < len(campeoes) - 1:
        print(campeoes[x], end='; ')
    else:
        print(campeoes[x], end='.')
        
        




# Exibindo a posição do Coritiba.
print('')
print('')
print(f'///////////// Posição do Coritiba/////////////')
for i in campeoes:
    if i == 'Coritiba':
        posicao_coritiba = campeoes.index(i)
        print(f'O Coritiba ficou em {posicao_coritiba - 1}° lugar.')    
    
    