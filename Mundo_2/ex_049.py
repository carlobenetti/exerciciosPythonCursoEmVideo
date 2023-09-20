#Refaça o exercicio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for
num = int(input('Digite um número inteiro: '))

for c in range(0, 11):
    print(f'{c} x {num} = {num * c}')