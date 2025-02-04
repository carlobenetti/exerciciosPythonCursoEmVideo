# Crie um programa onde o usuário possa digitar 5 valores numéricos.  
# [] Cadastreos em uma lista já na posição correta sem usar o sort.
# [] Mostre a lista ordenada.


lista = [0, 0, 0, 0, 0]
listaCopia = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))

    

    # lista[0]
    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0] 
    if lista[0] > lista[2]:
        lista[0], lista[2] = lista[2], lista[0]
    if lista[0] > lista[3]:
        lista[0], lista[3] = lista[3], lista[0]
    if lista[0] > lista[4]:
        lista[0], lista[4] = lista[4], lista[0]
    
    # lista[0]
    if lista[1] > lista[2]:
        lista[1], lista[2] = lista[2], lista[1]
    if lista[1] > lista[3]:
        lista[1], lista[3] = lista[3], lista[1]
    if lista[1] > lista[4]:
        lista[1], lista[4] = lista[4], lista[1]

    # lista[2]
    if lista[2] > lista[3]:
        lista[2], lista[3] = lista[3], lista[2]
    if lista[2] > lista[4]:
        lista[2], lista[4] = lista[4], lista[2]
    
    # lista[3]
    if lista[3] > lista[4]:
        lista[3], lista[4] = lista[4], lista[3]
    
    lista.append(valor)


    print(f'O valor {valor} foi adicionado a lista na posição {lista.index(valor)}')

    