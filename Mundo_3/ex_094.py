# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa num dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_pessoas = []

while True:
    quant = int(input('Quantas pessoas deseja cadastrar? '))
    for p in range(0, quant):
        pessoa = {}
        pessoa['nome'] = str(input('Nome: '))
        pessoa['sexo'] = str(input('Sexo [M ou F]: ')).split()[0]
        pessoa['idade'] = int(input('Idade: '))
        lista_pessoas.append(pessoa.copy())
