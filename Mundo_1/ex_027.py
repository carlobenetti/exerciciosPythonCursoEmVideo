#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.

nome = str(input('Digite seu nome: ')).lower()
nome = nome.strip().split()

print(f'Primeiro nome = {(nome)[0]} \nSegundo nome = {(nome)[-1]}')