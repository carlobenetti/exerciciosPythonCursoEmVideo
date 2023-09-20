# Leia três números, indique qual é o maior e qual é o menor.
amarelo = "\033[1;33m"; fim = "\033[m"

print(f'{amarelo} Digite 3 números: {fim} ')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

x = [n1, n2, n3]
x.sort()

print(f'O maior número é {amarelo}{x[-1]}{fim} \nO menor número é {amarelo}{x[0]}{fim}')

