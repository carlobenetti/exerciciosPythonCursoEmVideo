#Faca um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos

peso = []

for c in range(1, 6):
    peso.append(float(input(f'Digite o peso da {c}ª pessoa: ')))
peso.sort()
print(f'O menor peso é {peso[0]} kg, o maior peso é {peso[-1]} kg.')