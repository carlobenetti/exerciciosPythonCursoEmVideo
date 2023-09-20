#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from statistics import mean
nome = []
idade = []
sexo = []
tot_mulheres = 0

for c in range(1, 3):
    nome.append((input(f'Digite o nome da {c}ª pessoa: ')))
    idade.append(int(input(f'Digite a idade da {c}ª pessoa: ')))
    sexo.append(int(input('Se for homem digite 0, se for mulher digite 1: ')))
if sexo != 0:
    tot_mulheres += 1
idade.sort()

print(f'A média de idade do grupo é {mean(idade)} anos.')
print(f'A pessoa mais velha do grupo tem {idade[-1]} anos e se chama: ')
print(f'No total são {tot_mulheres} mulheres menores que 20.')