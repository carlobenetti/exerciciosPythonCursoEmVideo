# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados.
# E vai sortear 6 números entre 1 a 60 para cada jogo.
# Cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogosGerados = 0
continuar = 's'


jogosGerados = int(input('Quantos jogos você quer gerar? '))

for jogos in range(0, jogosGerados):
    valoresMegaSena = [randint(0, 61), randint(0, 61), randint(0, 61), randint(0, 61), randint(0, 61), randint(0, 61)]
    lista.append(valoresMegaSena)


contdr = 1
dormir = 1.5

for items in range(0, len(lista)):
    print(f'{contdr}o. ', end=' ')
    contdr += 1
    for subitems in range(0, 6):
        print(f'[{lista[items][subitems]:^10}]', end=' ')
    print()
    sleep(dormir)
    dormir = max(0.5, dormir * 0.8)

print()
print()
print(f'Lista composta = {lista}')

