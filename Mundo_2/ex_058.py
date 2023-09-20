#Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para
# vencer.
print(f"""{35*'-=-'}
                                    Jogo da adivinhação
{35*'-=-'}""")


from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Tente adivivnhar um número de 0 a 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador != computador:
        if computador < jogador:
            print(f'Huumm... Tente outra vez. Talvez com um número menor.')
        elif computador > jogador:
            print(f'Huumm... Tente outra vez. Talvez com um número maior.')
print(f'Você acertou!!!. Foram {palpites} palpites.')