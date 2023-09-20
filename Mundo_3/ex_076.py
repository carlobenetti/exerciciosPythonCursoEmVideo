#Crie um programa que tenha uma tupla única com nomes de produtos e seus
#respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

compras = ('arroz', 10, 'macarrão', 15, 'carne', 27.7)

verde = '\033[1;32m'


print(f"""{verde}{60*'-'}
{'PRODUTOS COMPRADOS':^50}
{60*'-'}\033[m""")

for posicao in range(0, len(compras)):
    if posicao % 2 == 0:
        print(compras[posicao], end='')
        print('.'*40, end=' R$ ')
    if posicao % 2 != 0:
        print(f'{compras[posicao]:.2f}')
print(60*'_')