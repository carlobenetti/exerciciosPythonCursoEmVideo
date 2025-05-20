"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""


from time import sleep

# Contagem de 1 até 10 passando de 1 em 1

def conntagemAte10():
    count1 = 0
    for i in range(0, 10):
        sleep(1)
        count1 += 1
        print(f'{count1}')


print(f'{conntagemAte10()}')






