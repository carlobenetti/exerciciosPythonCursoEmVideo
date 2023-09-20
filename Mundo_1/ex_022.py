#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao total sem considerar espaços.
#- Quantas letras tem o primeiro nome. Ana Maria Braga
nome = str(input('Type your name: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', ''))) #Total sem espaços
x = nome.split()
print(len(x[0]))