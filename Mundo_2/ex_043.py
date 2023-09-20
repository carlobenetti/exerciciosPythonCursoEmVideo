# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela acaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25; peso ideal
# 25 até 30: sobrepeso
# 30 até 40 Obesidade
# acima de 40: Obesidade morbida

print('Bom dia, por favor digite seu peso e sua altura: ')
peso = float(input('PESO Kg: '))
altura = float(input('ALTURA metros: '))
imc = peso / altura ** 2

if imc <= 18.5:
    resultado = 'abaixo do peso'
elif imc <= 25:
    resultado = 'com o peso ideal'
elif imc <= 30:
    resultado = 'com sobrepeso'
elif imc <= 40:
    resultado = 'obeso'
elif imc > 40:
    resultado = 'com obesidade morbida'
print(f'O seu imc é {imc:.2f}.\n Você está {resultado}')

