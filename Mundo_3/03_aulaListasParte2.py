lista = []
pessoas = []
cont = str()

while cont != 'n':
    pessoas = []
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(int(input('Digite a sua idade: ')))
    lista.append(pessoas[:])
    del pessoas
    cont = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]


print(f'Lista = {lista}')
for sublists in lista:
    print(f'nome: {sublists[0]}, idade: {sublists[1]}')
    





