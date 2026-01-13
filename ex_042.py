# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que triangulo de triângulo será formado:
# –EQUILÁTERO: todos os lados iguais  –ISÓSCELES: dois lados iguais, um diferente  –ESCALENO: todos os lados diferentes.
print('Olá, digite os três lados de um triângulo.')
n1 = float(input('Primeiro: '))
n2 = float(input('Segundo: '))
n3 = float(input('Terceiro: '))

if n1 + n2 >= n3 and n1 + n3 >= n2 and n2 + n3 >= n1:
    print(f'Os lados {n1, n2, n3} formam um triângulo ', end='')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não é um triângulo, tente outra vez.')

    