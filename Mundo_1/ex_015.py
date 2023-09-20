#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Type the kilometers run: '))
days = int(input('Type the days rented: '))
price = (km*0.15)+(days*60)
print(f'You have to pay R${price:.2f}.')
