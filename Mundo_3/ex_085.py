# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares 
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
        
    num[0].sort()
    num[1].sort()
print(f'\n{40 * "-"}\n{15*" "}Resultado\n{40 * "-"}')
print(f'Os valores são: {num}')
print(f'Números pares -> {num[0]} \nNúmeros impares -> {num[1]}')
