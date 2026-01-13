# Crie um programa onde o usuário insira 7 valores numéricos.
# Cadastreos em uma lista única que separe os valores pares e imapares.
# No final mostre os valores pares e impares em ordem crescente.

lista = [[], []]
timer = 0

for count in range(0, 7):
    timer += 1
    valor = int(input(f'Digite o {timer}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
    print(lista)


      
print(f'\nPares: {sorted(lista[0])},\nImpares: {sorted(lista[1])}')





