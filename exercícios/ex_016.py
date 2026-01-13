#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
v1 = float(input('Type a fractional number: '))
print(f'The whole portion is {trunc(v1)}')
