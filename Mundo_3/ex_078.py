# Faça um programa que leia 5 valores e guarde-os em uma lista.
# No final mostre qual foi o maior e o menor valor e suas respectivas
# posições na lista.

# Variáveis
maximo = 0
minimo = 0
lista_valores = []

for c in range(0, 5):
    lista_valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maximo = minimo = lista_valores[c]
    else:
        if lista_valores[c] > maximo:
            maximo = lista_valores[c]
        if lista_valores[c] < minimo:
            minimo = lista_valores[c]


print(f'\n{"-"*30}')
print(f'Os valores são: {lista_valores}.')
print(f'O valor máximo é {maximo} na posição: ', end='')
for i, v in enumerate(lista_valores):
    if v == maximo:
        print(f'{i}...', end='')
print()
print(f'O valor minimo é {minimo} na posição ', end='')
for i, v in enumerate(lista_valores):
    if v == minimo:
        print(f'{i}...', end='')
print()

