# Crie um programa onde o usuário possa digitar 5 valores numéricos.  
# [] Cadastreos em uma lista já na posição correta sem usar o sort.
# [] Mostre a lista ordenada.


lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)
    
    else: 
        pos = 0

        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('-=-' * 30)
print(f'Os valores da lista são: {lista}')



