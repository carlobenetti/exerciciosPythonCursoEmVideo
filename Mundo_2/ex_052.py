#Faça um programa que leia um numero e diga se ele é primo ou não
print(f'{38*"-"} \nDizendo se um número é primo ou não. \n{38*"-"}')

num = int(input('Digite um número: '))
soma = 0
count = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end='')
        count += 1
    else:
        print('\033[1;31m', end='')
    print(f'{c} ', end='')
print(f' -> Foram {count} números contados')
if count == 2:
    print('É primo')
else:
    print('Não é primo.')

