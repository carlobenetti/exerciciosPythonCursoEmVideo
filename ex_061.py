#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#  usando a estrutura while.
num = int(input('Digite um número: '))
cont = 1
razao = int(input('Digite a razão: '))
termo = num
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')