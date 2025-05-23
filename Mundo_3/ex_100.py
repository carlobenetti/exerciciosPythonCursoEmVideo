# Um programa que tenha uma lista chamada números 
# e duas funções chamadas sorteia() e somaPar().
# A primeira função ira sortear 5 números e ira colocalos dentro da lista 
# e a segunda função ira mostrar a soma entre todos os valoes PARES
# Sorteados pela funcão anterior.

from random import randint
from time import sleep


# A primeira função ira sortear 5 números e ira colocalos dentro da lista 
def sorteando():
    for items in range(0, 5):
        novoItem = randint(0, 100)
        lista.append(novoItem)
        sleep(0.3)
        print(f'{novoItem}', end=' ', flush=True)
    print()
    print(f'Lista completa: {lista}')

# A segunda função ira mostrar a soma entre todos os valoes PARES

def somaPar(lista):
    print(f'Os valores pares são:')
    for i in lista:
        sleep(0.3) 
        print(f'{i}', end=' ', flush=True)



########## CODIGO REAL ############
lista = []
print(f'Sorteando')
sorteando()
somaPar(lista)



        