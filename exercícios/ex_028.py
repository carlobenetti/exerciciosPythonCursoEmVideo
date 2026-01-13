# Faça o computador pensar em um nº inteiro de 0 a 5, peça para o usuário descobrir o nº, printe se acertou ou não.
from random import randint

computador = randint(0,5) # O computador "pensa" em um número de 0 a 5
jogador = int(input('Descubra qual número de 0 a 5 estou pensando: ')) # O jogador digita um núemro a ser adivinhado

if computador == jogador:
    print(f'Você vencêu, o número é {computador}')
else:
    print(f'Você perdeu, o número é {computador}. \nTente outra vez')
print('Até mais :)')