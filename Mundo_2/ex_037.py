#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de coversao:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um número: '))
x = int(input("""Escolha para qual base numérica você quer converter.
[1] para binário, [2] para octal e [3] para hexadecimal 
Escolha sua opção: """))

if x == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')

elif x == 2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')

elif x == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')

else:
    print(f'Essa opção é invavlida. Tente outra vez.')
    