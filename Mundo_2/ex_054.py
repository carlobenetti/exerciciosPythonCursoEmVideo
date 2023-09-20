# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade(21) e quantas jaa são maiores.
from datetime import date

ano_atual = date.today().year
totmaiores = 0
totmenores = 0

for pessoas in range(1, 8):
    nascimentos = int(input(f'Qual o ano de nascimento da {pessoas}ª pessoa: '))
    idade_pessoas = ano_atual - nascimentos
    if idade_pessoas >= 21:
        totmaiores += 1
    elif idade_pessoas < 21:
        totmenores += 1
print(f'São {totmaiores} maiores de idade e {totmenores} menores de idade.')

