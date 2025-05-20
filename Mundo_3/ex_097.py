"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:

~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""


texto = str(input('Digite a mensagem: '))


def escreva(texto): 
    print(f'{'~'*len(texto)}')
    print(texto)
    print(f'{'~'*len(texto)}')

print()
escreva(texto)

