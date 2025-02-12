# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
# [] Mostre quantas pessoas foram cadastradas.
# [] Uma listagem com as pessoas mais pesadas.
# [] Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0



while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])

    if len(princ) == 1:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

    temp.clear()

print('-=-'*30)
print(f'Os dados foram {princ}')
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')

print(f'O maior peso foi de {mai} Kg.')
for p in princ:
    if p[1] == mai:
        print(f'{p[1]}')

print(f'O menor peso foi de {men} Kg.')
for c in princ:
    if c[1] == men:
        print(f'{p[1]}')







