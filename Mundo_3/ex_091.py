# Um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem de vitória (sabendo que o vencedor tirou o maior número no dado).


from random import randint

tabela = []

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



# Resultado
for val in tabela:
    for k, v in jogadores.items():
        print(k, v)



