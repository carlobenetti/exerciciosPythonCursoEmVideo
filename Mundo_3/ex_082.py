# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Continuar? Sim ou não: ')).strip()[0]
    if continuar in 'Nn':
        break
print(lista)

# Separando par e impar
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    elif v % 2 == 1:
        lista_impar.append(v)


print(f'Lista digitada -> {lista}\n'
      f'Números pares da lista -> {lista_par}\n'
      f'Números impares de lista -> {lista_impar}')