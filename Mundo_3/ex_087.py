# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela com a formatação correta. 

# Aprimore o desafio anterior. Mostrando:
# [] A soma de todos os valores pares digitados.
# [] A soma dos valores da terceira coluna.
# [] O maior valor da segunda linha.



matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha} em {coluna}: '))


# Matriz original
print()
print('----------> Matriz crua')
print(matriz)

# Matriz normal
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()


# [] A soma de todos os valores pares digitados.
print()
valPares = []

for item in range(0, 3):
    for subitem in range(0, 3):
        if matriz[item][subitem] % 2 == 0:
            valPares.append(matriz[item][subitem])

if len(valPares) == 0:
    print('Não há valores pares.')
else:
    print(f'Os valors pares são: {valPares} = {sum(valPares)}')


# [] A soma dos valores da terceira coluna.
valTerceiraColuna = []

for blocoUm in range(0, 3):
    valTerceiraColuna.append(matriz[blocoUm][2])

print(f'Os valores da terceira coluna são: {valTerceiraColuna} = {sum(valTerceiraColuna)}')


# [] O maior valor da segunda linha.
valoresSegundaLinha = []

for items in range(0, 3):
    valoresSegundaLinha.append(matriz[items][1])


print(f'Os valores da segunda linha são: {valoresSegundaLinha} e o maior valor é {max(valoresSegundaLinha)}')

























