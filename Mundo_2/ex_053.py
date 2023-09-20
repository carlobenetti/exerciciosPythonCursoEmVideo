#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,desconsiderando os espaços.
palavra = str(input('Digite uma palavra: '))
palavra = palavra.lower().strip()
inverso = palavra[::-1]

print(f'A palavra escolhida foi {palavra}. \nSeu inverso é {inverso}.')

if palavra == inverso:
    print(f'{palavra} = {inverso}')
    print('É palindromo')
else:
    print(f'{palavra} != {inverso}')
    print('Não é um palindromo.')



