# c = (5, 2, 4, 9, 11, 6, 0, 1, 5, 6)
# """
# O index serve para encontrarmos a posição de algum elemento. O primeiro argumento representa o valor que desejo encontrar a posição. O segundo argumento serve para eu definir a partir de qual posição que quero começar a procurar pelo valor.
# No caso abaixo, eu desejo procurar a posição do segundo valor 5 na tupla. Assim eu peço para o computador procurar a partir do segundo elemento (1)
# """
# print(c.index(5, 1))

matriz = [[1,2,3], [4,5,6], [7,8,9]]



for i in range(0, 3):
    print(f'{matriz[i]}')

print()
print()
print()

for item in range(0, 3):
    for subitem in range(0, 3):
        print(f'{matriz[item][subitem]}', end=' ')
    print()

# [] O maior valor da segunda linha.
valoresSegundaLinha = []

for items in range(0, 3):
    valoresSegundaLinha.append(matriz[items][1])


print(f'Os valores da segunda linha são: {valoresSegundaLinha} e o maior valor é {max(valoresSegundaLinha)}')