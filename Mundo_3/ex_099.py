# Um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep


def maior(rangeNum, rangeLista):
    maior = 0
    menor = 0
    lista = []
    
    # Embelezamento
    print(f'{12*'-=-'}')
    
    # Analisando os valores passados
    print('Analisando os valores passados')    
    
    # Resultado da lista de números aleatórios
    for i in range(0, rangeLista):
        valorInteiro = randint(0, rangeNum)
        lista.append(valorInteiro)
        sleep(0.4)
        print(valorInteiro, end=' ', flush=True)
    print()
    
    # Mostrando a lista
    print()
    print(f'Ou seja: {lista}')
    
    count = 0
    
    if count == 0:
        for items in lista:
            if items > maior:
                menor = maior = items
    
    count += 1
    
    for items in lista:
        if items < menor:
            menor = items

    
        
    # Resultado maior e menor valor
    print(f'O maior: {maior} \nO menor: {menor}')

    # Embelezamento
    print(f'{12*'-=-'}')
    
    
    
    
    
    
    
    
# maior(--número máximo aleatório--, --tamanho da lista--)
maior(11, 10)
maior(100, 20)



