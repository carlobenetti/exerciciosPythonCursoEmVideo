# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados.
# E vai sortear 6 números entre 1 a 60 para cada jogo.
# Cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

from random import randint
from time import sleep


cont = 0
lista = []
tot = 1
jogos = []

print('-=-'*30)
print('     JOGANDO NA MEGASENA    ')
print('-=-'*30)

quantJogos = int(input('Quantos jogos você quer jogar? '))

while tot <= quantJogos:
    cont=0

    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'Os numeros sorteados foram {jogos}')


print('-=-'*3, f'Sorteando {quantJogos} jogos.', '-=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.8)

print('-=-'*5, 'Boa sorte', '-=-'*5)

