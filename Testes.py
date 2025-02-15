# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados.
# E vai sortear 6 números entre 1 a 60 para cada jogo.
# Cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

valor = 0
numeros = []
valoresMegaSena = []
lista = []
jogosGerados = 0
continuar = 's'

# Gerando os valores
jogosGerados = int(input('Quantos jogos você quer gerar? '))
for jogos in range(0, jogosGerados):
    for nums in range(0, 6):
        valor = randint(0, 61)
        if valor not in numeros:
            valoresMegaSena.append(valor) #[][]
    lista.append(sorted(valoresMegaSena[:])) #[]
    valoresMegaSena.clear()

contdr = 1
dormir = 1.5

# Imprimindo a lista
for items in range(0, len(lista)):
    print(f'{contdr}o. ', end=' ')
    contdr += 1
    for subitems in range(0, 6):
        print(f'[{lista[items][subitems]:^10}]', end=' ')
    print()
    sleep(dormir)
    dormir = max(0.3, dormir * 0.8)

print()
print()
print(f'Lista composta = {lista}')

