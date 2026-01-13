# Crie um programa que vai ler vários números e colocar em uma lista. Mostre: 
# [] Quantos números foram digitados.
# [] A lista de valores ordenada de forma decrescente.
# [] Se o valor 5 foi digitado e está ou não na lista

from random import randint

lista = []

for c in range(0, 5):
    lista.append(randint(0, 30))



print(lista)

