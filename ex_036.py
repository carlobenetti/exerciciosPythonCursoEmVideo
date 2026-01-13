# Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salario ou entao o emprestimo será negado.
"""Informações do comprador"""
valorcasa = float(input('Qual o valor da casa? '))
salariocomprador = float(input('De quanto é o seu salário? '))
anospagar = int(input('Em quantos anos você pretende pagar? '))
prestacaomensal = valorcasa / (anospagar*12)
trintaporcento = salariocomprador * (30/100)


""" Condições da compra """
if prestacaomensal <= trintaporcento:
    print(f'Seu empréstimo foi aprovada, ele é menor do que 30% do seu salário (30% de {salariocomprador:.2f} = '
          f'{trintaporcento:.2f}). \nVocê pagará uma prestação mensal de R$ {prestacaomensal:.2f}.')
elif prestacaomensal > trintaporcento:
    print(f'Sua empréstimo não foi aprovada pois a prestação mensal de R$ {prestacaomensal:.2f} é maior do que 30% '
          f'do seu salário (30% de {salariocomprador:.2f} = {trintaporcento:.2f}).')