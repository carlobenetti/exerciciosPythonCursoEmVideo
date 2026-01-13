# faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontrem
# no intervalo de 1 até 500
acumulador = 0
quantidad_C = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        acumulador += c #O acumulador recebe ele mesmo  e soma com C.
        quantidad_C += 1
print(f'Foram {quantidad_C} variáveis acumulando o valor {acumulador}.')

