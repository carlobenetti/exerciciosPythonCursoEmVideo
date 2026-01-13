# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
first = str(input('First student name: '))
second = str(input('Second student name: '))
third = str(input('Third student name: '))
fourth = str(input('Fourth student name: '))
lista = [first, second, third, fourth]
print(f'The choose student is {random.choice(lista)}')
