# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep
print('A contagem de fogos está prestes a começar: ')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!!!🥳')

