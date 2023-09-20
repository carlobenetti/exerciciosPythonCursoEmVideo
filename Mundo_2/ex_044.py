# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
#  1- à vista dinheiro/cheque: 10 % de desconto
#  2- a vista no cartao: 5% de desconto
#  3- em até 2X no cartao: preço normal
#  4- 3X ou mais no cartao; 20% de juros
cor_fim = '\033[m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'
print(f'{amarelo}{" Bem vindo ao mercadinho Big_Bom ":=^100}{cor_fim}')


preço = float(input('Digite o preço do produto R$: '))
forma_pagamento = int(input('''Escolha sua forma de pagamento.
[1] dinheiro/cheque.\n[2] a vista no cartão.\n[3] até 2x no cartão.\n[4] 3x ou mas no cartão.
Digite a sua opção: '''))

if forma_pagamento == 1:
    desconto = preço * (10/100)
    valor_pago = preço - desconto
    print(f'Você escolheu à vista no dinheiro/cheque: 10 % de desconto')
    print(f'Seu produto custa {preço}.\nVocê receberá um desconto de {amarelo}{desconto}{cor_fim}.'
          f'\nO valor pago será {valor_pago}')

elif forma_pagamento == 2:
    desconto = preço * (5/100)
    valor_pago = preço - desconto
    print(f'Você escolheu a vista no cartao: 5% de desconto.')
    print(f'Seu produto custa {preço}.\nVocê receberá um desconto de {amarelo}{desconto}{cor_fim}.'
          f'\nO valor pago será {verde}{valor_pago}{cor_fim}')

elif forma_pagamento == 3:
    print('Você escolheu em até 2X no cartao: preço normal.')
    print(f'O valor pago será {verde}{preço/2}{cor_fim}')

elif forma_pagamento == 4:
    juros = preço * (20/100)
    valor_pago = preço + juros
    print('Você escolheu 3X ou mais no cartao: 20% de juros')
    print(f'Seu produto custa {preço}.\nSerá acrescentado {amarelo}{juros}{cor_fim} reais de juros.'
          f'\nO valor pago será {vermelho}{valor_pago/3}{cor_fim}')
else:
    print('Opção invalida. Tente outra vez.')

    