# Um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep


def maior(rangeNum, rangeLista):
    maior = 0
    menor = 0
    lista = []
    
    for i in range(0, rangeLista):
        valorInteiro = randint(0, rangeNum)
        sleep(0.4)
        print(valorInteiro, end=' ', flush=True)
    print()
    
    for items in lista:
        if items > maior:
            maior = items
        elif items < menor:
                menor = items
        else:
            pass
    
    print(f'O maior: {maior} \nO   menor: {menor}')
    
# maior(--número máximo aleatório--, --tamanho da lista--)
maior(11, 10)
