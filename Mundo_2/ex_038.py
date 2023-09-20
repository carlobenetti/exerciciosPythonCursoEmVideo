# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O primeiro valor é maior pois {num1} é maior que {num2}')
elif num2 > num1:
    print(f'O segundo valor é maior pois {num2} é maior que {num1}')
elif num1 == num2:
    print(f'Os valores {num1} e {num2} são iguais.')
else:
    print('Tente novamente.')