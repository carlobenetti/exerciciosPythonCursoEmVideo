# Um programa que tenha uma lista chamada números 
# e duas funções chamadas sorteia() e somaPar().
# A primeira função ira sortear 5 números e ira colocalos dentro da lista 
# e a segunda função ira mostrar a soma entre todos os valoes PARES
# Sorteados pela funcão anterior.

from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        sleep(0.25)
        print(f'{num}', end=' ', flush=True)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            print(f'{valor}')
        elif valor % 2 == 1:
            print(f'{valor} É impar')
    # print(f'Somando os valores pares de {lista}, temos {soma}')

    
# Código principal
numeros = []
sorteia(numeros)
print()
print(numeros)
somaPar(numeros)
