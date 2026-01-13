#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
# separados.
x = int(input('Type a number from 0 to 9999: '))
print(f'Analyzing the number {x}')
print(f'Unidade: {x//1 % 10}')
print(f'Dezena: {x//10%10}')
print(f'Centena: {x//100%10}')
print(f'Milhar: {x//1000%10}')