#Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele diser que quer mostrar 0 termos.

num = int(input('Digite um número: '))
cont = 1
razao = int(input('Digite a razão: '))
termo = num
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print(f'Progressão finalziada com {total} termos mostrados.')

