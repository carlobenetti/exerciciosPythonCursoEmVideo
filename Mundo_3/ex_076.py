# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final mostre uma listagem de preços, organizando os dados em forma tabular.
# Ex: items = ('Frango', 3.50, 'Arroz', 4.6, 'Café', 16.50) Exemplo tabela:
# Frango.................. R$ 3.50
# Arroz................... R$ 4.60


lista_mercado = (
    'Frango', 3.50, 
    'Arroz', 4.6, 
    'Café', 16.50, 
    'Feijão', 7.80, 
    'Macarrão', 2.70, 
    'Leite', 4.0, 
    'Óleo', 5.5, 
    'Açúcar', 3.2, 
    'Sal', 1.8, 
    'Farinha', 3.0, 
    'Manteiga', 9.0, 
    'Queijo', 18.5, 
    'Presunto', 10.0, 
    'Tomate', 6.3, 
    'Alface', 2.0
)


even_values = lista_mercado[1::2]
odd_values = lista_mercado[0::2]


for i in range(0, len(even_values)):
    print(f'{odd_values[i]}...........{even_values[i]}')
    
    
    




