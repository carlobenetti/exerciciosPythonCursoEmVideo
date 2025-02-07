# Um programa que vai ler vários números e colocar em uma lista.
# Crie duas listas extras que vão conter apenas os valores pares e os valores impares.
# Mostre o conteúdo das 3 listas geradas.

lista = []
pares = []
imapres = []

cont = 'S'

while cont not in 'Nn':
    lista.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar? [S/N]: '))


for items in lista:
    if items % 2 == 0:
        pares.append(items)
    if items % 2 == 1:
        imapres.append(items)

print(f'Os valores digitados foram: {lista}. Sendo pares: {pares} e impares {imapres}.')


