# Um Programa que leia 5 valores e guardeos em uma lista.
# [] Mostrar qual foi o maior e menor valor junto a suas posições na lista.

from random import randint


lista = [0, 3, 2, 3]
maiorNumero = lista[0]
menorNumero = lista[0]
posMaior = []
posMenor = []


for maior in lista:
    if maior > maiorNumero:
        maiorNumero = maior
    
for menor in lista:
    if menor < menorNumero:
        menorNumero = menor



print(lista)

print(f'Menor número: {menorNumero}\nPosição na lista: ', end='')
# Pegando a posição do menor número de uma lista.
for pos, v in enumerate(lista):
    if v == menorNumero:
        print(f'{pos}', end='...')
        
print(f'\nMaior número: {maiorNumero}\nPosição na lista: ', end='')
# Pegando a posição do maior número de uma lista.
for pos, vMaiores in enumerate(lista):
    if vMaiores == maiorNumero:
        print(f'{pos}', end='...')



