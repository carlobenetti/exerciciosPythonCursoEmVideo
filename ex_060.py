#Faça um programa que leia um numero qualquer e mostre seu fatorial.
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
from math import factorial


num = int(input('Digite um número inteiro: '))
c = num
fatorial = 1 # 1 é o fator nulo da multiplicação/divivsão e 0 o fator nulo da soma/subtração

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else f' = ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}.')


