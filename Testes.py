varComposta = ('Hamburquer', 'Suco', 'Pizza', 'Pudim')


# Utilizar dos valores de um contador como valor de posição dentro da variável composta:

"""
dcascasca
"""

for cont in range(0, len(varComposta)):
    print(f'Vou comer {varComposta[cont]} na posição {cont}')




for pos, comida in enumerate(varComposta):
    print(f'Eu vou comer {comida} na posição {pos}')










