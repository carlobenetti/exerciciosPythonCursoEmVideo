# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
x1 = str(input('First student: '))
x2 = str(input('Second student: '))
x3 = str(input('Third student: '))
x4 = str(input('Fourth student: '))
lista = [x1, x2, x3, x4]
random.shuffle(lista)
print(f'Follow the order: {lista}')
