# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

lista_valores = []

for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista_valores[-1]:
        lista_valores.append(n)
        print(f'Adicionado ao fim da lista... Concluido!')
    else:
        pos = 0
        while pos < len(lista_valores):
            if n <= lista_valores[pos]:
                lista_valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('---'*30)
print(f'Os valores digitados em ordem foram {lista_valores}')
