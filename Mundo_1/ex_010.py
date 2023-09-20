#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
reais = float(input('\033[1;30;46m Digite quantos reais você têm: \033[m '))

print(f'Você possui {reais} Reais \nVocê pode comprar \033[1;30;45m{reais/5.53:.2f} Dolares.\033[m')

