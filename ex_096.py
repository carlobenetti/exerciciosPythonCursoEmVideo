"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""

def area(largura, comprimento):
    area = (largura*comprimento)/2

    print(f'A área do terreno é: {area}')


# Programa principal
largura = int(input('Digita a largura: '))
comprimento = int(input('Digite o comprimento: '))

area(largura, comprimento)





