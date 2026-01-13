#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print(f'{10*"-=-"}\033[1;30;46m Seja bem vindo a loja \033[m{10*"-=-"}')
preço = float(input('\033[1;30;49mDigite o preço do produto: \033[m'))
desconto = (preço*5)/100
print(f'O produto custa {preço} Reais, \nVocê recebeu um desconto de {desconto:.2f} Reais, '
      f'\nO novo valor é {preço - desconto:.2f}')
      