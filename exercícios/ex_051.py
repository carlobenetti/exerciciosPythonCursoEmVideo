#Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.
# No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite um número: '))
count = 0
razao = int(input('Digite a razão: '))

for c in range(0, 10):
    num += razao
    count += 1
    print(num, end=' ')
print(f'\nA quantidade impressa é de {count} valores.')

