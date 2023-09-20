# Ler um número inteiro e printar se ele é par ou impar.
n = int(input(f'\033[1;33mDigite um número inteiro: \033[m '))
cor = "\033[1;34m"; corfim = "\033[m"

if (n%2) == 0:
    print(f'Seu número é {n}, ele é {cor}par{corfim}.')
else:
    print(f'Seu número é {n}, ele é {cor}impar{corfim}.')

    