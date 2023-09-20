# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

words_tuple = ('arroz', 'cachorro', 'papagaio', 'serambicidae')
words_dictionary = list(words_tuple)

for i in words_tuple:
    print(f'\nNa palavra {i} temos: ', end='')
    for letter in i:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

