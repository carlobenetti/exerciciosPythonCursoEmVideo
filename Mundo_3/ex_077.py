# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Em seguida, você deve mostrar, para cada palavra, quais são as suas vogais.
# palavras = ('Programar', 'Mercado')
# >>> Na palavra Programar temos as vogais a o
# >>> Na palavra Mercado temos as vogais a e o

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')
    
        
    