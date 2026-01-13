# Um Programa que leia 5 valores e guardeos em uma lista.
# [] Mostrar qual foi o maior e menor valor junto a suas posições na lista.

listanum = []
mai = 0
men = 0
posMaior = []
posMenor = []



for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
        





print('=-=' * 30)
print(f'Você digitou os valores: {listanum}')



for pos, i in enumerate(listanum):
    if i == mai:
        posMaior.append(pos)
    if i == men:
        posMenor.append(pos)


print(f'O maior valor foi {mai}, na posição: ', end='')
print(f'{posMaior}')
print(f'O menor valor foi {men}, na posição: ', end='')
print(f'{posMenor}')



