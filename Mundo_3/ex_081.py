# Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_valores = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista_valores.append(n)
    cont += 1
    countinuar = str(input('Continuar sim ou não? ')).strip()[0]
    if countinuar in 'Nn':
        break
if 5 in lista_valores:
    is_five_in_list = 'está presente'
else:
    is_five_in_list = 'Não está presente'

print(f'Foram {cont} valores contados.\n'
      f'Lista decrescente -> {sorted(lista_valores, reverse=True)}.\n'
      f'O numero 5 {is_five_in_list} na lista. '
      f'Ele aparece {lista_valores.count(5)} vezes.')


      