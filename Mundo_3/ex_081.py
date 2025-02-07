# Crie um programa que vai ler vários números e colocar em uma lista:
# [] Quantos números foram digitados.
# [] A lista de valores ordenada de forma decrescente.
# [] Se o valor 5 foi digitado e está na lista ou não.

lista = []
cont = 'S'
CincoPresente = []
posCinco = []


while cont not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]: '))


for pos, values in enumerate(lista):
    if values == 5:
        CincoPresente.append(values)
        posCinco.append(pos)




print(f'Os valores digitados foram: {lista}.')

print(f'\nForam digitados {len(lista)} números.'
f'\nValores em ordem crescente: {sorted(lista)}')

if 5 in lista:
    print(f'O valor 5 está presente.\nEle apareceu {len(CincoPresente)} vezes. Nas posições: ',end='')
    for cincos in posCinco:
        print(f'{cincos}...', end=' ')
else:
    print('O valor 5 não estava presente na lista.')

