#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar  [ 2 ] Multiplicar  [ 3 ] Maior  [ 4 ] Novos numeros  [ 5 ] Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
cor_fim = '\033[m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'
preto = '\033[1;30m'

valor_01 = int(input('Digite um valor: '))
valor_02 = int(input('Digite outro valor: '))
l = [valor_01, valor_02]

var = int(input(f""" Olá, escolha o que deseja fazer
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa
Digite sua escolha: """))
print(f"""Valores escolhidos:
valor 1 = {preto}{valor_01}{cor_fim} e valor 2 = {preto}{valor_02}{cor_fim}
""")

c = 0
while c != 5:
    if var == 1: # [ 1 ] Somar
        print(f'A soma de {valor_01} + {valor_02} é {valor_01 + valor_02}')
        break
    elif var == 2: # [ 2 ] Multiplicar
        print(f'{verde}A multiplicação de {vermelho}{valor_01} x {valor_02}\033[m é {amarelo}{valor_01 * valor_02}{cor_fim}')
        break
    elif var == 3: # [ 3 ] Maior
        if valor_01 > valor_02:
            print(f'O maior número é: {valor_01}')
        elif valor_02 > valor_01:
            print(f'O maior número é: {valor_02}')
        break
    elif var == 4: # [ 4 ] Novos numeros
        valor_01 = int(input('Digite um valor: '))
        valor_02 = int(input('Digite outro valor: '))
        l = [valor_01, valor_02]
    else:
        break
print('Fim do programa')