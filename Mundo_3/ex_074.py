'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla
'''

from random import randint


tupla = []
counter = 0

while counter < 5:
    tupla.append(randint(0, 100))
    counter += 1

sortBiggest = sorted(tupla)

print(f'O maior é {sortBiggest[0]} e o menor é {sortBiggest[-1]}')




print(tupla)

