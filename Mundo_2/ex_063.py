#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Quantos números da sequência você quer? '))
t1 = 0
t2 = 1
print(30*'-=-')
print(f'{t1} -> {t2}', end='')
count = 3
while count <= n:
    t3 = t1 +t2
    print(f' -> {t3}', end='')
    count += 1
    t1 = t2
    t2 = t3
print(' FIM')

