"""
Aqui temos algumas formas de se imprimir os valores das tuplas.
"""


varComposta = ('Hamburquer', 'Suco', 'Pizza', 'Pudim', 'Docinhos')


# Forma 1
for comida in varComposta:
    print(f'{comida}')


# Forma 2
# Utilizar dos valores de um contador como valor de posição dentro da variável composta:
for cont in range(0, len(varComposta)):
    print(f'Vou comer {varComposta[cont]} na posição {cont}')



# Forma 3
for pos, comida in enumerate(varComposta):
    print(f'Eu vou comer {comida} na posição {pos}')



# Aqui podemos mostrar as variáveis em ordem (lista alfabética ou numérica)
print(sorted(varComposta))


# -------------------------------------------------------------------------------------------------------------------------------------------------

c = (5, 2, 4, 9, 11, 6, 0, 1, 5, 6)
"""
O index serve para encontrarmos a posição de algum elemento. O primeiro argumento representa o valor que desejo encontrar a posição. O segundo argumento serve para eu definir a partir de qual posição que quero começar a procurar pelo valor.
No caso abaixo, eu desejo procurar a posição do segundo valor 5 na tupla. Assim eu peço para o computador procurar a partir do segundo elemento (1)
"""
print(c.index(5, 1))


