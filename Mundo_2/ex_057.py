#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Por favor digite o seu sexo: ')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor digite o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} salvo com sucesso. 👍')


