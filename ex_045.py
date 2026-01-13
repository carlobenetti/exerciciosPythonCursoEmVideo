# 0 - Pedra, 1 - Papel, 2 - Tesoura
# Faça um algoritimo que jogue joquempo
from time import sleep
from random import randint

cor_fim = '\033[m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

desafio = int(input(f"""{amarelo}Eu te desafio a um jogo de Jo-ken-po, forasteiro. Você aceita?{cor_fim}
[0] Aceito!!! - [1] Não aceito, sou cagão.
Faça sua escolhe: """))
resultado = str()

if desafio == 0:
    print(f"""{amarelo}Escolha sua melhor mão, seu doente!!!{cor_fim}
[0] Pedra - [1] Papel - [2] Tesoura.""")
    player = int(input('Digite sua opção: '))
    print(f'{amarelo}Ok, lá vamos nós!!!...{cor_fim}'); sleep(1); print('Jo...'); sleep(1); print('Ken...'); sleep(1);
    print('Po!!!'); sleep(1)
    if player != 0 and player != 1 and player != 2:
        print('Acho que não entendi, seu babaca. Vou repetir.')
    elif computador == 0:  # Pedra
        if player == 1:
            resultado = 'Vitória'
        if player == 2:
            resultado = 'Perdeu'
        elif player == 0:
            resultado = 'Empate'
    elif computador == 1:  # Papel
        if player == 0:
            resultado = 'Perdeu'
        if player == 2:
            resultado = 'Vitória'
        elif player == 1:
            resultado = 'Empate'
    elif computador == 2:  # Tesoura
        if player == 0:
            resultado = 'Vitória'
        if player == 1:
            resultado = 'Perdeu'
        elif player == 2:
            resultado = 'Empate'
        else:
            print(resultado)
    print(f'O jogador usou {itens[player]}. O computador usou {itens[computador]}. \nO resultado é: {resultado}')
    if resultado == 'Vitória':
        print(f'{verde}Não é que esse bostinha tem capacidade. Mas e o bambu?{cor_fim}')
    elif resultado == 'Perdeu':
        print(f'{vermelho}KKKKKKKK seu troxa!!!{cor_fim}')
    elif resultado == 'Empate':
        print(f'{vermelho}Foda-se?{cor_fim}')
if desafio == 1:
    print(f'{amarelo}Você é o bunda mole que eu esperava, parábens.{cor_fim} {vermelho}(¬_¬){cor_fim}')