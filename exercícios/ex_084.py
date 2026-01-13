# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
# [] Mostre quantas pessoas foram cadastradas.
# [] Uma listagem com as pessoas mais pesadas.
# [] Uma listagem com as pessoas mais leves.

cont = 's'
contador = 0
lista = []
personalData = []
maiorPeso = menorPeso = 0


# Adicionado o nome e peso a lista.
while cont != 'n':
    personalData.append(str(input('Digite seu nome: ')))
    personalData.append(int(input('Digite seu peso: ')))
    lista.append(personalData[:])
    personalData.clear()
    contador += 1
    cont = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    

# Separando o maior e menor valor.
contadorPesos = 0
for pesos in lista:
    if contadorPesos == 0:
        maiorPeso = menorPeso = pesos[1]
    else:
        if pesos[1] > maiorPeso:
            maiorPeso = pesos[1]
        elif pesos[1] < menorPeso:
            menorPeso = pesos[1]
    contadorPesos += 1



# Imprimindo os dados.
print()
print(f'{contador} pessoas participaram da pesquisa.')
for data in lista:
    print(f'Nome: {data[0]} \nPeso: {data[1]}')
    print()
    


# Quem pesa mais e quem pesa menos.
print(f'O maior peso foi {maiorPeso} Kg. Peso de ', end='')
for pesoPessoas in lista:
    if pesoPessoas[1] == maiorPeso:
        print(f'[{pesoPessoas[0]}]', end=' ')

print(f'\nO menor peso foi {menorPeso} Kg. Peso de ', end='')
for pesoPessoas in lista:
    if pesoPessoas[1] == menorPeso:
        print(f'[{pesoPessoas[0]}]', end=' ')
    
    